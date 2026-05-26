from dotenv import load_dotenv
load_dotenv()

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Provide financial data, stock prices, analyst recommendations, and company fundamentals",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True,
    )],
    instructions=["Use tables to display financial data"],
    show_tool_calls=True,
    markdown=True,
)

# Playground app
app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
