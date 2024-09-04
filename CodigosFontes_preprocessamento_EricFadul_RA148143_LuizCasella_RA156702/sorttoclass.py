import os
import pandas as pd

main_path = r'E:\all images'
output_c1 = r'E:\dataset2\c1'
output_c2 = r'E:\dataset2\c2'
label_path = r'labels.xlsx'

labels_df = pd.read_excel(label_path)

# Criar um dicionário para mapear indivíduos às suas labels
individual_label_map = {}
for idx, row in labels_df.iterrows():
    individual_id = row['individual_id']  # Supondo que exista uma coluna 'individual_id' para identificar o indivíduo
    individual_id = individual_id.split('_')[1]
    label = row['label']  # Supondo que a coluna de labels seja chamada 'label'
    individual_label_map[individual_id] = label


for root, dirs, files in os.walk(main_path, topdown=False):
    for filename in files:
        image_path = os.path.join(root, filename)
        individual_extracted_id = filename.split('_')[2].strip()
        if individual_extracted_id in individual_label_map:
            label = individual_label_map[individual_extracted_id]
            if label == 0:
                os.makedirs(output_c1, exist_ok=True)
                output_path = f"{output_c1}\{filename}"
                os.rename(image_path, output_path)
            else:
                os.makedirs(output_c2, exist_ok=True)
                output_path = f"{output_c2}\{filename}"
                os.rename(image_path, output_path)