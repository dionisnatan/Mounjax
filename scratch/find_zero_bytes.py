
import os

def find_zero_byte_files(root_dir):
    zero_byte_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:
                zero_byte_files.append(file_path)
    
    if zero_byte_files:
        print("Zero-byte files found:")
        for f in zero_byte_files:
            print(f"- {f}")
    else:
        print("No zero-byte files found.")

if __name__ == "__main__":
    find_zero_byte_files('.')
