# 🧪 Wordchemy

**Wordchemy** is a clone of the classic Wordle game — built with Python and Flask. Players have six attempts to guess a secret five-letter word, with helpful feedback after each guess.

---

## ✨ Features

- 🎮 Classic Wordle-style gameplay  
- 🔠 Real-time feedback with coloured tiles  
- 🧠 Keeps track of guesses and attempts using Flask sessions  
- 💡 End-of-game result screen with win/lose status

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher  
- `Flask` module  

You can install Flask with:

```bash
pip install flask
```

### Running the App

1. Clone the repository

```bash
git clone https://github.com/Shadan13/Wordchemy.git
cd wordchemy
```

2. Run the app

```bash
python app.py
```

3. Open your browser and go to `http://127.0.0.1:5000`

---

## 📁 Project Structure

```text
Wordchemy/
├── app.py               # Main Flask app
├── WORDS.txt            # Word list for the game
├── templates/
│   ├── index.html       # Main game screen
│   └── result.html      # Game result screen
├── static/
│   └── favicon.ico      # Wordchemy favicon
```

---

## 🧠 How It Works

- A word is randomly chosen from WORDS.txt and stored in session
- Player guesses are submitted via a form
- The backend checks each letter:
  - `"O"` = correct letter & correct position
  - `"Y"` = correct letter, wrong position
  - `"X"` = incorrect letter
- The game ends when the word is guessed or attempts run out

---

## 🛠 Customization

- Add or modify the word list in `WORDS.txt`
- Tweak feedback logic in `get_feedback()` if you'd like custom rules
- Style it up with your own CSS and favicon under `static/`

---

Created by Shadan Siddiqui  
Inspired by Wordle, built using Flask and pure Python magic ✨
