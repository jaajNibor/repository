    # By Javier Perez Mota

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Générateur de QR Code")
        master.geometry("400x400")  # Taille de la fenêtre

        self.label = tk.Label(master, text="Veuillez entrer une adresse URL pour générer un QR Code :", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 12), width=40)
        self.entry.pack(pady=5)

        self.generate_button = tk.Button(master, text="Générer QR Code", font=("Helvetica", 12), command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.image_label = tk.Label(master)
        self.image_label.pack()
        self.qr_image = None 
        

    def generate_qr_code(self):
        url = self.entry.get()
        if url:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            img = img.resize((300, 300))  # Redimensionner l'image du QR code

            self.qr_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.qr_image)
            self.image_label.image = self.qr_image
        else:
            messagebox.showwarning("Avertissement", "Veuillez entrer une adresse URL pour générer un QR Code.")

def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()  
