Here's a README file for your Image Encryption Tool:

---

# Image Encryption Tool

Done By Anoop C Kulkarni

This Python program allows users to encrypt and decrypt images using pixel manipulation techniques. The tool performs operations such as adding or subtracting a key value from each pixel's RGB values to securely encrypt and decrypt images.

## Features

- **Encrypt Images**: Encrypts an image by modifying each pixel's RGB values using a user-defined key.
- **Decrypt Images**: Decrypts an encrypted image by reversing the encryption process with the same key.
- **Simple and Fast**: Provides a straightforward method for image encryption using basic mathematical operations.

## Requirements

- Python 3.x
- Pillow library for image processing

## Installation

1. **Clone the Repository** (if hosted on a version control system like GitHub) or download the `main.py` file directly.
2. Install the Pillow library using pip:
   ```bash
   pip install pillow
   ```

## Usage

1. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Run the program using the command:
     ```bash
     python main.py
     ```

2. **Follow the Prompts**:
   - **Choose Operation**: Enter `E` to encrypt an image or `D` to decrypt an image.
   - **Enter the Image Path**: Provide the full path to the image file you want to encrypt or decrypt. Ensure the path is correctly formatted (see Notes below).
   - **Enter the Output Path**: Provide the path where you want to save the output image.
   - **Enter the Key**: Provide an integer value to use as the key for encryption/decryption.

3. **View the Output**:
   - The program will save the encrypted or decrypted image to the specified output path.

## Example

### Encrypting an Image:

```bash
Image Encryption/Decryption Tool
Would you like to encrypt or decrypt an image? (E/D): E
Enter the path to the image file: C:/Users/anoop/OneDrive/Pictures/Screenshots/bcv.png
Enter the path to save the output image: C:/Users/anoop/OneDrive/Pictures/Screenshots/encrypted_bcv.png
Enter the encryption/decryption key (integer): 42
Encrypted image saved as C:/Users/anoop/OneDrive/Pictures/Screenshots/encrypted_bcv.png
```

### Decrypting an Image:

```bash
Image Encryption/Decryption Tool
Would you like to encrypt or decrypt an image? (E/D): D
Enter the path to the image file: C:/Users/anoop/OneDrive/Pictures/Screenshots/encrypted_bcv.png
Enter the path to save the output image: C:/Users/anoop/OneDrive/Pictures/Screenshots/decrypted_bcv.png
Enter the encryption/decryption key (integer): 42
Decrypted image saved as C:/Users/anoop/OneDrive/Pictures/Screenshots/decrypted_bcv.png
```

## Notes

- **File Path Formatting**:
  - On Windows, use forward slashes (`/`) instead of backslashes (`\`) to avoid escape character issues.
  - Alternatively, use raw strings by prefixing the file path with `r`, e.g., `r"C:\path\to\image.png"`.

- **Key**:
  - The key used for encryption must be the same as the one used for decryption.

- **Limitations**:
  - This tool uses a basic encryption method. For highly sensitive data, consider using more advanced cryptographic techniques.


## Contributing

Feel free to fork this project, submit issues, or contribute by creating pull requests.

## Acknowledgements

This tool is a simple example of image encryption using pixel manipulation, inspired by basic cryptographic principles.

