import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation
print((len)(chars))
print(''.join(secrets.choice(chars) for _ in range (40)))
# You can edit the numbers of digits for your password by changing the number 40 to what ever number you like.
