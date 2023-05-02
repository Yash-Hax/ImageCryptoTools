# Image Cryptography

Its a Python package that provides encryption and decryption functionality for images. It currently supports the following encryption algorithms:

- AES-128
- AES-192
- AES-256

## Installation

To install Image Crypto Tools, run the following command:

```pip install .```


Alternatively, you can download the source code and run the following command:

```python setup.py install```


## Usage

To encrypt an image, import the `encrypt_image` function from the `encryption` module and call it with the path to the image file and the encryption key:

```python
from encryption import encrypt_image

encrypt_image('path/to/image.jpg', 'my secret key')

To decrypt an encrypted image, import the decrypt_image function from the encryption module and call it with the path to the encrypted image file and the encryption key:

from encryption import decrypt_image

decrypt_image('path/to/encrypted_image.jpg', 'my secret key')

