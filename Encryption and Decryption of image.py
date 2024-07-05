import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os

class ImageEncryptorDecryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption and Decryption")

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.select_image_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack()

        self.image_path = ""
        self.encrypted_image_path = ""

    def select_image(self):
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def encrypt_image(self):
        if not self.image_path:
            tk.messagebox.showerror("Error", "Please select an image first.")
            return

        password = tk.simpledialog.askstring("Input", "Enter password for encryption:", show="*")
        if not password:
            return

        output_filename = os.path.splitext(os.path.basename(self.image_path))[0] + "_encrypted.png"
        self.encrypted_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=output_filename)

        if not self.encrypted_image_path:
            return

        with open(self.image_path, "rb") as f:
            plaintext = f.read()

        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.get_key(password), AES.MODE_CBC, iv)
        ciphertext = iv + cipher.encrypt(self.pad(plaintext))

        with open(self.encrypted_image_path, "wb") as f:
            f.write(ciphertext)

        tk.messagebox.showinfo("Success", "Image encrypted successfully.")

    def decrypt_image(self):
        if not self.encrypted_image_path:
            tk.messagebox.showerror("Error", "No encrypted image found.")
            return

        password = tk.simpledialog.askstring("Input", "Enter password for decryption:", show="*")
        if not password:
            return

        with open(self.encrypted_image_path, "rb") as f:
            ciphertext = f.read()

        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.get_key(password), AES.MODE_CBC, iv)
        plaintext = self.unpad(cipher.decrypt(ciphertext[AES.block_size:]))

        decrypted_image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile="decrypted_image.png")

        if not decrypted_image_path:
            return

        with open(decrypted_image_path, "wb") as f:
            f.write(plaintext)

        tk.messagebox.showinfo("Success", "Image decrypted successfully.")

    def get_key(self, password):
        hasher = SHA256.new(password.encode())
        return hasher.digest()

    def pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size).encode()

    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorDecryptor(root)
    root.mainloop()
