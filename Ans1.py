
def MoveNext(ch,n):
	nchr='a'
	if ord(ch)+n<=ord('z'):
		nchr=chr(ord(ch)+n)
	else:
		nchr=chr( ord(ch)-ord('z') +ord('a')+ n-1)
	return nchr

def Jumble(strn, n):
	if strn is  None or not isinstance(strn, str):
		return "Not a string"
	try:
		n = int(n)
	except ValueError:
		return  "Wrong N: Integer required"
	if (n<1 or n>1000):
		return  "N should range between [1-1000]"
	retArray =""
	i=0;
	for chr in strn:
		if chr>='a'and chr<='z':
			retArray += MoveNext(chr, n%26)
		elif chr>='0'and chr<='9':
			retArray+=chr
		else:
			pass
	return retArray;

