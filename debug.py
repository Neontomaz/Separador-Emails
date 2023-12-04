import os
import shutil
import pathlib
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk



#    nf = tuple(map(str, nfs.split(',')))
def start():
    if input_notas.get() == "" or input_origem.get() == "" or input_destino.get() == "" :
        messagebox.showinfo(title="ERROR", message="CAMPOS EM BRANCO")
    else:
        notas = input_notas.get()
        origem = input_origem.get()
        destino = input_destino.get()
        
        nf = tuple(map(str, notas.split(',')))
        
        
        for arquivo in os.listdir(origem):
        
            for padrao in nf:
                if padrao in arquivo:
                    
                    # Cria um diretório com o nome do arquivo
                    if pathlib.Path(f"{destino}/{padrao}").exists():
                        shutil.copy2(os.path.join(origem, arquivo), pathlib.Path(f"{destino}/{padrao}"))
                    else:    
                        diretorio_novo = pathlib.Path(f"{destino}/{padrao}")
                        diretorio_novo.mkdir()
                    # Copia o arquivo para dentro do diretório
                        shutil.copy2(os.path.join(origem, arquivo), diretorio_novo)
            
            

origem = 'C:/Users/carlos.mendes/Desktop/NOTAS 03'
destino = 'C:/Users/carlos.mendes/Desktop/saida'


i = 0


app = ctk.CTk()
app.geometry("740x370")
app._set_appearance_mode("Dark")


#Label Contador
lb_contador  = ctk.CTkLabel(master=app, text=f"Encontrados: {i}", text_color="White", width=80, bg_color='#3c3c3c')
lb_contador.place(x=180, y=40)

# LABELS
lb_origem = ctk.CTkLabel(master=app, text="LOCAL DAS NOTAS:", text_color="White", width=100, bg_color='#3c3c3c')
lb_destino = ctk.CTkLabel(master=app, text="LOCAL DESTINO:", text_color="White", width=100, bg_color='#3c3c3c')
lb_notas  = ctk.CTkLabel(master=app, text="NOTAS:", text_color="White", width=80, bg_color='#3c3c3c')



lb_origem.place(x=20, y=40)
lb_destino.place(x=20, y=100)
lb_notas.place(x=20, y=170)

# INPUTS
input_origem = ctk.CTkEntry(master=app, corner_radius=8, bg_color='#3c3c3c') 
input_destino = ctk.CTkEntry(master=app, corner_radius=8, bg_color='#3c3c3c')
input_notas = ctk.CTkEntry(master=app, corner_radius=8, bg_color='#3c3c3c')

input_origem.place(x=20, y=60)
input_destino.place(x=20, y=120)
input_notas.place(x=20, y=190)
# BUTTONS
btn_start = ctk.CTkButton(master=app, text="Organizar", font=('Times bold' ,14), command=start, corner_radius=8, bg_color='#3c3c3c')
btn_quit = ctk.CTkButton(master=app, text="Fechar", font=('Times bold' ,14), command=app.destroy, corner_radius=8, bg_color='#3c3c3c')


btn_start.place(x=20, y=250)
btn_quit.place(x=20, y=290)
app.mainloop()
"""
for arquivos in os.listdir(origem):
    if '88129_1' in arquivos:
        if (pathlib.Path(f'C:/Users/carlos.mendes/Desktop/saida/{arquivos}')).exists():
            print('Ja existe o diretorio iremos apenas copiar o arquivo')
            shutil.copy2(os.path.join(origem, arquivos), pathlib.Path(f'C:/Users/carlos.mendes/Desktop/saida/{arquivos}'))
        else:
            diretorio_novo = pathlib.Path(f'C:/Users/carlos.mendes/Desktop/saida/{arquivos}')
            diretorio_novo.mkdir()
            # Copia o arquivo para dentro do diretório
            shutil.copy2(os.path.join(origem, arquivos), diretorio_novo)
        i += 1 
        
print(i)
"""