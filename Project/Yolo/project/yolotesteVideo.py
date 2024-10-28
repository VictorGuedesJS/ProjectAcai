import torch
import cv2

# Função para carregar o modelo treinado
def load_model(weights_path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
    return model

# Função para detectar açaí em um frame da webcam com filtro de confiança
def detect_acai_from_frame(frame, model, confidence_threshold=0.75):
    results = model(frame)
    # Filtrar resultados pela confiança
    detections = results.pandas().xyxy[0]  # Pega os resultados no formato pandas
    filtered_detections = detections[detections['confidence'] > confidence_threshold]  # Filtra por confiança

    # Se houver detecções com confiança maior que 75%, renderiza
    if not filtered_detections.empty:
        results.render()  # Renderizar as caixas de detecção no frame
    return results.ims[0]  # Retorna o frame com as detecções

# Função principal para captura da webcam e detecção em tempo real
def run_webcam_detection(model):
    # Usar DirectShow como backend da webcam no Windows
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Erro ao acessar a webcam.")
        return

    while True:
        # Ler o frame atual da webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Realizar a detecção de açaí no frame com confiança mínima de 75%
        detected_frame = detect_acai_from_frame(frame, model, confidence_threshold=0.75)

        # Exibir o frame com as detecções usando OpenCV
        cv2.imshow('Detecção de Açaí em Tempo Real', detected_frame)

        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera os recursos da webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()

# Caminho dos pesos treinados
weights_path = 'C:/Users/VICTOR HUGO/PycharmProjects/Yolo/yolov5/runs/train/exp5/weights/best.pt'

# Carregar o modelo
model = load_model(weights_path)

# Iniciar a detecção em tempo real
run_webcam_detection(model)
