def calculate_risk(threats):

    score = 0

    for threat in threats:

        if threat["risk"] == "Medium":
            score += 3

        elif threat["risk"] == "High":
            score += 5

        elif threat["risk"] == "Critical":
            score += 10

    return score