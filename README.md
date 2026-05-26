# 🤖 Agentic AI Applications

A collection of AI agent implementations demonstrating multi-agent architectures, tool integration, and real-world applications using modern LLM frameworks.

## Projects

| Project | Description | Status |
|---------|-------------|--------|
| [Financial AI Analyst](./Financial%20AI%20Analyst/) | Multi-agent system for stock analysis, market data, and financial news | ✅ Complete |

## Tech Stack

- **Agent Framework:** Phidata
- **LLM Provider:** Groq (Llama 3.3 70B)
- **UI:** Streamlit
- **Language:** Python 3.10+

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Agentic-AI-Applications.git
cd Agentic-AI-Applications
```

### 2. Create virtual environment
```bash
python -m venv .venv
```

### 3. Activate virtual environment
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure environment variables
```bash
cp .env.example .env
```

Add your API keys to `.env`:
```
GROQ_API_KEY=your_groq_api_key
PHIDATA_KEY=your_phidata_key
```

## API Keys

| Key | Source |
|-----|--------|
| GROQ_API_KEY | [console.groq.com/keys](https://console.groq.com/keys) |
| PHIDATA_KEY | [phidata.app](https://phidata.app) |

## License

MIT
