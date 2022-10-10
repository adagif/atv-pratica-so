import socket

def cliente(host="localhost", port=3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        menu=""" MENU
0. Data
2) Hora
3) Data e Hora"""
        x = ""
        print(menu)
        while(x not in ["0", "1", "2"]):
            x = input("Escolha: ")
            if x not in ["0", "1", "2"]:
                print("Indisponivel")
        sock.send(x.encode('utf-8'))
        print(sock.recv(2048).decode())



if __name__ == "__main__":
    cliente()
