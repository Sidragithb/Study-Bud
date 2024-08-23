
# StudyBuddy Django Project

## Overview

StudyBuddy is a Django-based web application designed to connect students with study partners globally. This README provides a detailed overview of the project's structure, including HTML templates and Python files, as well as their interactions.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Base Template (`base.html`)](#base-template-basehtml)
3. [Header Template (`navbar.html`)](#header-template-navbarhtml)
4. [HTML Pages and Corresponding Views](#html-pages-and-corresponding-views)
   - [Home Page](#home-page)
   - [Login Page](#login-page)
   - [Register Page](#register-page)
   - [User Profile Page](#user-profile-page)
   - [Settings Page](#settings-page)
   - [Room List Page](#room-list-page)
   - [Room Detail Page](#room-detail-page)
   - [Search Results Page](#search-results-page)
   - [Recent Activities Page](#recent-activities-page)
   - [Additional Pages](#additional-pages)
5. [Python Files](#python-files)
   - [Views](#views)
   - [Models](#models)
   - [Forms](#forms)
   - [URLs](#urls)
6. [Static Files](#static-files)
7. [Contributing](#contributing)

## Project Structure

Here’s the structure of the StudyBuddy project:

```
studybuddy/
├── manage.py
├── studybuddy/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── templates/
│       ├── base.html
│       ├── navbar.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       ├── settings.html
│       ├── room_list.html
│       ├── room_detail.html
│       ├── search_results.html
│       ├── recent_activities.html
│       ├── page_12.html
│       ├── page_13.html
│       ├── page_14.html
│       ├── page_15.html
│       ├── page_16.html
│       ├── page_17.html
│       ├── page_18.html
│       ├── page_19.html
│       ├── page_20.html
│       ├── page_21.html
│       ├── page_22.html
│       ├── page_23.html
│       ├── page_24.html
│       ├── page_25.html
│       ├── page_26.html
│       ├── page_27.html
│       ├── page_28.html
│       ├── page_29.html
│       └── page_30.html
├── static/
│   ├── images/
│   │   ├── logo.svg
│   │   └── avatar.svg
│   ├── styles/
│   │   └── style.css
│   └── js/
│       └── script.js
└── app_name/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Base Template (`base.html`)

The `base.html` template provides the foundational layout for all pages.

### Code

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="{% static 'assets/favicon.ico' %}" type="image/x-icon" />
    <link rel="stylesheet" href="{% static 'styles/style.css' %}" />
    <title>StudyBuddy - Find study partners around the world!</title>
</head>
<body>
    {% include "navbar.html" %}
    {% if messages %}
    <ul class="messages">
    {% for message in messages %}
        <li>{{ message }}</li>
    {% endfor %}
    </ul>
    {% endif %}
    {% block content %}
    {% endblock content %}
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Explanation

- **Common Layout**: Provides the structure for all pages.
- **Static Files**: Links CSS and JavaScript files.
- **Content Block**: Placeholder for page-specific content.

## Header Template (`navbar.html`)

Defines the navigation bar for the application.

### Code

```html
{% load static %}

<header class="header header--loggedIn">
    <div class="container">
        <a href="{% url 'home' %}" class="header__logo">
            <img src="{% static 'images/logo.svg' %}" alt="StudyBuddy Logo" />
            <h1>StudyBuddy</h1>
        </a>
        
        <form class="header__search" method="GET" action="{% url 'home' %}">
            <label>
                <svg aria-label="search" version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                    <title>search</title>
                    <path d="M32 30.586l-10.845-10.845c1.771-2.092 2.845-4.791 2.845-7.741 0-6.617-5.383-12-12-12s-12 5.383-12 12c0 6.617 5.383 12 12 12 2.949 0 5.649-1.074 7.741-2.845l10.845 10.845 1.414-1.414zM12 22c-5.514 0-10-4.486-10-10s4.486-10 10-10c5.514 0 10 4.486 10 10s-4.486 10-10 10z"></path>
                </svg>
                <input name="q" placeholder="Search for rooms..." />
            </label>
        </form>
        
        <nav class="header__menu">
            {% if request.user.is_authenticated %}
            <div class="header__user">
                <a href="{% url 'update-user' %}">
                    <div class="avatar avatar--medium active">
                        <img src="{{ request.user.avatar.url }}" alt="{{ request.user.username }}'s avatar" />
                    </div>
                    <p>{{ request.user.username }}<span>{{ request.user.username }}</span></p>
                </a>
                <button class="dropdown-button">
                    <svg aria-label="chevron-down" version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                        <title>chevron-down</title>
                        <path d="M16 21l-13-13h-3l16 16 16-16h-3l-13 13z"></path>
                    </svg>
                </button>
            </div>
            
            <div class="dropdown-menu">
                <a href="{% url 'update-user' %}" class="dropdown-link">
                    <svg aria-label="tools" version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                        <title>tools</title>
                        <path d="M27.465 32c-1.211 0-2.35-0.471-3.207-1.328l-9.392-9.391c-2.369 0.898-4.898 0.951-7.355 0.15-3.274-1.074-5.869-3.67-6.943-6.942-0.879-2.682-0.734-5.45 0.419-8.004 0.135-0.299 0.408-0.512 0.731-0.572 0.32-0.051 0.654 0.045 0.887 0.277l5.394 5.395 3.586-3.586-5.394-5.395c-0.232-0.232-0.336-0.564-0.276-0.887s0.272-0.596 0.572-0.732c2.552-1.152 5.318-1.295 8.001-0.418 3.274 1.074 

5.869 3.67 6.943 6.942 0.806 2.457 0.752 4.987-0.15 7.358l9.392 9.391c0.844 0.842 1.328 2.012 1.328 3.207-0 2.5-2.034 4.535-4.535 4.535zM15.101 19.102c0.26 0 0.516 0.102 0.707 0.293l9.864 9.863c0.479 0.479 1.116 0.742 1.793 0.742 1.398 0 2.535-1.137 2.535-2.535 0-0.668-0.27-1.322-0.742-1.793l-9.864-9.863c-0.294-0.295-0.376-0.74-0.204-1.119 0.943-2.090 1.061-4.357 0.341-6.555-0.863-2.631-3.034-4.801-5.665-5.666-1.713-0.561-3.468-0.609-5.145-0.164l4.986 4.988c0.391 0.391 0.391 1.023 0 1.414l-5 5c-0.188 0.188-0.441 0.293-0.707 0.293s-0.52-0.105-0.707-0.293l-4.987-4.988c-0.45 1.682-0.397 3.436 0.164 5.146 0.863 2.631 3.034 4.801 5.665 5.666 2.2 0.721 4.466 0.604 6.555-0.342 0.132-0.059 0.271-0.088 0.411-0.088z"></path>
                    </svg>
                    Settings
                </a>
                <a href="{% url 'logout' %}" class="dropdown-link">
                    <svg aria-label="sign-out" version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                        <title>sign-out</title>
                        <path d="M3 0h22c0.553 0 1 0 1 0.553l-0 3.447h-2v-2h-20v28h20v-2h2l0 3.447c0 0.553-0.447 0.553-1 0.553h-22c-0.553 0-1-0.447-1-1v-30c0-0.553 0.447-1 1-1z"></path>
                        <path d="M21.879 21.293l1.414 1.414 6.707-6.707-6.707-6.707-1.414 1.414 4.293 4.293h-14.172v2h14.172l-4.293 4.293z"></path>
                    </svg>
                    Logout
                </a>
            </div>
            {% else %}
            <a href="{% url 'login' %}">
                <img src="{% static 'images/avatar.svg' %}" alt="Login Avatar" />
                <p>Login</p>
            </a>
            {% endif %}
        </nav>
    </div>
</header>
```

### Explanation

- **Header Layout**: Includes the logo, search bar, and user authentication state.
- **Dropdown Menu**: Provides options for authenticated users.

## HTML Pages and Corresponding Views

### Home Page

The landing page of StudyBuddy.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="home">
    <h2>Welcome to StudyBuddy</h2>
    <p>Your gateway to finding study partners around the world!</p>
    <a href="{% url 'room-list' %}" class="btn btn-primary">Browse Rooms</a>
</div>
{% endblock %}
```

#### Explanation

- **Content**: Introduction and call-to-action button.

#### View

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

### Login Page

Allows users to authenticate.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="login">
    <h2>Login</h2>
    <form method="POST" action="{% url 'login' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Login</button>
    </form>
</div>
{% endblock %}
```

#### Explanation

- **Login Form**: For user authentication.

#### View

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
```

### Register Page

Allows new users to create an account.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="register">
    <h2>Register</h2>
    <form method="POST" action="{% url 'register' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Register</button>
    </form>
</div>
{% endblock %}
```

#### Explanation

- **Registration Form**: For creating a new account.

#### View

```python
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
```

### User Profile Page

Displays user information and allows updates.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="profile">
    <h2>{{ user.username }}'s Profile</h2>
    <div class="avatar">
        <img src="{{ user.avatar.url }}" alt="{{ user.username }}'s avatar" />
    </div>
    <p>Email: {{ user.email }}</p>
    <a href="{% url 'update-profile' %}" class="btn btn-primary">Edit Profile</a>
</div>
{% endblock %}
```

#### Explanation

- **User Details**: Shows the user's profile and avatar.

#### View

```python
from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')
```

### Settings Page

Allows users to configure application preferences.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="settings">
    <h2>Settings</h2>
    <form method="POST" action="{% url 'update-settings' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Save Changes</button>
    </form>
</div>
{% endblock %}
```

#### Explanation

- **Settings Form**: For updating user settings.

#### View

```python
from django.shortcuts import render

def settings(request):
    return render(request, 'settings.html')
```

### Room List Page

Displays a list of available study rooms.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="room-list">
    <h2>Available Study Rooms</h2>
    <ul>
        {% for room in rooms %}
        <li>
            <a href="{% url 'room-detail' room.id %}">{{ room.name }}</a>
        </li>
        {% empty %}
        <li>No rooms available.</li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

#### Explanation

- **List of Rooms**: Shows all available rooms.

#### View

```python
from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})
```

### Room Detail Page

Provides detailed information about a specific study room.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="room-detail">
    <h2>{{ room.name }}</h2>
    <p>{{ room.description }}</p>
    <a href="{% url 'join-room' room.id %}" class="btn btn-primary">Join Room</

a>
</div>
{% endblock %}
```

#### Explanation

- **Room Details**: Shows information and provides an option to join the room.

#### View

```python
from django.shortcuts import render, get_object_or_404
from .models import Room

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})
```

### Search Results Page

Displays search results for rooms.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="search-results">
    <h2>Search Results</h2>
    <ul>
        {% for room in rooms %}
        <li>
            <a href="{% url 'room-detail' room.id %}">{{ room.name }}</a>
        </li>
        {% empty %}
        <li>No rooms found.</li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

#### Explanation

- **Search Results**: Shows the results based on the search query.

#### View

```python
from django.shortcuts import render
from .models import Room

def search_results(request):
    query = request.GET.get('q')
    rooms = Room.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'rooms': rooms})
```

### Recent Activities Page

Shows recent activities in the app.

#### Code

```html
{% extends "base.html" %}

{% block content %}
<div class="recent-activities">
    <h2>Recent Activities</h2>
    <ul>
        {% for activity in activities %}
        <li>{{ activity.description }} - {{ activity.timestamp }}</li>
        {% empty %}
        <li>No recent activities.</li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

#### Explanation

- **Recent Activities**: Displays recent events or actions.

#### View

```python
from django.shortcuts import render
from .models import Activity

def recent_activities(request):
    activities = Activity.objects.all().order_by('-timestamp')
    return render(request, 'recent_activities.html', {'activities': activities})
```

### Additional Pages

For pages 12 to 30, follow the same structure as above. Each page will have its own HTML template and corresponding view in the `views.py` file. Ensure each template extends `base.html` and includes relevant content and forms.

## Python Files

### Views (`views.py`)

Defines the logic for rendering HTML templates and handling user interactions.

### Models (`models.py`)

Defines the data structure and schema for the application.

### Forms (`forms.py`)

Handles form rendering and validation.

### URLs (`urls.py`)

Maps URLs to views.

## Static Files

- **Images**: Icons, logos, avatars.
- **Styles**: CSS files for styling.
- **JavaScript**: JS files for interactivity.

## Contributing

Feel free to contribute to the StudyBuddy project by submitting issues or pull requests. Please follow the coding standards and ensure all code is thoroughly tested before submission.

---

