var http = require('http');
var fs = require('fs');
http.createServer(funtion(requestAnimationFrame,res){
    fs.readFile('myfile.html',function(err,data){
        res.writeHead(200,{'content-type': 'text.html'});
        res.write(data);
        return res.end();
    });

}).listen(8080);