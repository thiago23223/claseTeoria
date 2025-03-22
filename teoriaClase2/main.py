from peliculas import input_movies,average_calculation,over_average
 
duracion_peliculas = input_movies()
print("DURACIONES DE LAS PELICULAS : ",duracion_peliculas)
promedio = average_calculation(duracion_peliculas)
print(" EL PROMEDIO DE LAS DURACIONES INGRESADAS ES DE : ", promedio)
pasan_promedio = over_average(duracion_peliculas)
print(" LA CANTIDAD DE PELICULAS QUE SUPERAN EL PROMEDIO ES DE : ", pasan_promedio)




