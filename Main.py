import tkinter as tk
import WebcamApp
import Imageapp

print('Selecione:')
print('1 - Para abrir a webcam')
print('2 - Para enviar arquivo')
entrada = input()



if entrada == '1':
    root = tk.Tk()
    app = WebcamApp.WebcamApp(root)
    root.mainloop()
elif entrada == '2':
    caminho = input('Digite o caminho:')
    root = tk.Tk()
    app = Imageapp.Imageapp(root, caminho)
    root.mainloop()
else:
    print('Opção inválida. Escolha 1 ou 2.')
