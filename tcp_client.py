import socket

def start_client(server_host="127.0.0.1", server_port=9000):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((server_host, server_port))
    print(f"[Client] 已连接 {server_host}:{server_port}")
    print("[Client] 输入消息后回车发送，输入 quit 退出\n")

    with client_sock:
        while True:
            try:
                msg = input("你: ").strip()
            except (EOFError, KeyboardInterrupt):
                break

            if not msg:
                continue
            if msg.lower() == "quit":
                print("[Client] 退出")
                break

            client_sock.sendall((msg + "\n").encode("utf-8"))
            reply = client_sock.recv(4096).decode("utf-8").strip()
            print(f"服务器: {reply}\n")

if __name__ == "__main__":
    start_client()