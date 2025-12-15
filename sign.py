# sign.py
import secrets
from params import G, p, q
from hash_utils import hash_int

def sign(message: bytes, x: int):
    """
    Schnorr Signing
    Returns: (R, s)
    """
    # 1. Random nonce
    r = secrets.randbelow(q - 1) + 1

    # 2. Commitment (G* R mod p)
    R = pow(G, r, p)

    # 3. Challenge
    c = hash_int(message + R.to_bytes(32, 'big'))

    # 4. Response
    s = (r + c * x) % q

    return R, s
