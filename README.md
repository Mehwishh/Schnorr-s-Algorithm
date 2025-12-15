# Schnorr Signature Scheme – Python Implementation

## Overview
This repository contains a **modular and standards-aligned implementation of the Schnorr Digital Signature Scheme** in Python.  
The code is designed for **academic study, cryptographic research, and hardware–software co-design validation** (e.g., FPGA-based implementations).

This is a **proof-of-concept implementation**, not a production-grade cryptographic library.

---

## Key Features
- Clean separation of **Key Generation**, **Signing**, and **Verification**
- Cryptographically secure randomness (`secrets`)
- SHA-256–based challenge computation
- Minimal, auditable codebase





## Cryptographic Parameters
Defined in `params.py`:

- **p**: Large prime modulus  
- **q**: Prime order of the subgroup  
- **G**: Generator of the subgroup  

They satisfy the Schnorr requirement:

G^q mod p = 1

## Algorithm Description

### Key Generation
1. Choose private key `x ∈ [1, q−1]`
2. Compute public key:
Y = G^x mod p
### Signature Generation
Given message `m` and private key `x`:

1. Generate random nonce `r`
2. Compute commitment:
            R = G^r mod p
3. Compute challenge:
             c = H(m || R)
4. Compute response:
           s = (r + c·x) mod q

Signature:
            (R, s)

### Signature Verification
Given `(R, s)` and public key `Y`:

1. Recompute:
        c = H(m || R)
2. Verify:
        G^s mod p == R · Y^c mod p



If the equation holds, the signature is valid.

---

## Usage Example
```python
from top_model import Schnorr

schnorr = Schnorr()

private_key, public_key = schnorr.generate_keys()

message = b"Hello Schnorr"
signature = schnorr.sign_message(message, private_key)

is_valid = schnorr.verify_signature(message, signature, public_key)
print("Signature valid:", is_valid)

Security Notes
Uses cryptographically secure randomness
Hash-based challenge prevents replay attacks
