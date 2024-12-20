from mido import Message, MidiFile, MidiTrack
import pygame


#En base a un tono y tipo de escala, genera un 
# acorde con su progresion
def generador_progresion(tonalidad, modo="mayor"):
   
    grados_mayores = {
        "I": 0,  # Tónica
        "IV": 5,  # Subdominante
        "V": 7   # Dominante
    }

    grados_menores = {
        "i": 0,  # Tónica
        "iv": 5,  # Subdominante
        "v": 7   # Dominante (puede ser mayor en menor armónica)
    }

    # Seleccionamos los grados según el modo
    grados = grados_mayores if modo.lower() == "mayor" else grados_menores

    # Mapeo de notas para cada tono
    notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    # Encuentra el índice de la tonalidad
    indice_tonica = notas.index(tonalidad.upper())

    # Genera los acordes en la progresión
    progresion = [
        notas[(indice_tonica + grados[grado]) % 12] + f"-{grado}"
        for grado in grados
    ]

    # Añade la tónica al final para cerrar la progresión
    progresion.append(progresion[0])

    return progresion



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


    #Recorre la progresion y la guarda en el archivo
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


def main():

    tono= input("Ingrese la tonalidad,  (Por Ejemplo: C, D, A): ").upper()
    escala = input("Ingrese si el tipo de escala es mayor o menor: ").lower()


    progresion = generador_progresion(tono, escala)

    print(f"Se ingreso la progresión: {progresion}")

    file = "progresion.mid"
    grabar_progresion_MIDI(progresion, file)

    opcion_reproducir = input("¿Desea reproducir la progresión? (s/n): ")
    if opcion_reproducir == "s":
        file = "progresion.mid"
        reproductor(file)

   

if __name__ == "__main__":
    main()




















