import numpy as np
import matplotlib.pyplot as plt
import OpenEXR
import Imath

# Definir les dimensions de l'image et le nombre de canaux
width =  2880
height = 1860
channels = 3

# Lire le fichier RAW en mode binaire
file_path = 'Image0_RGB16.raw'
with open(file_path, 'rb') as file:
    raw_data = np.frombuffer(file.read(), dtype=np.uint16)

# Restructurer les donnees en une matrice 3D de taille (2880, 1860, 3)
image_data = raw_data.reshape((height, width, channels))

plt.imshow(image_data)
plt.show()

# Normaliser l'image pour que les valeurs soient comprises entre 0 et 1
image_normalized = image_data / np.max(image_data)

# Appliquer la correction gamma
gamma = 0.1
image_gamma_corrected = np.power(image_normalized, gamma)

# Convertir l'image en 8 bits (0-255)
image_8bit = (image_gamma_corrected * 255).astype(np.uint8)

# Afficher l'image corrigee
plt.imshow(image_8bit)
plt.show()

# Exporter l'image au format EXR

# Configuration du fichier EXR
output_exr_path = "image_gamma_corrected.exr"
header = OpenEXR.Header(width, height)
FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)  # Type pour les canaux dans OpenEXR

# Creer un fichier EXR avec des canaux flottants
exr_file = OpenEXR.OutputFile(output_exr_path, header)

# Convertir les canaux R, G, B pour OpenEXR
red_channel = image_gamma_corrected[:, :, 0].astype(np.float32).tobytes()
green_channel = image_gamma_corrected[:, :, 1].astype(np.float32).tobytes()
blue_channel = image_gamma_corrected[:, :, 2].astype(np.float32).tobytes()

# Ecrire les trois canaux dans le fichier EXR
exr_file.writePixels({'R': red_channel, 'G': green_channel, 'B': blue_channel})

# Fermer le fichier EXR
exr_file.close()

