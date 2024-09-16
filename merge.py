# # Noms des fichiers WARC.WET à fusionner
# nom_fichier1 = 'grosfichier1.warc.wet'
# nom_fichier2 = 'grosfichier2.warc.wet'

# # Nom du fichier de sortie
# nom_fichier_sortie = 'fichier_fusionne.warc.wet'

# # Ouvrir le fichier de sortie en mode écriture
# with open(nom_fichier_sortie, 'wb') as fichier_sortie:  # Notez le 'wb' pour le mode binaire
#     # Ouvrir le premier fichier en mode lecture binaire
#     with open(nom_fichier1, 'rb') as fichier1:
#         # Copier le contenu du premier fichier dans le fichier de sortie
#         while True:
#             buffer = fichier1.read(1024*1024)  # Lire en morceaux de 1 Mo
#             if not buffer:
#                 break
#             fichier_sortie.write(buffer)

#     # Ouvrir le deuxième fichier en mode lecture binaire
#     with open(nom_fichier2, 'rb') as fichier2:
#         # Copier le contenu du deuxième fichier dans le fichier de sortie
#         while True:
#             buffer = fichier2.read(1024*1024)  # Lire en morceaux de 1 Mo
#             if not buffer:
#                 break
#             fichier_sortie.write(buffer)

# print(
#     f"Les fichiers '{nom_fichier1}' et '{nom_fichier2}' ont été fusionnés en '{nom_fichier_sortie}'.")


# Définir le nombre total de fichiers à fusionner
nombre_de_fichiers = 6  # Mettez ici le nombre exact de fichiers

# Nom du fichier de sortie
nom_fichier_sortie = 'fichier_fusionne.warc.wet'

# Ouvrir le fichier de sortie en mode écriture binaire
with open(nom_fichier_sortie, 'wb') as fichier_sortie:
    # Boucle pour parcourir tous les fichiers
    for i in range(1, nombre_de_fichiers + 1):
        # Générer le nom du fichier courant
        nom_fichier = f'grosfichier{i}.warc.wet'

        # Ouvrir le fichier courant en mode lecture binaire
        with open(nom_fichier, 'rb') as fichier:
            # Copier le contenu du fichier dans le fichier de sortie
            while True:
                buffer = fichier.read(1024*1024)  # Lire en morceaux de 1 Mo
                if not buffer:
                    break
                fichier_sortie.write(buffer)

print(f"Tous les fichiers ont été fusionnés en '{nom_fichier_sortie}'.")
