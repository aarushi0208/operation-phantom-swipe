from pathlib import Path
import hashlib

project_folder = Path(__file__).resolve().parent.parent

dictionary_file = project_folder / "cryptography" / "dictionary.txt"
hash_file = project_folder / "cryptography" / "password_hash.txt"

target_hash = hash_file.read_text(encoding="utf-8").strip()

print("======================================")
print(" DICTIONARY PASSWORD RECOVERY")
print("======================================")

found = False

with open(dictionary_file, "r", encoding="utf-8") as file:

    for candidate in file:
        candidate = candidate.strip()

        candidate_hash = hashlib.sha256(
            candidate.encode()
        ).hexdigest()

        print(f"Testing: {candidate}")

        if candidate_hash == target_hash:
            print()
            print("Password found!")
            print(f"Recovered test password: {candidate}")
            print()
            print("Controlled academic simulation only.")
            found = True
            break

if not found:
    print()
    print("Password was not found in the dictionary.")