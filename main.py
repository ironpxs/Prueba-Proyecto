from ppt import juego_ppt
from calculadora import calculadora
from tiempo import sayDate, sayHour
from reproducir import playPhrase, playSong
from escuchame import filtrarPalabrasClave, escuchar
from crear_audios import *

playPhrase("mensaje_inicial")

print(mensaje_inicial)
nom_usuario = escuchar()


mensaje_bienvenida = "Bienvenido, " + nom_usuario
print(mensaje_bienvenida)
switchTextToVoice("mensaje_bienvenida",mensaje_bienvenida)
playPhrase("mensaje_bienvenida")


mensaje_comando = nom_usuario + ">"

print(mensaje_comando)
comando = escuchar().lower()
while True:
        
    if filtrarPalabrasClave(comando,["fecha","date","dia","día"]):
        mensaje_fecha = sayDate()
        switchTextToVoice("mensaje_fecha",mensaje_fecha)
        playPhrase("mensaje_fecha")

    elif filtrarPalabrasClave(comando,["hora","tiempo"]):
        mensaje_hora = sayHour()
        switchTextToVoice("mensaje_hora",mensaje_hora)
        playPhrase("mensaje_hora")
        
    elif filtrarPalabrasClave(comando,["juego","jugar","piedra","papel", "tijera", "ppt"]):
        juego_ppt()

    elif filtrarPalabrasClave(comando,["calculadora", "calcular", "sumar","suma","div","multi","resta"]):
        menu = '''
        Menú de operaciones
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        '''
        print(menu)

        playPhrase("mensaje_operacion")
        operacion = int(input(mensaje_operacion))
    
        playPhrase("mensaje_primer")
        primer_num = int(input(mensaje_primer))

        playPhrase("mensaje_segundo")
        segundo_num = int(input(mensaje_segundo))

        if operacion == 1:
            nom_operacion = "suma"
        elif operacion == 2:
            nom_operacion = "resta"
        elif operacion == 3:
            nom_operacion = "multiplicacion"
        elif operacion == 4:
            nom_operacion = "division"
            
        resultado = calculadora(nom_operacion,primer_num,segundo_num)

        mensaje_resultado = "La " + nom_operacion + " entre " + str(primer_num) + " y " + str(segundo_num) + " es " + str(resultado)
        print(mensaje_resultado)
        switchTextToVoice("mensaje_resultado",mensaje_resultado)
        playPhrase("mensaje_resultado")


    elif filtrarPalabrasClave(comando,["cancion","musica", "música","canción"]):
        print(mensaje_fav)
        playPhrase("mensaje_fav")
        playSong("nothing")
    
    elif filtrarPalabrasClave(comando,["termina","terminar", "salir","cerrar","cierra","chao"]):
        break
    else:
        print(mensaje_noentiendo)
        playPhrase("mensaje_noentiendo")
    
    mensaje_comando = nom_usuario + ">"

    print(mensaje_comando)
    comando = escuchar().lower()
    

print("Chao")

