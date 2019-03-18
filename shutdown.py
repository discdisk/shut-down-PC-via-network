from http.server import HTTPServer, BaseHTTPRequestHandler  
import os

class RequestHandler(BaseHTTPRequestHandler):  
    def _writeheaders(self):
        print('head')
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
        self._writeheaders()
        print('get')
        print(self.path)
        flag=0
        if self.path=='/shutdown':
            print('ssssssssssssss')
            buf = """<html><head> <title>shutting down</title> </head><body> <h1>shutting down</h1></body></html>"""
            flag=1
        else:
            buf = """<html><head> <title>ESP8266 Pins</title> </head><body> <h1>ESP8266 Pins</h1></body></html>"""
            print('aaavvvvaaaaaaa')
            flag=0
        self.protocal_version = 'HTTP/1.1'  
        self.wfile.write(buf.encode())  
        if flag==1: 
            print('aaaaaaaaaaaaaaaa')
            os.system('shutdown -s -t 1')    #关机
  
def start_server(port):  
    http_server = HTTPServer(('', int(port)), RequestHandler)  
    http_server.serve_forever() #设置一直监听并接收请求  

print('start')
start_server(8088)