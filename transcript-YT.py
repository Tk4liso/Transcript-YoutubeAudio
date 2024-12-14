# Campaña de Gears: https://www.youtube.com/watch?v=smZ3vKiYZBE


import yt_dlp
from moviepy.editor import AudioFileClip
import whisper
import os

#Descargar el audio del video de YouTube 
def descargar_audio_youtube(url, output_path="audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_video.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Descarga el audio
    os.rename("temp_video.mp3", output_path)
    return output_path

#Transcribir el audio
def transcribir_audio(audio_path, output_file="transcripcion.txt"):
    model = whisper.load_model("base")  #Aquí cambiar el modelo por si falla
    result = model.transcribe(audio_path)
    
    #Guardar transcripción en un archivo de texto
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result["text"])
    return output_file

#Ingresar el URL del video
url = input("Ingresa el URL del video de YouTube: ")

#Descargar y transcribir
audio_path = descargar_audio_youtube(url)
archivo_transcripcion = transcribir_audio(audio_path)

#Informar al usuario y limpiar archivos temporales
print(f"\nLa transcripción se ha guardado en: {archivo_transcripcion}")
os.remove(audio_path)
