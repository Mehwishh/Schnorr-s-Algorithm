# verify.py
from params import G, p
from hash_utils import hash_int

def verify(message: bytes, signature: tuple, P: int) -> bool:
    """
    Schnorr Verification
    """
    R, s = signature

    c = hash_int(message + R.to_bytes(32, 'big'))

    left = pow(G, s, p)
    right = (pow(P, c, p) * R) % p

    return left == right
