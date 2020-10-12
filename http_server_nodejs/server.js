const http =require("http");
var fs=require('fs');
var qs=require('querystring')
const { dirname } = require("path");
const host='localhost';
const port=8080;

const requestListener=function(req,res){
    if (req.method == 'POST') {
        var body = '';

        req.on('data', function (data) {
            body += data;

            // Too much POST data, kill the connection!
            // 1e6 === 1 * Math.pow(10, 6) === 1 * 1000000 ~~~ 1MB
            if (body.length > 1e6)
                req.connection.destroy();
        });

        req.on('end', function () {
            var post = JSON.parse(body);
            console.log(post);
            console.log(post.id);
        });
        
    }
}

const server=http.createServer(requestListener);
server.listen(port,host,function(){
    console.log(`this server is running on http :// ${host}:${port}`);
})