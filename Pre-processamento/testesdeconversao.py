import os
import numpy as np
import cv2
from sklearn.preprocessing import StandardScaler
import pandas as pd

file_path = r'C:\Users\Cabas\Desktop\trabalho_ia\individual_1_1\CE_individual_1_1_1245.txt'

# Carregando o arquivo de texto em um DataFrame
df = pd.read_csv(file_path, delim_whitespace=True)

# Dividir a matriz em duas partes: primeiras 6 linhas e últimas 6 linhas
first_six_lines = df.iloc[:, :6]
last_six_lines = df.iloc[:, 6:]

# Normalizar cada parte separadamente
scaler = StandardScaler()
normalized_first_six = scaler.fit_transform(first_six_lines)
normalized_last_six = scaler.fit_transform(last_six_lines)

# Juntar as duas partes normalizadas novamente
normalized_matrix = np.hstack((normalized_first_six, normalized_last_six))

# Converter a matriz normalizada para o intervalo 0-255
normalized_matrix = cv2.normalize(normalized_matrix, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Salvar a imagem na mesma pasta com o mesmo nome, mas extensão .png
output_path = file_path.replace('.txt', '.png')
cv2.imwrite(output_path, normalized_matrix)

