# 📈 Financial AI Analyst

A multi-agent AI system that combines web search and financial data capabilities to provide comprehensive stock analysis, market insights, and real-time financial information.

## Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Finance Agent** | Stock prices, fundamentals, analyst recommendations | YFinance |
| **Web Search Agent** | Latest news and web information | DuckDuckGo |
| **Multi-Agent** | Combines both for comprehensive analysis | Both |

## How to Run

### Streamlit Chat UI
```bash
streamlit run "Financial AI Analyst/app.py"
```

### Command Line
```bash
python "Financial AI Analyst/finantial_agent.py"
```

## Example Queries

- "What is the current stock price of NVDA?"
- "Show me analyst recommendations for TSLA"
- "Compare the fundamentals of AAPL and MSFT"
- "Summarize analyst recommendations and share the latest news for NVDA"

## Architecture

```
User Query
    │
    ▼
Multi-Agent (Supervisor)
    ├── Finance Agent → YFinance API → Stock data, fundamentals, recommendations
    └── Web Search Agent → DuckDuckGo → Latest news, web results
    │
    ▼
Combined Response
```

## Tech Stack

- **Framework:** Phidata
- **LLM Provider:** Groq
- **LLM Models:**
  - Web Search Agent: `llama-3.3-70b-versatile` (Meta Llama 3.3 70B)
  - Finance Agent: `qwen/qwen3-32b` (Qwen 3 32B)
  - Multi-Agent Supervisor: `openai/gpt-oss-120B` (GPT OSS 120B)
- **Tools:** YFinance, DuckDuckGo
- **UI:** Streamlit
