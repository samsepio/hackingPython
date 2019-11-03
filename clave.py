import time

clave=input("dime una clave: ");
diccionario="abcdefghijklmnñopqrstuvwxyz123456789"
inicio=time.time();
for c1 in diccionario:
    for c2 in diccionario:
        for c3 in diccionario:
            for c4 in diccionario:
                intento=c1+c2+c3+c4
                if intento == clave:
                    print("clave encontrada",intento);
final = time.time()
print("tiempo consumido: ",format(final-inicio));
