'use strict'

const express = require('express');
const {PythonShell} = require("python-shell");
const socketIO=require('socket.io');

//Configuracion del sevidor
const app = express();

app.use(express.static(__dirname + '/src'));

var server = app.listen(3000, ()=> console.log('listening on port 3000...'));

//Configuracion del socket
var io = socketIO(server);

io.on('connection', function(socket){
	console.log("made socket connection");

	socket.on('request', function(data){
		console.log(data);
		pythonScript(data);
	});

});

//Comunicacion con python
function pythonScript(arg){
	var options = {
		mode: 'text',
		encoding: 'utf8',
		pythonOptions: ['-u'],
		scriptPath: './',
		args: [arg],
		pythonPath: '/usr/bin/python'
	};


	var test = new PythonShell('main.py', options);
	test.on('message', function (message){
		console.log(message);
		io.emit('response', message);
	});
}