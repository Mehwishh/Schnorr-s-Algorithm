# keygen.py
import secrets
from params import G, p, q

def keygen():
    """
    Generate Schnorr key pair
    x: private key (≤255 bits)
    P: public key (≤256 bits)
    """
    x = secrets.randbelow(q - 1) + 1
    P = pow(G, x, p)
    return x, P
