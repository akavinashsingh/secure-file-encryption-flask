

# 🔐 Secure XOR File Encryption Console

A **cybersecurity-inspired web application** built using **Flask and TinyDB** that allows authenticated users to **securely encrypt and decrypt files using XOR encryption** through a terminal-style interface.

This project focuses on **secure access control**, **file handling**, and a **command-console UI** to simulate a lightweight security tool environment.

---

## 📸 Screenshots

### 🔑 Secure Login Console

<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/775e1a36-65dc-46c7-b41f-896ce9e1a374" />

### 🧑‍💻 Operator Registration Module

<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/8ce2d238-186a-4342-beea-2549b1c0ebed" />

### 🛡️ Command Center Dashboard

<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/7692d423-c5c9-408c-ac7b-18c2c17db54e" />

### 🔐 File Encryption & Decryption Interface

<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/e5d6bd87-0281-4f25-93a7-e6f09df646f7" />

---

## ✨ Features

* 🔒 Secure user authentication (Login & Register)
* 🧠 XOR-based file encryption and decryption
* 📁 Upload and download encrypted/decrypted files
* 🖥️ Cybersecurity / terminal-style UI
* 🗄️ Lightweight database using TinyDB
* 🚪 Session handling with logout support
* ☁️ Cloud-deployable (Render compatible)

---

## 🛠️ Tech Stack

| Layer      | Technology               |
| ---------- | ------------------------ |
| Backend    | Python (Flask)           |
| Database   | TinyDB                   |
| Frontend   | HTML + CSS (Terminal UI) |
| Encryption | XOR Cipher               |
| Deployment | Render                   |
| Server     | Gunicorn                 |

---

## 📂 Project Structure

```
secure-xor-console/
├── app.py
├── requirements.txt
├── database.json
├── output/
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── encrypt.html
│   └── decrypt.html
└── static/
    └── style.css
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/secure-xor-console.git
cd secure-xor-console
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## ☁️ Deployment (Render)

* Build Command:

```bash
pip install -r requirements.txt
```

* Start Command:

```bash
gunicorn app:app
```

The app is fully compatible with **Render Web Services**.

---

## 🔐 Security Note

⚠️ **XOR encryption is used for educational purposes only**.
This project demonstrates **encryption concepts, access control, and secure file handling**, not production-grade cryptography.

---

## 🚀 Future Enhancements

* 🔑 Password hashing (bcrypt)
* 🧾 Encryption audit logs
* 🔐 AES or RSA encryption support
* 👥 Role-based access control
* 🧠 File integrity verification (hashing)
* 🌙 Dark/light terminal themes

---

## 👨‍💻 Author

**Avinash Kumar**
Computer Science Student | Web & Security Enthusiast

📌 *This project was built as a hands-on cybersecurity learning exercise using Flask.*

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 🛠️ Improve it


Just say the word 💻🛡️
