from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Apply encryption by modifying pixel values using the key
    encrypted_array = (image_array + key) % 256

    # Create a new image from the encrypted array
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, output_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_image)

    # Apply decryption by reversing the encryption operation
    decrypted_array = (encrypted_array - key) % 256

    # Create a new image from the decrypted array
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Would you like to encrypt or decrypt an image? (E/D): ").upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")
        return

    image_path = input("Enter the path to the image file: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == 'E':
        encrypt_image(image_path, output_path, key)
    elif choice == 'D':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
