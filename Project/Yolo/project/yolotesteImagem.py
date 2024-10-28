import torch
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Função para carregar o modelo treinado
def load_model(weights_path):
    # Carregar o modelo treinado com os pesos ajustados
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
    return model

# Função para detectar açaí em uma imagem
def detect_acai(image_path, model):
    # Carregar a imagem
    img = cv2.imread(image_path)

    # Realizar a inferência
    results = model(img)

    # Exibir a imagem com as detecções
    results.show()

    # Analisar as detecções
    detections = results.pred[0]  # [xmin, ymin, xmax, ymax, conf, class]

    # Verificar se há algum açaí detectado
    for detection in detections:
        class_id = int(detection[5])  # Classe detectada
        confidence = detection[4]     # Confiança da detecção
        if class_id == 0:  # Se 0 for a classe do açaí no seu dataset
            print(f"Açaí detectado com {confidence:.2f} de confiança!")
            return True

    print("Nenhum açaí detectado.")
    return False

# Função para abrir o diálogo de seleção de imagem e fazer a detecção
def open_image(model):
    # Abrir um diálogo para selecionar a imagem
    file_path = filedialog.askopenfilename()

    if file_path:
        # Detectar se há açaí na imagem
        is_acai = detect_acai(file_path, model)
        result_text.set(f"Açaí detectado" if is_acai else "Nenhum açaí detectado")

# Configuração básica da interface gráfica com Tkinter
def create_gui(model):
    # Criar janela principal
    root = tk.Tk()
    root.title("Detecção de Açaí")

    # Texto de resultado
    global result_text
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text)
    result_label.pack()

    # Botão para abrir imagem
    open_button = tk.Button(root, text="Abrir Imagem", command=lambda: open_image(model))
    open_button.pack()

    # Iniciar o loop da interface gráfica
    root.mainloop()

# Caminho dos pesos treinados
weights_path = 'C:/Users/VICTOR HUGO/PycharmProjects/Yolo/yolov5/runs/train/exp5/weights/best.pt'

# Carregar o modelo
model = load_model(weights_path)

# Criar a interface gráfica
create_gui(model)
