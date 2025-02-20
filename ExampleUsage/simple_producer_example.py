from Producer import Producer

def main():
    # Create a simple message
    message = {
        "user_id": 123,
        "action": "login",
        "timestamp": "2024-03-20T10:00:00"
    }

    # Create producer instance
    producer = None
    try:
        producer = Producer(topic='user-events')
        print("Sending message to Kafka...")
        producer.produce_message(message)
        print("Message sent!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up resources
        if producer:
            producer.close()
            print("Producer closed.")

if __name__ == "__main__":
    main() 