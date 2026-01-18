# Live News RAG — DataQuest 2026

## Overview
This project is a **Dynamic Retrieval-Augmented Generation (RAG)** system developed for **DataQuest 2026 (Megalith, IIT Kharagpur)**.

The system demonstrates **Live AI** by continuously ingesting changing news data and generating answers that always reflect the **latest available information**, without restarting the system or re-indexing data.


## Problem Motivation
Most traditional RAG systems rely on static datasets. Once the data changes, the system becomes outdated unless it is manually restarted or re-indexed.

This project solves that limitation by:
- Ingesting data continuously
- Updating the knowledge base incrementally
- Producing answers that change automatically as new data arrives


## High-Level Architecture
```
Live News API
↓
Python News Writer (Streaming)
↓
File-based Data Stream (JSON)
↓
Pathway Real-Time Ingestion Engine
↓
Latest Document Retrieval
↓
OpenAI Language Model (RAG)
↓
Real-Time Answer
```


## Key Features
-  **Real-time data ingestion** using Pathway file-system streaming
-  **Incremental updates** without restarting or re-indexing
-  **Retrieval-Augmented Generation (RAG)** using OpenAI
-  Answers reflect the **latest state of the data**
-  Deterministic and reproducible demo flow
-  Clean and minimal codebase


## Technology Stack
- **Pathway** — real-time data processing engine
- **Python 3.10**
- **OpenAI API** — large language model
- **NewsAPI** — live news data source


## Project Structure
```
dataquest-live-news-rag/
│
├── app.py              # Main application: Pathway ingestion + RAG demo
├── write_news.py       # Live news fetcher (streams news into data/)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .env.example        # Environment variable template (API keys not committed)
│
├── data/               # Live data stream (JSON files written here)
│   └── news_*.json
│
└── venv/               # Python virtual environment
```

## How Real-Time Behavior Is Achieved

1. News articles are fetched continuously from a live API
2. Each article is written as a new JSON file
3. Pathway automatically detects file additions and ingests them incrementally
4. The retrieval layer always reads the most recent documents
5. Asking the same question after new data arrives produces a **different answer**

This demonstrates **true real-time reasoning** over evolving data.


## How to Run the Project

### 1. Environment Setup
```
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a .env file in the project root:

```
NEWS_API_KEY=your_newsapi_key
OPENAI_API_KEY=your_openai_key
```

If the OpenAI API key is not configured, the application will exit gracefully
with a clear message indicating that the required environment variable is missing.

### Environment Variables & Security

This project uses API keys for external services (NewsAPI and OpenAI).  
For security reasons, **API keys are not committed to the public repository**.

- The `.env` file is intentionally excluded from version control.
- A template file `.env.example` is provided in the repository to indicate
  the required environment variables.

Before running the project, evaluators should:
1. Create a local `.env` file using `.env.example` as reference
2. Add their own valid API keys

This follows standard industry practices for handling sensitive credentials.

### 3. Run the System

Terminal 1 (RAG system)

```
python app.py

```

Terminal 2 (Live data writer)

```
python write_news.py
```

Let the writer run for 10–15 seconds, then stop it.

## Demo Scenario
Question:

What are the latest important news updates?

### Demo Steps:
1. Start the RAG system
2. Inject live news articles
3. Observe Pathway ingest data in real time
4. Ask the question
5. Stop the writer, restart it, and ask again
6. Observe that the answer changes automatically

This proves the system reacts instantly to new information.

## Why Pathway?
Pathway enables:

- Unified batch and streaming pipelines

- Incremental computation

- Low-latency updates on changing data

These capabilities make it ideal for building Live AI systems.

## Team Information

Team Size: 2

Team Members: Mrunali Kamerikar, Riddhima Taose

Event: DataQuest 2026 (Megalith, IIT Kharagpur)
