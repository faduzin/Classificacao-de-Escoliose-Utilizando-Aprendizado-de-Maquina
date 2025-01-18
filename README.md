# Scoliosis Classification Using Machine Learning

This repository contains code and results from experiments conducted by students in the AI course at UNIFESP – São José dos Campos Campus. The primary goal is to **classify scoliosis severity** (based on Cobb angle) using data collected by a baropodometer and various machine learning models.

## Project Description

Scoliosis is a medical condition involving an abnormal lateral curvature of the spine. Standard diagnosis typically requires X-ray imaging, but this project explores using baropodometer pressure data for classification. We apply machine learning techniques to categorize individuals into different scoliosis severity groups.

### Objectives
- Use sensor pressure data collected by a baropodometer to classify patients into “mild” or “moderate” scoliosis groups based on their Cobb angle.
- Explore different AI models, such as Multilayer Perceptron (MLP) and Convolutional Neural Networks (CNNs), to optimize classification results.

## Repository Structure

```scss
scoliosis-classification-ml/
├─ README.md
├─ README.pt-br.md
├─ docs/
│   ├─ presentation.pdf
│   └─ report.pdf
├─ notebooks/
│   ├─ training.ipynb
├─ preprocessing/
│   ├─ normalization_test.ipynb
│   ├─ image_conversion.py
│   ├─ pngglue.py
│   ├─ pngmover.py
│   ├─ sort_to_class.py
│   └─ extract_500.py
└─ requirements.txt
```

## How to Run

1. **Clone the Repository**  
```bash
git clone https://github.com/faduzin/scoliosis-classification-ml.git
```

2. **Navigate to the Project Folder**  
```bash
cd scoliosis-classification-ml
```

3. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

4. **Open and Run the Notebooks**  
```bash
jupyter notebook
```

- Navigate to the `notebooks/` folder in the Jupyter interface.
- Open `training_part1.ipynb` or `training_part2.ipynb` to run and explore the experiments.

## Data Sctructure:
- **Data Spreadsheet**: Contains anthropometric data, sensor measurements, and patients’ Cobb angles.
- **Raw Data**: Text files containing sensor readings, organized into folders by patient and condition (open eyes or closed eyes).

## Trained Models & Approaches

- **MLP** (Multilayer Perceptron): Network topology `[30-44-1]`.  
- **SVM** (Support Vector Machine): Trains on numeric features derived from the baropodometer data.  
- **CNN** (Convolutional Neural Network): Uses architectures like ResNet50 and EfficientNet to classify images generated from sensor data.

## Results

Key metrics used for evaluating model performance include:

- **Balanced Accuracy**: Addresses class imbalance by averaging recall obtained on each class.  
- **F1-Score**: Harmonic mean of precision and recall.  
- **ROC-AUC**: Assesses how well the model can distinguish between classes.

The highest balanced accuracy achieved was around **60.34% ± 11.25%** with an SVM, and **62.27%** in one of the folds using ResNet50.

## Conclusion

These findings demonstrate the potential for **identifying scoliosis severity** using baropodometer data. However, improvements can still be made, particularly regarding data quality and class balance.

## References

- Fanfoni, C. et al. *Evaluation of scoliosis using baropodometer and artificial neural network*. 2017.  
- Castro Forero, F. R. *Baropodometric System and Scoliosis Classification Using Machine Learning Techniques*. 2019.
