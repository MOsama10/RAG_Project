from langchain.prompts.prompt import PromptTemplate

sql_template = PromptTemplate(
    input_variables=["question", "schema_info"],
    template="""
You are an expert SQL assistant.
The database has the following schema:
{schema_info}

Convert the following user question into a syntactically correct PostgreSQL query.
Only return the SQL query. Do not include any explanations.

Question: "{question}"
SQL:
"""
)

summary_template = PromptTemplate(
    input_variables=["question", "sql_query", "query_results"],
    template="""
You are a helpful assistant that explains database query results in natural language.

The user asked: "{question}"

The following SQL query was executed:
```sql
{sql_query}
```

And it returned these results:
{query_results}

Provide a clear, concise summary of these results that directly answers the user's question.
Focus on the most important insights and patterns in the data.
Do not mention SQL or queries in your response - just provide the answer as if you're directly responding to the user.
"""
)
