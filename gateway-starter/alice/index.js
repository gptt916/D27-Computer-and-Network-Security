var request = require('request');

var config = {};

var do_request = function(){
    request.get("http://welcome.seclab.space/", function (err, response, body) {
        if (err) return console.log(err);
        if (response.statusCode != 200) return console.log(response.statusCode);
        return console.log(body);
    });
};

setInterval(do_request, 1 * 1000);