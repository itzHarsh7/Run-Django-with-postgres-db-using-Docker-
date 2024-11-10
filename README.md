# 🚀 **Django Project with Docker & PostgreSQL**

Welcome to the **Django Project**. This project leverages Docker for containerization, PostgreSQL as the database, and a **custom user model** using `AbstractBaseUser` and `BaseManager` for flexible user authentication.

---

## 📝 **Environment Variables**

Before running the project, you need to create a `.env` file in the root directory of your project with the following credentials:

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=5432  # Default PostgreSQL port
SECRET_KEY=your_django_secret_key
DJANGO_DEBUG=True  # Set to False in production

*Make sure the .env file is not shared publicly, and it is added to .gitignore to keep sensitive data secure.*

---

# 🛠️ **Building the Docker Container**
To build the Docker container, simply run:

docker-compose up --build

# 📋 **How It Works**

- *Database Connectivity:*
When you run the docker-compose up --build command, Docker will first ensure that the database is set up and connected correctly. It will also create necessary migrations for Django.
- *Automatic Migration & Role Creation*
The Docker container will automatically run Django migrations to set up the database schema. It will also create default roles, including a superuser role, which is predefined in the code.
- *Default Superuser Credentials:*
The superuser credentials (username and password) are pre-configured and baked into the code for development purposes. Once the server is up and running, you can access the admin panel.

---

# **📦 Docker Setup**

## Steps to Set Up the Project:
- Clone the repository.

- Create a .env file in the root directory (see above for required variables).

- Build and start the container with:
    - docker-compose up --build

- The server will start automatically, and migrations will be applied. After this, you can access the Django admin panel at:
 - http://localhost:8000/admin
 - Use the pre-configured superuser credentials to log in.

---

# **🧑‍💻 Project Structure**

- **Dockerfile**: Defines how to build the Docker image.
- **docker-compose.yml**: The configuration for Docker Compose.
- **authentication/:** Contains authentication logic, including the custom user model.
- **TestScope/:** The main Django application that contains settings and URLs.

---

# **💡 Key Features**
- **🦸‍♂️ Custom User Model:** Using AbstractBaseUser and BaseManager for flexible user management.
- **🛠️ Role-based Access Control:** Automatically creates roles, including a default superuser.
- **🔒 Secure Setup:** The .env file ensures sensitive data like passwords and secret keys are not hard-coded.

---

# **🚀 Run It Locally**
To run the project locally, simply ensure you have Docker and Docker Compose installed, then use the following commands:

- **Build the Docker container:**
    - *docker-compose up --build*
- Access the Django Admin at http://localhost:8000/admin

---

# **🧑‍💻 Tech Stack**
- 🐍 Django (Python Web Framework)
- 🐳 Docker (Containerization)
- 🐘 PostgreSQL (Database)
- 🌐 Django REST Framework (For API support)
- 📅 Future Improvements
- 🔐 Implement OAuth or JWT Authentication for more robust security.
- 🧹 Clean up and optimize Dockerfile for smaller image sizes.