# params.py
# ============================================
# 256-bit Proof-of-Concept Schnorr Parameters
# ============================================

# 256-bit prime (NOT secure, for PoC only)
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

# Subgroup order
q = (p - 1) // 2

# Generator
G = 2
