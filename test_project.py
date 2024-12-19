
from project import generador_progresion, grabar_progresion_MIDI, reproductor
from unittest.mock import patch
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

@patch("pygame.mixer.music")
@patch("pygame.mixer")
def test_reproductor(mock_mixer, mock_music):
    # Configurar el mock
    mock_mixer.init.return_value = None
    mock_music.load.return_value = None
    mock_music.play.return_value = None
    mock_mixer.get_busy.side_effect = [True, False]  # Simula que el audio se está reproduciendo y luego termina

    # Llamar a la función
    reproductor("test_file.mid")

    # Verificar que las funciones correctas fueron llamadas
    mock_mixer.init.assert_called_once()
    mock_music.load.assert_called_once_with("test_file.mid")
    mock_music.play.assert_called_once()
    assert mock_mixer.get_busy.call_count == 2