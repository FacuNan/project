# Generador de Progresiones Musicales en Python

#### Video Demo: https://youtu.be/tu-video-aqui

#### Descripción:
El **Generador de Progresiones Musicales en Python** es una herramienta que permite a los usuarios crear progresiones de acordes aleatorias en formato MIDI, basadas en una tonalidad y tipo de escala especificados. Además, permite guardar las progresiones generadas y reproducirlas directamente desde la aplicación.

El proyecto utiliza bibliotecas como `pygame` y `mido` para gestionar la creación y reproducción de archivos MIDI, lo que lo hace ideal para músicos, compositores, o cualquier persona interesada en explorar progresiones musicales.

#### Características:
- Generación aleatoria de progresiones musicales según la tonalidad y escala seleccionadas.
- Guardado automático de las progresiones en formato MIDI.
- Reproducción directa de los archivos MIDI generados.
- Código modular y bien estructurado, facilitando la ampliación o personalización del programa.

#### Tecnologías:
- **Python**: Lenguaje principal del proyecto.
- **Bibliotecas**:
  - `pygame`: Para la reproducción de archivos MIDI.
  - `mido`: Para la creación y manejo de archivos MIDI.

#### Uso:
1. **Clonar el repositorio**:

[Repositorio Github:] (https://github.com/FacuNan/project.git)

2. **Instalar las dependencias**:
Asegúrate de tener Python instalado. Luego, instala las bibliotecas necesarias con:

pip install -r requirements.txt

[Ver dependencias:] (docs/requirements.txt)

3. **Ejecutar el programa**:
Ejecuta el archivo principal del proyecto:

python project.py

4. **Instrucciones en pantalla**:
El programa te guiará paso a paso para seleccionar una tonalidad, tipo de escala, y generar la progresión musical.

#### Notas:
- Este proyecto no incluye la funcionalidad de conversión de MIDI a otros formatos de audio (como WAV o MP3) debido a problemas técnicos encontrados durante el desarrollo.
- Asegúrate de tener configurado un sintetizador MIDI en tu sistema operativo para una correcta reproducción de los archivos.

#### Estructura del proyecto:
- **`project.py`**: Archivo principal del programa.
- **`requirements.txt`**: Lista de dependencias del proyecto.
- **`test_project.py`**: Archivo de pruebas automatizadas usando `pytest`.

#### Próximos pasos:
- Agregar soporte para conversión de archivos MIDI a otros formatos de audio.
- Ampliar las opciones de generación de progresiones con más tipos de escalas y acordes.




