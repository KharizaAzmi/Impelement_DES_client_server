import socket
import DES

def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host, port))

    while True:
        message = input("Enter the message you want to encrypt (q to quit) -> ")

        if message == 'q':
            break

        key = "123456789AABCDEF"
        encryptedMessage = DES.bin2hex(DES.encrypt(message, key))

        mySocket.send(encryptedMessage.encode())
        # Menampilkan hasil enkripsi di layar
        print("Encrypted message = ", encryptedMessage)
        # received_data = mySocket.recv(1024).decode()
        # print("Received Encrypted Message from Server =", received_data)
        print("-----------------------------------------------------------------\n")

    mySocket.close()

if __name__ == '__main__':
    Main()
