from encryption import encrypt_image, decrypt_image
from preprocessing import preprocess_image
from key_generation import generate_keys

# path to the input image file
input_file = "input_image.jpg"

# path to the output encrypted image file
encrypted_file = "encrypted_image.jpg"

# path to the output decrypted image file
decrypted_file = "decrypted_image.jpg"

# generate the keys for symmetric and asymmetric encryption
symmetric_key, public_key, private_key = generate_keys()

# preprocess the input image file
preprocessed_image = preprocess_image(input_file)

# encrypt the preprocessed image using symmetric and asymmetric encryption
encrypted_image = encrypt_image(preprocessed_image, symmetric_key, public_key)

# save the encrypted image to file
encrypted_image.save(encrypted_file)

# decrypt the encrypted image using symmetric and asymmetric encryption
decrypted_image = decrypt_image(encrypted_image, symmetric_key, private_key)

# save the decrypted image to file
decrypted_image.save(decrypted_file)
