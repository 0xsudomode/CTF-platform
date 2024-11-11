from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),  # User profile page
    path('challenges/', views.challenges_by_category, name='challenges'),
    path('challenges/<str:category>/', views.challenges_by_category, name='challenges_by_category'),
    path('challenge/<int:challenge_id>/', views.solve_challenge, name='solve_challenge'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
]