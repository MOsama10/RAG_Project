from langchain.sql_database import SQLDatabase
import os
from dotenv import load_dotenv
import json

load_dotenv()

def get_db_connection():
    return SQLDatabase.from_uri(
        f"postgresql+psycopg2://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
    )

def format_results_for_prompt(results):
    if not results:
        return "No results found."
    formatted = json.dumps(results, indent=2, default=str)
    if len(formatted) > 2000:
        sample = results[:5]
        formatted = json.dumps(sample, indent=2, default=str)
        formatted += f"\n\n... and {len(results) - 5} more results (showing only first 5)"
    return formatted
