import random
from mido import Message, MidiFile, MidiTrack
import pygame
from pydub import AudioSegment
import os


# Genera una progresión de acordes en base a un tono y tipo de escala
def generador_progresion(key: str, tipo_escala: str):
    grado_mayor = ["I", "ii", "iii", "IV", "V", "vi", "vii"]
    grado_menor = ["i", "II", "III", "iv", "v", "VI", "VII"]
    acordes = grado_mayor if tipo_escala == "mayor" else grado_menor
    progresion = random.sample(acordes, 4)
    return [f"{key}-{acorde}" for acorde in progresion]


# Guarda la progresión en un archivo MIDI
def grabar_progresion_MIDI(progresion, file_name="progresion.mid"):
    midi = MidiFile()
    pista = MidiTrack()
    midi.tracks.append(pista)
    note_mapping = {'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71}

    for acorde in progresion:
        tono = acorde.split("-")[0]
        nota = note_mapping.get(tono.upper(), 60)  # Busca la nota
        pista.append(Message("note_on", note=nota, velocity=64, time=0))
        pista.append(Message("note_off", note=nota, velocity=64, time=480))

    midi.save(file_name)
    print(f"La progresión se guardó en {file_name}")


# Reproduce un archivo MIDI
def reproductor(file_name):
    pygame.mixer.init()  # Inicia el mezclador de audio
    try:
        print(f"Reproduciendo {file_name}")
        pygame.mixer.music.load(file_name)  # Carga el archivo
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    except pygame.error as e:
        print(f"Error al reproducir el archivo: {e}")

    print(f"La reproducción de {file_name} ha finalizado")


# Convierte el archivo MIDI a otro formato de audio (WAV o MP3)
def convertir_a_formato(origen, formato_destino="wav"):
    try:
        print(f"Convirtiendo {origen} a formato {formato_destino}...")
        audio = AudioSegment.from_file(origen, format="midi")
        nuevo_archivo = os.path.splitext(origen)[0] + f".{formato_destino}"
        audio.export(nuevo_archivo, format=formato_destino)
        print(f"Archivo convertido exitosamente a {nuevo_archivo}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")


# Flujo principal
def main():
    tono = input("Ingrese la tonalidad, (Por Ejemplo: C, D, A): ")
    escala = input("Ingrese si el tipo de escala es mayor o menor: ")
    progresion = generador_progresion(tono, escala)
    print(f"Se ingresó la progresión: {progresion}")
    file = "progresion.mid"
    grabar_progresion_MIDI(progresion, file)

    opcion_reproducir = input("¿Desea reproducir la progresión? (s/n): ")
    if opcion_reproducir.lower() == "s":
        reproductor(file)

    opcion_convertir = input("¿Desea convertir la progresión a otro formato? (s/n): ")
    if opcion_convertir.lower() == "s":
        formato = input("Ingrese el formato de destino (wav, mp3): ").strip().lower()
        convertir_a_formato(file, formato)


if __name__ == "__main__":
    main()
