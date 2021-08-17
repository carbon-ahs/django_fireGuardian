var a = prompt('Days');
var y = a/365; 
console.log(Math.floor(y),Math.floor(a%365/30),Math.floor(a%365)%30);