import socket
import threading
import time

def EscolhaCliente(c):
    opt = (c.recv(2048)).decode()
    ans = ""
    if(opt == "0"):
        ans = time.strftime("%d/%m/%y")
    elif(opt == "1"):
        ans = time.strftime("%H:%M")
    elif(opt == "2"):
        ans = time.strftime("%d/%m/%y"+"e"+ "%H:%M")
    c.send(ans.encode())
    c.close()

def servidor(host="localhost", port=3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(5)
        while True:
            client, address = sock.accept()
            t = threading.Thread(target=EscolhaCliente, args=(client,))
            t.start()
            t.join()

if __name__ == "__main__":
    servidor()
