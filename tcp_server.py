import socket
import threading

def handle_client(conn, addr):
    print(f"[+] 连接来自 {addr}")
    with conn:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            print(f"  收到: {data.decode()}")
            conn.sendall(data.upper())
    print(f"[-] 断开 {addr}")

def start_server(host="0.0.0.0", port=9000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    print(f"[Server] 监听 {host}:{port}")

    while True:
        conn, addr = sock.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()