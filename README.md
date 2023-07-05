# Challenge Inceptia

Cada archivo en este repositorio representa un ejercicio diferente del PDF adjunto.

## Configuración del entorno

1. Crea un entorno virtual para el proyecto:

   python -m venv nombre_entorno_virtual

2. Activa el entorno virtual:

   - En Windows:
     nombre_entorno_virtual\Scripts\activate
     
   - En macOS/Linux:
     source nombre_entorno_virtual/bin/activate

3. Instala las dependencias del proyecto:

   pip install -r requirements.txt

## Ejecución de los ejercicios en el "bot"
El archivo bot.py contiene una simulacion del bot que sigue el flujo marcado en el diagrama. Se aplicaron algunas modificaciones 
1. Navega al directorio del proyecto:

   cd ruta_al_directorio_del_proyecto

2. Ejecuta el archivo del bot

   python bot.py

   > Asegúrate de tener configurado el .env con la variable API_KEY
   > Asegúrate de tener el entorno virtual activado antes de ejecutar el archivo.

3. Completa los datos y/u Observa los resultados de salida para verificar si se cumple la tarea del ejercicio.


## Ejecución de los ejercicios por separado

Cada archivo en este repositorio representa un ejercicio diferente. Para probar cada ejercicio, sigue los siguientes pasos:

1. Navega al directorio del proyecto:

   cd ruta_al_directorio_del_proyecto


2. Ejecuta el archivo de ejercicio deseado:

   python nombre_archivo.py

   > descomenta primero las líneas de código que estan debajo de:
    ''' # En caso de que se quiera probar el codigo, descomentar las siguientes lineas '''
   > Asegúrate de tener el entorno virtual activado antes de ejecutar el archivo.
   > En el caso del ej1.py configura el .env con la API_KEY

3. Completa los datos y/u Observa los resultados de salida para verificar si se cumple la tarea del ejercicio.
