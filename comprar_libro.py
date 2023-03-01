print('Ve a la bibilioteca')
print('Elige un libro')
libro = ('')
libro= input()
print ('Has elegido un gran libro', 'llamado', libro , 'gran eleccion')

print('Este libro tiene un valor')

valor= ('')
valor= input()
print('Has pagado tu libro con un valor de:', valor, )
print('confirma por favor con un si o no, si ya terminaste')
confirmar=("")
confirmar= input("")
if confirmar == "si":
    print("Ya pagaste el producto te puedes ir")
else:
    print('Termina de pagar o elegir otro libro, gracias')