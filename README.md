# Sloan Digital Sky Survey (SDSS) Galaxy Classification Using Machine Learning

   This project uses machine learning to classify galaxies from the SDSS dataset into 'STARFORMING' and 'STARBURST' categories, enabling real-time predictions through a web application.

___

![Galaxy Classification](/static/images/pic1.avif)

---

![Galaxy Classification](/static/images/pic2.avif)

---

## Contents 

- [About Dataset](#about-dataset)
- [Project Overview](#project-overview)
- [Project Flow](#project-flow)
- [Architecture](#architecture)
- [Project Phases](#project-phases)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Deployment](#deployment)
- [Google Badges](#google-badges)

---

## About Dataset

### SDSS Galaxy Classification DR18

   The Sloan Digital Sky Survey (SDSS) has scanned about one-third of the sky and identified around 1 billion objects, including nearly 3 million galaxies. This project utilizes a dataset with 100,000 rows of photometric image data, focusing on classifying galaxies into two subclasses: 'STARFORMING' and 'STARBURST'. The dataset is available for download from Kaggle [here](https://www.kaggle.com/datasets/bryancimo/sdss-galaxy-classification-dr18).

---

## Project Overview

   The Galaxy Classification Project aims to predict galaxy subclasses using machine learning techniques. This project encompasses data collection, preparation, exploratory data analysis (EDA), model building, performance testing, and deployment. The final model is integrated with a web framework to provide real-time predictions based on user input.

---

## Project Flow

   1. **User Interaction:** Users input galaxy data through a web-based interface.
   2. **Model Analysis:** The machine learning model integrated into the web application analyzes the input data.
   3. **Prediction Display:** The model's prediction for the galaxy subclass is displayed on the user interface.

### Key Steps

   1. **Data Collection & Preparation**
      - **Collect the Dataset:** Obtain the dataset from SDSS.
      - **Data Preparation:** Clean and preprocess the data for analysis.
   
   2. **Exploratory Data Analysis (EDA)**
      - **Descriptive Statistics:** Analyze fundamental characteristics of the data.
      - **Visual Analysis:** Use visual tools to explore patterns and trends.
   
   3. **Model Building**
      - **Training the Model:** Train various machine learning algorithms.
      - **Testing the Model:** Evaluate the models using performance metrics.
   
   4. **Performance Testing**
      - **Evaluation Metrics:** Assess the model using metrics like accuracy, precision, recall, F1-score, and confusion matrix.
      - **Model Evaluation:** Compare models based on these metrics to determine the best performer.
      - **Hyperparameter Tuning:** Optimize model performance by adjusting hyperparameters.
   
   5. **Model Deployment**
      - **Save the Best Model:** Store the best-performing model for future use.
      - **Integrate with Web Framework:** Implement the model within a Flask web application for user interaction.

---

## Architecture

   The Galaxy Classification Project follows a modular architecture:
   
   - **Data Preparation Module:** Handles loading, cleaning, and preparing the dataset.
   - **Model Training Module:** Trains and evaluates various machine learning models.
   - **Web Application Module:** Implements a Flask web application for user interaction.
   - **Deployment Module:** Manages the deployment and running of the application.

---

## Project Phases

### 1. Data Collection & Preparation

   - **Collect the Dataset**

      - The dataset for this project is sourced from the Sloan Digital Sky Survey (SDSS). It consists of photometric image data for galaxies, with 100,000 rows and two primary galaxy subclasses: 'STARFORMING' and 'STARBURST'. Download the dataset from Kaggle [here](https://www.kaggle.com/datasets/bryancimo/sdss-galaxy-classification-dr18).

   - **Data Preparation**

      - **Handling Missing Values:** Identify and address missing values in the dataset.
      - **Data Type Conversion:** Convert the 'subclass' column from object to integer using ordinal encoding.
      - **Feature Selection:** Select relevant features for model training and refine the dataset.

### 2. Exploratory Data Analysis (EDA)

   - **Descriptive Statistics**
   
      - **Purpose:** Understand the fundamental characteristics of the data.
      - **Tools:** Utilize Pandas `describe()` function to summarize statistics such as mean, standard deviation, and percentiles.
   
   - **Visual Analysis**
   
      - **Purpose:** Visually explore data to identify patterns, trends, and outliers.
      - **Tools:** Use Seaborn and Matplotlib for visualizations like box plots and heatmaps.

### 3. Model Building

   - **Training the Model**
   
      Train various machine learning algorithms to identify the best model:
   
      - **Decision Tree Classifier:** A simple and interpretable model.
      - **Logistic Regression:** A statistical method for binary classification.
      - **Random Forest Classifier:** An ensemble method that improves accuracy through multiple decision trees.
   
   - **Testing the Model**
   
      - **Metrics:** Evaluate model performance using accuracy, precision, recall, F1-score, and confusion matrix.
      - **Comparison:** Compare models based on these metrics to determine the best performer.

### 4. Performance Testing

   - **Evaluation Metrics**

      - **Purpose:** Ensure the model’s effectiveness and robustness.
      - **Metrics:** Use accuracy, precision, recall, F1-score, and confusion matrix to assess performance.

   - **Model Evaluation**

      After training and testing various models, the performance metrics for each model are compared. The table below summarizes the precision, recall, F1-score, and accuracy of each model:

|         **Model**        | **Precision Class 0** | **Precision Class 1** | **Recall Class 0** | **Recall Class 1** | **f1-score Class 0** | **f1-score Class 1** | **Accuracy** |
|:------------------------:|:---------------------:|:---------------------:|:------------------:|:------------------:|:--------------------:|:--------------------:|:------------:|
| Decision Tree Classifier |          0.78         |          0.80         |        0.80        |        0.78        |         0.79         |         0.79         |  **0.79168** |
| Logistic Regression      |          0.79         |          0.81         |        0.82        |        0.78        |         0.80         |         0.80         |  **0.80165** |
| Random Forest Classifier |          0.84         |          0.81         |        0.82        |        0.84        |         0.83         |         0.82         |  **0.82575** |

   - **Performance Analysis**
   
      - **Decision Tree Classifier:**
        - **Strengths:** Balanced recall for both classes, providing a consistent prediction rate.
        - **Weaknesses:** Lower precision for Class 0, indicating that the model is less accurate in predicting Class 0 instances.
        - **Overall Performance:** The model has the lowest overall accuracy compared to others.
      
      - **Logistic Regression:**
        - **Strengths:** Good precision for both classes and high recall for Class 0, making it a reliable choice for balanced performance.
        - **Weaknesses:** Lower recall for Class 1, suggesting it is less effective at identifying Class 1 instances.
        - **Overall Performance:** Moderate overall accuracy, offering a balanced performance between precision and recall.
      
      - **Random Forest Classifier:**
        - **Strengths:** Highest precision and recall for both classes, indicating a well-rounded and effective model.
        - **Weaknesses:** None significant compared to other models.
        - **Overall Performance:** The best overall accuracy, making it the preferred model for this classification task.

   - **Hyperparameter Tuning**

      Optimize the model performance by adjusting hyperparameters to improve accuracy further.

### 5. Model Deployment

   - **Save the Best Model**
   
      - **File:** `RF.pkl` - Save the best-performing Random Forest model using Python’s `pickle` module. This avoids retraining the model and allows for future use.
   
   - **Integrate with Web Framework**
   
      - **Web Application:** Build using Flask to create a user-friendly interface.
      - **HTML Pages**:
        - `index.html` - The main page where users input their data.
        - `inner-page.html` - The results page displaying predictions.

---

## Features

   - **User-Friendly Interface:** Provides an intuitive interface for users to input galaxy data and view predictions.
   - **Real-Time Predictions:** Uses a trained machine learning model to deliver immediate results based on user inputs.
   - **Comprehensive Analysis:** Includes detailed steps in exploratory data analysis, model building, performance testing, and deployment.

---

## Installation

   1. **Clone the Repository:**
   
       ```bash
       git clone https://github.com/atul-maurya-30/galaxy.git
       cd galaxy
       ```
   
   2. **Install Required Packages:**
   
       ```bash
       pip install -r requirements.txt
       ```
---

## Usage

   1. **Run the Flask Application:**
   
       ```bash
       python app.py
       ```
   
   2. **Access the Web Application:** Open a web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
   
   3. **Enter Galaxy Data:** Use the form on `index.html` to input galaxy data.
   
   4. **View Predictions:** After submitting the input data, view predictions on `inner-page.html`.

---
## License

   This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Deployment

You can access the deployed application here: [Galaxy Classifier](https://galaxy-classifier.onrender.com)

Feel free to try out the app and explore its features.

---

### Google Badges

I have earned various Google Cloud badges showcasing my skills and expertise. You can view them here:

- [Google Cloud Badges]([https://your-google-badges-link.com](https://www.cloudskillsboost.google/public_profiles/9797efa8-4ca6-4c86-92d1-e6890f3ad461))


---

Thank you for exploring the Galaxy Classification Project! We hope this project provides valuable insights into galaxy classification using machine learning. For any questions or contributions, please feel free to reach out.

---
