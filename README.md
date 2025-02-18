# Simple Login Page
A simple login page created in Django, perfect for recycling in future projects. Built in an afternoon of boredom, this application is designed to be flexible and easy to adapt to different databases. While it was originally developed using a PostgreSQL database, it can be easily configured to work with other databases by referring to the relevant documentation.

# ✨ Features
Simple and Clean Design: Easy-to-use login interface.

Flexible Database Configuration: Originally built for PostgreSQL, but can be adapted to other databases.

Quick Setup: Get up and running in no time.

# 🛠️ Installation
Clone the repository:
```
git clone https://github.com/yourusername/simple-login.git
cd simple-login
```
Install dependencies:
Make sure to install all the required packages listed in requirements.txt. They are not just for decoration!
```
pip install -r requirements.txt
```
Configure the database:

Create a .env file in the simple_login directory with the following structure:
```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
```
Replace the placeholders with your actual database credentials.

Run migrations:
```
python manage.py migrate
```
Start the development server:

python manage.py runserver
Access the application:
Open your browser and go to http://127.0.0.1:8000/ to see the login page in action.

# 🚀 Usage
This login page can be used as a starting point for any project requiring user authentication. Feel free to customize and extend it to fit your needs.
