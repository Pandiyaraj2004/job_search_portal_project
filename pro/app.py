from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session and flash messages

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize the database
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY, 
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Check if user exists
def user_exists(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user

# Add new user
def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Login Route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = user_exists(username)
        if user and user[1] == hash_password(password):
            session["username"] = username  # Save username in session
            return redirect(url_for("main"))
        else:
            flash("Invalid credentials. Try again.", "error")
    return render_template("login.html")

# Sign-Up Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match. Try again.", "error")
            return redirect(url_for("signup"))
        
        if user_exists(username):
            flash("Username already exists. Try a different one.", "error")
            return redirect(url_for("signup"))
        
        register_user(username, password)
        flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html")

# Main Page Route (Get Started Page)
@app.route("/main")
def main():
    if "username" in session:
        username = session["username"]
        return render_template("main.html", username=username)
    return redirect(url_for("login"))

# Get Started Action
@app.route("/get_started", methods=["POST"])
def get_started():
    # Redirect to the home page or another specific page
    return redirect(url_for("home"))

# Home Page Route
@app.route("/home")
def home():
    if "username" in session:
        username = session["username"]
        return render_template("home.html", username=username)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
