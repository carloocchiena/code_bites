# generate true alphanumeric string 
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, 
# account authentication, security tokens, and related secrets.
# In particular, secrets should be used in preference to the default pseudo-random number generator in the random module, 
# which is designed for modelling and simulation, not security or cryptography.

import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
print(password)
