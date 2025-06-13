
---

# WhatsApp Chat Analyzer

A Streamlit-based web app to analyze WhatsApp chat exports. It provides detailed statistics, visualizations, and insights on message counts, word usage, media sharing, emojis, activity timelines, and user behavior.

---

## Features

* Upload WhatsApp chat export text file (`.txt`)
* View overall or individual user chat statistics
* Summary metrics: total messages, words, media shared, links shared
* Most active users in the group
* Word cloud visualization of frequently used words
* Most common words bar chart
* Emoji usage statistics with percentages
* Monthly and weekly activity timelines and heatmaps
* Interactive, user-friendly Streamlit interface

---

## Project Structure

```
/Code Files
├── app.py              # Main Streamlit app
├── preprocess.py       # Data preprocessing logic
├── stats.py            # Statistical analysis and visualization functions
├── README.md           # This file
├── requirements.txt    # Project dependencies
└── .gitignore          # Git ignore rules (e.g., .conda folder)
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jowin-henry/WA-Chat-Analyser.git
cd WA-Chat-Analyser
```

2. Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Upload your WhatsApp chat export `.txt` file via the sidebar.
* Choose to analyze overall group or individual users.
* Click **Show Analysis** to display visualizations and stats.

---

## Dependencies

* Python 3.7+
* streamlit
* pandas
* matplotlib
* numpy
* wordcloud
* regex

*(Make sure to check `requirements.txt` for the exact versions.)*

---

## Notes

* The app expects a WhatsApp exported chat file in text format.
* Group notifications (e.g., "User added") are excluded from user-specific analyses.
* Monthly timeline plots intelligently format dates to avoid overcrowding the x-axis.

---
## Outputs



