import pytest
from project import generador_progresion, grabar_progresion_MIDI, convertir_audio

def test_generador_progresion():
    progresion = generador_progresion("A", "mayor")
    assert len(progresion) == 4
    assert all(acorde.startswith("A-") for acorde in progresion)

def test_grabar_progresion_MIDI(tmp_path):
    progresion = ["C-I", "C-IV", "C-V", "C-vi"]
    file = tmp_path / "test_progresion.mid"
    grabar_progresion_MIDI(progresion, str(file))

    assert file.exists()
    assert file.stat().st_size > 0

def test_convertir_audio(tmp_path):
    # Crear un archivo MIDI de prueba
    progresion = ["C-I", "C-IV", "C-V", "C-vi"]
    midi_file = tmp_path / "test_progresion.mid"
    grabar_progresion_MIDI(progresion, str(midi_file))

    # Convertir el archivo MIDI a mp3
    wav_file = convertir_audio(str(midi_file), "mp3")
    assert wav_file.exists()
    assert wav_file.suffix == ".mp3"
    assert wav_file.stat().st_size > 0
