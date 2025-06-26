
FROM python:3.10.18
WORKDIR /app
COPY . /app
Run pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "consumer:app", "--host", "0.0.0.0", "--port", "8080"]
