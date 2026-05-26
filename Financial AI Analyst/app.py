from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Page config
st.set_page_config(page_title="Finance AI Agent", page_icon="📈", layout="wide")
st.title("📈 Finance AI Multi-Agent")
st.caption("Powered by Groq + Phidata | Web Search & Financial Data")

# Sidebar - Agent selection
st.sidebar.header("Select Agent")
agent_choice = st.sidebar.radio(
    "Choose an agent:",
    ["Multi-Agent (Both)", "Web Search Agent", "Finance Agent"],
)

# Initialize agents
@st.cache_resource
def get_web_agent():
    return Agent(
        name="Web Search Agent",
        role="Search the web for information",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )

@st.cache_resource
def get_finance_agent():
    return Agent(
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

@st.cache_resource
def get_multi_agent():
    return Agent(
        team=[get_web_agent(), get_finance_agent()],
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=["Always include sources", "Use tables to display financial data"],
        show_tool_calls=True,
        markdown=True,
    )

# Select active agent
if agent_choice == "Web Search Agent":
    active_agent = get_web_agent()
elif agent_choice == "Finance Agent":
    active_agent = get_finance_agent()
else:
    active_agent = get_multi_agent()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about stocks, finance, or search the web..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = active_agent.run(prompt)
                result = response.content if response else "Sorry, I couldn't process that request."
            except Exception:
                result = "⚠️ The agent encountered an error processing your request. Try a simpler query like 'What is the stock price of NVDA?'"
        st.markdown(result)

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": result})
