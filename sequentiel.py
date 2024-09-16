import time
import os

temps_execution = []
temps_comptage = []
temps_tri = []
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


# p_177mo, p_177mo2 = split_warc_wet_file1(
#     'CC-MAIN-20221001003954-20221001033954-00277.warc.wet')
# p_118mo, p_118mo2, p_118mo3 = split_warc_wet_file2(
#     'CC-MAIN-20221001003954-20221001033954-00277.warc.wet')
# p_86mo, p_86mo2, p_86mo3, p_86mo4 = split_warc_wet_file3(
#     'CC-MAIN-20221001003954-20221001033954-00277.warc.wet')
# p_43mo, p_43mo2 = split_warc_wet_file1(p_86mo)
# p_22mo, p_22mo2 = split_warc_wet_file1(p_43mo)

# Récupérer la taille des fichiers
# p1_size = os.path.getsize(p1)
# print(f"La premiere partie du fichier warc.wet fait {p1_size}")
# p1_1_size = os.path.getsize(p1_1)
# print(f"La premiere partie du fichier p1 fait {p1_1_size}")
# p1_1_1_size = os.path.getsize(p1_1_1)
# print(f"La premiere partie du fichier p1_1 fait {p1_1_1_size}")

# Ouvrir le fichier d'entrée
# with open("input.txt", encoding="utf-8") as f:  # 1ko
# with open("forestier_mayotte.txt", encoding="utf-8") as f:  # 2ko
# with open("deontologie_police_nationale.txt", encoding="utf-8") as f:  # 8ko
# with open("domaine_public_fluvial.txt", encoding="utf-8") as f:  # 70ko
# with open("procedure_civile.txt", encoding="utf-8") as f: # 1.5Mo
# with open("travail.txt", encoding="utf-8") as f: # 10Mo
# with open("sante_publique.txt", encoding="utf-8") as f:  # 18Mo
    # with open(p_22mo, encoding="utf-8") as f: # 22Mo
    # with open(p_43mo, encoding="utf-8") as f: # 43Mo
    # with open(p_86mo, encoding="utf-8") as f: # 86Mo
    # with open(p_118mo, encoding="utf-8") as f: # 118Mo
    # with open(p_177mo, encoding="utf-8") as f: # 177Mo
    # with open("CC-MAIN-20221001003954-20221001033954-00277.warc.wet", encoding="utf-8") as f: # 344Mo
with open("grosfichier2.warc.wet", encoding="utf-8") as f:

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
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    endTime2 = time.time()
    totalTimeSorting = endTime2 - startTime2

    # Trier le dictionnaire par nombre d'occurrences décroissant seulement
    # startTime2 = time.time()
    # sorted_word_count = sorted(
    #     word_count.items(), key=lambda x: x[1], reverse=True)
    # endTime2 = time.time()
    # totalTimeSorting = endTime2 - startTime2

    # Trier le dictionnaire par ordre alphabétique croissant
    # sorted_word_count = sorted(word_count.items(), key=lambda x: x[0].lower())

    # # Trier le dictionnaire par ordre alphabétique décroissant / Compter le temps d'execution
    # startTime2 = time.time()
    # sorted_word_count = sorted(
    #     word_count.items(), key=lambda x: x[0].lower(), reverse=True)
    # endTime2 = time.time()
    # totalTimeSorting = endTime2 - startTime2

    # Afficher le résultat non trié
    # for word, count in word_count.items():
    #     print(f"{word}: {count}")

    # # Afficher le résultat trié avec un saut de ligne
    # for word, count in sorted_word_count:
    #     print(f"{word}: {count},")

    # Afficher les 50 premiers mots
    # for word, count in sorted_word_count[:50]:
    #     print(f"{word}: {count}")
    print(f"Les 50 premiers mots : {sorted_word_count[:50]}")

    # Afficher les mots et leur occurences à la suite
    # for word in sorted_word_count:
    #     print(word)

    # Afficher le nombre de mots
    print(f"Nombre de mots uniques : {len(word_count)}")

    # Afficher le temps d'execution
    print(
        f"Temps d'execution pour le comptage des occurences : {totalTimeCounting}")
    print(f"Temps d'execution pour le tri : {totalTimeSorting}")
