import re
import random as rdm

# SENDER INPUT
sender_details = []
for count in range(3):
    try:
        if count == 0:
            print("Recepient ID no")
        elif count == 1:
            print("Amount To Transfer")
        elif count == 2:
            print("Password")
        details = input('--> ')
        sender_details.append(details)
    except ValueError as err:
        print(f'Encountered error: {err}')

# simple character pool
special_characters = "0123456789@#$_&-+*!:/}{[]|~"

# Encryption salts / hashes
id_number_hash = str(rdm.randint(1, 10))
amount_hash = "010201020"
password_hash = "1946729"

# Caesar Cypher Algorithm
shift = 3

def caesar_encrypt(text, shift):
    encrypted = ""
    for ch in text:
        encrypted += chr((ord(ch) + shift) % 256)
    return encrypted

def caesar_decrypt(text, shift):
    decrypted = ""
    for ch in text:
        decrypted += chr((ord(ch) - shift) % 256)
    return decrypted


# ENCRYPT SENDER DETAILS
sender_encrypted_details = []

encrypt_id_key = caesar_encrypt(sender_details[0], shift) + id_number_hash
encrypt_amount_key = caesar_encrypt(sender_details[1], shift) + amount_hash
encrypt_pass_key = caesar_encrypt(sender_details[2], shift) + password_hash

sender_encrypted_details.append({
    "id": encrypt_id_key,
    "amount": encrypt_amount_key,
    "password": encrypt_pass_key
})

print("\nSender encrypted:", sender_encrypted_details)

# RECEIVER INPUT
print("\n--- RECEIVER INPUT ---")
receiver_details = []
for count in range(3):
    if count == 0:
        print("Your ID no")
    elif count == 1:
        print("Amount To Transfer")
    elif count == 2:
        print("Password")
    details = input('<-- ')
    receiver_details.append(details)

# decrypt format for receiver (same logic, Caesar decrypt)
decrypt_id_key = caesar_encrypt(receiver_details[0], shift) + id_number_hash
decrypt_amount_key = caesar_encrypt(receiver_details[1], shift) + amount_hash
decrypt_pass_key = caesar_encrypt(receiver_details[2], shift) + password_hash

# AUTHENTICITY CHECK
sender_block = sender_encrypted_details[0]

id_match = decrypt_id_key == sender_block["id"]
amount_match = decrypt_amount_key == sender_block["amount"]
password_match = decrypt_pass_key == sender_block["password"]

print("\n--- VERIFICATION RESULTS ---")
print("ID Match:       ", id_match)
print("Amount Match:   ", amount_match)
print("Password Match: ", password_match)

if id_match and amount_match and password_match:
    print("\nPayment Verified ✓")
else:
    print("\nPayment Declined ✗")
