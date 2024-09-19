from PIL import Image
import numpy as np

# Chemin vers le fichier RAW
file_path = 'Image0_RGB24.raw'

# Dimensions de l'image (exemple)
height = 1860
width = 2880
channels = 3  # Rouge, Vert, Bleu

# Ouvrir le fichier en mode binaire
with open(file_path, 'rb') as file:
    raw_data = file.read()  # Lire toutes les données du fichier

# Initialiser une liste vide pour stocker les pixels
image_data = []

# Lire les données 9 octets à la fois (24 bits par canal, 72 bits par pixel)
for i in range(0, len(raw_data), 9):
    r = int.from_bytes(raw_data[i:i+3], 'big')  # 24 bits pour le canal rouge
    g = int.from_bytes(raw_data[i+3:i+6], 'big')  # 24 bits pour le canal vert
    b = int.from_bytes(raw_data[i+6:i+9], 'big')  # 24 bits pour le canal bleu
    image_data.append((r, g, b))

# Maintenant, nous avons une liste de tuples (r, g, b) avec 24 bits par canal
# Nous devons reformater cela en une image

# Restructurer les données dans un tableau 2D de taille (height, width, 3)
# Vous pouvez utiliser Pillow ou une autre bibliothèque pour manipuler les données

# Convertir la liste en un tableau numpy et le reformer en une image
image_array = np.array(image_data).reshape((height, width, channels))

# Créer une image avec Pillow
image = Image.fromarray(image_array.astype('uint8'))  # Attention ici à l'affichage
image.show()  # Afficher l'image
