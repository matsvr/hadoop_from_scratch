import time
import os
import matplotlib.pyplot as plt
import numpy as np

temps_execution1 = []
temps_comptage1 = []
temps_tri1 = []
temps_execution2 = []
temps_comptage2 = []
temps_tri2 = []
tailles_petits_fichiers = [1, 2, 8, 70, 1436, 10861, 17688]
tailles_grands_fichiers = [21558, 43113, 86226, 114969, 172464, 344903]
tailles_fichiers = [1, 2, 8, 70, 1436, 10861, 17688,
                    21558, 43113, 86226, 114969, 172464, 344903]

# Cette fonction permet de séparer un fichier .warc.wet en deux parties égales


def split_warc_wet_file1(file_path):
    # Read the .warc.wet file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Get the size of the file
    file_size = len(data)

    # Calculate the split point, which is half of the file size
    split_point = file_size // 2

    # Ensure the split point is at the end of a line
    while data[split_point] != ord('\n'):
        split_point += 1

    # Split the file into two parts
    part1 = data[:split_point]
    part2 = data[split_point:]

    # Write the first part to a new file
    part1_path = file_path + '.part1'
    with open(part1_path, 'wb') as file:
        file.write(part1)

    # Write the second part to a new file
    part2_path = file_path + '.part2'
    with open(part2_path, 'wb') as file:
        file.write(part2)

    return part1_path, part2_path

# Cette fonction permet de séparer un fichier .warc.wet en trois parties égales


def split_warc_wet_file2(file_path):
    # Read the .warc.wet file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Get the size of the file
    file_size = len(data)

    # Calculate the split point, which is one third of the file size
    split_point1 = file_size // 3

    # Ensure the split point is at the end of a line
    while data[split_point1] != ord('\n'):
        split_point1 += 1

    # Calculate the split point, which is two thirds of the file size
    split_point2 = split_point1 * 2

    # Ensure the split point is at the end of a line
    while data[split_point2] != ord('\n'):
        split_point2 += 1

    # Split the file into three parts
    part1 = data[:split_point1]
    part2 = data[split_point1:split_point2]
    part3 = data[split_point2:]

    # Write the first part to a new file
    part1_path = file_path + '.part1'
    with open(part1_path, 'wb') as file:
        file.write(part1)

    # Write the second part to a new file
    part2_path = file_path + '.part2'
    with open(part2_path, 'wb') as file:
        file.write(part2)

    # Write the third part to a new file
    part3_path = file_path + '.part3'
    with open(part3_path, 'wb') as file:
        file.write(part3)

    return part1_path, part2_path, part3_path


# Cette fonction permet de séparer un fichier .warc.wet en quatre parties égales
def split_warc_wet_file3(file_path):
    # Read the .warc.wet file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Get the size of the file
    file_size = len(data)

    # Calculate the split point, which is one fourth of the file size
    split_point1 = file_size // 4

    # Ensure the split point is at the end of a line
    while data[split_point1] != ord('\n'):
        split_point1 += 1

    # Calculate the split point, which is two fourths of the file size
    split_point2 = split_point1 * 2

    # Ensure the split point is at the end of a line
    while data[split_point2] != ord('\n'):
        split_point2 += 1

    # Calculate the split point, which is three fourths of the file size
    split_point3 = split_point1 * 3

    # Ensure the split point is at the end of a line
    while data[split_point3] != ord('\n'):
        split_point3 += 1

    # Split the file into four parts
    part1 = data[:split_point1]
    part2 = data[split_point1:split_point2]
    part3 = data[split_point2:split_point3]
    part4 = data[split_point3:]

    # Write the first part to a new file
    part1_path = file_path + '.part1'
    with open(part1_path, 'wb') as file:
        file.write(part1)

    # Write the second part to a new file
    part2_path = file_path + '.part2'
    with open(part2_path, 'wb') as file:
        file.write(part2)

    # Write the third part to a new file
    part3_path = file_path + '.part3'
    with open(part3_path, 'wb') as file:
        file.write(part3)

    # Write the fourth part to a new file
    part4_path = file_path + '.part4'
    with open(part4_path, 'wb') as file:
        file.write(part4)

    return part1_path, part2_path, part3_path, part4_path

# Cette fonction permet de séparer un fichier .warc.wet en n parties égales


def split_file(file_path, n):
    # Read the .warc.wet file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Get the size of the file
    file_size = len(data)

    # Calculate the split point, which is one nth of the file size
    split_point = file_size // n

    # Ensure the split point is at the end of a line
    while data[split_point] != ord('\n'):
        split_point += 1

    # Split the file into n parts
    parts = []
    for i in range(n):
        if i == n - 1:
            parts.append(data[split_point * i:])
        else:
            parts.append(data[split_point * i:split_point * (i + 1)])

    # Write the parts to new files
    part_paths = []
    for i, part in enumerate(parts):
        part_path = file_path + '.part' + str(i + 1)
        part_paths.append(part_path)
        with open(part_path, 'wb') as file:
            file.write(part)

    return part_paths


