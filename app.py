"""
app.py - Sample Python Project Showcase
This script demonstrates basic data parsing and automation logic in Python.
"""

def generate_project_summary(project_name, language, status="Completed"):
    """Generates a structured log for portfolio projects."""
    summary = {
        "project_name": project_name,
        "primary_language": language,
        "status": status
    }
    return summary

def main():
    projects = [
        ("Portfolio Website", "HTML / Bootstrap"),
        ("Data Scraper Tool", "Python"),
        ("CSV File Cleaner", "Python")
    ]
    
    print("--- My Developer Portfolio Projects ---")
    for name, lang in projects:
        info = generate_project_summary(name, lang)
        print(f"Project: {info['project_name']} | Stack: {info['primary_language']} | Status: {info['status']}")

if __name__ == "__main__":
    main()