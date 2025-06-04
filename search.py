import sys
import os

LOG_PATH = os.path.expanduser("~/.crumb/history.org")

def search_log(query):
    if not os.path.exists(LOG_PATH):
        print("No history file found.")
        return

    with open(LOG_PATH, "r") as f:
        entries = f.read().split("* ")[1:]  # split on org-mode headings

    found = 0
    for entry in entries:
        if query.lower() in entry.lower():
            print(f"* {entry.strip()}\n")
            found += 1

    if found == 0:
        print("No matches found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: search_crumb.py <search term>")
    else:
        search_log(sys.argv[1])