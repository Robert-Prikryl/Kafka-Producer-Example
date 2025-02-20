import socket

conf = {
    # Kafka broker(s) address
    'bootstrap.servers': 'localhost:9092',

    # Client identifier CAN BE REPLACED WITH A UNIQUE IDENTIFIER FOR THE PRODUCER
    'client.id': socket.gethostname(),

    # Acknowledgment settings (1: leader acknowledgment)
    'acks': '1',
    
    # Number of retries if the request fails
    'retries': 3,
    
    # Retry backoff time in milliseconds
    'retry.backoff.ms': 1000,
    
    # Maximum size of a request in bytes
    'message.max.bytes': 1000000
}