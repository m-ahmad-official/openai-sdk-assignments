# 🛡️ Input & Output Guardrails with OpenAI Agent SDK

This project demonstrates how to implement input and output guardrails using the OpenAI Agent SDK.
The system ensures that user prompts and agent responses follow specific rules before being processed or displayed.

---

## 📌 Features

**Input Guardrail**: Blocks math-related queries.

**Output Guardrail**: Blocks political content.

**Agent Integration**: Customer Support Agent with both guardrails.

---

## 🗂️ Project Structure

```bash
├── data_schema/
│ ├── math_output.py # Schema for math guardrail
│ └── politics_output.py # Schema for politics guardrail
│
├── guardrail_function/
│ ├── input_guardrail_function.py # Checks if input is math
│ └── output_guardrail_function.py # Checks if output contains politics
│
├── my_agent/
│ ├── agent.py # Customer support agent with guardrails
│ └── politics_agent.py # Agent to analyze political content
│
├── my_config/
│ └── gemini_config.py # Gemini model configuration (API key, base URL)
│
├── main.py # Entry point to run the agent
└── README.md # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Environment Variables

Create a .env file in the root directory:

```ini
GEMINI_API_KEY=your_api_key_here
GEMINI_BASE_URL=your_base_url_here
```

---

## 🚀 Running the Project

```bash
python main.py
```

If the input contains math → ❌ Blocked.

If the agent tries to respond with politics → ❌ Blocked.

Otherwise → ✅ Response is displayed.

---

## 🛡️ Guardrail Logic

### 🔢 Input Guardrail (Math)

Uses MathOutPut schema.

Detects if query is math-related.

Example:

```yaml
Enter your question: What is 2+2?
Input guardrail tripped: invalid prompt (math detected)
```

### 🏛️ Output Guardrail (Politics)

Uses PoliticsOutput schema.

Detects political content in responses.

Example:

```yaml
Enter your question: Tell me about elections
Output guardrail tripped: response contained politics
```

---

## 🎯 Learning Objectives

Understand how to integrate guardrails with agents.

Learn to apply structured validation (Pydantic models) for safe input/output.

Explore custom rule-based moderation using OpenAI Agent SDK.
