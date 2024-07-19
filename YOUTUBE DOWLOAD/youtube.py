import yt_dlp as youtube_dl
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

    ydl_opts = {
        'outtmpl': caminho_salvo + '/%(title)s.%(ext)s',
        'noplaylist': True  # Adicionando esta linha para evitar o download de playlists
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
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
janela.configure(bg='black')  # Fundo preto para a janela

# Configuração de estilo
font_style = ("Helvetica Neue", 12)
button_style = {"font": ("Helvetica Neue", 14), "bg": "#FFD700", "fg": "black", "bd": 0, "activebackground": "#FFA500"}

# Widgets da interface
url_label = tk.Label(janela, text="URL do Vídeo:", bg='black', fg='white', font=font_style)  # Texto em amarelo sobre fundo preto
url_label.pack(pady=(20, 5))

url_entry = tk.Entry(janela, width=50, font=font_style, bd=1, relief="solid")
url_entry.pack(pady=5)

download_button = tk.Button(janela, text="Baixar Vídeo", command=download_video, **button_style)
download_button.pack(pady=20)

pasta_label = tk.Label(janela, text="Selecione a pasta de destino.", bg='black', fg='white', font=font_style)  # Texto em amarelo sobre fundo preto
pasta_label.pack(pady=5)

# Iniciar o loop da interface
janela.mainloop()
