from kafka import KafkaConsumer

def run():
    consumer = KafkaConsumer("orders", "payments-completed", group_id="py-analytics",
                             bootstrap_servers="kafka:9092")
    for message in consumer:
        process(message)

def process(message):
    pass
