# Social Media REST API

A backend social media application built with **Python**, **Django**, and **Django REST Framework (DRF)**. The API enables users to register, authenticate, create posts, interact with other users, and receive notifications through secure RESTful endpoints.

---

## Features

- User registration and authentication
- User profile management
- Follow and unfollow users
- Create, edit, update, and delete posts
- Like and unlike posts
- Create and manage comments
- Personalized user feed
- User notifications
- RESTful API architecture
- Authentication and permission-based access control

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (can easily be configured for PostgreSQL or MySQL)
- Pillow (Media Uploads)
- Token Authentication

---

# Project Structure

```
social_media_api/
│
├── accounts/
├── posts/
├── notifications/
├── media/
├── social_media_api/
└── manage.py
```

---

# API Endpoints

## Authentication & User Management

Base URL

```
/api/accounts/
```

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register/` | Register a new user |
| POST | `/login/` | Authenticate a user |
| POST | `/logout/` | Log out the authenticated user |
| GET | `/profile/` | Retrieve the authenticated user's profile |
| GET | `/profile/<user_id>/` | View another user's profile |
| POST | `/follow/<user_id>/` | Follow a user |
| POST | `/unfollow/<user_id>/` | Unfollow a user |

---

## Posts

Base URL

```
/api/
```

### Posts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/posts/` | Retrieve all posts |
| POST | `/posts/` | Create a new post |
| GET | `/posts/<id>/` | Retrieve a single post |
| PUT | `/posts/<id>/` | Update a post |
| PATCH | `/posts/<id>/` | Partially update a post |
| DELETE | `/posts/<id>/` | Delete a post |

---

### Comments

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/comments/` | Retrieve comments |
| POST | `/comments/` | Create a comment |
| GET | `/comments/<id>/` | Retrieve a specific comment |
| PUT | `/comments/<id>/` | Update a comment |
| DELETE | `/comments/<id>/` | Delete a comment |

---

### Social Interactions

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/feed/` | Retrieve personalized feed |
| POST | `/posts/<id>/like` | Like a post |
| POST | `/posts/<id>/unlike` | Unlike a post |

---

## Notifications

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/notifications/` | Retrieve user notifications |

---

# Installation

Clone the repository

```bash
git clone https://github.com/laura-juma/social-media-api.git
```

Navigate to the project

```bash
cd social-media-api
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create an administrator account

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

---

# Authentication

Most endpoints require authentication.

Include the authentication token in the request header.

```
Authorization: Token <your_token>
```

or

```
Authorization: Bearer <access_token>
```

depending on your authentication implementation.

---

# Example JSON Response

```json
{
    "id": 1,
    "author": "Laura",
    "content": "My first post!",
    "likes": 8,
    "comments": 3,
    "created_at": "2026-07-25T10:30:00Z"
}
```

---

# Future Improvements

- Direct messaging
- Real-time chat with WebSockets
- Stories
- Hashtags
- Bookmarks
- Post sharing
- Email verification
- Swagger/OpenAPI documentation
- Rate limiting
- Deployment using Docker

---

# Author

**Laura Neema Juma**

Computer Science Student | Python Backend Developer

---