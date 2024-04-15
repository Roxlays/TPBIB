import socket
import pickle

def send_command(command, args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 65432))
        s.sendall(pickle.dumps((command, args)))
        data = s.recv(1024)
        return pickle.loads(data)

def main():
    print("Bienvenue dans le client de la bibliothèque réseau")
    while True:
        cmd = input("Entrez la commande (ADD, GET, DEL, QUIT): ")
        if cmd == 'QUIT':
            break
        if cmd in ['ADD', 'GET', 'DEL']:
            args = input("Entrez les arguments : ").split(',')
            print("Réponse du serveur:", send_command(cmd, args))
        else:
            print("Commande inconnue")

if __name__ == '__main__':
    main()
