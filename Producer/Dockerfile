FROM python:3.10.18
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "producer:app", "--host", "0.0.0.0", "--port", "8080"]
