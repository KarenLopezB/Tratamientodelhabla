import wave
import numpy as np 
import matplotlib.pyplot as plt

#Cargar archivo wav en la variable

goodmorning = wave.open('good-morningMan.wav', 'r')
goodafternoon = wave.open('good-afternoon.wav', 'r')

#Obtener todos los frames del objeto wave
frames = goodmorning.readframes(-1)
frames_after = goodafternoon.readframes(-1)

#Mostrar el resultado de frames
#print(frames[:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer (frames, dtype='int16')
ondaconvertida_after = np.frombuffer (frames_after, dtype='int16')
#print (ondaconvertida [:10])

#morning
framerate_gm = goodmorning.getframerate()

print(framerate_gm)

time_gm = np.linspace(start=0, stop=len(ondaconvertida) /framerate_gm, num=len(ondaconvertida))

print(time_gm[:10])

#afternoon
framerate_ga = goodafternoon.getframerate()

print(framerate_ga)

time_ga = np.linspace(start=0, stop=len(ondaconvertida_after) /framerate_ga, num=len(ondaconvertida_after))

print(time_ga[:10])

#Generación de la gráfica
plt.title('Good morning vs Good afternoon')

#Etiquetas de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#Agregar información de las ondas para graficar
plt.plot(time_ga, ondaconvertida_after, label='Good Afternoon')
plt.plot(time_gm, ondaconvertida, label='Good Morning', alpha=0.5)

plt.legend()
plt.show()