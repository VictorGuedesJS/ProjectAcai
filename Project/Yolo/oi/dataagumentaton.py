import os
import cv2
import albumentations as A

# Caminho para o diretório onde suas imagens e anotações estão atualmente
input_images_dir = "C:/Users/VICTOR HUGO/PycharmProjects/TesteTCC/dataset/acai/"
output_images_dir = "C:/Users/VICTOR HUGO/PycharmProjects/TesteTCC/dataset/augmented_dataset/"
output_labels_dir = "C:/Users/VICTOR HUGO/PycharmProjects/TesteTCC/dataset/anot/"

# Cria diretórios de saída, se ainda não existirem
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

# Defina quantas cópias aumentadas deseja gerar por imagem
num_augmented = 6

# Carrega as imagens
image_files = [f for f in os.listdir(input_images_dir) if f.endswith('.jpg') or f.endswith('.png')]


# Função para criar uma anotação padrão
def create_annotation(label_path):
    with open(label_path, 'w') as f:
        f.write("0 0.5 0.5 0.5 0.5\n")  # Escreve o padrão fixo


# Função para aplicar augmentações e salvar as novas imagens e anotações
def augment_and_save(image_path, image_name, augmenter, num_copies):
    # Carregar a imagem usando OpenCV
    image = cv2.imread(image_path)

    # Aplicar augmentações e salvar novas imagens e anotações
    for i in range(num_copies):
        # Augmentação da imagem
        augmented = augmenter(image=image)
        augmented_image = augmented["image"]

        # Criar novo nome de arquivo
        base_name = os.path.splitext(image_name)[0]
        new_image_name = f"{base_name}_aug_{i + 1}.jpg"
        new_image_path = os.path.join(output_images_dir, new_image_name)

        # Salvar a imagem aumentada
        cv2.imwrite(new_image_path, augmented_image)

        # Criar e salvar a anotação correspondente
        new_label_name = f"{base_name}_aug_{i + 1}.txt"
        new_label_path = os.path.join(output_labels_dir, new_label_name)
        create_annotation(new_label_path)


# Definir a sequência de augmentação usando Albumentations
augmenter = A.Compose([
    A.HorizontalFlip(p=0.5),  # Flip horizontal com 50% de probabilidade
    A.Rotate(limit=25, p=0.5),  # Rotação aleatória entre -25 e 25 graus
    A.RandomBrightnessContrast(p=0.5),  # Ajuste de brilho e contraste aleatórios
    A.GaussianBlur(blur_limit=(3, 7), p=0.3),  # Aplicar desfoque gaussiano
])

# Para cada imagem, gerar as augmentações e criar anotações
for image_file in image_files:
    image_path = os.path.join(input_images_dir, image_file)
    augment_and_save(image_path, image_file, augmenter, num_augmented)

print(f"Data augmentation completa! {num_augmented} novas cópias de cada imagem foram criadas.")