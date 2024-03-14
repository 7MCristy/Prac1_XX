#lectura del fichero client.cfg
'''
with open ('client.cfg', 'r') as cl_file:
    lines = cl_file.read().splitlines()
    lines_treatment(lines)
'''
#este codigo de arriba lee por línias eol fichero y las guarda en una lista

#Yo quiero un duccionario, pero probemos con la lsita
#podemos utilizar **kwargs (key arguments)que espera un diccionario (valor, resultado) para un número indefinido de elementos
#definiremos la función lectura de las línias
with open ('client.cfg', 'r') as cl_file:
    lines = cl_file.read()
    lines_treatment(lines)


def lines_treatment(**kwargs){
print(kwargs)
for key in kwargs
    print(key,':' , kwrgs[key] )
}
