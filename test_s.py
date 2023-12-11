
import socket

HOST = ''
PORT = 7896

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print("等待连接...")
    conn, addr = s.accept()
    print("连接已建立：", addr)
    
    # 发送数据到客户端
    while True:
        data = input('请输入要发送给客户端的数据（输入"quit"退出）：')
        
        if data == "quit":
            break
       

        conn.sendall(data.encode())
        received_data = conn.recv(1024).decode()
        print("接收到的数据：", received_data)

print("服务器运行结束。")