p_177mo, p_177mo2 = split_warc_wet_file1(
    'CC-MAIN-20221001003954-20221001033954-00277.warc.wet')
p_118mo, p_118mo2, p_118mo3 = split_warc_wet_file2(
    'CC-MAIN-20221001003954-20221001033954-00277.warc.wet')
p_86mo, p_86mo2, p_86mo3, p_86mo4 = split_warc_wet_file3(
    'CC-MAIN-20221001003954-20221001033954-00277.warc.wet')
p_43mo, p_43mo2 = split_warc_wet_file1(p_86mo)
p_22mo, p_22mo2 = split_warc_wet_file1(p_43mo)

liste_petits_fichiers = [
    "input.txt",
    "forestier_mayotte.txt",
    "deontologie_police_nationale.txt",
    "domaine_public_fluvial.txt",
    "procedure_civile.txt",
    "travail.txt",
    "sante_publique.txt"]

liste_grands_fichiers = [
    p_22mo,
    p_43mo,
    p_86mo,
    p_118mo,
    p_177mo,
    "CC-MAIN-20221001003954-20221001033954-00277.warc.wet"]

liste_entière = liste_petits_fichiers + liste_grands_fichiers

# Ouvrir les fichiers d'entrée
# for file in liste_petits_fichiers:
#     with open(file, encoding="utf-8") as f:

#         # Initialiser un dictionnaire pour stocker les occurrences des mots
#         word_count = {}

#         # Parcourir chaque ligne du fichier / Compter le temps d'execution
#         startTime1 = time.time()
#         for line in f:

#             # Séparer la ligne en mots
#             words = line.split()

#             # Parcourir chaque mot et incrémenter le compteur
#             for word in words:
#                 if word in word_count:
#                     word_count[word] += 1
#                 else:
#                     word_count[word] = 1
#         endTime1 = time.time()
#         totalTimeCounting = endTime1 - startTime1

#         # Pour les mots ayant le même nombre d'occurrences, les trier par ordre alphabétique croissant
#         startTime2 = time.time()
#         sorted_word_count = sorted(
#             word_count.items(), key=lambda x: (-x[1], x[0]))
#         endTime2 = time.time()
#         totalTimeSorting = endTime2 - startTime2

#         temps_execution1.append(totalTimeCounting + totalTimeSorting)
#         temps_comptage1.append(totalTimeCounting)
#         temps_tri1.append(totalTimeSorting)

for file in liste_grands_fichiers:
    with open(file, encoding="utf-8") as f:

        # Initialiser un dictionnaire pour stocker les occurrences des mots
        word_count = {}

        # Parcourir chaque ligne du fichier / Compter le temps d'execution
        startTime1 = time.time()
        for line in f:

            # Séparer la ligne en mots
            words = line.split()

            # Parcourir chaque mot et incrémenter le compteur
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        endTime1 = time.time()
        totalTimeCounting = endTime1 - startTime1

        # Pour les mots ayant le même nombre d'occurrences, les trier par ordre alphabétique croissant
        startTime2 = time.time()
        sorted_word_count = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0]))
        endTime2 = time.time()
        totalTimeSorting = endTime2 - startTime2

        temps_execution2.append(totalTimeCounting + totalTimeSorting)
        temps_comptage2.append(totalTimeCounting)
        temps_tri2.append(totalTimeSorting)

# tracer le graphique du temps d'execution pour les petits fichiers
# plt.plot(tailles_petits_fichiers, temps_execution1, label="Petits fichiers")
# plt.plot(tailles_petits_fichiers, temps_comptage1, label="Comptage")
# plt.plot(tailles_petits_fichiers, temps_tri1, label="Tri")
# plt.xlabel('Taille des fichiers (en octets))')
# plt.ylabel('Temps d\'execution (en secondes)')
# plt.title('Temps d\'execution pour les petits fichiers')
# plt.legend()
# plt.show()

# tracer le graphique du temps d'execution pour les grands fichiers
plt.plot(tailles_grands_fichiers, temps_execution2, label="Grands fichiers")
plt.plot(tailles_grands_fichiers, temps_comptage2, label="Comptage")
plt.plot(tailles_grands_fichiers, temps_tri2, label="Tri")
plt.xlabel('Taille des fichiers (en octets))')
plt.ylabel('Temps d\'execution (en secondes)')
plt.title('Temps d\'execution pour les grands fichiers')
plt.legend()
plt.show()
