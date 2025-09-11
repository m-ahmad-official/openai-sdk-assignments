# 🛡️ Custom Web Search Tool

A simple web search utility powered by the Tavily API, designed to be integrated with AI agents. This tool retrieves structured web results, extracts relevant answers, and provides sources in a clean, consumable format.

---

## 🚀 Introduction

This project implements a custom web search tool using the Tavily API. It allows AI agents (or standalone scripts) to query the web and receive processed results that include both a summarized answer and source links with snippets.

---

## ✨ Features

Fetches live search results from the Tavily API

Returns summarized answers along with raw content

Formats results into an answer + sources structure for AI agent use

Lightweight and easy to integrate with other AI frameworks

---

## 📂 Project Structure

```bash
├── my_config/
│   └── tavily_config.py   # API key & base URL configuration
├── my_tool/
│   └── search_tool.py     # Core function to call Tavily API
├── my_agent/
│   └── search_agent.py    # Wrapper for AI agents
├── main.py                # Example entrypoint for CLI usage
└── README.md              # Documentation
```

---

## ⚙️ Installation

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

---

## 🔑 Configuration

You need to set up your Tavily API credentials. Create a .env file in the project root:

```ini
TAVILY_API_KEY=your_api_key_here
TAVILY_BASE_URL=https://api.tavily.com/search
```

---

## 🖥️ Usage

Run the tool via CLI:

```bash
python main.py
```

You’ll be prompted for a query:

```csharp
Enter your question: Who is Rawalpindi Express?
```

---

## 📝 Example Output

```kotlin
Shoaib Akhtar is a former Pakistani cricketer nicknamed the "Rawalpindi Express" for his fast bowling. He debuted for Pakistan and is known for his speed. The nickname reflects his roots in Rawalpindi, Pakistan.

Sources:
- Shoaib Akhtar (https://en.wikipedia.org/wiki/Shoaib_Akhtar)
  Shoaib Akhtar is a Pakistani former international cricketer and commentator. Nicknamed the "Rawalpindi Express", he is the fastest bowler in cricketing....

- Shoaib Akhtar Birthday: Celebrating the Rawalpindi Express (https://www.instagram.com/p/DNRCav9zyUN/)
  The Rawalpindi Express, Shoaib Akhtar, is a name synonymous with speed and aggression on the cricket field. As we celebrate his birthday,....

- How Shoaib Akhtar became the 'Rawalpindi Express' (https://www.msn.com/en-us/travel/article/fast-and-furious-how-shoaib-akhtar-became-the-rawalpindi-express/ar-AA1qChhF)
  Shoaib Akhtar, born in Rawalpindi, Pakistan, earned the nickname 'Rawalpindi Express' due to his extraordinary speed and roots. Debuting for Pakistan in....
```

---

## 🛠️ Troubleshooting

**Invalid API Key error** → Ensure your .env file has the correct TAVILY_API_KEY.

**Request failed** → Check TAVILY_BASE_URL matches Tavily’s endpoint.

**Empty results** → Try increasing max_results in search_tool.py.
