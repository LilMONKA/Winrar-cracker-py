import os
import subprocess
import sys
from pathlib import Path

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_7zip():
    """Check if 7-Zip is installed"""
    seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
    if not os.path.exists(seven_zip_path):
        print("7-Zip not installed!")
        input("Press Enter to exit...")
        sys.exit(1)
    return seven_zip_path

def get_file_path(prompt):
    """Get and validate file path from user"""
    file_path = input(prompt).strip('"')
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        input("Press Enter to exit...")
        sys.exit(1)
    return file_path

def attempt_crack(seven_zip_path, archive, password, output_dir="cracked"):
    """Attempt to extract with given password"""
    print(f"ATTEMPT: {password}")
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)
    
    # Run 7z command
    cmd = [
        seven_zip_path,
        'x',  # extract
        f'-p{password}',
        archive,
        f'-o{output_dir}',
        '-y'  # yes to all
    ]
    
    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    return result.returncode == 0

def main():
    print("=" * 40)
    print("Zipwn - Archive Password Cracker")
    print("=" * 40)
    print()
    
    # Check for 7-Zip
    seven_zip_path = check_7zip()
    
    # Get archive path
    archive = get_file_path("Enter Archive: ")
    
    # Get wordlist path
    wordlist = get_file_path("Enter Wordlist: ")
    
    print("\nCracking...")
    
    # Try each password
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                password = line.strip()
                if not password:  # Skip empty lines
                    continue
                    
                if attempt_crack(seven_zip_path, archive, password):
                    print(f"\n{'='*40}")
                    print(f"Success! Password Found: {password}")
                    print(f"{'='*40}")
                    input("\nPress Enter to exit...")
                    sys.exit(0)
    
    except KeyboardInterrupt:
        print("\n\nCracking interrupted by user")
        sys.exit(1)
    
    print("\nPassword not found in wordlist")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()