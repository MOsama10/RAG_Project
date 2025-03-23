# main.py
from run_llama_cli import generate_sql, generate_summary
from db_query import run_sql, get_schema_info
from prompt_templates import sql_template, summary_template
from langchain_sql import format_results_for_prompt
import json

def rag_pipeline(question):
    print(f"\n❓ User: \"{question}\"")
    schema_info = get_schema_info()
    sql_prompt = sql_template.format(question=question, schema_info=schema_info)
    sql_query = generate_sql(sql_prompt)
    print(f"\n📊 SQL Query: {sql_query}")
    try:
        results = run_sql(sql_query)
        formatted_results = format_results_for_prompt(results)
        summary_prompt = summary_template.format(
            question=question,
            sql_query=sql_query,
            query_results=formatted_results
        )
        summary = generate_summary(summary_prompt)
        print(f"\n💬 LLM Output: {summary}")
        return {
            "question": question,
            "sql_query": sql_query,
            "results": results,
            "summary": summary
        }
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return {
            "question": question,
            "sql_query": sql_query,
            "error": str(e)
        }

if __name__ == "__main__":
    print("🔍 RAG SQL Query System")
    print("=" * 40)
    while True:
        user_input = input("\nEnter your question (or 'exit' to quit): ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            break
        rag_pipeline(user_input)