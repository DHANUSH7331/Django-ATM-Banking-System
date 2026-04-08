**🏦 Django ATM Banking System**

A mini banking web application built using Django that simulates ATM-style operations such as account creation, OTP-based PIN generation, balance checking, deposit, withdrawal, and fund transfer.

This project demonstrates backend development, session handling, OTP verification, email integration, reCAPTCHA validation, and core banking workflows.

**✨ Features**
**👤 Account Creation**

Create new bank accounts with file upload support
Google reCAPTCHA validation to prevent bots
Stores customer details securely in database

**🔐 PIN Generation Using OTP**

Generates OTP and sends to registered email
OTP verification before setting ATM PIN
Session-based verification flow

**💰 Banking Operations**

Check account balance
Deposit money
Withdraw money
Transfer funds between accounts

**📧 Email Integration**

Sends OTP using Gmail SMTP

**🛠️ Tech Stack**

Technology	Purpose
Python	Programming Language
Django	Backend Framework
SQLite	Database
HTML/CSS	Frontend Templates
Gmail SMTP	Email OTP
Google reCAPTCHA	Bot Protection

**📂 Project Structure**
ATM-Banking-System/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── utils/
│   │     └── otp.py
│
├── templates/
│   ├── index.html
│   ├── acc_creation.html
│   ├── pin_gen.html
│   ├── valid.html
│   ├── check.html
│   ├── transaction.html
│   └── acc_transfer.html
│
├── screenshots/
├── db.sqlite3
└── manage.py

**⚙️ Installation & Setup**

1️⃣ Clone Repository
git clone https://github.com/yourusername/django-atm-banking.git
cd django-atm-banking
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install django
pip install django-recaptcha

**🔑 Configure Email for OTP**

Open settings.py and add:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'

⚠️ Use Gmail App Password, not your normal password.

**🤖 Configure Google reCAPTCHA**

Add in settings.py

RECAPTCHA_PUBLIC_KEY = 'your_public_key'
RECAPTCHA_PRIVATE_KEY = 'your_private_key'

**Get keys from:**
https://www.google.com/recaptcha/admin

**🗄️ Database Migration**
python manage.py makemigrations
python manage.py migrate
▶️ Run the Server
python manage.py runserver

**Open in browser:**

http://127.0.0.1:8000/
🔄 Application Workflow

1️⃣ User creates a bank account
2️⃣ User generates PIN via OTP verification
3️⃣ User performs banking operations:

Balance Check
Deposit
Withdraw
Fund Transfer

**📸 Screenshots**

🏠 Home Page
<img width="1919" height="947" alt="Screenshot 2026-04-07 233819" src="https://github.com/user-attachments/assets/e4cf49ec-a20f-436b-b664-23934dfd113a" />

👤 Account Creation Page

<img width="1893" height="948" alt="Screenshot 2026-04-07 233828" src="https://github.com/user-attachments/assets/d8a166b0-a9d5-40f2-afd2-edbc0f89827a" />

🔐 PIN Generation Page

<img width="1918" height="945" alt="Screenshot 2026-04-07 233839" src="https://github.com/user-attachments/assets/b475a905-63a8-4baf-bb79-d8c7a855a97f" />

💰 Check Balance Page
<img width="1919" height="947" alt="Screenshot 2026-04-07 233850" src="https://github.com/user-attachments/assets/430027b7-c335-4bf1-a618-a24d11dd1159" />

💵 Deposit / Withdraw Page

<img width="1919" height="945" alt="Screenshot 2026-04-07 233857" src="https://github.com/user-attachments/assets/94d78de5-756f-44d6-9b5f-2cf8f443d654" />

🔁 Fund Transfer Page

<img width="1919" height="949" alt="Screenshot 2026-04-07 233906" src="https://github.com/user-attachments/assets/28405028-8f4f-42ca-9d1c-7e1292add29a" />

🚨 Disclaimer

This project is created for learning and demonstration purposes only.
It is not production-ready banking software.

📈 Future Improvements
Add user authentication system
Add transaction history
Add REST API support
Improve UI with Bootstrap
Add audit logging & security enhancements
👨‍💻 Author

Dhanush
