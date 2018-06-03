const express = require('express')
const app = express()
var Jumbler = require('./JumbleHelper');
var bodyParser = require('body-parser');

app.use(bodyParser.json());
app.post('/jumble/:_shift',function(req,res){
	var string = req.body.message;
	var N=req.params._shift

	var ret=Jumbler.Jumble(string,N)
	res.json({"jumbled":ret});
}); 


app.listen(3001);
console.log('Running on port 3001')