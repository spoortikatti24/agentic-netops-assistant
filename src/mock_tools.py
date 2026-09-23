# src/mock_tools.py
import time
from typing import Dict, Any, List
from src.mock_db import MOCK_ACTIVE_DIRECTORY, MOCK_NETWORK_TELEMETRY, MOCK_FIREWALL_LOGS, MOCK_RAG_DOCS

def query_active_directory(netid: str) -> Dict[str, Any]:
    """Queries simulated Active Directory for user account status and group memberships."""
    time.sleep(0.1)
    user = MOCK_ACTIVE_DIRECTORY.get(netid.lower())
    if not user:
        return {"status": "Error", "message": f"User '{netid}' not found in Active Directory."}
    return {"status": "Success", "data": user}

def query_network_state(ip_address: str) -> Dict[str, Any]:
    """Queries simulated network telemetry for interface, routing, and port status."""
    time.sleep(0.1)
    device = MOCK_NETWORK_TELEMETRY.get(ip_address)
    if not device:
        return {"status": "Error", "message": f"IP '{ip_address}' not found in network telemetry topology."}
    return {"status": "Success", "data": device}

def query_firewall_logs(src_ip: str, dst_ip: str) -> Dict[str, Any]:
    """Searches simulated firewall logs for recent traffic events between source and destination IPs."""
    time.sleep(0.1)
    matching_logs = [
        log for log in MOCK_FIREWALL_LOGS 
        if log["src_ip"] == src_ip and log["dst_ip"] == dst_ip
    ]
    return {"status": "Success", "count": len(matching_logs), "logs": matching_logs}

def retrieve_architecture_docs(query: str) -> List[str]:
    """Performs semantic lookup over mock architecture policies and IPAM documentation."""
    time.sleep(0.1)
    results = [doc for doc in MOCK_RAG_DOCS if any(word in doc.lower() for word in query.lower().split())]
    return results if results else [MOCK_RAG_DOCS[0]]
