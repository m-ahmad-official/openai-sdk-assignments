# Multi-Agent Guardrail System

## 📌 Introduction

This project extends OpenAI’s Agent SDK handoff example by implementing input and output guardrails at both the agent level and run level.

We use a multi-agent setup with:

🌤 **Weather Agent** – Provides weather updates

✈️ **Flight Agent** – Provides flight schedules and fares

🏨 **Hotel Agent** – Provides hotel availability and bookings

The system enforces business rules:

🚫 **Input Guardrails** – Block queries about Indian cities.

🚫 **Output Guardrails** – Block responses about U.S. cities.

---

## 🏗 Architecture

### Run-Level Guardrails

Applied before any agent starts (input filter).

Applied after all agents finish (output filter).

### Agent-Level Guardrails

Each agent validates its own input/output before execution.

Agents handoff tasks between each other, but queries/responses are filtered through the guardrails pipeline.

---

## File Structure

```css
├── data_schema/
│   ├── india_cities_output.py
│   ├── usa_cities_output.py
├── guardrail_function/
│   ├── input_guardrail_function.py
│   ├── output_guardrail_function.py
├── my_agent/
│   ├── agents.py
├── my_config/
│   ├── gemini_config.py
├── main.py
```

---

## 🛡️ Guardrail Logic

### 1. Input Guardrails

Reject queries mentioning **Indian cities.**

Example:

❌ Weather in Delhi → Blocked

✅ Weather in Dubai → Allowed

### 2. Output Guardrails

Reject final outputs containing **U.S. cities.**

Example:

❌ Hotels in New York → Blocked Output

✅ Hotels in Dubai → Allowed

### 3. Guardrail Levels

**Agent-Level** → Validates before agent runs.

**Run-Level** → Ensures system-wide compliance before/after run.

---

## ⚙️ Installation

### 1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install dependencies:

```bash
uv sync
```

### 3. Set up environment variables in .env:

```bash
GEMINI_API_KEY=your_api_key_here
GEMINI_BASE_URL=https://api.gemini.com/v1
```

---

## 🚀 Usage

```bash
uv run main.py
```

Example session:

```yaml
Enter your query: flights dubai to channai
❌ Reject query

Enter your query: hotels in new york
❌ Blocked Output

Enter your query: weather in paris
✅ Final Answer: Your request has been transferred to the Weather Agent.
```

---

## ✨ Features

Multi-agent orchestration with handoffs.

Agent-level guardrails for early validation.

Run-level guardrails for system-wide compliance.

Works with OpenAI’s Agent SDK + custom Gemini model config.
