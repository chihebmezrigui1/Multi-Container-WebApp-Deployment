# Final Project: Multi-Container Web Application Deployment

## Application Architecture Overview

This project consists of a web application with a **frontend** and **backend** deployed using **Docker** and **Kubernetes**. The application allows for interaction between the frontend and backend through RESTful APIs. The backend handles requests related to data processing and storage, while the frontend provides the user interface.

/ **Project Structure**
-- //app-data 
     log.txt
-- //backend
     app.py
     Dockerfile
     requirements.txt
-- //frontend
     //templates
       displayData.html
       index.html
     app.py
     Dockerfile
     requirements.txt
-- //kubernetes
    backend-deployment.yaml
    backend-hpa.yaml
    backend-pv.yaml
    backend-pvc.yaml
    backend-service.yaml
    frontend-deployment.yaml
    frontend-hpa.yaml
    frontend-service.yaml
docker-compose.yaml

### Components

- **Frontend**: The user interface built using a web framework flask. It communicates with the backend via API calls to fetch or send data.
- **Backend**: A RESTful API that handles logic for data processing, computations, and storage. It connects to a persistent data store in log.txt in app-data.
- **Docker Registry**: A local Docker registry (running on `localhost:5000`) is used to store and pull the Docker images for both frontend and backend.
- **Kubernetes**: The application is orchestrated using Kubernetes for deployment, scaling, and management of the frontend and backend containers.
- **Persistent Volume**: A PersistentVolume (backend-pv.yaml)  and PersistentVolumeClaim (backend-pvc.yaml) are used for backend data storage.

## Deployment Instructions

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Minikube**: Used to set up a local Kubernetes cluster.
    ```bash
        minikube stop
        minikube start

- **Docker Compose**: Used for managing multi-container Docker applications.
- **Kubernetes Cluster**: Can be set up with Minikube or any other Kubernetes provider.
- **kubectl**: The Kubernetes command-line tool for managing clusters.
      ```bash 
    kubectl apply -f backend-deployment.yaml
    kubectl apply -f frontend-deployment.yaml
    kubectl apply -f backend-service.yaml
    kubectl apply -f frontend-service.yaml
    kubectl apply -f backend-pv.yaml
    kubectl apply -f backend-pvc.yaml
    kubectl apply -f backend-hpa.yaml
    kubectl apply -f frontend-hpa.yaml


### 1. Deployment with Docker Compose

#### Build and Push Docker Images

1. **Run the Docker Registry**:
   ```bash
  docker run -d -p 5000:5000 --name registry registry   
  docker build -t localhost:5000/final-project-backend .


  Check Folder Images contain Screenshots :) 

