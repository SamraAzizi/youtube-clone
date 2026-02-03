# YouTube Clone - Django Web Application

A full-featured YouTube clone built with Django, replicating the core functionalities of the world's largest video-sharing platform. This project demonstrates modern web development practices with a focus on user experience, video handling, and social features.

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

