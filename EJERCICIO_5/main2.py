from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import requests
hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            with open("index.html", "r", encoding="utf-8") as file:
                html_content = file.read()
                self.wfile.write(bytes(html_content, "utf-8"))

        elif self.path.endswith(".css"):
            css_path = self.path.lstrip("/")
            if os.path.exists(css_path):
                self.send_response(200)
                self.send_header("Content-type", "text/css; charset=utf-8")
                self.end_headers()

                with open(css_path, "r", encoding="utf-8") as file:
                    self.wfile.write(bytes(file.read(), "utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

        elif self.path.startswith("/imagenes/"):
            file_path = self.path.lstrip("/")
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header("Content-type", "image/webp")  # Adjust as needed for other image types
                self.end_headers()

                with open(file_path, "rb") as file:
                    self.wfile.write(file.read())
            else:
                self.send_response(404)
                self.end_headers()
                
        elif self.path == "/example":
            url = "https://jsonplaceholder.typicode.com/comments"
            response = requests.get(url)
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
                
            self.wfile.write(bytes(response.text, "utf-8"))
    
        
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")