import tkinter as tk
from tkinter import ttk
import cv2 
from PIL import Image, ImageTk
import os
import numpy as np
import filtros  

class Imageapp:
    def __init__(self, window, image_path):
        self.window = window
        self.window.title("Webcam App")

        self.current_image_path = image_path

        self.current_image = None
        self.current_filter = 'Padrão'  # Define o filtro padrão inicial
        self.current_sticker = None

        self.canvas = tk.Canvas(window, width=1200, height=768)
        self.canvas.pack()

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
        
        self.valor_selecionado = tk.StringVar(window)
        self.valor_selecionado.set(opcoes[0])
        
        self.filter_button = tk.OptionMenu(window, self.valor_selecionado, *opcoes, command=self.change_filter)
        self.filter_button.pack()

        self.update_image()

    def update_image(self):

        frame = cv2.imread(self.current_image_path)
        
        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            filter_function = self.filtros_disponiveis.get(self.current_filter)
            if filter_function:
                frame = filter_function(frame)

            self.current_image = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=self.current_image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
    def download_image(self):
        if self.current_image is not None:
            file_path = os.path.expanduser("~/Downloads/captured_image.jpg")
            self.current_image.save(file_path)
            os.startfile(file_path)

    def change_filter(self, selected_filter):
        self.current_filter = selected_filter
        self.update_image()