# Dockerfile

# Utilise une image Python officielle
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /code

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le reste du projet
COPY . .

# Ouvrir le port 8000
EXPOSE 8000

# Commande par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
