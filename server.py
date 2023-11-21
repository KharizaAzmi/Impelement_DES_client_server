import socket
import DES

def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host, port))

    print("Waiting for connection.....")

    mySocket.listen(1)
    
    conn, addr = mySocket.accept()
    print("Koneksi dari: " + str(addr))

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        key = "123456789AABCDEF"
        decryptedMessage = DES.decrypt(data, key)
        print("Decrypted Message = ", DES.bin2text(decryptedMessage))
        # Kirim pesan terdekripsi ke client
        # print("Sending Decrypted Message to Client =", decryptedMessage)
        # conn.send(DES.bin2text(decryptedMessage).encode())
        print("-----------------------------------------------------------------\n")

    conn.close()

if __name__ == '__main__':
    Main()
