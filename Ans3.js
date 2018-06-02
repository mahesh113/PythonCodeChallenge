const express = require('express')
const app = express()
var bodyParser = require('body-parser');

var PythonShell = require('python-shell')
var JumbleApp = new PythonShell('Ans1.py')
app.use(bodyParser.json());
app.post('/jumble/:_shift',function(req,res){
	var string = req.body.message;
	var N=req.params._shift

	var spawn = require("child_process").spawn;
	var pythonProcess = spawn('python',["Ans1.py", string, N]);


	pythonProcess.stdout.on('data', function (data){
		
	});
	//JumbleApp.send(string,N)
	console.log(a)
	
	//res.json(str);
}); 


app.listen(3001);
console.log('Running on port 3001')