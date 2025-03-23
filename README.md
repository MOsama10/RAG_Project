# 📦 Retrieval-Augmented Generation (RAG) with PostgreSQL and Offline LLM

## 📝 Overview
This project demonstrates a full-stack setup that combines a PostgreSQL database with an offline Large Language Model (LLM) to implement Retrieval-Augmented Generation (RAG). Natural language questions are converted into SQL queries to retrieve data from the database and generate human-readable answers locally using an LLM.

## 🔧 Key Features

### 🗄️ Database Setup (PostgreSQL)
- Creates a PostgreSQL test database.
- Includes 5 to 10 tables, each with 5–6 meaningful fields.
- Tables contain up to 1,000 rows of realistic sample data.
- Optimized for fast querying with indexes and efficient schema design.

### 🤖 Offline Large Language Model
- Deploys a local LLM such as LLaMA, DeepSeek, or GPT-NeoX.
- Runs without cloud dependency (no OpenAI API).
- Includes quantization or performance tuning for efficient local inference.

### 🔍 RAG Implementation (with LangChain)
- Converts user questions to optimized SQL queries.
- Executes queries on PostgreSQL to fetch relevant information.
- Generates readable, contextual answers using offline LLMs.

## 📁 Project Structure
```
rag_project/
├── data/                   # Data files or database dumps
├── env/                    # Environment configs
├── llama_cpp/             # LLaMA model interface
├── llama-b*               # LLaMA binaries
├── db_query.py            # SQL execution and data handling
├── generate_data.py       # Populates PostgreSQL with sample data
├── langchain_sql.py       # LangChain interface and RAG logic
├── main.py                # Entry point for running the system
├── prompt_templates.py    # Prompts for question-to-SQL conversion
├── run_llama_cli.py       # CLI to run local LLM inference
├── test_Q.txt             # Sample test questions
├── requirements.txt       # Python dependencies
└── er_diagram.png         # Entity-Relationship diagram for DB
```

## 🚀 Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/MOsama10/rag_project.git
cd rag_project
```

### 2. Set Up the Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Initialize and Populate PostgreSQL
- Set up your PostgreSQL server and create a new database.
- Run `generate_data.py` to populate tables.

### 4. Deploy the Offline LLM
- Follow instructions in `llama_cpp/` or `run_llama_cli.py` to run the LLM locally.

### 5. Run the System
```bash
python main.py
```

## 🧪 Example Use Case
- Input: "Which products have the highest ratings this month?"
- Output: The system translates this to SQL, queries the DB, and generates a summary answer using the LLM.

## 🎥 Demo

[![Watch the demo](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://github.com/MOsama10/RAG_Project/blob/main/RAG_Task.mp4?raw=true)

---

Enjoy building local RAG systems with no cloud dependencies! 💡

