import os
import numpy as np
import cv2
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Caminho da pasta onde estão os arquivos .txt
main_folder_path = r'C:\Users\Cabas\Desktop\trabalho_ia\pasta'

# Função para processar cada arquivo
def process_file(file_path):
    # Ler o arquivo e converter as linhas em uma matriz numpy, usando apenas as 10 primeiras colunas
    df = pd.read_csv(file_path, delim_whitespace=True)

    # Dividir a matriz em duas partes: primeiras 6 linhas e últimas 6 linhas
    first_six_lines = df.iloc[:, :6]
    last_six_lines = df.iloc[:, 6:]

    # Normalizar cada parte separadamente
    scaler = MinMaxScaler(feature_range=(-1,1))
    normalized_first_six = scaler.fit_transform(first_six_lines)
    normalized_last_six = scaler.fit_transform(last_six_lines)

    # Juntar as duas partes normalizadas novamente
    normalized_matrix = np.hstack((normalized_first_six, normalized_last_six))

    # Converter a matriz normalizada para o intervalo 0-255
    normalized_matrix = cv2.normalize(normalized_matrix, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Salvar a imagem na mesma pasta com o mesmo nome, mas extensão .png
    output_path = file_path.replace('.txt', '.png')
    cv2.imwrite(output_path, normalized_matrix)
    print('Imagem: ', output_path,'criada com sucesso')

# Iterar sobre todos os arquivos .txt na pasta
for root, dirs, files in os.walk(main_folder_path):
    for filename in files:
        if filename.endswith('.txt'):
            file_path = os.path.join(root, filename)
            process_file(file_path)

print("Processamento concluído!")