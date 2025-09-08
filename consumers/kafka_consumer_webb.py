"""
kafka_consumer_webb.py

Consume messages from a Kafka topic and process them.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os

# Import external packages
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_consumer import create_kafka_consumer
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

load_dotenv()

data_team_messages = 0

#####################################
# Getter Functions for .env Variables
#####################################


def get_kafka_topic() -> str:
    """Fetch Kafka topic from environment or use default."""
    topic = os.getenv("KAFKA_TOPIC", "unknown_topic")
    logger.info(f"Kafka topic: {topic}")
    return topic


def get_kafka_consumer_group_id() -> int:
    """Fetch Kafka consumer group id from environment or use default."""
    group_id: str = os.getenv("KAFKA_CONSUMER_GROUP_ID_JSON", "default_group")
    logger.info(f"Kafka consumer group id: {group_id}")
    return group_id



#####################################
# Define a function to process a single message
# #####################################

def process_message(message: str) -> None:
    """
    Process a single message and filter for data team related content.

    Counts data team messages and alerts on issues.

    Args:
        message (str): The message to process.
    """
    global data_team_messages
    
    logger.info(f"Processing message: {message}")
    
    # Data team keywords to look for
    data_keywords = [
        "data-team", "etl", "pipeline", "sql", "dashboard", "analytics", 
        "warehouse", "query", "database", "report", "data source"
    ]
    
    # Check if message is data team related
    message_lower = message.lower()
    is_data_related = any(keyword in message_lower for keyword in data_keywords)
    
    if is_data_related:
        data_team_messages += 1
        logger.warning(f"DATA TEAM MESSAGE #{data_team_messages}: {message}")
        
        # Specific alerts for different types of data issues
        if "failed" in message_lower or "error" in message_lower or "bug" in message_lower:
            logger.error("URGENT: Data team reporting an issue!")
        elif "completed" in message_lower or "running" in message_lower or "up" in message_lower:
            logger.info("GOOD NEWS: Data team reports success!")



#####################################
# Define main function for this module
#####################################


def main() -> None:
    """
    Main entry point for the consumer.

    - Reads the Kafka topic name and consumer group ID from environment variables.
    - Creates a Kafka consumer using the `create_kafka_consumer` utility.
    - Processes messages from the Kafka topic.
    """
    logger.info("START consumer.")

    # fetch .env content
    topic = get_kafka_topic()
    group_id = get_kafka_consumer_group_id()
    logger.info(f"Consumer: Topic '{topic}' and group '{group_id}'...")

    # Create the Kafka consumer using the helpful utility function.
    consumer = create_kafka_consumer(topic, group_id)

     # Poll and process messages
    logger.info(f"Polling messages from topic '{topic}'...")
    try:
        for message in consumer:
            message_str = message.value
            logger.debug(f"Received message at offset {message.offset}: {message_str}")
            process_message(message_str)
    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Error while consuming messages: {e}")
    finally:
        consumer.close()
        logger.info(f"Kafka consumer for topic '{topic}' closed.")

    logger.info(f"END consumer for topic '{topic}' and group '{group_id}'.")


#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
