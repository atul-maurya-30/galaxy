# Galaxy Classification Project
## Model Evaluation

After training and testing various models, the performance metrics for each model were compared to determine the best performing algorithm. The table below summarizes the precision, recall, f1-score, and accuracy of each model:

|         **Model**        | **Precision Class 0** | **Precision Class 1** | **Recall Class 0** | **Recall Class 1** | **f1-score Class 0** | **f1-score Class 1** | **Accuracy** |
|:------------------------:|:---------------------:|:---------------------:|:------------------:|:------------------:|:--------------------:|:--------------------:|:------------:|
| Decision Tree Classifier |          0.86         |          0.56         |        0.85        |        0.58        |         0.86         |         0.57         |  **0.78515** |
| Logistic Regression      |          0.85         |          0.72         |        0.93        |        0.50        |         0.89         |         0.59         |  **0.82725** |
| Random Forest Classifier |          0.93         |          0.57         |        0.87        |        0.73        |         0.90         |         0.64         |  **0.8417**  |

#### Analysis

- **Decision Tree Classifier**: 
  - **Strengths**: High precision for Class 0.
  - **Weaknesses**: Lower recall for Class 1, indicating that the model misses some instances of Class 1.
  - **Overall Performance**: The model has the lowest overall accuracy compared to others.

- **Logistic Regression**:
  - **Strengths**: Good balance in precision for both classes, making it a reliable choice.
  - **Weaknesses**: Lower recall for Class 1, suggesting it is less effective at identifying Class 1 instances.
  - **Overall Performance**: Moderate overall accuracy, making it a decent choice but not the best.

- **Random Forest Classifier**:
  - **Strengths**: Highest precision and recall for Class 0, and higher recall for Class 1.
  - **Weaknesses**: Slightly lower precision for Class 1 compared to Logistic Regression.
  - **Overall Performance**: Best overall accuracy, indicating it performs best across all metrics.

## About Dataset
### SDSS Galaxy Classification DR18

The Sloan Digital Sky Survey (SDSS) has searched about one-third of the sky and found around 1 billion objects and almost 3 million of those are galaxies. It contains 100,000 rows of photometric image data and the galaxy subclass is limited to two types, 'STARFORMING' or 'STARBURST'

## Project Overview

The Galaxy Classification Project aims to predict galaxy subclasses using machine learning techniques. The project involves data collection, preparation, exploratory data analysis (EDA), model building, performance testing, and deployment. The final model is integrated with a web framework to provide real-time predictions based on user input.

## Project Flow

1. **User Interaction**: Users interact with a web-based UI to input data.
2. **Model Analysis**: The input data is analyzed using a machine learning model integrated into the web application.
3. **Prediction Display**: The model’s prediction is displayed to the user on the UI.

## Detailed Steps

### 1. Data Collection & Preparation

#### Collect the Dataset
The dataset for this project is sourced from the Sloan Digital Sky Survey (SDSS). It consists of photometric image data for galaxies, with 100,000 rows and two primary galaxy subclasses: 'STARFORMING' and 'STARBURST'. The dataset can be downloaded from Kaggle [here](https://www.kaggle.com/datasets/your-dataset-link).

#### Data Preparation
- **Handling Missing Values**: Missing values are identified and appropriately handled.
- **Data Type Conversion**: The 'subclass' column is converted from object to integer using ordinal encoding.
- **Feature Selection**: The dataset is refined by selecting relevant features for model training.

### 2. Exploratory Data Analysis (EDA)

#### Descriptive Statistics
- **Purpose**: To understand the fundamental characteristics of the data.
- **Tools**: Pandas `describe()` function to summarize statistics like mean, standard deviation, and percentiles.

#### Visual Analysis
- **Purpose**: To visually explore data and identify patterns, trends, and outliers.
- **Tools**: Seaborn and Matplotlib for creating visualizations like box plots and heatmaps.

### 3. Model Building

#### Training the Model
Different machine learning algorithms are trained to find the best model:
- **Decision Tree Classifier**: A simple and interpretable model.
- **Logistic Regression**: A statistical method for binary classification.
- **Random Forest Classifier**: An ensemble method that improves accuracy through multiple decision trees.

#### Testing the Model
- **Metrics**: Accuracy, precision, recall, F1-score, and confusion matrix are used to evaluate model performance.
- **Comparison**: Models are compared based on these metrics to select the best-performing model.

### 4. Performance Testing

#### Evaluation Metrics
- **Purpose**: To ensure the model's effectiveness and robustness.
- **Metrics**: Includes accuracy, precision, recall, F1-score, and confusion matrix.
- **Hyperparameter Tuning**: Comparing model performance before and after hyperparameter tuning to improve accuracy.

### 5. Model Deployment

#### Save the Best Model
- **File**: `RF.pkl` - The best-performing Random Forest model is saved using Python’s `pickle` module. This avoids the need to retrain the model and allows for future use.

#### Integrate with Web Framework
- **Web Application**: Built using Flask to create a user-friendly interface.
- **HTML Pages**: 
  - `index.html` - The main page where users input their data.
  - `inner-page.html` - The page displaying the prediction results.

### Web Framework Integration

#### Building HTML Pages
- **Files**: 
  - `index.html` - Contains the form for user input.
  - `inner-page.html` - Displays the prediction results.

#### Building Server-Side Script
- **File**: `app.py` - Contains Flask routes for rendering HTML pages and handling user inputs.
- **Functionality**: 
  - Load the saved model (`RF.pkl`).
  - Render HTML pages.
  - Retrieve input values from the UI and make predictions using the model.

#### Running the Web Application
1. **Setup**: Open VS Code and navigate to the folder containing `app.py`.
2. **Command**: Run `python app.py` to start the Flask server.
3. **Access**: Open a web browser and go to `http://127.0.0.1:5000` to interact with the web application.
4. **Usage**: Enter input values on the `index.html` page and view predictions on the `inner-page.html` page.


