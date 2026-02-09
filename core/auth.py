import jwt 
import bcrypt 

#This is my "Gatekeeper" 
#Who are you? (user)
"""Handles user login and session management, and 
   ensuring that the 'Sender' is allowed to initiate the payment.
   This involves making use of JSON Web Tokens and password hashing like bcrypt.
"""