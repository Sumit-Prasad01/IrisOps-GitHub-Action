# End-to-End MLOps Project with GitHub Actions & Kubernetes

An **end-to-end Machine Learning & MLOps project** showcasing how to build, train, package, and deploy an ML application using **Flask, Docker, GitHub Actions, and Kubernetes**.

This project focuses on **CI/CD automation with GitHub Actions**, production-ready ML pipelines, and cloud/Kubernetes-compatible deployment.

---

## 📌 Project Overview

This project demonstrates the complete ML workflow:
- Data processing and experimentation using Jupyter notebooks
- Model training through a structured pipeline
- Flask-based web application for inference
- Docker-based containerization
- CI/CD automation using **GitHub Actions**
- Deployment using **Kubernetes YAML manifests**

It is designed to reflect **real-world ML engineering practices**.

---

## 🧠 Tech Stack

| Category | Tools |
|--------|------|
| Programming | Python |
| Machine Learning | Scikit-learn |
| Web Framework | Flask |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Orchestration | Kubernetes |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
├── .github/workflows/             # GitHub Actions CI/CD pipelines
├── artifacts/                     # Trained models and outputs
├── notebooks/                     # Jupyter notebooks for testing & EDA
├── pipeline/                      # Training & inference pipelines
├── src/                           # Core ML source code
├── static/                        # Static files for Flask app
├── templates/                     # HTML templates
├── application.py                 # Flask app entry point
├── main.py                        # Training pipeline entry point
├── kubernetes-deployment.yaml     # Kubernetes deployment file
├── Dockerfile                     # Docker configuration
├── requirements.txt               # Dependencies
├── pyproject.toml                 # Project metadata
├── setup.py                       # Package setup
├── README.md                      # Documentation
└── .gitignore
```

---

## ⚙️ Local Setup

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd mlops-github-actions-project
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate       # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Model Training

Run the complete training pipeline:
```bash
python main.py
```

This step includes:
- Data preprocessing
- Feature engineering
- Model training
- Artifact generation

Artifacts are stored inside the `artifacts/` directory.

---

## 🌐 Flask Application

Run the Flask app locally:
```bash
python application.py
```

Access the application at:
```
http://localhost:5000
```

---

## 🐳 Docker

### Build Docker Image
```bash
docker build -t mlops-github-actions .
```

### Run Docker Container
```bash
docker run -p 5000:5000 mlops-github-actions
```

---

## 🔁 CI/CD with GitHub Actions

- CI/CD workflows are defined in `.github/workflows/`
- Pipeline stages include:
  - Code checkout
  - Dependency installation
  - Pipeline execution
  - Docker image build
  - Kubernetes deployment

Each push to the repository triggers the workflow automatically.

---

## ☸️ Kubernetes Deployment

Deploy the application to Kubernetes:
```bash
kubectl apply -f kubernetes-deployment.yaml
```

Check deployment status:
```bash
kubectl get pods
kubectl get services
```

---

## 🚀 Key Features

- End-to-end ML pipeline
- Production-ready Flask service
- Dockerized application
- GitHub Actions–based CI/CD
- Kubernetes deployment
- Clean and scalable project layout

---



