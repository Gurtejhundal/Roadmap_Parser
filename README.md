 Roadmap Parser & Task Tracker

Roadmap Parser is a Streamlit application that transforms any learning or career roadmap into a clean, structured weekly task tracker.
Paste a roadmap or auto-generate one with AI, and the app instantly extracts timeframes and tasks, organizes them into checklists, and helps you track progress with complete clarity—no excuses, no confusion.

Key Features

Roadmap Parsing
Converts raw roadmap text into structured Months, Weeks, Days, and Hours.

AI Auto-Generation
Type a goal (e.g., “8-month roadmap to learn Data Science”) and instantly generate a ready-to-use roadmap.

Task Tracking
Every task becomes a checkbox you can tick off as you execute.

Local Database
Uses SQLite to store roadmaps, timeframes, and task completion status.

PDF Export
Download your roadmap or tasks as a clean, formatted PDF.

Multiple Themes
Cyberpunk, Neon, Titanium, Ember Glow, Aqua Glow — fully styled UI themes.

Duplicate Protection
Prevents importing roadmaps with the same name.



📦 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Roadmap_Parser.git
cd Roadmap_Parser


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

🧠 How It Works

Input a roadmap

Paste your roadmap text

OR auto-generate one using the built-in goal input

Parser extracts structure
The app detects:

Timeframes (Week 1, Month 2, Day 3, etc.)

Tasks (- Learn Python, - Install VS Code, etc.)

Everything is stored in a database
Your tasks, timeframes, and completion status persist automatically.
