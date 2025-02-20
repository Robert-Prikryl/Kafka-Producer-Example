# Simple Kafka Producer Example

This project demonstrates a basic implementation of a Kafka producer using Python and the confluent-kafka library.

## Prerequisites

- Python 3.6+
- Apache Kafka running locally (default: localhost:9092)
- confluent-kafka package

## Installation

Install requirements into venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Project Structure

The project is organized as follows:

- `Config.py`: Defines the configuration for the Kafka producer.
- `Producer.py`: Defines the `Producer` class for producing messages to Kafka.
- `ExampleUsage`: Contains example of how to use the `Producer` class in your project.

## Usage

To use the `Producer` class, follow these steps:

1. Import the `Producer` class:

```python
from Producer import Producer
```

2. Create a producer instance:

```python
producer = Producer(topic='your_topic_name')
```

3. Produce a message:

```python
producer.produce_message(message_data)
```

4. Close the producer:

```python
producer.close()
```

Example usage is in `ExampleUsage` folder.

## Configuration

The `Config.py` file contains the configuration for the Kafka producer. You can modify the configuration as needed.

