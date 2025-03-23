import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def run_sql(sql_query):
    conn = psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return [dict(zip(colnames, row)) for row in rows]

def get_schema_info():
    """Get schema information for all tables in the database"""
    conn = psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD")
    )
    cur = conn.cursor()
    
    # Get table names
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    tables = [row[0] for row in cur.fetchall()]
    
    schema_info = []
    
    for table in tables:
        cur.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = '{table}'
        """)
        columns = [f"{row[0]} ({row[1]})" for row in cur.fetchall()]
        schema_info.append(f"Table: {table}\\nColumns: {', '.join(columns)}\\n")
    
    cur.close()
    conn.close()
    
    return "\\n".join(schema_info)
