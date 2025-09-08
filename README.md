# buzzline-02-webb

Streaming data analytics using Apache Kafka. This project demonstrates real-time data filtering and analytics using Python producers and consumers.

## Overview

Apache Kafka is a streaming platform that uses publish-subscribe patterns:
- **Producers** publish streaming data to topics
- **Consumers** subscribe to topics to process data in real-time

This project includes custom scripts that simulate company chat analytics.

## Setup Requirements

- Python 3.11
- Apache Kafka running on WSL (Windows) or locally (Mac/Linux)
- Virtual environment (.venv)

## Quick Start

### 1. Setup Virtual Environment

**Windows:**
```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 2. Start Kafka

Follow the setup instructions in [SETUP_KAFKA.md](SETUP_KAFKA.md) to install and start Kafka.

### 3. Run Custom Company Chat Analytics

**Start the Producer (simulates company chat):**

Windows:
```powershell
.venv\Scripts\activate
py -m producers.kafka_producer_webb
```

Mac/Linux:
```bash
source .venv/bin/activate
python3 -m producers.kafka_producer_webb
```

**Start the Consumer (filters for data team messages):**

Open a new terminal and run:

Windows:
```powershell
.venv\Scripts\activate
py -m consumers.kafka_consumer_webb
```

Mac/Linux:
```bash
source .venv/bin/activate
python3 -m consumers.kafka_consumer_webb
```

## What the Custom Scripts Do

- **Producer (`kafka_producer_webb.py`)**: Simulates a busy company-wide chat with messages from different teams and channels
- **Consumer (`kafka_consumer_webb.py`)**: Filters messages to identify data team related content and provides real-time analytics:
  - Counts data team messages
  - Alerts on issues (failed, error, bug)
  - Celebrates successes (completed, running, up)
  - Detects keywords: data-team, ETL, pipeline, SQL, dashboard, analytics, warehouse, etc.

## Original Example Scripts

The project also includes the original example scripts:
- `producers/kafka_producer_case.py`
- `consumers/kafka_consumer_case.py`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE.txt) for details.