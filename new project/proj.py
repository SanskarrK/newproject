import json
import random
import os

# Path for storing mood-quote data
DATA_FILE = "quotes.json"

# Sample data if file doesn't exist
default_data = {
    "happy": [
        "Happiness is not something ready-made. It comes from your own actions.",
        "The purpose of our lives is to be happy.",
        "Smile — it’s free therapy!"
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "Every storm runs out of rain.",
        "Crying is how your heart speaks when your lips can’t explain the pain."
    ],
    "tired": [
        "Rest when you’re weary. Refresh and renew yourself.",
        "Sometimes the most productive thing you can do is rest.",
        "Fatigue is the best pillow."
    ],
    "motivated": [
        "Don’t watch the clock; do what it does. Keep going.",
        "The secret of getting ahead is getting started.",
        "Dream big and dare to fail."
    ]
}

# Create file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump(default_data, f, indent=4)

# Load data
with open(DATA_FILE, "r") as f:
    quotes_data = json.load(f)

# User interaction
mood = input("How are you feeling today? (happy, sad, tired, motivated): ").lower()

if mood in quotes_data:
    quote = random.choice(quotes_data[mood])
    print(f"\n💡 Quote for you:\n{quote}")
else:
    print("\nSorry, I don't have quotes for that mood yet.")

# Optional: Add new mood & quote
choice = input("\nDo you want to add a new quote for this mood? (y/n): ").lower()
if choice == "y":
    new_quote = input("Enter your quote: ")
    if mood not in quotes_data:
        quotes_data[mood] = []
    quotes_data[mood].append(new_quote)
    with open(DATA_FILE, "w") as f:
        json.dump(quotes_data, f, indent=4)
    print("✅ Quote added successfully!")
print(marks.values())