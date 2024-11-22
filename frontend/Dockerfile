# Use Python image
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8777

CMD ["python", "app.py"]
