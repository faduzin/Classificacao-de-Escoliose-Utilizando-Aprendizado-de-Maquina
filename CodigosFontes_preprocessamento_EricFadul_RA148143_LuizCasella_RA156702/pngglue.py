import os
import cv2
import numpy as np

def load_images_from_folder(folder, individual_id):
    images = []
    # Carrega e ordena as imagens com base no número da imagem no nome do arquivo
    for filename in sorted(os.listdir(folder), key=lambda x: int(x.split('_')[-1].split('.')[0])):
        if filename.startswith(f"CE_individual_{individual_id}_"):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
    return images

def create_larger_image(images, output_folder, output_prefix, group_id):
    rows = []
    for i in range(0, 20, 5):  # Agrupa as imagens em blocos de 5 para formar as linhas
        row = np.hstack(images[i:i+5])
        rows.append(row)
    large_image = np.vstack(rows)  # Une as linhas verticalmente

    output_filename = f"{output_prefix}_group_{group_id}.png"
    cv2.imwrite(os.path.join(output_folder, output_filename), large_image)
    print(f"Salvo: {output_filename}")

def process_images(folder, individual_id, output_folder, output_prefix):
    images = load_images_from_folder(folder, individual_id)
    num_images = len(images)
    group_id = 0

    for i in range(0, num_images, 20):
        if i + 20 <= num_images:
            create_larger_image(images[i:i+20], output_folder, output_prefix, group_id)
            group_id += 1

# Especificar os parâmetros
main_folder_path = r'C:\Users\Cabas\Desktop\trabalho_ia\pasta'
output_folder = r'C:\Users\Cabas\Desktop\trabalho_ia\images'

for root, dirs, files in os.walk(main_folder_path, topdown=False):
    for name in dirs:
        image_folder = os.path.join(root, name)
        individual_id = name.split('_')[1]
        sampling_id = name.split('_')[2]
        os.makedirs(output_folder, exist_ok=True)
        output_prefix = f"individual_{individual_id}_{sampling_id}"
        process_images(image_folder, individual_id, output_folder, output_prefix)

# Processar as imagens
process_images(image_folder, individual_id, output_folder, output_prefix)
