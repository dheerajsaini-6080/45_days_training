"""
Q1: Student Profile Card using F-Strings and Type Hints
"""

from typing import Dict


def create_profile(profile: Dict[str, str]) -> str:
    return (
        f"Name  : {profile['name']}\n"
        f"Course: {profile['course']}\n"
        f"Role  : {profile['role']}\n"
        f"Skills: {', '.join(profile['skills'])}"
    )


student = {
    "name": "Dheeraj Saini",
    "course": "AI & DS",
    "role": "Student",
    "skills": ["Python", "ML", "Git"]
}

print(create_profile(student))