
# Classificação de Escoliose Utilizando Aprendizado de Máquina

Este repositório contém o código e os resultados dos experimentos realizados por alunos da disciplina de IA da UNIFESP - Campus São José dos Campos para a **Classificação de Escoliose** utilizando dados obtidos por meio de um baropodômetro e modelos de inteligência artificial. O objetivo principal deste projeto foi classificar pacientes em dois grupos, de acordo com o ângulo de Cobb, utilizando redes neurais e outras técnicas de aprendizado de máquina.

## Descrição do Projeto

A escoliose é uma condição médica que envolve uma curvatura lateral anormal da coluna vertebral. O diagnóstico padrão exige exames de raio-x, mas este projeto explora o uso de um baropodômetro para obter dados sobre a distribuição da pressão plantar de indivíduos e, a partir desses dados, aplicar modelos de aprendizado de máquina para classificá-los de acordo com a gravidade da escoliose.

### Objetivos:
- Utilizar dados de sensores de pressão obtidos por um baropodômetro para classificar pacientes em grupos de escoliose leve ou moderada, com base no ângulo de Cobb.
- Explorar diferentes arquiteturas de modelos de IA, como redes neurais artificiais (MLP) e redes neurais convolucionais (CNN), para otimizar os resultados.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `preprocessamento/`: Scripts utilizados no pré-processamento dos dados. Esses scripts incluem:
  - **normalization_test.ipynb**: Testes de normalização.
  - **image_conversion.py**: Aplicação de normalizações e conversão dos arquivos .txt em .png.
  - **pngglue.py**: Agrupamento das imagens de 20 em 20 para formação de uma imagem maior.
  - **pngmover.py**: Para mover os arquivos para um diretório.
  - **sorttoclass.py**: Para mover os arquivos para um diretório de acordo com sua classe.
  - **500_extractor.py**: Para extrair somente as 500 imagens centrais de cada partição das amostras (Closed Eyes ou Open Eyes).

- Arquivos principais (notebooks, relatório, slides) estão localizados na raiz do repositório:
  - **Treino_pt1.ipynb**: Parte 1 de todo o treinamento.
  - **Treino_pt.ipynb**: Parte 2 de todo o treinamento.
  - **Relatorio.pdf**: Relatório completo do projeto.
  - **Apresentacao.pdf**: Slides da apresentação.

## Como Executar
Para visualização dos dados e resultados nos arquivos ".ipynb", recomenda-se o uso do site: https://nbviewer.org/, porém no atual momento a base de dados não foi publicada, assim não é possivel executar o codigo, porem ainda são passados por padrão passos para execução do código.

### Pré-requisitos:
Não há um arquivo de requisitos. Para instalar as dependências necessárias, utilize as seguintes bibliotecas:

```bash
pip install numpy pandas matplotlib scikit-learn torch torchvision opencv-python
```

### Passo a Passo:
1. Clone o repositório:
   ```bash
   git clone https://github.com/username/escoliose-classificacao.git
   ```
2. Coloque os dados brutos no diretório `data/`.
3. Execute os notebooks para realizar o pré-processamento e o treinamento dos modelos.

### Estrutura dos Dados:
- **Planilha de dados**: Contém dados antropométricos, medições dos sensores e os ângulos de Cobb dos pacientes.
- **Dados brutos**: Arquivos de texto com as leituras dos sensores, organizados em pastas por paciente e condição (olhos abertos ou fechados).

### Modelos Treinados:
- **MLP**: Rede neural perceptron multicamadas com topologia `[30-44-1]`.
- **SVM**: Rede neural por vetor de suporte.
- **CNN**: Utilização da ResNet50 e EfficientNet para classificação das imagens geradas.

## Resultados

Os resultados obtidos nos experimentos são apresentados através das seguintes métricas:

- **Acurácia Balanceada**: Leva em conta a distribuição desigual das classes.
- **F1-Score**: Média harmônica entre precisão e recall.
- **ROC-AUC**: Curva ROC para avaliar a discriminação entre classes.

Os modelos alcançaram uma acurácia balanceada máxima de **60.34% ± 11.25%** ao utilizar uma Support Vector Machine (SVM), e **62.27%** em um dos folds ao utilizar a ResNet50.

## Conclusão

Os resultados indicam que é possível identificar a gravidade da escoliose a partir dos dados coletados por um baropodômetro. No entanto, há espaço para melhorias na qualidade dos dados e no equilíbrio entre as classes.

## Referências

- FANFONI, Caroline et al. *Evaluation of scoliosis using baropodometer and artificial neural network*. 2017.
- CASTRO FORERO, Fabian Rodrigo. *Sistema Baropodométrico e Classificação de Escoliose Utilizando Técnicas de Machine Learning*. 2019.
