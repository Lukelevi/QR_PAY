## Objective: 
- I will need to to create a wrapper that the backend/frontend can call to transform the payment data into a secure string.

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
