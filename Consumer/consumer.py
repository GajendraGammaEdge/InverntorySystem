import pika
import json
from fastapi import  FastAPI
app = FastAPI()

def process_action(action_message):
    print(f"Processing action {action_message}")
    mess = {
        "action_Type": "Action_Proces",
        "message": action_message['sender_id'],
        "status": "Processed"
    }
    return mess

def action_on(ch, method, properties, body):
    action_data = json.loads(body)
    print("Message is being received")
    response_mes = process_action(action_data)
    rabbitMq = RabbitManagerMQ(host="rabbitmq", username="Gajendra@9109", password="123456")
    rabbitMq.publish_message("publish_message", response_mes)
    ch.basic_ack(delivery_tag=method.delivery_tag)

class RabbitManagerMQ:

    def __init__(self, host, username, password):
        self.host = host
        self.credentials = pika.PlainCredentials(username, password)

    def connection_check(self):
        return pika.BlockingConnection(pika.ConnectionParameters(self.host, credentials=self.credentials))

    def publish_message(self, queue: str, message: dict):
        connection = self.connection_check()
        channel = connection.channel()
        try:
            channel.queue_declare(queue=queue, durable=True)
            channel.basic_publish(
                exchange="",
                routing_key=queue,
                body=json.dumps(message),
                properties=pika.BasicProperties(delivery_mode=2),
            )
        finally:
            channel.close()
            connection.close()

def start_consuming():
    rabbitMq = RabbitManagerMQ(host="rabbitmq", username="Gajendra@9109", password="123456")
    connection = rabbitMq.connection_check()
    channel = connection.channel()

    channel.queue_declare(queue="action_queue", durable=True)
    channel.basic_consume(queue="action_queue", on_message_callback=action_on, auto_ack=False)
    print("Starting to consume messages...")
    channel.start_consuming()

@app.get("/receive")
async  def getting_message():
    return start_consuming();

if __name__ == '__main__':
        getting_message()