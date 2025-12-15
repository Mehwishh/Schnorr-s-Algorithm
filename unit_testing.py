# unit_testing.py
from top_model import Schnorr

def test_key_generation():
    print("TEST 1: Key Generation")
    schnorr = Schnorr()
    x, P = schnorr.generate_keys()
    print("Private key x (bits):", x.bit_length())
    print("Public key P (bits):", P.bit_length())
    print("PASS\n")

def test_signing():
    print("TEST 2: Signing")
    schnorr = Schnorr()
    x, P = schnorr.generate_keys()
    message = b"Final Year Project - Schnorr PoC"
    signature = schnorr.sign_message(message, x)
    print("Signature generated")
    print("PASS\n")
    return message, signature, P

def test_verification():
    print("TEST 3: Verification")
    schnorr = Schnorr()
    message, signature, P = test_signing()

    valid = schnorr.verify_signature(message, signature, P)
    print("Correct verification:", valid)

    invalid = schnorr.verify_signature(b"Wrong message", signature, P)
    print("Wrong message verification:", invalid)

    assert valid is True
    assert invalid is False
    print("PASS\n")

if __name__ == "__main__":
    test_key_generation()
    test_verification()
