#!/usr/bin/python3.5

try:
	f = open("fiser.py", "r")

	s = f.read()

	print (s)

except FileNotFoundError:
	print ("Ceva nu este bine. Probabil ca ai gresit numele fisierului")
except IOError:
	print ("Problema IO")
except ValueError:
	print ("Problema de variablie")
except Exception:
	print ("o eroare")
else:
	f.close()

print ("Multumesc pentru utilizare !")

def testFunc( d = 0 ):
	try:
		a = d + 1
	except TypeError:
		print ("Ai gresit tipul valoarii introduse")
	else:
		return a


print (testFunc(1))

print (testFunc("str"))

print ("Salut. Ai terminat !")