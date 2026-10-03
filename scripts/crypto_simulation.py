from pathlib import Path
import hashlib

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Folder containing the synthetic protected evidence
protected_folder = project_folder / "cryptography" / "protected_evidence"

# Make sure the folder exists
protected_folder.mkdir(parents=True, exist_ok=True)

# Synthetic evidence
evidence = """SIMULATED TRANSACTION RECORD

Case ID: OPS-PS-2026-001

Transaction ID: TEST-TXN-001

Amount: INR 100

Status: SIMULATION ONLY

Purpose:
Academic Digital Forensics Assignment

No real financial information is contained in this file.
"""

# Test password for our academic simulation
password = "phantom2026"

# Generate SHA-256 representation of the test password
password_hash = hashlib.sha256(password.encode()).hexdigest()

# Save synthetic evidence
evidence_file = protected_folder / "simulated_transaction.txt"
evidence_file.write_text(evidence, encoding="utf-8")

# Save password hash
hash_file = project_folder / "cryptography" / "password_hash.txt"
hash_file.write_text(password_hash, encoding="utf-8")

print("======================================")
print("      CRYPTOGRAPHY SIMULATION")
print("======================================")

print()
print("Synthetic evidence created successfully!")
print()
print(f"Evidence file:")
print(evidence_file)

print()
print("SHA-256 password representation:")
print(password_hash)

print()
print("This is a controlled academic simulation.")
print("No real account, device, or password was accessed.")