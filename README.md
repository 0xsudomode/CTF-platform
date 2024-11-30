
# Django CTF Platform

## 📖 Overview

A Capture The Flag (CTF) platform built using Django.  
This platform allows users to create, manage, and participate in CTF challenges with features like real time scoring, and challenge tracking.

## 🌟 Features

- User registration and login  
- Challenge creation and management  
- Real-time scoring system  
- Admin panel for easy management  

## 🛠️ Installation

Follow these steps to get the platform up and running on your local machine:

### Prerequisites

- Python 3.8+ installed  
- pip (Python package manager)  
- Virtual environment (optional but recommended)  

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/0xsudomode/CTF-platform.git
    cd CTF-platform
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

    Access the platform at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## ⚙️ Configuration

- Add your database credentials and other settings in `settings.py`.  
- Optionally, configure environment variables for sensitive data.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repository.  
2. Create a new branch: `git checkout -b feature-name`.  
3. Make your changes and commit them: `git commit -m 'Add feature-name'`.  
4. Push to the branch: `git push origin feature-name`.  
5. Submit a pull request.

## 📜 License

MIT License  

## 📬 Contact

If you have any questions or suggestions, feel free to contact me at [abdelhamidaghamir@gmail.com](mailto:abdelhamidaghamir@gmail.com).
