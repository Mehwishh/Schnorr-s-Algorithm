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
- Easily extensible to EC-Schnorr or post-quantum schemes (e.g., Dilithium)

---

## Repository Structure
schnorr-signature/
│── README.md
│── top_model.py # High-level API
│── keygen.py # Key generation
│── sign.py # Signature generation
│── verify.py # Signature verification
│── params.py # Public parameters (p, q, G)
│── hash_utils.py # Hash-to-integer utility
└── examples/
└── demo.py

yaml
Copy code

---

## Cryptographic Parameters
Defined in `params.py`:

- **p**: Large prime modulus  
- **q**: Prime order of the subgroup  
- **G**: Generator of the subgroup  

They satisfy the Schnorr requirement:

G^q mod p = 1

yaml
Copy code

---

## Algorithm Description

### Key Generation
1. Choose private key `x ∈ [1, q−1]`
2. Compute public key:
Y = G^x mod p

yaml
Copy code

---

### Signature Generation
Given message `m` and private key `x`:

1. Generate random nonce `r`
2. Compute commitment:
R = G^r mod p

markdown
Copy code
3. Compute challenge:
c = H(m || R)

markdown
Copy code
4. Compute response:
s = (r + c·x) mod q

makefile
Copy code

Signature:
(R, s)

yaml
Copy code

---

### Signature Verification
Given `(R, s)` and public key `Y`:

1. Recompute:
c = H(m || R)

markdown
Copy code
2. Verify:
G^s mod p == R · Y^c mod p

yaml
Copy code

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

Follows Schnorr’s mathematical specification strictly

⚠️ This implementation is not hardened against side-channel attacks and should not be used in production systems without further protections and audits.

Intended Use
Cryptography coursework and labs

Research prototypes

FPGA / hardware co-design validation

Comparison with ECDSA and Dilithium

Educational demonstrations

Future Work
Elliptic Curve Schnorr (EC-Schnorr)

Deterministic nonce generation (RFC-style)

Batch verification

Post-quantum migration (Dilithium)

License
Educational and research use only.

Final Note
This project emphasizes clarity, correctness, and architectural discipline.
The code is deliberately explicit and minimal to support learning, verification, and extension.

yaml
Copy code

---

If you want, I can:
- tighten this for a **final-year project report**,  
- rewrite it for a **research paper appendix**, or  
- adapt it specifically for **FPGA / hardware documentation**.

Just say which direction.
