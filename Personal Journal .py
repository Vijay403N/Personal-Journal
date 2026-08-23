import json
import os
from datetime import datetime

DATA_FILE = "journal.json"

def load_entries():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_entries(entries):
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def add_entry(entries, text):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text
    }
    entries.append(entry)
    save_entries(entries)
    print("Entry saved.")

def show_entries(entries):
    print("\n--- Journal Entries ---")
    for i, e in enumerate(entries, 1):
        print(f"{i}. [{e['date']}] {e['text']}")

def search_entries(entries, keyword):
    results = [e for e in entries if keyword.lower() in e["text"].lower()]
    print("\n--- Search Results ---")
    for e in results:
        print(f"[{e['date']}] {e['text']}")

def main():
    entries = load_entries()
    while True:
        print("\n=== Personal Journal ===")
        print("1. Add Entry")
        print("2. Show Entries")
        print("3. Search Entries")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            text = input("Write your entry: ")
            add_entry(entries, text)
        elif choice == "2":
            show_entries(entries)
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            search_entries(entries, keyword)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
