## Objective: 
- I will need to to create a `wrapper` that the backend/frontend can call to transform the payment data into a secure string.

## Use of Symmetric Encryption ##
- Use AES-GCM (Advanced Encryption Standard with Galois/Counter Mode). It provides both encryption (secrecy) and authentication (ensures the data hasn't been tampered with)

## Use of Key Derivation ##
- Use a Key Derivation Function (KDF) like Scrypt or PBKDF2 to turn the user's password into a strong cryptographic key.

**crypto/advanced**
- This section handles the "identity" and "longevity" of the system

**/signatures.py**
Even if a QR code is encrypted, soeone could generate a "fake" payment QR code. I make use of Digital Signatures (using Ed25519 or RSA)

- The `sender` signs the data with a private key.
- The receiver verifies the signature with a public key to prove the QR code actually came from your system.

**/key_rotation**
- This script handles the logic for retiring old `keys` and transitioning new ones without breaking pending transactions. 
# In a production environment, you cannot use the same master key forever # 

**crypto/security_audit/**
- This is a specialized folder for internal security checks. 

### Logging:
- Track (without storing any sensitive passwords) how many failed decryption attempts occur.

### Validation:
- Scripts to ensure that the keys being generated meet the required entropy (randomness) standards.


----     ---- 

## Security & Cryptography ##

cryptography library

Symmetric encryption (Fernet / AES)

Secure key handling

hashlib

Password hashing (SHA-256 or stronger)

Optional enhancements:

HMAC for integrity

Key derivation (PBKDF2 / Argon2)

🔹 QR Code Handling

Generation: qrcode or segno

Scanning/Decoding: pyzbar or opencv-python

🔹 Backend Framework (Choose One)

Flask — simple, beginner-friendly

FastAPI — modern, scalable, built-in validation

🔹 Database

SQLite (default)

Optional upgrade: PostgreSQL81

ORM:

SQLAlchemy

Used to store:

User IDs

Encrypted transaction records

Audit logs

🔹 Frontend / UI

Web Interface (Recommended)

HTML, CSS, JavaScript

Flask/FastAPI templates (Jinja2)

Alternative:

Tkinter or PyQt for desktop GUI

**Team Structure & Role Allocation**
## Teammate 1 – Security & Cryptography ##

Encryption & decryption logic

Key management

Integrity verification

Security testing

## Teammate 2 – Frontend & UX ##

Web or GUI interface

QR code display & scanning

User feedback & validation

Interface usability

## Teammate 3 – Backend & Data Management ##

API endpoints

Database models

Authentication logic

Transaction handling

## Teammate 4 – Testing & Documentation ##

Unit & integration tests

Performance checks

User documentation

Code quality & formatting

**Proposed Project Structure**

project/
├── core/            # Encryption & security logic
│   ├── crypto.py
│   └── auth.py
├── backend/         # API, database, models
│   ├── api.py
│   ├── models.py
│   └── database.py
├── frontend/        # Web or GUI interface
│   ├── templates/
│   └── static/
├── tests/           # Unit & integration tests
│   └── test_core.py
└── docs/            # Documentation

## Collaboration & Workflow ##

Version Control: Git + GitHub

Branching Strategy: Feature branches + pull requests

Code Reviews: Mandatory peer review before merging

Task Tracking: Trello / GitHub Projects / Notion

Communication: Discord / Slack

## Optional Advanced Enhancements ##

Transaction history & analytics

Offline mode with sync

Multi-language support

Blockchain-backed audit logs

Role-based user permissions

## Why This Project Works ##

This project is:

Technically achievable

Educationally rich

Highly modular

Well-suited for teamwork

Aligned with real-world software practices

It bridges the gap between theory and practical system design while remaining approachable for a student development team.
