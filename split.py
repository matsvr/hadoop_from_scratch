import sys
import os


def split_file(file_path, n):
    # On lit le fichier .warc.wet en binaire
    with open(file_path, 'rb') as file:
        data = file.read()

    # On récupère la taille du fichier
    file_size = len(data)

    # On calcule le point de séparation, qui est la taille du fichier divisé par le nombre de workers
    split_point = file_size // n

    # On s'assure que le point de séparation est à la fin d'une ligne
    while data[split_point] != ord('\n'):
        split_point += 1

    # On sépare le fichier en n parties
    parts = []
    for i in range(n):
        if i == n - 1:
            parts.append(data[split_point * i:])
        else:
            parts.append(data[split_point * i:split_point * (i + 1)])

    # On écrit chaque partie dans un nouveau fichier
    part_paths = []
    for i, part in enumerate(parts):
        part_path = file_path + '.part' + str(i + 1)
        part_paths.append(part_path)
        with open(part_path, 'wb') as file:
            file.write(part)

    return part_paths


n = 0
with open('machines.txt', 'r') as f:
    # On peut remplacer par l'IP ou le hostname du serveur
    hosts = [line.strip() for line in f.readlines()]
    n = len(hosts)

splits = split_file(
    # Chemin d'accès du fichier en local
    "/home/matsvr/RenduTP_Mathieu_SAUVEUR/adeployer/splits/grosfichier6.warc.wet.part1", n)

print(f"Fichier séparé en {n} parties")

# Supprime le fichier original du répertoire local
os.remove(
    "/home/matsvr/RenduTP_Mathieu_SAUVEUR/adeployer/splits/grosfichier6.warc.wet.part1")

print("Fichier original supprimé")
