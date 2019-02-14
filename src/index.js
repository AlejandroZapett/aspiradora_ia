const socket = io();

//DOM
var button0 = document.getElementById('Cero');
var button1 = document.getElementById('Uno');
var button2 = document.getElementById('Dos');
var button3 = document.getElementById('Tres');
var button4 = document.getElementById('Cuatro');
var button5 = document.getElementById('Cinco');
var button6 = document.getElementById('Seis');
var button7 = document.getElementById('Siete');

//Functions
button0.addEventListener('click', function(){
	socket.emit('request', '0');
});
button1.addEventListener('click', function(){
	socket.emit('request', '1');
});
button2.addEventListener('click', function(){
	socket.emit('request', '2');
});
button3.addEventListener('click', function(){
	socket.emit('request', '3');
});
button4.addEventListener('click', function(){
	socket.emit('request', '4');
});
button5.addEventListener('click', function(){
	socket.emit('request', '5');
});
button6.addEventListener('click', function(){
	socket.emit('request', '6');
});
button7.addEventListener('click', function(){
	socket.emit('request', '7');
});

//response
var division = document.getElementById('response-area');
var imagenes = [];
var imagen = document.createElement("IMG");

socket.on('response', function(message){
	hijos = parseMessage(message);
	console.log(message);
	hijos.forEach(function(e){
		name = "img/"+e.replace(" ", "")+".png";
		console.log(name);
		var imagen = document.createElement("IMG");
		imagen.setAttribute("src", name);
		imagenes.push(imagen)
	});

	console.log(imagenes)
	imagenes.forEach(function(e){
		division.appendChild(e)
	});

	imagenes = [];

});

function parseMessage(message){
	return message.replace("[","").replace("]","").split(",")
}
