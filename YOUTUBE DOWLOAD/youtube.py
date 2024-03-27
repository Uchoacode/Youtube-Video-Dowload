from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def dowload_video(url, caminho_salvo):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        resolucao_maxima = streams.get_highest_resolution()
        resolucao_maxima.download(output_path=caminho_salvo)
        print('Video Salvo!')
    except Exception as e:
        print(e)


def abrir_file_dialog():
    pasta = filedialog.askdirectory()
    if pasta:
        print(f'Selecione a Pasta: {pasta}')

    return pasta


if __name__ == "__main__":

    janela = tk.Tk()
    janela.withdraw()

    video_url = input('Coloque o Link do Vídeo: ')
    salve_dir = abrir_file_dialog()

    if salve_dir:
        print('Dowload Começou...')
        dowload_video(video_url, salve_dir)
    else:
        print('Localização Invalida!')
