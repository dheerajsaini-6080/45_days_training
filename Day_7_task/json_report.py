"""
Q2: JSON Report
"""

import json

with open("profile.json", "r") as file:
    data = json.load(file)

skills = [skill.upper() for skill in data["skills"]]

print(f"Name   : {data['name']}")
print(f"Role   : {data['role']}")
print(f"Skills : {', '.join(skills)}")