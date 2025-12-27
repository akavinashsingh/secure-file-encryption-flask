from flask import Flask, render_template, request, redirect, url_for, session, send_file
from tinydb import TinyDB, Query
import os

app = Flask(__name__)
app.secret_key = "secretkey"

OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# TinyDB setup
db = TinyDB("database.json")
users = db.table("users")
User = Query()

def xor_bytes(data, key):
    key = key.encode()
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        user = users.get(User.username == u)
        if user and user["password"] == p:
            session["user"] = u
            return redirect(url_for("dashboard"))
        error = "Invalid login"

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        if users.get(User.username == u):
            error = "User already exists"
        else:
            users.insert({
                "username": u,
                "password": p
            })
            return redirect(url_for("login"))

    return render_template("register.html", error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        file = request.files["file"]
        key = request.form["key"]

        data = file.read()
        encrypted = xor_bytes(data, key)

        out_path = os.path.join(OUTPUT_FOLDER, "encrypted_" + file.filename)
        with open(out_path, "wb") as f:
            f.write(encrypted)

        return send_file(out_path, as_attachment=True)

    return render_template("encrypt.html")

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        file = request.files["file"]
        key = request.form["key"]

        data = file.read()
        decrypted = xor_bytes(data, key)

        out_path = os.path.join(OUTPUT_FOLDER, "decrypted_" + file.filename)
        with open(out_path, "wb") as f:
            f.write(decrypted)

        return send_file(out_path, as_attachment=True)

    return render_template("decrypt.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
