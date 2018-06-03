function Shift(ch, N) {
	N=parseInt(N);
	asciiCode=parseInt(ch.charCodeAt(0));
	zAscii=parseInt('z'.charCodeAt(0));
	if (asciiCode+N<=zAscii){
		console.log('y')
		return  String.fromCharCode(asciiCode+N)
	}
	else{
		console.log('n')
		return String.fromCharCode( asciiCode  -zAscii +'a'.charCodeAt(0)+ N-1)
	}
}

 module.exports.Jumble=function(strn, N) {
	if(!(typeof strn === 'string' || strn instanceof String))	{
		return "Not a string";
	}
	if(isNaN(parseInt(N, 10))) 
	{
		return  "Not Number"
	} 
	var n=parseInt(N, 10);

 	if (n<1 || n>1000){
		return  "N should range between [1-1000]";
 	}
	var retArray ="";

	for(i=0;i<strn.length;i++){
		if(strn[i]>='a'&&strn[i]<='z'){
			retArray+=Shift(strn[i],N);
			console.log('--loop'+i+retArray)
		}
		else if(strn[i]>='0'&&strn[i]<='9'){
			retArray+=strn[i]
		}

	}
	return retArray;
}