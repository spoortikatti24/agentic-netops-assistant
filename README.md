# 🤖 Agentic NetOps & Identity Assistant

An intelligent AI agent built with LangChain and Ollama (llama3.1) for cross-domain network troubleshooting.

## 🚀 Quickstart Guide

`✨ Key Features
Autonomous Multi-Tool Reasoning: Uses the ReAct (Reasoning + Acting) framework to sequence investigations across identity, network state, security logs, and policy docs.

Identity & Access Management (IAM) Inspection: Queries mock Active Directory records to check user status, account lockouts, and security group memberships.

Network Telemetry Integration: Fetches real-time status, port states, and operational telemetry for network assets and gateway devices.

Firewall Log Correlation: Analyzes source-to-destination traffic logs to pinpoint exact dropped packets and blocked ports (e.g., DENY on port 3306).

RAG-Driven Policy Retrieval: Searches internal Knowledge Base / IPAM documentation to cross-reference traffic drops against organizational compliance rules.

100% Local Execution: Powered by ollama/llama3.1 with native tool-calling capabilities—keeping logs and operational data completely offline.

🏗️ System Architecture
Plaintext
               +----------------------------------+
               |  User Query (PowerShell/CLI)     |
               +----------------------------------+
                                |
                                v
               +----------------------------------+
               |       LangChain Agent Loop       |
               |       (Ollama / llama3.1)        |
               +----------------------------------+
                                |
        +-----------------------+-----------------------+
        |                       |                       |
        v                       v                       v
+---------------+       +---------------+       +---------------+
|    AD Tool    |       | Network Tool  |       | Firewall Tool |
| (mock_db.py)  |       | (mock_db.py)  |       | (mock_db.py)  |
+---------------+       +---------------+       +---------------+
        |                       |                       |
        +-----------------------+-----------------------+
                                |
                                v
               +----------------------------------+
               |   Unified Root Cause Diagnosis   |
               +----------------------------------+
The agent executes a tool-calling loop over four core enterprise tools:

ad_tool: Queries Active Directory user status, lockout flags, and group memberships.

net_tool: Checks router/switch port status, interface state, and operational IP telemetry.

log_tool: Searches firewall ALLOW / DENY traffic logs by source and destination IPs.

doc_tool: Performs search/RAG over internal IPAM, VLAN, and network security policies.

📁 Repository Structure
Plaintext
agentic-netops-assistant/
├── src/
│   ├── agent.py          # Main ReAct agent loop using ChatOllama & tool execution
│   ├── mock_tools.py     # LangChain tool bindings wrapping simulated queries
│   └── mock_db.py        # Simulated Active Directory, telemetry logs, & policy docs
├── config.py             # Project configuration and local model settings
├── requirements.txt      # Frozen Python dependencies
├── .gitignore            # Ignores venv, caches, and environment files
├── LICENSE               # MIT License
└── README.md             # Project documentation
🚀 Quickstart Guide
Prerequisites
Python 3.10+

Ollama installed on Windows/Linux/macOS

1. Model Setup
Pull the local LLM with native tool-calling capabilities:

PowerShell
ollama pull llama3.1
2. Environment Setup
Clone the repository, create a virtual environment, and install dependencies:

PowerShell
git clone [https://github.com/spoortikatti24/agentic-netops-assistant.git](https://github.com/spoortikatti24/agentic-netops-assistant.git)
cd agentic-netops-assistant

python -m venv venv
.\venv\Scripts\Activate.ps1   # On Windows PowerShell
pip install -r requirements.txt
3. Run the Assistant
Execute the main agent logic:

PowerShell
python src\agent.py
💡 Example Execution
Sample Input Query:

"Why can't user 'jdoe' access the database server at 10.20.4.15?"

Agent Diagnostic Trace:

AD Lookup: Checks jdoe -> Identifies user belongs to DB-Admins and is Active (not locked out).

Network Query: Checks 10.20.4.15 -> Confirms server interface is UP.

Firewall Log Search: Queries traffic between user IP (10.10.2.45) and DB server (10.20.4.15) -> Identifies DENY entries on port 3306.

Policy Doc Lookup: Searches security guidelines -> Discovers Rule 104 requiring explicit Zero-Trust access request for database subnets.

🛠️ Troubleshooting & Common Fixes
Ollama Tool Error (status code: 400): Ensure you are using llama3.1 (or qwen2.5) instead of llama3:latest, as older base models do not support function-calling schemas.

Import Errors for ChatOllama: Make sure langchain-ollama is installed in your venv (pip install langchain-ollama) rather than relying on legacy langchain_community.

🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.powershell
ollama pull llama3.1
python src/agent.py
`
