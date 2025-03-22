def input_movies():
    """Esta función me devuelve una lista con la duración de las películas ingresadas por teclado."""
    input_value = input("Ingresá la duración de una película  (0 para finalizar): ")
    movies_duration = []
    stop = False #booleano q me marca el fin de la carga
    while(not stop):
        if input_value.isnumeric(): #pregunto si el valor ingresado fue un numero
            input_value = int(input_value)
            if(input_value != 0):
                movies_duration.append(input_value)
            else:
                stop = True
                break
        else:
            print("No ha ingreasdo una duracion valida")
        input_value = input("Ingresá la duración de una película  (0 para finalizar): ") #cargo un nuevo valor
    return movies_duration

def average_calculation(movies_duration):
    """Esta funcion calcula el promedio de valores de el contenido de la lista que recibe como parametro."""
    if len(movies_duration)  == 0:
        average = 0
    else:
        average = sum(movies_duration) / len(movies_duration)
    return average

def over_average(movies_duration):
    """ Esta funcion calcula cuantas peliculas superan el promedio de minutos de duracion de la lista."""
    average = average_calculation(movies_duration)
    over = 0 #elementos q superen el promedio
    for elem in  movies_duration:
        if average < elem:
            over +=1
    return over



        


