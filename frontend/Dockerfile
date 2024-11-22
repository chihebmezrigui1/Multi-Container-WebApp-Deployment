# Dockerfile pour le frontend
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port du frontend
EXPOSE 3403

# Démarrer l'application
CMD ["python", "app.py"]
