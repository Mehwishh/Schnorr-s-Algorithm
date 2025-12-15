# top_model.py
from keygen import keygen
from sign import sign
from verify import verify

class Schnorr:
    """
    Top model combining KeyGen, Sign, Verify
    """

    def generate_keys(self):
        return keygen()

    def sign_message(self, message: bytes, private_key: int):
        return sign(message, private_key)

    def verify_signature(self, message: bytes, signature: tuple, public_key: int):
        return verify(message, signature, public_key)
