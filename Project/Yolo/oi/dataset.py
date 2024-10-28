import os
import shutil
import random

# Caminho para o diretório onde suas imagens e anotações estão atualmente
input_images_dir = "C:/Users/VICTOR HUGO/PycharmProjects/TesteTCC/dataset/augmented_dataset/"
input_labels_dir = "C:/Users/VICTOR HUGO/PycharmProjects/TesteTCC/dataset/anot/"
output_base_dir = "C:/Users/VICTOR HUGO/PycharmProjects/TesteTCC/dataset/training"

# Percentual de dados para validação (ex: 20% para validação)
val_split = 0.2

# Função para criar diretórios, se não existirem
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Criar a estrutura de pastas
train_images_dir = os.path.join(output_base_dir, "images/train")
val_images_dir = os.path.join(output_base_dir, "images/val")
train_labels_dir = os.path.join(output_base_dir, "labels/train")
val_labels_dir = os.path.join(output_base_dir, "labels/val")

create_dir(train_images_dir)
create_dir(val_images_dir)
create_dir(train_labels_dir)
create_dir(val_labels_dir)

# Obter lista de todas as imagens no diretório de entrada
image_files = [f for f in os.listdir(input_images_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Embaralhar as imagens para dividir aleatoriamente entre treino e validação
random.shuffle(image_files)

# Definir índice de divisão (train/val)
val_size = int(len(image_files) * val_split)

# Separar arquivos de treino e validação
val_files = image_files[:val_size]
train_files = image_files[val_size:]

# Função para mover e renomear arquivos
def move_and_rename(files, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir, prefix):
    for i, file_name in enumerate(files):
        # Caminhos de origem e destino
        base_name = os.path.splitext(file_name)[0]
        image_src = os.path.join(src_img_dir, file_name)
        label_src = os.path.join(src_lbl_dir, base_name + ".txt")

        # Novo nome para os arquivos (ex: image_001.jpg, image_001.txt)
        new_base_name = f"{prefix}_{i+1:04d}"
        image_dest = os.path.join(dest_img_dir, new_base_name + ".jpg")
        label_dest = os.path.join(dest_lbl_dir, new_base_name + ".txt")

        # Mover e renomear a imagem
        shutil.copy(image_src, image_dest)

        # Mover e renomear a anotação se existir
        if os.path.exists(label_src):
            shutil.copy(label_src, label_dest)
        else:
            print(f"Anotação para {file_name} não encontrada.")

# Mover arquivos de treino e validação para suas respectivas pastas
move_and_rename(train_files, input_images_dir, input_labels_dir, train_images_dir, train_labels_dir, "train")
move_and_rename(val_files, input_images_dir, input_labels_dir, val_images_dir, val_labels_dir, "val")

print("Estrutura de pastas criada e arquivos renomeados com sucesso!")
