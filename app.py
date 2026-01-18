import os
import json
import time
from dotenv import load_dotenv
from openai import OpenAI
import pathway as pw

load_dotenv()

# API KEY SAFETY CHECK 
if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY not set. Please configure .env before running.")
    exit(1)
    
# OpenAI 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# Pathway: Live ingestion 
news = pw.io.fs.read(
    "./data",
    format="json",
    schema=pw.schema_from_dict({
        "title": str,
        "content": str,
        "source": str
    })
)

#  RAG logic 
def load_latest_documents(n=5):
    files = sorted(
        [f for f in os.listdir("data") if f.endswith(".json")],
        reverse=True
    )[:n]

    docs = []
    for f in files:
        with open(os.path.join("data", f)) as fp:
            item = json.load(fp)
            docs.append(item["title"] + "\n" + item.get("content", ""))

    return docs


def answer_question(question: str):
    context = load_latest_documents()

    prompt = f"""
You are a news analyst AI.
Answer the question using ONLY the news below.

News:
{chr(10).join(context)}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Use only the provided news context."},
            {"role": "user", "content": prompt}
        ]
    )

    print("\n" + "=" * 60)
    print("DEMO QUESTION:")
    print(question)
    print("-" * 60)
    print("DEMO ANSWER:")
    print(response.choices[0].message.content)
    print("=" * 60 + "\n")


# MAIN 
if __name__ == "__main__":
    print("Starting Pathway engine...")
    pw.run()  # starts live ingestion

    # Allow some time for news files to arrive
    time.sleep(12)

    # Run demo
    answer_question("What are the latest important news updates?")

    print("\nDemo completed successfully. Exiting.\n")

