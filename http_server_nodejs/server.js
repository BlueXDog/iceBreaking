const http =require("http");
const fs=require('fs').promises;
const host='localhost';
const port=8080;

const requestListener=function(req,res){
   console.log(__dirname)

    fs.readFile("/home/vinh/Documents/ice_breaking/training-vinh/http_server_nodejs/index.html")
    .then(contents => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(contents);
    })
    .catch(err => {
        res.writeHead(500);
        res.end(err);
        return;
    });
}


const server=http.createServer(requestListener);
server.listen(port,host,function(){
    console.log(`this server is running on http :// ${host}:${port}`);
})