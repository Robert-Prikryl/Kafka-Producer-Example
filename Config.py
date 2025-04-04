import socket

conf = {
    # Kafka broker bootstrap servers (host:port)
    'bootstrap.servers': '',
    # Security protocol to use (PLAINTEXT, SSL, SASL_PLAINTEXT, SASL_SSL)
    'security.protocol': '',
    # SASL mechanism to use for authentication (PLAIN, GSSAPI, SCRAM-SHA-256, etc)
    'sasl.mechanism': '',
    # Username for SASL/PLAIN or SASL/SCRAM authentication
    'sasl.username': '',
    # Password for SASL/PLAIN or SASL/SCRAM authentication
    'sasl.password': '',

    # (Optional) Client identifier CAN BE REPLACED WITH A UNIQUE IDENTIFIER FOR THE PRODUCER
    'client.id': socket.gethostname(),
    # (Optional) Acknowledgment settings (1: leader acknowledgment) 
    'acks': '1',
    # (Optional) Number of retries if the request fails
    'retries': 3,
    # (Optional) Retry backoff time in milliseconds
    'retry.backoff.ms': 1000,
}