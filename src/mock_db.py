# src/mock_db.py

MOCK_ACTIVE_DIRECTORY = {
    "jdoe": {
        "netid": "jdoe",
        "full_name": "John Doe",
        "status": "Active",
        "bad_password_count": 0,
        "groups": ["Domain Users", "Workstation_Users"],  # Missing 'Finance_DB_Users'
        "assigned_ip": "10.100.12.45"
    },
    "asmith": {
        "netid": "asmith",
        "full_name": "Alice Smith",
        "status": "Locked Out",
        "bad_password_count": 5,
        "groups": ["Domain Users", "Finance_DB_Users"],
        "assigned_ip": "10.100.12.88"
    }
}

MOCK_NETWORK_TELEMETRY = {
    "10.20.4.15": {
        "hostname": "db-fin-prod-01.internal",
        "zone": "PCI_SECURE",
        "status": "UP",
        "open_ports": [5432, 22],
        "interface_errors": 0
    },
    "10.100.12.45": {
        "hostname": "workstation-jdoe",
        "access_switch": "sw-floor2-core01",
        "port": "Gi1/0/22",
        "port_status": "Connected",
        "interface_errors": 0
    }
}

MOCK_FIREWALL_LOGS = [
    {
        "timestamp": "2026-09-22T16:30:00Z",
        "src_ip": "10.100.12.45",
        "dst_ip": "10.20.4.15",
        "dst_port": 5432,
        "action": "DENY",
        "rule_id": "DEFAULT_IMPLICIT_DENY",
        "reason": "Src NetID jdoe lacks required AD entitlement group 'Finance_DB_Users'"
    }
]

MOCK_RAG_DOCS = [
    "Policy FW-2026-SEC: Access to PCI_SECURE zone (10.20.4.0/24) requires explicit AD membership in group 'Finance_DB_Users' and an active ticket entry.",
    "Subnet Mapping: 10.100.12.0/24 is assigned to Floor 2 Corporate Workstations via 802.1X dynamic VLAN assignment."
]
