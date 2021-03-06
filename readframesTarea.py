import wave
import numpy as np 
import matplotlib.pyplot as plt

#Cargar archivo wav en la variable

netflixintro = wave.open('netflix-intro.wav', 'r')
boogatito = wave.open('boo-gatito.wav', 'r')

#Obtener todos los frames del objeto wave
frames_net = netflixintro.readframes(-1)
frames_boo = boogatito.readframes(-1)


#Convierte el audio de bytes a enteros
ondaconvertida_net = np.frombuffer (frames_net, dtype='int16')
ondaconvertida_boo = np.frombuffer (frames_boo, dtype='int16')

#netflix-intro
framerate_net = netflixintro.getframerate()

print(framerate_net)

time_net = np.linspace(start=0, stop=len(ondaconvertida_net) /framerate_net, num=len(ondaconvertida_net))

print(time_net[:10])

#boo-gatito
framerate_boo = boogatito.getframerate()

print(framerate_boo)

time_boo = np.linspace(start=0, stop=len(ondaconvertida_boo) /framerate_boo, num=len(ondaconvertida_boo))

print(time_boo[:10])

#Generación de la gráfica
plt.title('Netflix intro vs Boo gatito')

#Etiquetas de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#Agregar información de las ondas para graficar
plt.plot(time_net, ondaconvertida_net, label='Netflix intro')
plt.plot(time_boo, ondaconvertida_boo, label='Boo gatito', alpha=0.5)

plt.legend()
plt.show()