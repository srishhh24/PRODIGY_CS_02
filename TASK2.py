from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixels = image.load()

        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Apply encryption transformation
                r_new = (r + key) % 256
                g_new = (g + key) % 256
                b_new = (b + key) % 256
                pixels[x, y] = (r_new, g_new, b_new)

        image.save(output_path)
        print(f"Image successfully encrypted and saved as {output_path}")
    except Exception as e:
        print("Error:", e)

def decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixels = image.load()

        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Apply decryption transformation
                r_new = (r - key) % 256
                g_new = (g - key) % 256
                b_new = (b - key) % 256
                pixels[x, y] = (r_new, g_new, b_new)

        image.save(output_path)
        print(f"Image successfully decrypted and saved as {output_path}")
    except Exception as e:
        print("Error:", e)

def main():
    print("=== Simple Image Encryption Tool ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_path = input("Enter the path to the image to encrypt: ")
            output_path = input("Enter the output encrypted image filename (e.g. encrypted.png): ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypt_image(input_path, output_path, key)

        elif choice == '2':
            input_path = input("Enter the path to the encrypted image: ")
            output_path = input("Enter the output decrypted image filename (e.g. decrypted.png): ")
            key = int(input("Enter the same key used for encryption: "))
            decrypt_image(input_path, output_path, key)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
