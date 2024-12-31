# Blog API Project

This project is a **Blog API** developed using **Django REST Framework (DRF)**, designed to demonstrate my expertise in backend development, containerization, and cloud deployment. The project implements essential features of a blogging platform with a focus on scalability and production readiness.

---

## Features Implemented

### 1. Backend Development:
- Built RESTful APIs for blog posts and user authentication using Django REST Framework (DRF).
- Utilized a custom user model for flexible user authentication and management.
- Documentating the api endpoint using drf-spectacular

### 2. Authentication:
- Implemented authentication and authorization using Django's default token-based system.
- Used permissions to secure APIs and ensure fair usage.

### 3. Static File Management:
- Served static files using **WhiteNoise** for local development.
- Configured **Nginx** to handle static files efficiently in production.

### 4. Production-Ready Deployment:
- Dockerized the application using a well-structured `Dockerfile` and `docker-compose`.
- Deployed the application on **AWS** with the following setup:
  - Used **AWS Elastic Container Registry (ECR)** to store and manage Docker images.
  - Configured and deployed the app on **AWS EC2** instances for scalable infrastructure.
- Configured **Gunicorn** as the WSGI server and **Nginx** as the reverse proxy for load balancing and security.

### 5. Environment Management:
- Created separate `.env` files for development and production environments to manage sensitive information securely.
- Applied Django security best practices (e.g., SSL redirection, secure cookies, HSTS).

### 6. Database Integration:
- Utilized **PostgreSQL** as the database.

### 7. Containerization and Orchestration:
- Developed a `docker-compose.prod.yml` file to orchestrate containers for production, including:
  - Web application container (Gunicorn-based Django app).
  - Database container (PostgreSQL).

### 8. Cloud Deployment:
- Automated image builds and pushes to **AWS ECR** for seamless updates.
- - Successfully deployed the Dockerized application to **AWS EC2**.

---

## Technology Stack

- **Framework**: Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Containerization**: Docker, Docker Compose  
- **Web Server**: Gunicorn  
- **Reverse Proxy**: Nginx  
- **Cloud Provider**: AWS (IAM, ECR, EC2, Elastic IP)  
- **Static File Management**: WhiteNoise, Nginx  
