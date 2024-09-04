import os
import shutil
from collections import defaultdict

# Caminhos de origem e destino
src_folder = r"E:\dataset\c2"
dst_folder = r"E:\all images"

# Dicionário para armazenar imagens por indivíduo e amostra
images_dict = defaultdict(list)

# Percorre a pasta de origem
for filename in os.listdir(src_folder):
    if filename.startswith("OE_"):
        parts = filename.split('_')
        individuo = parts[2]
        amostra = parts[3]
        img_num = int(parts[4].split('.')[0])
        
        # Adiciona a imagem à lista correspondente no dicionário
        images_dict[(individuo, amostra)].append((img_num, filename))

# Processa cada amostra de cada indivíduo
for (individuo, amostra), images in images_dict.items():
    # Ordena as imagens pelo número da imagem
    images.sort()
    
    # Determina o índice central
    total_images = len(images)
    central_start = max(0, (total_images - 500) // 2)
    central_images = images[central_start:central_start + 500]
    
    # Move as imagens centrais para a pasta de destino
    for _, filename in central_images:
        src_file = os.path.join(src_folder, filename)
        dst_file = os.path.join(dst_folder, filename)
        shutil.move(src_file, dst_file)

print("Movimentação concluída.")
