# Para empaquetar usamos el siguiente comando

# pyinstaller your_program.py --noconsole --noconfirm

# pyinstaller FLET/CursoFletOficial/1.GettingStarted/ContadorAscendente/Contador.py --noconsole --noconfirm

# LA APLICACION ESTARA EN LA CARPETA DIST, esta aplicación tiene muchas carpetas
# y un .exe que es el que se ejecuta para abrir la aplicación


# Para empaquetar un solo archivo .exe, se ejecuta el siguiente comando:
# pyinstaller your_program.py --noconsole --noconfirm --onefile


# Para agregar un icono a la aplicación:
# pyinstaller your_program.py --noconsole --noconfirm --onefile --icon <<your-image.png>>


#Para agregar assets o archivos como imagenes, videos, data
# pyinstaller your_program.py --noconsole --noconfirm --onefile --add-data "assets:assets"

#AppVeyor es una aplicación almacenada en github que permite empaquetar aplicaciones iOS, Windows, Linux desde cualquier SO (Sistema Operativo)
