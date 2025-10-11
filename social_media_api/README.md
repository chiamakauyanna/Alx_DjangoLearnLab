# 🧩 Social Media API

A RESTful social media backend built with **Django Rest Framework (DRF)** and deployed on **Render**.  
It allows user registration, login, following/unfollowing other users, creating posts, adding comments, and liking posts.

---

## 🚀 Live API
**Base URL:**  
👉 [https://social-media-api-g0nq.onrender.com](https://social-media-api-g0nq.onrender.com)

---

## 📌 Key Features

- 🔐 **User Authentication** — Register, login, and manage user profiles  
- 👥 **Follow System** — Follow/unfollow other users  
- 📝 **Post Management** — Create, update, and delete posts  
- 💬 **Comments** — Add and view comments on posts  
- ❤️ **Likes** — Like and unlike posts  
- ⚙️ **Token Authentication** using DRF tokens  
- ☁️ **Deployed on Render** with PostgreSQL or SQLite fallback

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend Framework | Django & Django REST Framework |
| Database | PostgreSQL (Render) / SQLite (local) |
| Deployment | Render |
| Authentication | Token-based (DRF Tokens) |

---

## ⚙️ Setup & Installation (Local Development)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/social_media_api.git
cd social_media_api
````

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File

```bash
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` for the admin panel.

---

## 🧑‍💻 API Endpoints

### 🔹 Auth & Profile

| Method | Endpoint                      | Description                      |
| ------ | ----------------------------- | -------------------------------- |
| `POST` | `/api/accounts/register/`     | Register a new user              |
| `POST` | `/api/accounts/login/`        | Login and get token              |
| `GET`  | `/api/accounts/profile/`      | View or update user profile      |
| `GET`  | `/api/accounts/create-admin/` | Create admin user (Render setup) |

### 🔹 Users & Follows

| Method | Endpoint                             | Description     |
| ------ | ------------------------------------ | --------------- |
| `POST` | `/api/accounts/users/<id>/follow/`   | Follow a user   |
| `POST` | `/api/accounts/users/<id>/unfollow/` | Unfollow a user |

### 🔹 Posts

| Method      | Endpoint           | Description            |
| ----------- | ------------------ | ---------------------- |
| `GET`       | `/api/posts/`      | List all posts         |
| `POST`      | `/api/posts/`      | Create a post          |
| `GET`       | `/api/posts/<id>/` | Retrieve a single post |
| `PUT/PATCH` | `/api/posts/<id>/` | Update a post          |
| `DELETE`    | `/api/posts/<id>/` | Delete a post          |

### 🔹 Comments & Likes

| Method | Endpoint                    | Description   |
| ------ | --------------------------- | ------------- |
| `POST` | `/api/posts/<id>/comments/` | Add a comment |
| `POST` | `/api/posts/<id>/like/`     | Like a post   |
| `POST` | `/api/posts/<id>/unlike/`   | Unlike a post |

---

## 🔑 Authentication

Use **Token Authentication** in your API requests:

```
Authorization: Token <your_token_here>
```

---

## 🧰 Admin Panel

Access: [https://social-media-api-g0nq.onrender.com/admin/](https://social-media-api-g0nq.onrender.com/admin/)

Default superuser (if created via `/api/accounts/create-admin/`):

```
Username: admin
Password: Admin@12345
```

---

## 🛠 Deployment (Render)

### Environment Variables

Set these in your Render dashboard under **Environment**:

```
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-render-postgres-url
ALLOWED_HOSTS=social-media-api-g0nq.onrender.com
```

### Procfile

```
web: gunicorn social_media_api.wsgi
```

---

## 👤 Author

**Chiamaka Uyanna**
🔗 LinkedIn: [@chiamakauyanna](https://www.linkedin.com/in/chiamakauyanna/)
