#codificacion

def creartxt():
    archivo=open('3.txt','w')
    archivo.close
def grabartxt(palabra):
    archivo=open('3.xtx','a')
    archivo.write(palabra)
    archivo.write("\n")
    archivo.close
    
list={'T':0,'R':1,'W':2,'A':3,'G':4,'M':5,'Y':6,'F':7,'P':8,'D':9,'X':10,'B':11,'N':12,'J':13,'Z':14,'S':15,'Q':16,'V':17,'H':18,'L':19,'C':20,'K':21,'E':22}
palabra='TEROOMENJA'
print (palabra)
creartxt()

letras=sorted(list.keys())
a=len(letras)
for p in palabra:
    print (p)
    if(p in letras):
        palabra.replace(p,(list[p]))
print(palabra)        

