from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(10):
    msg = f"message-{i}".encode('utf-8')
    producer.send('demo-topic', msg)
    print(f"Sent: {msg}")
    time.sleep(1)

producer.flush()
