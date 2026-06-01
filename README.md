📌 Project Description

This project is a simple containerized Flask web application integrated with Redis for persistent visitor tracking. The application demonstrates Docker-based development, service communication, and live development workflows using Docker Compose.

The web app displays a dynamic page that counts how many times the homepage has been visited. Each request increments a counter stored in Redis, ensuring the count persists even if the container restarts.

The project also includes a modern UI upgrade with Bootstrap styling, dark/light mode toggle, and a user input feature. It is fully containerized using Docker and orchestrated with Docker Compose, allowing easy deployment and development.

🚀 Key Features
Flask web server running inside Docker
Redis integration for persistent counter storage
Docker Compose multi-service setup (web + redis)
Live development using volume mounting
Modern UI (Bootstrap, dark mode, animations)
Visitor name input support
Real-time page updates during development
🧠 Technologies Used
Python (Flask)
Redis
Docker
Docker Compose
HTML / CSS / Bootstrap


# 🚀 Flask + Redis + Docker Project

A simple containerized web application built with Flask and Redis. The app counts page visits and displays them in a modern UI. It is fully dockerized using Docker Compose for easy development and deployment.

---

## 📌 Features

- Flask web application
- Redis-backed visit counter
- Docker & Docker Compose setup
- Live code updates using volumes
- Bootstrap-based UI
- Dark/Light mode toggle
- Visitor name input

---

## 🏗️ Project Structure
project3/
│── app.py
│── tempaltes/
  -base.html  
  -index.html  
  -error.html
│── requirements.txt
│── Dockerfile
│── docker-compose.yml


---

## ⚙️ Setup & Run

### 1. Clone the project
```bash
git clone <repo-url>
cd project3
