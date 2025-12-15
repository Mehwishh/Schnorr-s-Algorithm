# hash_utils.py
import hashlib
from params import q

def hash_int(data: bytes) -> int:
    """
    SHA-256 hash → integer mod q
    Output size: 256-bit hash reduced to ~255 bits
    """
    h = hashlib.sha256(data).digest()   # 256-bit output
    return int.from_bytes(h, 'big') % q
