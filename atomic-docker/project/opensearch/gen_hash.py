from bcrypt import gensalt, hashpw

password = b"Nrock127234!"
hashed_password = hashpw(password, gensalt())
print(hashed_password.decode())
