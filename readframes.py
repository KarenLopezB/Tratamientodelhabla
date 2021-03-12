import wave
import numpy as np 

#Cargar archivo wav en la variable

goodmorning = wave.open('good-morningMan.wav', 'r')

#Obtener todos los frames del objeto wave
frames = goodmorning.readframes(-1)

#Mostrar el resultado de frames
print(frames[:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer (frames, dtype='int16')

#Muestra los primeros 10 resultados de int
print (ondaconvertida [:10])