import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Hello World!")
root.geometry("500x300")

# Função para mover o botão "Não" para uma nova posição aleatória na tela
def mover_botao_nao(event):
    novo_x = random.randint(0, root.winfo_width() - botao_nao.winfo_width())
    novo_y = random.randint(0, root.winfo_height() - botao_nao.winfo_height())
    botao_nao.place(x=novo_x, y=novo_y)

# Função para exibir um GIF triste quando o usuário clica em "Não"
def mostrar_gif_triste():
    triste_img = Image.open("sad.gif")
    triste_gif = ImageTk.PhotoImage(triste_img)
    gif_label = tk.Label(root, image=triste_gif)
    gif_label.image = triste_gif
    gif_label.pack()
    root.after(3000, gif_label.destroy)

# Função para exibir um GIF feliz com animação quando todas as perguntas são respondidas com "Sim"
def mostrar_gif_feliz():
   
    def atualizar_frame(ind):
        frame = frames[ind]
        gif_label.configure(image=frame)
        ind += 1
        if ind == num_frames:  
            ind = 0
        root.after(100, atualizar_frame, ind)  

    feliz_img = Image.open("happy.gif")
    frames = []

    for frame in range(0, feliz_img.n_frames):
        feliz_img.seek(frame)
        frame_image = ImageTk.PhotoImage(feliz_img.copy())
        frames.append(frame_image)

    num_frames = len(frames)

    gif_label = tk.Label(root)
    gif_label.pack()

    atualizar_frame(0)

perguntas = ["Você me ama?", "Você quer ficar comigo para sempre?", "Você acha que sou especial?"]
indice_pergunta = 0

# Função para ir para a próxima pergunta quando o usuário clica em "Sim"
def proxima_pergunta():
    global indice_pergunta
    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        pergunta_label.config(text=perguntas[indice_pergunta])
    else:
        mostrar_gif_feliz() 
        botao_sim.config(state="disabled")
        botao_nao.config(state="disabled")

# Criação da interface do Tkinter
pergunta_label = tk.Label(root, text=perguntas[indice_pergunta], font=("Arial", 14))
pergunta_label.pack(pady=20)

botao_sim = tk.Button(root, text="Sim", command=proxima_pergunta)
botao_sim.pack(side="left", padx=50)

botao_nao = tk.Button(root, text="Não", command=mostrar_gif_triste)
botao_nao.pack(side="right", padx=50)
botao_nao.bind("<Enter>", mover_botao_nao)

# Inicia o loop principal do Tkinter
root.mainloop()
