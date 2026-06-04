def detect_threats(logs):

    threats = []

    failed_attempts = {}

    for log in logs:

        if log["event"] == "Failed Login":

            user = log["user"]

            failed_attempts[user] = (
                failed_attempts.get(user, 0) + 1
            )

            if failed_attempts[user] >= 3:

                threats.append({
                    "type":"Brute Force Attack",
                    "risk":"High",
                    "description":"Multiple failed logins"
                })

        if log["event"] == "Privilege Escalation":

            threats.append({
                "type":"Privilege Escalation",
                "risk":"Critical",
                "description":"Unauthorized admin access"
            })

        if log["event"] == "Malware Detected":

            threats.append({
                "type":"Malware Infection",
                "risk":"Critical",
                "description":"Suspicious executable uploaded"
            })

        if log["event"] == "Port Scan":

            threats.append({
                "type":"Network Reconnaissance",
                "risk":"Medium",
                "description":"Network scanning detected"
            })

    return threats