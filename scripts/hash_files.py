import hashlib
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Evidence folder
evidence_folder = project_folder / "evidence"

# Output file
output_file = project_folder / "acquisition" / "hashes_sha256.txt"


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


# Create acquisition folder if it doesn't exist
output_file.parent.mkdir(parents=True, exist_ok=True)

with open(output_file, "w", encoding="utf-8") as output:

    for file_path in sorted(evidence_folder.rglob("*")):

        if file_path.is_file():

            file_hash = calculate_sha256(file_path)

            relative_path = file_path.relative_to(project_folder)

            output.write(
                f"{relative_path} | SHA-256 | {file_hash}\n"
            )

            print(f"File: {relative_path}")
            print(f"SHA-256: {file_hash}")
            print("-" * 70)

print("\nHashing completed successfully!")
print(f"Results saved to: {output_file}")