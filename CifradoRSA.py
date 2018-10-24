#Zona de funciones
def es_primo(num):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
    for i in range(2,num):
        if (num%i)==0:
            # es divisible
            return False
    return True

def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

#Pedir Variables
print("Introduzca el numero p")
p=int(input())
if es_primo(p):
	print("Numero P correcto")
	print("Introduzca el numero q")
	q=int(input())
	if es_primo(q):
		print ("Numero Q correcto")
		n=p*q
		print("N es "+str(n))
		pi_n=(p-1)*(q-1)
		print("0n vale "+str(pi_n))
		print("Introduzca el numero e")
		e=int(input())
		if (e>0 and e<pi_n) and (mcd(pi_n,e)==1) and es_primo(e):
			print("Numero E correcto.")
		else:
			print("Numero E no correcto.")
	else:
		print("Numero Q incorrecto no es primo")
else:
	print("Numero P incorrecto no es primo")
#Cifrado RSA
print("Introduzca el mensaje")
m=int(input())
print("La formula es: C="+str(m)+"^"+str(e)+"(mod "+str(n)+")")
c=(m**e)%n
print("El criptograma es: "+str(c))