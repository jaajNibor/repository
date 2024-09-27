import tkinter as tk
from QRCodeGen import QRCodeGeneratorApp  # Importation du fichier QRCodeGen qui sert à générer le QR code
import pytest
from PIL import ImageTk, Image

@pytest.fixture
def app():
    # Création de la fenêtre Tkinter avant chaque test
    root = tk.Tk()
    root.withdraw()
    app_instance = QRCodeGeneratorApp(root)
    
    yield app_instance  # Retourner l'instance de l'application pour les tests
    
    # Teardown: Fermer la fenêtre Tkinter après chaque test
    root.quit()  # Quitter la boucle principale de Tkinter
    root.after(10, root.destroy)  # Fermer la fenêtre avec un petit délai

class TestQRCodeGen:
    
    def test_qr_code_generation_url_valide(self, app):
        # Test pour vérifier que le QR code est généré correctement pour une URL valide
        app.entry.insert(0, "https://google.com")
        app.generate_qr_code()
        
        # Vérifier que le QR code a été généré
        assert app.qr_image is not None, "Le QR code n'a pas été généré correctement."

        
    def test_qr_code_url_vide(self, app):
        # Test pour une URL vide

        app.entry.insert(0, "")  # Insérer une chaîne vide
        app.generate_qr_code()
        
        # Vérifier qu'aucun QR code n'a été généré
        assert app.qr_image is None, "Un QR code a été généré alors que l'URL était vide."
    def test_qr_code_url_trop_longue(self, app):
        # Test pour une URL très longue
        app.entry.insert(0, "ceci/est/une/url/tres/longue" + "haha" * 100)
        app.generate_qr_code()
        
        # Vérifier que le QR code a été généré malgré la longueur de l'URL
      
        assert app.qr_image is not None, "Le QR code n'a pas été généré pour une URL très longue."

'''    def test_qr_code_generation_url_non_valide(self, app):
        #vérifier avec une mauvaise url
        app.entry.insert(0,"hg.cette-url-n'est-pa-valide")
        app.generate_qr_code()
        assert not hasattr(app, 'qr_image'), "l'url est valide."
   ''' 