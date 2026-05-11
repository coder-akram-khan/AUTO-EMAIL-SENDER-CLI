<div align="center">

# 📬 AUTO EMAIL SENDER CLI

**A powerful, terminal-based Python tool for sending automated emails — fast, flexible, and fully scriptable.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SMTP](https://img.shields.io/badge/Protocol-SMTP%20%2F%20SSL-00C853?style=for-the-badge&logo=gmail&logoColor=white)](https://docs.python.org/3/library/smtplib.html)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=gnometerminal&logoColor=white)]()

<br/>

> _Stop clicking. Start scripting. Automate your emails straight from the terminal._

<br/>

</div>

---

## 🚀 Overview

**AUTO EMAIL SENDER CLI** is a lightweight yet capable command-line tool that lets you send emails programmatically using Python's `smtplib` and `email` libraries. Whether you're sending notifications, bulk messages, or automated alerts — this tool puts the power directly in your terminal.

No GUI. No bloat. Pure automation.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📤 **Send Emails via CLI** | Trigger email sends directly from your terminal with a single command |
| 🔐 **SSL/TLS Encryption** | Secure SMTP connection using SSL to keep your credentials and content safe |
| 📎 **Attachment Support** | Attach files to your emails effortlessly |
| 🧾 **HTML & Plain Text** | Send beautifully formatted HTML emails or simple plain-text messages |
| 👥 **Multiple Recipients** | Send to one or many recipients in a single run |
| ⚙️ **Configurable** | Easy-to-edit configuration — no hardcoded secrets |
| 🐍 **Pure Python** | Zero third-party dependencies — uses only Python standard library |

---

## 📁 Project Structure

```
AUTO-EMAIL-SENDER-CLI/
│
├── auto_email_sender.py     # Main script — entry point for the CLI tool
├── config.py                # Configuration: SMTP settings, credentials
├── requirements.txt         # Dependencies (if any)
├── README.md                # Project documentation
└── .env.example             # Example environment variable template
```

---

## ⚙️ Prerequisites

- Python **3.8** or higher
- A Gmail (or any SMTP-compatible) account
- Gmail App Password *(required if using Gmail with 2FA — see setup below)*

---

## 🔧 Installation

**1. Clone the repository**

```bash
git clone https://github.com/coder-akram-khan/AUTO-EMAIL-SENDER-CLI.git
cd AUTO-EMAIL-SENDER-CLI
```

**2. (Optional) Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Gmail App Password Setup

> Gmail blocks direct password login for scripts. You'll need to generate an **App Password**.

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (if not already enabled)
3. Navigate to **App Passwords** → Select *Mail* → Select *Device*
4. Copy the generated 16-character password
5. Use that password in your configuration (not your regular Gmail password)

---

## 🛠️ Configuration

Edit the configuration section in `auto_email_sender.py` (or `config.py`) with your credentials:

```python
SENDER_EMAIL    = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password_here"   # NOT your Gmail login password
SMTP_SERVER     = "smtp.gmail.com"
SMTP_PORT       = 465                         # SSL port
```

> 🔒 **Security Tip:** Never commit credentials to version control. Use environment variables or a `.env` file.

Using a `.env` file:

```bash
# .env
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
```

---

## ▶️ Usage

### Basic Usage

```bash
python auto_email_sender.py
```

### Send to a Specific Recipient

```bash
python auto_email_sender.py --to recipient@example.com --subject "Hello!" --body "This is an automated message."
```

### Send with an Attachment

```bash
python auto_email_sender.py --to recipient@example.com --subject "Report" --body "See attached." --attach report.pdf
```

### Send HTML Email

```bash
python auto_email_sender.py --to recipient@example.com --subject "Newsletter" --html email_template.html
```

> ⚠️ _Flag names may vary — refer to `python auto_email_sender.py --help` for exact CLI options._

---

## 📤 How It Works

```
┌─────────────────────────────────────────────────┐
│                   Your Terminal                 │
│   python auto_email_sender.py [options]         │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Load Config / Args    │
        │  (sender, recipient,   │
        │   subject, body, etc.) │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  Build Email Message   │
        │  (MIMEMultipart +      │
        │   HTML/Plain + Files)  │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  SMTP SSL Connection   │
        │  smtp.gmail.com:465    │
        └────────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │   Email Sent! ✅       │
        └────────────────────────┘
```

---

## 🧪 Example Output

```
$ python auto_email_sender.py

╔══════════════════════════════════════╗
║       AUTO EMAIL SENDER CLI          ║
╚══════════════════════════════════════╝

[*] Connecting to smtp.gmail.com:465 ...
[✓] Connection established.
[*] Authenticating sender: akram@gmail.com
[✓] Authentication successful.
[*] Sending email to: recipient@example.com
[✓] Email sent successfully!

```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/awesome-feature`
3. Commit your changes: `git commit -m "Add awesome feature"`
4. Push to the branch: `git push origin feature/awesome-feature`
5. Open a **Pull Request**

Please ensure your code follows PEP 8 style guidelines and includes relevant comments.

---

## 🛡️ Security Notice

- **Never** hardcode credentials directly into the script
- Add `.env` and `config.py` (if containing secrets) to your `.gitignore`
- Use App Passwords instead of your primary account password
- Consider rotating credentials periodically

---

## 📌 Roadmap

- [x] Send plain-text emails via CLI
- [x] SSL/TLS encrypted SMTP connection
- [x] File attachment support
- [x] HTML email support
- [ ] Bulk email sending from CSV
- [ ] Email scheduling (cron-compatible)
- [ ] Support for other SMTP providers (Outlook, Yahoo, SendGrid)
- [ ] Rich TUI interface with `rich` or `textual`

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Akram Khan**

[![GitHub](https://img.shields.io/badge/GitHub-coder--akram--khan-181717?style=flat-square&logo=github)](https://github.com/coder-akram-khan)

---

<div align="center">

_If you found this useful, please ⭐ star the repo — it means a lot!_

</div>
