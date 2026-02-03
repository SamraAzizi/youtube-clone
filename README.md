# YouTube Clone - Django Web Application

A YouTube clone built with Django. This project demonstrates modern web development practices with a focus on user experience with django 

## 🌟 Features

### 🎬 Video Management
- **Video Upload & Processing**: Upload videos with thumbnails, titles, and descriptions


### 👤 User Features
- **User Authentication**: Secure registration, login, and password management


### 💬 Engagement Features
- **Like/Dislike System**: Express opinions on videos




## 🛠️ Technology Stack

### Backend
- **Django 4.2+**: Python web framework
- **Django REST Framework**: API development

### Frontend
- **HTML5/CSS3**: Modern semantic markup and styling
- **JavaScript (ES6+)**: Interactive features
- **Custom CSS**: YouTube-like interface components


## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+


## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/samraAzizi/youtube-clone.git
cd youtube-clone
```
### 2. Create Virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Environment Configuration
```bash
cp .env.example .env
```

### 4. Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```bash
youtube-clone/
├── accounts/              # User authentication and profiles
│   ├── models.py         # User models
│   ├── views.py          # Authentication views
│   ├── urls.py           # User-related URLs
│   └── templates/        # Auth templates
├── videos/               # Core video functionality
│   ├── models.py         # Video, Comment, Like models
│   ├── views.py          # Video views and API
│   └── templates/        # Video templates
├── youtube/            # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── static/              # Static files
│   ├── css/            # Stylesheets
├── templates/           # Base templates
│   └── base.html       # Main templat             
├── requirements.txt    # Python dependencies
└── manage.py          # Django management script
```