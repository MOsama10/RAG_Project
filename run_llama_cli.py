import subprocess
import os

def run_llama_cli(prompt, max_tokens=256, temperature=0.3):
    """Run a prompt through the local llama.cpp model and return the output"""
    llama_exe = os.path.join("llama_cpp", "main.exe")
    model_path = os.path.join("llama_cpp", "models", "mistral.gguf")

    try:
        result = subprocess.run(
            [llama_exe, "-m", model_path, "-p", prompt, "--temp", str(temperature), "--n-predict", str(max_tokens)],
            capture_output=True, text=True, timeout=400
        )
        output = result.stdout
        return output.strip()
    except Exception as e:
        return f"Error running llama.cpp: {e}"

def generate_sql(prompt):
    """Generate SQL from a prompt"""
    output = run_llama_cli(prompt)
    if "SQL:" in output:
        sql = output.split("SQL:")[-1].strip()
    else:
        sql = output
    sql = sql.replace("```sql", "").replace("```", "").replace("[end of text]", "").strip()
    if not sql.endswith(";"):
        sql += ";"
    return sql

def generate_summary(prompt):
    """Generate a natural language summary from a prompt"""
    output = run_llama_cli(prompt, max_tokens=512, temperature=0.7)
    return output.replace("[end of text]", "").strip()

if __name__ == "__main__":
    result = generate_sql("Convert this to SQL: Show all orders placed after January 1, 2023")
    print("\n\U0001F4C4 Model Output:\n")
    print(result)
