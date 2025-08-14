✨ Features :

🔒 Encrypt images with a numeric key

🔓 Decrypt images using the same key

🖼️ Supports common formats like .png, .jpg, .jpeg, etc.

💡 Beginner-friendly code with clear structure

⚙️ How It Works :

The program shifts each pixel's R, G, and B values by the encryption key.
During decryption, the shift is reversed using the same key.

Example with key = 50:

Original pixel (120, 200, 50)

Encrypted pixel (170, 250, 100)

Decryption restores it to (120, 200, 50)

📦 Installation :

Clone the repository

git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool


Install dependencies

pip install pillow


Run the program ;

python image_encryption.py

🖥️ Usage

When you run the script, you’ll see a menu:

=== Simple Image Encryption Tool ===

Options:
1. Encrypt an image
2. Decrypt an image
3. Exit


Example encryption:

Enter your choice (1/2/3): 1
Enter the path to the image to encrypt: sample.png
Enter the output encrypted image filename (e.g. encrypted.png): secret.png
Enter the encryption key (an integer): 50
Image successfully encrypted and saved as secret.png


Example decryption:

Enter your choice (1/2/3): 2
Enter the path to the encrypted image: secret.png
Enter the output decrypted image filename (e.g. decrypted.png): restored.png
Enter the same key used for encryption: 50
Image successfully decrypted and saved as restored.png

📂 File Structure
.
├── image_encryption.py   # Main Python script
└── README.md             # Documentation
