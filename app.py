import random
from flask import Flask, render_template, request, redirect, session
import secrets

# Initialize Flask app
app = Flask(__name__)
# Generate a secure random secret key for session management
app.secret_key = secrets.token_hex(16)

# Load word list from file and convert all words to uppercase
words = []
with open("WORDS.txt") as f:
    for line in f:
        words.append(line.strip().upper())

@app.route('/', methods=["GET", "POST"])
def index():
	 # If session doesn't have a game in progress, start a new one
    if "word" not in session:
        session["word"] = random.choice(words)  # Random answer word
        session["attempts"] = 6  # Number of attempts allowed
        session["guesses"] = []  # List to track past guesses and feedback

    if request.method == "POST":
		# Get the player's guess from form input
        guess = request.form.get("guess")
        if guess:
            guess = guess.upper()
			# Validate the guess: must be 5 letters and alphabetic
            if len(guess) == 5 and guess.isalpha():
                feedback = get_feedback(guess, session["word"])  # Get feedback (O/Y/X)
                session["guesses"].append((guess, feedback))  # Store guess and its feedback
                session["attempts"] -= 1  # Decrement remaining attempts

				# Redirect to result page if game is over (correct guess or 0 attempts left)
                if guess == session["word"] or session["attempts"] == 0:
                    return redirect("/result")
					
	# Render the main game page, passing guesses and remaining attempts
    return render_template("index.html", guesses=session["guesses"], attempts=session["attempts"], zip=zip)

@app.route("/result")
def result():
	# Retrieve guesses from session
    guesses = session.get("guesses")
    if guesses:
		# Check if any guess was correct
        won = any(guess == session["word"] for guess, _ in guesses)
        word = session.get("word")
        if word:
            session.clear()   # Clear session data for next game
            return render_template("result.html", word=word, won=won)
			
	# Render result page with final word even if session data is missing
    return render_template("result.html", word=word)

def get_feedback(guess, word):
    """
    Compares the guess to the target word and returns a list of feedback:
    'O' for correct letter in correct position,
    'Y' for correct letter in wrong position,
    'X' for incorrect letter.
    """
    result = [""] * 5  # Placeholder for feedback symbols
    used_indices = []  # Indices of letters already matched in exact position

	# Mark exact matches with 'O'
    for i in range(5):
        if guess[i] == word[i]:
            result[i] = "O"
            used_indices.append(i)
			
	# Build list of remaining letters not already matched
    remaining_letters = [word[i] for i in range(5) if i not in used_indices]

	# Mark correct letters in wrong positions with 'Y', rest as 'X'
    for i in range(5):
        if result[i] == "":
            if guess[i] in remaining_letters:
                result[i] = "Y"
                remaining_letters.remove(guess[i])
            else:
                result[i] = "X"

    return result

if __name__ == "__main__":
    app.run()
