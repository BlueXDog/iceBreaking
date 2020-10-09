from http.server import BaseHTTPRequestHandler
import os
import json
#cac phuong thuc can thuc hien 
# insert tao moi ban ghi 
# update ban ghi trong db 
# read ban ghi 
# delete ban ghi 
from DB_connect import insert_row ,update_row, read_row,delete_row


class Server(BaseHTTPRequestHandler):
    def _set_response(self,message):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')      
        self.end_headers()
        self.wfile.write(b'hello this is vinh')
        self.wfile.write(bytes(message,'utf-8'))

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = "File not found"
                self.send_error(404,f)
        except Exception :
            f = "File not found"
            self.send_error(404,f)
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        #print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
         #       str(self.path), str(self.headers), post_data.decode('utf-8'))
        print("Post request \n",str(self.path))

        print("Post data ", post_data.decode('utf-8'))
        
        post_data_json=json.loads(str(post_data.decode('utf-8')))
        # print(post_data_json)
        command =post_data_json['command']
        print("this is method :",command)
        #print("this is menu ",str(post_data_json['menu']))
        if command=="insert":
            insert_row(studentName=post_data_json['name'],location=post_data_json['location'])
            self._set_response("insert success")
        elif command=="read":
            row_data=read_row(post_data_json['id'])
            self._set_response(row_data)
        elif command=="delete":
            delete_row(post_data_json['id'])
            self._set_response("delete success")
        elif command=="update":
            update_row(post_data_json['id'],post_data_json['name'],post_data_json['location'])        
        
        



        


