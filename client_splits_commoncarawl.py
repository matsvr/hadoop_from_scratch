import socket
import os
import struct
import traceback
import time
import json
import threading
import random

# Fonction pour envoyer et recevoir des messages


def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)


def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    if not lengthbuf:
        return ''
    length, = struct.unpack('!I', lengthbuf)
    return recvall(sock, length)


def recvall(sock, count):
    fragments = []
    while count:
        chunk = sock.recv(count)
        if not chunk:
            return None
        fragments.append(chunk)
        count -= len(chunk)
    arr = b''.join(fragments)
    return arr


def map_start(host, port, splits):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        # Envoie map start à host
        send_one_message(client_socket, '------> map start <------'.encode())
        splits_json = json.dumps(splits)
        send_one_message(client_socket, splits_json.encode())
        response = recv_one_message(client_socket).decode()

    except Exception as e:
        print(f"Cannot connect with {host}: {e}")
        traceback.print_exc()


def shuffle_start(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        # Envoie shuffle start à host
        send_one_message(
            client_socket, '------> shuffle start <------'.encode())
        response = recv_one_message(client_socket).decode()

    except Exception as e:
        print(f"Cannot connect with {host}: {e}")
        traceback.print_exc()


def reduce_start(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        # Envoie recduce start à host
        send_one_message(
            client_socket, '------> reduce start <------'.encode())
        response = recv_one_message(client_socket).decode()

    except Exception as e:
        print(f"Cannot connect with {host}: {e}")
        traceback.print_exc()


def bye(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        message = '------> Bye !! <------'
        send_one_message(client_socket, message.encode())
        client_socket.close()

    except Exception as e:
        print(f"Cannot connect with {host}: {e}")
        traceback.print_exc()


def main():
    # Open the hosts file and read the hosts into a list
    with open('machines.txt', 'r') as f:
        # replace with the server IP address or hostname
        hosts = [line.strip() for line in f.readlines()]
        splits = []
        # for i in range(len(hosts)):
        for i in range(10):
            # splits.append(
            #     f"/tmp/msauveur-23/adeployer/splits/travail.txt.part{i+1}")
            # splits.append(f"/tmp/msauveur-23/adeployer/splits/S{i}.txt")
            # splits.append(
            #     f"/tmp/msauveur-23/adeployer/splits/fichier_fusionne2.warc.wet.part{i+1}")
            # On utilise les commoncrawl
            splits.append(
                f"/cal/commoncrawl/CC-MAIN-20230320144934-20230320174934-0030{i}.warc.wet")
        splits_to_send_to_host = {}
        for i in range(len(hosts)):
            splits_to_send_to_host[i] = []
        fichiers_par_serveur = len(splits) // len(hosts)
        fichiers_restants = len(splits) % len(hosts)
        port = 6900
        servers = []
        for i in range(len(hosts)):
            servers.append((hosts[i], port))

        for host in hosts:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

            # send "Hello"
            message = '------> hello !! <------'
            send_one_message(client_socket, message.encode())
            response = recv_one_message(client_socket).decode()
            print(f'Received response from {socket.gethostname()}: {response}')

            # send file
            filename = 'machines.txt'
            filesize = os.path.getsize(filename)
            message = 'file'
            send_one_message(client_socket, message.encode())
            send_one_message(client_socket, filename.encode())
            send_one_message(client_socket, str(filesize).encode())
            with open(filename, 'rb') as f:
                data = f.read(1024)
                while data:
                    send_one_message(client_socket, data)
                    # add a 1 second delay between sending messages
                    # time.sleep(1)
                    data = f.read(1024)
            response = recv_one_message(client_socket).decode()
            print(f'Received response by {socket.gethostname()}: {response}')

        print("\n")

        # Nous allons faire les machines se dire bonjour entre elles
        for host1 in hosts:
            client_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host1, port))

            # Envoie Go a host
            message = '------> go <------'
            send_one_message(client_socket, message.encode())
            response = recv_one_message(client_socket).decode()
            print(f'Received response from {host1}: {response}')
        time.sleep(2)

        print("\n")

        # Premier threading pour lancer en simultanée le map sur chaque host
        threads1 = []
        map_debut = time.time()
        for server in servers:
            index_split = 0
            for server in servers:
                # Déterminer le nombre de fichiers à assigner à ce serveur
                nombre_a_assigner = fichiers_par_serveur + \
                    (1 if fichiers_restants > 0 else 0)
                fichiers_restants -= 1

                # Assigner les fichiers au serveur
                for _ in range(nombre_a_assigner):
                    if index_split < len(splits):
                        splits_to_send_to_host[servers.index(
                            server)].append(splits[index_split])
                        index_split += 1

            thread = threading.Thread(target=map_start, args=(
                server[0], server[1], splits_to_send_to_host[servers.index(
                    server)]))
            thread.start()
            threads1.append(thread)

        for thread in threads1:
            thread.join()
        map_fin = time.time()
        map_total = map_fin - map_debut
        print(f"map operation finished ! -------> {map_total} seconds")
        time.sleep(2)

        # Deuxième threading pour lancer en simultanée le shuffle sur chaque host
        threads2 = []
        shuffle_debut = time.time()
        for server in servers:
            thread = threading.Thread(
                target=shuffle_start, args=(server[0], server[1]))
            thread.start()
            threads2.append(thread)

        for thread in threads2:
            thread.join()
        shuffle_fin = time.time()
        shuffle_total = shuffle_fin - shuffle_debut
        print(f"shuffle operation finished ! -------> {shuffle_total} seconds")
        time.sleep(2)

        # Troisième threading pour lancer en simultanée le reduce sur chaque host
        threads3 = []
        reduce_debut = time.time()
        for server in servers:
            thread = threading.Thread(
                target=reduce_start, args=(server[0], server[1]))
            thread.start()
            threads3.append(thread)

        for thread in threads3:
            thread.join()
        reduce_fin = time.time()
        reduce_total = reduce_fin - reduce_debut
        print(f"reduce operation finished ! -------> {reduce_total} seconds")
        time.sleep(2)

        print("\n")

        # Combiner les résultats du reduce de chaque host et récupérer le temps d'exécution
        resultats = []
        operations_durations = {}
        for server in servers:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                client_socket.connect((server[0], server[1]))
                message = '------> Envoie moi les résultats <------'
                send_one_message(client_socket, message.encode())
                response1_json = recv_one_message(client_socket).decode()
                response1 = json.loads(response1_json)
                response2_json = recv_one_message(client_socket).decode()
                response2 = json.loads(response2_json)
                operations_durations[server[0]] = response1
                for item in response2.items():
                    resultats.append(item)

            except Exception as e:
                print(f"Cannot connect with {server[0]}: {e}")
                traceback.print_exc()

        # On print dans le terminal le temps d'exécution de chaque opération et les résultats pour chaque host
        print("Operations durations:")
        for server in servers:
            print(f"{server[0]}: {operations_durations[server[0]]}\n")

        print(
            f"Overall we have waited {map_total + shuffle_total + reduce_total} seconds")

        print(
            f"Nombre de mots uniques dans les résultats globaux : {len(resultats)}")

        # Dernier threading pour dire bye à chaque host
        threads4 = []
        for server in servers:
            thread = threading.Thread(
                target=bye, args=(server[0], server[1]))
            thread.start()
            threads4.append(thread)

        for thread in threads4:
            thread.join()


if __name__ == '__main__':
    main()
