import random
from mido import Message, MidiFile, MidiTrack
import pygame
from pydub import AudioSegment
import os

#En base a un tono y tipo de escala, genera un 
# acorde con su progresion
def generador_progresion(key: str, tipo_escala:str):

    #Lista de grados de escala mayores y menores

    grado_mayor = ["I", "ii", "iii", "IV", "V", "vi", "vii"]
    grado_menor = ["i", "II", "III", "iv", "v", "VI", "VII"]

    #Si el acorde es mayo devuelve la lista de escala mayor, 
    # de lo contrario la lista de grados de escala menor
    acordes = grado_mayor if tipo_escala == "mayor" else grado_menor

    #Selecciona 4 acordes random de la escala seleccionada
    progresion = random.sample(acordes, 4)

    #Retorna una lista de acordes y sus progresiones
    return [f"{key}-{acorde}" for acorde in progresion]



#Guarda la progresión en un archivo de tipo MIDI, 
# para reproducir posteriormente
def grabar_progresion_MIDI(progresion, file_name = "progresion.mid"):
    
    midi = MidiFile() #Creamo archivo Midi
    pista = MidiTrack() #Se crea pista vacia

    midi.tracks.append(pista) #Se agrega la pista al archivo

    #Diccionario que contiene el tono y su valor digitalizado
    note_mapping = {
        'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71
    }


    #Recorre la progrsion y la guarda en el archivo
    for acorde in progresion:

        tono = acorde.split("-")[0]

        nota = note_mapping.get(tono.upper(), 60) #Busca la nota

        pista.append(Message("note_on", note=nota, velocity=64, time=0))
        pista.append(Message("note_off", note=nota, velocity=64, time=480))

        midi.save(file_name)
        print(f"La progresión se guardo en {file_name}")


#Función para reproducir el archivo
def reproductor(file_name):
    pygame.mixer.init() #Inicia el mezclador de audio
    try:
        print(f"Reproduciendo  {file_name}")
        pygame.mixer.music.load(file_name) #carga el archivo
        pygame.mixer.music.play()

        while pygame.mixer.get_busy():
            pass
    except pygame.error as e:
        
        print(f"Error al reproducir el archivo: {e}")



    print(f"La reproducción de {file_name} ha finalizado")




def convertir_audio(origen, nuevo_formato="wav"):
    try:
        #Se carga el archivo para realizar el cambio del formato
        audio = AudioSegment.from_file(origen, format ="midi")
        #Fragmenta el archvo y cambia la extensión
        nuevo_audio = os.path.splitext(origen[0] + f"{nuevo_formato}")

        audio.export(nuevo_audio, format= nuevo_formato)
        return nuevo_audio
    except Exception as e:
        print(f"No se pudo convertir el archivo, {e}")





def main():

    tono= input("Ingrese la tonalidad,  (Por Ejemplo: C, D, A): ")
    escala = input("Ingrese si el tipo de escala es mayor o menor: ")


    progresion = generador_progresion(tono, escala)

    print(f"Se ingreso la progresión: {progresion}")

    file = "progresion.mid"
    grabar_progresion_MIDI(progresion, file)

    opcion_reproducir = input("¿Desea reproducir la progresión? (s/n): ")
    if opcion_reproducir == "s":
        file = "progresion.mid"
        reproductor(file)

    opcion_convertir = input("¿Deseas cambiar el formato? (s/n): ").lower()

    if opcion_convertir == "s":
        formato = input("Ingrese el tipo de formato: ").strip().lower()
        convertir_audio(file, formato)



if __name__ == "__main__":
    main()




















