# Social Media API

---

You can create user profile with picture, 
bio and other details. Users can create posts, add hashtags to posts and follow other users.

Security is assured by use of JWT tokens authentication.

Comprehensive documentation.

---

## Installation

1. Clone the repository:
git clone https://github.com/MaksNochvai/py-social-media-api/
2. Set up a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate # Activation of the virtual environment (Unix)
venv\Scripts\activate # Activation of the virtual environment (Windows)
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Start the development server:
```
python manage.py migrate
python manage.py runserver
```
5. Load fixture data:
```
python manage.py loaddata fixture_data.json
```
# Getting access

------------------------------------
- create user via /api/user/register/
- get access token via /api/user/token

----

## Technologies Used
The Airport Service API is built with the following technologies:

- Django: A powerful web framework for building web applications in Python.
- Django REST framework: A toolkit for building Web APIs with Django.
- SQLite: A lightweight, serverless database used for development purposes.
- Python: The programming language used for the backend development.

----

## Features
The Social Media API provides the following features:

1. Hashtags:

- Users can view and manage hashtags with their unique names.
2. Posts:

- Users can create, view, and manage posts. Posts consist of a title, text content, creation timestamp, and an optional picture. Users can also add multiple hashtags to their posts.
3. Users:

- User accounts are managed with an extended User model that uses email as the unique identifier instead of a username. Users can create regular accounts and superuser accounts. The superuser accounts have staff and superuser privileges.
4. User Profiles:

- Each user can have a user profile that includes a username, profile picture, bio, and information about their followers and following.