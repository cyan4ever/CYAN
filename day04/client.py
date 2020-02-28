from socket import *

#服务器地址
# server_addr=("127.0.0.1",4567)

sockfd=socket()

#连接服务器
#sockfd.connect(server_addr)
sockfd.connect(("127.0.0.1",4567))

#发送接收消息
while True:
    data = input(">>")
    if data=="":
        break
    sockfd.send(data.encode())
    msg=sockfd.recv(1024)
    print("From server:",msg.decode())

sockfd.close()
