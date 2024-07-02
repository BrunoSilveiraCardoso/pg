import cv2 as cv
import numpy as np

def standard(img):
  return img

def gray_scale(img):
    
    gray_values = np.dot(img[...,:3], [0.33, 0.33, 0.33])
    img[..., :3] = gray_values[..., np.newaxis]
    
    return img

def media_pond(img):
    weighted_mean = np.dot(img[...,:3], [0.07, 0.71, 0.21])
    
    img[..., :3] = weighted_mean[..., np.newaxis]
    
    return img

def colorizacao(imagem, cor = [255, 0, 100]):
    imagem[..., 0] |= cor[0]  # Canal Azul
    imagem[..., 1] |= cor[1]  # Canal Verde
    imagem[..., 2] |= cor[2]  # Canal Vermelho
    
    return imagem

def negativo(imagem):
  return 255 - imagem

def binarizacao(imagem, k=100):

    media_pond = np.dot(imagem[...,:3], [0.07, 0.71, 0.21])
    
    imagem[media_pond < k] = 0
    imagem[media_pond >= k] = 255
    
    return imagem

def cartoonize(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    edges = cv.Laplacian(gray, cv.CV_8U, ksize=5)
    ret, edges = cv.threshold(edges, 150, 255, cv.THRESH_BINARY_INV)
    color = cv.bilateralFilter(image, 9, 250, 250)
    cartoon = cv.bitwise_and(color, color, mask=edges)
    return cartoon

def edge_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 100, 200)
    return edges

def laplacian(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    laplacian = cv.Laplacian(gray, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    return laplacian

def sobel(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=5)
    sobelx = np.uint8(np.absolute(sobelx))
    sobely = np.uint8(np.absolute(sobely))
    sobel_combined = cv.bitwise_or(sobelx, sobely)
    return sobel_combined

def blur(image):
    blurred_image = cv.blur(image, (10, 8))
    return blurred_image