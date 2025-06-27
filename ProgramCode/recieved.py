import os
import sys
import pika

class main:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="gajendra ")
    # print(channel.queue_declare(queue="gajendra"))

    # channel.basic_publish(exchange='',routing_key="hello",body="Hello PY")
    # print(channel.basic_publish(exchange='',routing_key="hello",body="Hello PY"))
    # channel.close()

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)