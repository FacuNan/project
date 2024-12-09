import pytest
from project import generador_progresion, grabar_progresion_MIDI, reproductor

def test_generador_progresion():

    progresion = generador_progresion("A","mayor")
    assert len(progresion) == 4
    assert all(acorde.startswith("A-") for acorde in progresion)



def test_grabar_progresion_MIDI(tmp_path):
    progresion =["C-I", "IV", "V", "iv"]
    file = tmp_path / "test_progresion_mid"
    grabar_progresion_MIDI(progresion, str(file))

    assert file.exists()
    assert file.stat().st_size > 0


