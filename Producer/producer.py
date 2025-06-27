from fastapi import FastAPI, HTTPException
import pika
import uuid
import json
from pydantic import BaseModel

app = FastAPI()

class RabbitManagerMQ:
    def __init__(self, host: str, username: str, password: str):
        self.host = host
        self.credentials = pika.PlainCredentials(username, password)

    def check_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(self.host, credentials=self.credentials))

    def produce_message(self, queue: str, message: dict):
        connection = self.check_connection()
        channel = connection.channel()
        try:
            channel.queue_declare(queue=queue, durable=True)
            channel.basic_publish(
                exchange="",
                routing_key=queue,
                body=json.dumps(message),
                properties=pika.BasicProperties(delivery_mode=2)
            )
        finally:
            channel.close()
            connection.close()

rabbitMq = RabbitManagerMQ(host="rabbitmq", username="gajendra9109", password="123456")

class RequestModelMessage(BaseModel):
    data: str

@app.post("/sender")
async def Sending_Message(request: RequestModelMessage):
    try:
        sender_id = str(uuid.uuid4())
        message_data = {
            "type": "action",
            "sender_id": sender_id,
            "data": request.data
        }
        rabbitMq.produce_message("action_queue", message_data)
        return {"Status": "Action Sent", "action_id": sender_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")
