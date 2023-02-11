from datetime import datetime as dt

# %A Día de la semana en inglés
# %B El mes en inglés
# %d El día del mes
# %m El mes
# %Y El año
# %H Hora en formato 24 horas
# %I Hora en formato 12 horas
# %p AM o PM en formato de 12 horas
# %M Minutos
# %S Segundos

def sayDate():
    fecha = dt.now().strftime("%d/%m/%Y")
    mensaje = "Hoy estamos " + fecha
    print(mensaje)
    return mensaje

def sayHour():
    hora = dt.now().strftime("%I:%M %p")
    mensaje = "La hora es " +  hora
    print(mensaje)
    return mensaje
