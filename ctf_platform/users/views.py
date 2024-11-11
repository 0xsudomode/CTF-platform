import django.db
from django.shortcuts import render,redirect, get_object_or_404 
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from . import models 
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
            form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
    
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')  # Redirect to the home page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
    
def logout_user(request):
    logout(request)
    messages.info(request,'You have successfully logged out.')
    return redirect('login')


@login_required
def solve_challenge(request, challenge_id):
    challenge = get_object_or_404(models.Challenge, id=challenge_id)

    # Check if the user has already solved this challenge
    solved = models.Scoreboard.objects.filter(user=request.user, challenge=challenge).exists()
    
    if solved:
        return render(request, 'users/solve_challenge.html', {
            'challenge': challenge, 
            'error': 'You have already solved this challenge!'
        })

    if request.method == 'POST':
        submitted_flag = request.POST.get('flag')

        # Check if the submitted flag is correct
        if submitted_flag == challenge.flag:
            # Correct flag submission, award points and mark as solved
            models.Scoreboard.objects.create(user=request.user, challenge=challenge, points=challenge.difficulty)
            return redirect('scoreboard')  # Redirect to the scoreboard after solving the challenge
        else:
            # Incorrect flag
            return render(request, 'users/solve_challenge.html', {
                'challenge': challenge, 
                'error': 'Incorrect flag! Try again.'
            })

    return render(request, 'users/solve_challenge.html', {'challenge': challenge, 'solved': solved})



def scoreboard(request):
    # Get all users and their scores
    scores = models.Scoreboard.objects.values('user__username').annotate(total_score=django.db.models.Sum('points')).order_by('-total_score')
    return render(request, 'users/scoreboard.html', {'scores': scores})

def home(request):
    return render(request, 'users/home.html')

def index(request):
    return render(request,'users/index.html')

@login_required(login_url='/login/')
def challenges_by_category(request, category=None):
    if category:
        challenges = models.Challenge.objects.filter(category=category)
    else:
        challenges = models.Challenge.objects.all()

    return render(request, 'users/challenges_by_category.html', {'challenges': challenges, 'category': category})

@login_required(login_url='/login/')
def user_profile(request):
    user = request.user
    # Get all challenges solved by the user
    solved_challenges = models.Scoreboard.objects.filter(user=user)
    total_score = sum([score.points for score in solved_challenges])
    
    return render(request, 'users/user_profile.html', {
        'user': user,
        'solved_challenges': solved_challenges,
        'total_score': total_score
    })