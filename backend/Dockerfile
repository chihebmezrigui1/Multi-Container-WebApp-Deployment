# Use Python image
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3402

CMD ["python", "app.py"]
