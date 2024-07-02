import tkinter as tk
from tkinter import ttk
import cv2 
from PIL import Image, ImageTk
import os
import numpy as np
import filtros  

class WebcamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam App")

        self.video_capture = cv2.VideoCapture(0)
        #opções padrão 
        self.current_filter = 'standard'
        self.current_sticker = None

        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()
        
        #botão para salvar imagem
        self.download_button = tk.Button(window, text='Salvar', command=self.download_image)
        self.download_button.pack()
        
        opcoes = ['Padrão', 'Escala de cinza', 'Média Ponderada', 'Colorização', 'Negativo', 'Binarização', 'Cartoonização', 'Detecção de limites', 'Laplace', 'Sobel', 'Blur']
        self.filtros_disponiveis = {
            'Padrão': filtros.standard,
            'Escala de cinza': filtros.gray_scale,
            'Média Ponderada': filtros.media_pond,
            'Colorização': filtros.colorizacao,
            'Negativo': filtros.negativo,
            'Binarização': filtros.binarizacao,
            'Cartoonização': filtros.cartoonize,
            'Detecção de limites': filtros.edge_detection,
            'Laplace': filtros.laplacian,
            'Sobel': filtros.sobel,
            'Blur': filtros.blur
        }
        
        #armazena a opção
        self.valor_selecionado = tk.StringVar(window)
        self.valor_selecionado.set(opcoes[0])
        
        #cria o menu de filtros
        self.filter_button = tk.OptionMenu(window, self.valor_selecionado, *opcoes, command=self.change_filter)
        self.filter_button.pack()

        #trecho descartado
        opcoes_sticker = ['gamado', 'descolado', 'faceiro', 'bolado', 'envergonhado']

        self.valor_selecionado_dois = tk.StringVar(window)
        self.valor_selecionado_dois.set(opcoes_sticker[0])

        self.sticker_button = tk.OptionMenu(window, self.valor_selecionado_dois, *opcoes_sticker, command=self.insert_image)
        self.sticker_button.pack()

        self.update_webcam()
    
    def update_webcam(self):
        ret, frame = self.video_capture.read()

        if ret:
            #conversão para o tk aceitar
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            filter_function = self.filtros_disponiveis.get(self.current_filter)
            if filter_function:
                frame = filter_function(frame)

            self.current_image = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=self.current_image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.window.after(15, self.update_webcam)

    def download_image(self):
        if self.current_image is not None:
            file_path = os.path.expanduser("~/Downloads/captured_image.jpg")
            self.current_image.save(file_path)
            os.startfile(file_path)

    def change_filter(self, selected_filter):
        self.current_filter = selected_filter

    def insert_image(self, selected_sticker):
        self.current_sticker = selected_sticker
