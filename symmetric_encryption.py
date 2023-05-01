from Crypto.Cipher import AES
import os

# Encryption function
def encrypt(key, plaintext):
    # Pad the plaintext to be a multiple of 16 bytes
    padded_plaintext = plaintext + ((16 - len(plaintext) % 16) * '{')
    
    # Generate a random initialization vector (IV) using os.urandom
    iv = os.urandom(AES.block_size)
    
    # Create a new AES cipher object with the given key and mode of operation
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encrypt the padded plaintext using the AES cipher object and IV
    ciphertext = cipher.encrypt(padded_plaintext.encode('utf-8'))
    
    # Return the IV and ciphertext as a tuple
    return iv + ciphertext

# Decryption function
def decrypt(key, iv_and_ciphertext):
    # Split the IV and ciphertext from the input
    iv = iv_and_ciphertext[:AES.block_size]
    ciphertext = iv_and_ciphertext[AES.block_size:]
    
    # Create a new AES cipher object with the given key and mode of operation
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext using the AES cipher object and IV, then remove the padding
    plaintext = cipher.decrypt(ciphertext).rstrip('{').decode('utf-8')
    
    # Return the plaintext as a string
    return plaintext
