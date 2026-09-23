# src/agent.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

# Dynamic import fallbacks for AgentExecutor
try:
    from langchain.agents import AgentExecutor
except ImportError:
    try:
        from langchain.agents.agent import AgentExecutor
    except ImportError:
        from langchain_classic.agents import AgentExecutor

# Dynamic import fallbacks for create_tool_calling_agent
try:
    from langchain.agents import create_tool_calling_agent
except ImportError:
    try:
        from langchain.agents.tool_calling_agent.base import create_tool_calling_agent
    except ImportError:
        from langchain_classic.agents import create_tool_calling_agent

from src.mock_tools import (
    query_active_directory,
    query_network_state,
    query_firewall_logs,
    retrieve_architecture_docs,
)

@tool
def ad_tool(netid: str) -> dict:
    """Lookup AD user state, lockouts, and groups by NetID."""
    return query_active_directory(netid)

@tool
def net_tool(ip_address: str) -> dict:
    """Lookup network device state and telemetry by IP address."""
    return query_network_state(ip_address)

@tool
def log_tool(src_ip: str, dst_ip: str) -> dict:
    """Search firewall DENY/ALLOW logs between two IP addresses."""
    return query_firewall_logs(src_ip, dst_ip)

@tool
def doc_tool(query: str) -> list:
    """Search network policies and IPAM documentation."""
    return retrieve_architecture_docs(query)

tools = [ad_tool, net_tool, log_tool, doc_tool]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert NetOps & Identity AI Assistant. "
               "When investigating user connectivity or permission issues, ALWAYS inspect "
               "Active Directory status, check network state/logs, and review network security policies "
               "before giving a final diagnosis."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

def run_agent(query: str):
    llm = ChatOllama(model="llama3.1", temperature=0)
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor.invoke({"input": query})

if __name__ == "__main__":
    test_query = "Why can't user 'jdoe' access the database server at 10.20.4.15?"
    print(f"\n--- Running Mock Query: {test_query} ---\n")
    response = run_agent(test_query)
    print("\n--- Final Diagnosis ---\n")
    print(response["output"])
