#invertir el contenido de una cadena
def creartxt():
    archivo=open('2.txt','w')
    archivo.close
def grabartxt(palabra):
    archivo=open('2.xtx','a')
    archivo.write(palabra)
    archivo.close
def invertir(cadena):
    a=len(cadena)
    cambia=cadena
    for p in cadena:
        print (p)
        cambia.replace(cambia[a],p)
        a=a-1
    print(cambia)
invertir("HOLA")

