from Pyfhel import Pyfhel

class HomomorphicEncryption:
    def __init__(self):
        self.HE = Pyfhel()

    def setup(self):
        self.HE.contextGen(p=65537, m=1024)
        self.HE.keyGen()

    def encrypt(self, plaintext):
        self.ciphertext = self.HE.encryptInt(int(plaintext))
        return self.ciphertext

    def decrypt(self, ciphertext):
        decrypted = self.HE.decryptInt(ciphertext)
        return decrypted

    def add(self, ciphertext1, ciphertext2):
        sum_ciphertext = ciphertext1 + ciphertext2
        return sum_ciphertext

    def multiply(self, ciphertext1, ciphertext2):
        product_ciphertext = ciphertext1 * ciphertext2
        return product_ciphertext
