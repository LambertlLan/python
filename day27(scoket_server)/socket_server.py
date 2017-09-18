# __author: Lambert
# __date: 2017/9/18 11:01
# 创建一个socketserver 至少分以下几步
#
# First, you must create a request handler class by subclassing the BaseRequestHandlerclass and overriding its handle() method; this method will process incoming requests. 　　
# Second, you must instantiate one of the server classes, passing it the server’s address and the request handler class.
#     Then call the handle_request() orserve_forever() method of the server object to process one or many requests.
# Finally, call server_close() to close the socket.
import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print('服务端启动.....')
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))
                print('waiting.....')
                conn.sendall(client_data)
            conn.close()


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8081), Myserver)
    server.serve_forever()
