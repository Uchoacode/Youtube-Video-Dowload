from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return

    caminho_salvo = filedialog.askdirectory()
    if not caminho_salvo:
        messagebox.showerror("Erro", "Por favor, selecione uma pasta para salvar o vídeo.")
        return

    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        resolucao_maxima = streams.get_highest_resolution()
        resolucao_maxima.download(output_path=caminho_salvo)
        messagebox.showinfo("Sucesso", "Vídeo salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar o vídeo: {e}")

def abrir_file_dialog():
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_label.config(text=f'Selecionado: {pasta}')
    return pasta

# Configuração da janela principal
janela = tk.Tk()
janela.title("Downloader de Vídeos do YouTube")
janela.geometry("500x300")
janela.configure(bg='white')

# Configuração de estilo
font_style = ("Helvetica Neue", 12)
button_style = {"font": ("Helvetica Neue", 14), "bg": "#007AFF", "fg": "white", "bd": 0, "activebackground": "#005BB5"}

# Widgets da interface
url_label = tk.Label(janela, text="URL do Vídeo:", bg='white', font=font_style)
url_label.pack(pady=(20, 5))

url_entry = tk.Entry(janela, width=50, font=font_style, bd=1, relief="solid")
url_entry.pack(pady=5)

download_button = tk.Button(janela, text="Baixar Vídeo", command=download_video, **button_style)
download_button.pack(pady=20)

pasta_label = tk.Label(janela, text="Selecione a pasta de destino.", bg='white', font=font_style)
pasta_label.pack(pady=5)

# Iniciar o loop da interface
janela.mainloop()
