# Generador de Progresiones Armónicas MIDI

#### Video Demo: [URL del video aquí]

---

#### Descripción:

El **Generador de Progresiones Armónicas MIDI** es una herramienta diseñada para músicos, compositores y entusiastas de la música que buscan crear progresiones armónicas de manera rápida y eficiente. Este proyecto permite generar progresiones basadas en las escalas mayores o menores, siguiendo una estructura comúnmente utilizada en la música occidental.

### Funcionalidad Principal:

El programa genera progresiones armónicas en formato MIDI con la siguiente estructura clásica:
- **Tónica (I)**: El punto de inicio, representando la estabilidad tonal.
- **Subdominante (IV)**: Aporta movimiento hacia la tensión.
- **Dominante (V)**: Crea tensión que busca resolución.
- **Tónica (I)**: Retorno a la estabilidad inicial.

Adicionalmente, soporta escalas mayores y menores, asegurando flexibilidad para adaptarse a distintos estilos y tonalidades musicales.

### Características:

1. **Generación de Progresiones**:
   - El usuario puede seleccionar la tonalidad base y el modo (mayor o menor).
   - Se genera automáticamente una progresión clásica I-IV-V-I.

2. **Exportación a MIDI**:
   - La progresión generada se guarda en un archivo `.mid` que puede ser utilizado en software de producción musical.

3. **Reproducción Integrada**:
   - El programa incluye una función para reproducir la progresión directamente desde la terminal.

4. **Ampliable**:
   - Código modular que permite futuras expansiones, como añadir nuevos tipos de progresiones o modos musicales.

### Tecnologías Utilizadas:

- **Python**: Lenguaje principal del proyecto.
- **mido**: Para la creación y manipulación de archivos MIDI.
- **pygame**: Para la reproducción de archivos de audio MIDI.
- **pytest**: Para pruebas unitarias y garantizar la calidad del código.

### Instalación y Uso:

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/FacuNan/project.git
   cd proyecto
   ```

2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar el programa:
   ```bash
   python project.py
   ```

4. Para pruebas unitarias:
   ```bash
   pytest
   ```

### Ejemplo de Uso:

- **Generación de Progresión en A Mayor**:
   ```
   Se ingresó la progresión: ['A-I', 'A-IV', 'A-V', 'A-I']
   La progresión se guardó en progresion.mid
   ¿Desea reproducir la progresión? (s/n): s
   Reproduciendo progresion.mid...
   ```

### Próximos Pasos:

- Añadir soporte para progresiones personalizadas introducidas por el usuario.
- Implementar más modos y escalas (e.g., modos griegos).
- Mejorar la interfaz gráfica para usuarios sin experiencia en programación.

### Créditos:

- **Nombre del Autor:** Facundo Comercio
- **GitHub:** FacuNan
- **Ciudad y País:** La Plat, Buenos Aires, Argentina
- **Fecha de Creación:** 20/12/2024

¡Gracias por explorar este proyecto! Si tienes comentarios o sugerencias, no dudes en contactarme.







