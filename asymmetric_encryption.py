from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair():
    """
    Generate an RSA key pair of 2048 bits and return the public and private keys
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def encrypt_with_public_key(data, public_key):
    """
    Encrypt the given data using the provided public key
    """
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(data)
    return ciphertext

def decrypt_with_private_key(ciphertext, private_key):
    """
    Decrypt the given ciphertext using the provided private key
    """
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    data = cipher.decrypt(ciphertext)
    return data
