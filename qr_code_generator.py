import qrcode  # Importation de la bibliothèque "qrcode"
from PIL import Image

def generate_qr_code_with_color(text, file_name, fill_color="#153462", back_color="white"):
    # Configuration du QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Génération de l'image QR Code avec les couleurs spécifiées
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    # Sauvegarde de l'image
    img.save(file_name)

# Insère ton texte pour générer un QR Code
text = "https://vexcloud.fr"
# Définit le nom du fichier pour sauvegarder l'image QR code
file_name = "qr_code_custom_color.png"
# Génération du QR Code avec la couleur spécifiée
generate_qr_code_with_color(text, file_name, fill_color="#153462")
print(f"Le QR code a été généré et sauvegardé sous le nom de {file_name}")