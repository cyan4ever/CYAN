import socket

#创建TCP套接字对象
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(("127.0.0.1",4567))

#设置监听套接字
sockfd.listen(3)


while True:
#处理客户端链接
    print("Waiting for connect..")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)

    #收发消息
    while True:
        data = connfd.recv(1024)
        if data.decode()=="":
            break
        print("Recv:",data.decode())

        msg=connfd.send(b'Thanks')
        print("Send %d bytes"%msg)

    connfd.close()
sockfd.close()
