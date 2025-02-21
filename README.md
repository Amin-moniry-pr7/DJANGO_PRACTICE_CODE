# 🚀 DJANGO_PRACTICE_TEST

## 📌 Project Overview

This project is a simple Django application designed to practice and test basic Django functionalities. It includes:

- **Model-based List View:** Displays a list of messages stored in the database.
- **Templates:** Custom templates (`F_D.html`, `S_D.html`) for rendering views and creating dynamic content.
- **Admin Panel:** Allows you to manage data in the Django Admin interface.

---

## 📋 Prerequisites

1. 🐍 Python 3.x
2. 🌐 Django 5.x
3. 🗃 SQLite (default database)


## 📂 Project Structure

```
DJANGO_PRACTICE_TEST/
│
├── 📜 manage.py                # Django management script
├── 📚 db.sqlite3               # SQLite database file
├── 🌱 .env                     # Environment variables for project settings
├── 💻 PM_A/                    # Custom Django app
│   ├── 📦 migrations/
│   ├── 🗂 models.py            # Model definitions
│   ├── 🌐 views.py             # Views handling
│   ├── 🔗 urls.py              # URL routing for PM_A app
│   ├── 🖥 templates/           # Template files (F_D.html, S_D.html)
│   ├── 🗂 admin.py             # Register models with admin site
│   └── 📑 tests.py             # Test cases for views and responses
└── 🏗 django_AM/
    ├── ⚙ settings.py          # Main project settings
    ├── 🔗 urls.py              # Global URL routing
    └── 🖥 wsgi.py              # WSGI configuration for the project
```


## 📝 Code Explanation

### 1. **views.py**
In `views.py`, you define the class-based view `PMRESPONDE`, which inherits from `ListView`. This view will display a list of items from your `ab` model. The `ListView` automatically handles rendering the list, while the template (`S_D.html`) displays the content.

```python
from django.views.generic import ListView
from .models import ab

class PMRESPONDE(ListView):
    model = ab
    template_name = 'S_D.html'  # This is the template that will be used to render the list of items.
```

### 2. **models.py**
In `models.py`, you've defined a simple model `ab` with a single field `text`. This model will store messages that are shown in the `ListView`.

```python
from django.db import models

class ab(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text  # This will display the text when rendering the list of items in the admin panel.
```

### 3. **urls.py**
In `urls.py`, you map the root URL (`''`) to the `PMRESPONDE` class-based view. This ensures that when you visit the homepage of the app, the list of messages is displayed.

```python
from django.urls import path
from .views import PMRESPONDE

urlpatterns = [
    path('', PMRESPONDE.as_view(), name='PM_A'),  # Maps the root URL to the PMRESPONDE view.
]
```

### 4. **templates (F_D.html & S_D.html)**
In your templates, you have `F_D.html` and `S_D.html`.

- `F_D.html` is likely a base template that other templates inherit from (this is indicated by the `{% extends 'F_D.html' %}` line in the `S_D.html` template).
- `S_D.html` is used to render the list of messages from the `ab` model.

For `S_D.html`, here's how you render the list:

```html
{% extends 'F_D.html' %}

{% block content %}
    <h1><b>!USERS MESSAGES!</b></h1>

    <ul>
        {% for ab_item in object_list %}
            <li>{{ ab_item.text }}</li>  <!-- Displays each message stored in the ab model -->
        {% endfor %}
    </ul>
{% endblock %}
```

### 5. **admin.py**
You register the `ab` model in `admin.py` to allow it to be managed through the Django Admin interface.

```python
from django.contrib import admin
from .models import ab

admin.site.register(ab)  # Registers the ab model to appear in the Django Admin panel.
```

### 6. **tests.py**
In `tests.py`, you have test cases that check if the view correctly renders the template and returns a 200 status code:

```python
from django.test import SimpleTestCase
from django.urls import reverse

class TestViews(SimpleTestCase):
    def test_1(self):
        response = self.client.get('/PM_A/')
        self.assertEqual(response.status_code, 200)  # Checks if the status code is 200, meaning the page loaded correctly.

    def test_2(self):
        response = self.client.get(reverse('PM_A'))  # Uses the URL name to generate the URL.
        self.assertEqual(response.status_code, 200)

    def test_3(self):
        response = self.client.get(reverse('PM_A'))
        self.assertTemplateUsed(response, 'S_D.html')  # Verifies that the correct template is used.
```

---

## 🔧 Running the Application

To run your Django application, make sure you have completed the installation and setup steps, including creating a superuser if you want to access the Admin interface.

1. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   This starts the Django development server. By default, the server will run on `http://127.0.0.1:8000/`.

2. **Access the Admin Panel**
   - To access the Django Admin interface, visit `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created earlier.

3. **Visit the Application's Home Page**
   - After starting the server, navigate to `http://127.0.0.1:8000/` in your browser to view the list of messages from the `ab` model, rendered using the `S_D.html` template.

---



## 🛠 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Amin-moniry-pr7/DJANGO_PRACTICE_CODE.git
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory and configure your settings like the secret key.

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the Django Admin:
   ```bash
   python manage.py createsuperuser
   ```


## 🔧 Git Commands
To set up a Git repository and push changes:
```bash
🚀 git init
📌 git add *
📝 git commit -m "Django_Project"
🔗 git remote add amin "repository_address"
⬆ git push amin master
```


   
## 📜 License
🔖 This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License.**

```
Copyright (c) 2025 Amin Moniry
You are free to use and modify this code for non-commercial purposes.
```


## 📍 GitHub Repository

You can find the full code of the project on GitHub at the following link:

https://github.com/Amin-moniry-pr7

