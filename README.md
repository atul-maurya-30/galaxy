# SDSS Galaxy Classification DR18
About Dataset
The Sloan Digital Sky Survey (SDSS) has searched about one-third of the sky and found around 1 billion objects and almost 3 million of those are galaxies. It contains 100,000 rows of photometric image data and the galaxy subclass is limited to two types, 'STARFORMING' or 'STARBURST'
**galaxy.ipynb**:This files contains Data collection,Data preprocessing,model Building

+--------------------------+-------------------+-------------------+-------------------+--------------+
|         **Model**        |    **Precision    |      **Recall     |     **f1-score    | **Accuracy** |
|                          |    (Class-0)**    |    (Class-0)**    |    (Class-0)**    |              |
+--------------------------+---------+---------+---------+---------+---------+---------+--------------+
|                          | **Class | **Class | **Class | **Class | **Class | **Class |              |
|                          |   0**   |   1**   |   0**   |   1**   |   0**   |   1**   |              |
+--------------------------+---------+---------+---------+---------+---------+---------+--------------+
| Decision Tree Classifier | 0.86    | 0.56    | 0.85    | 0.58    | 0.86    | 0.57    | **0.78515**  |
+--------------------------+---------+---------+---------+---------+---------+---------+--------------+
| Logistic Regression      | 0.85    | 0.72    | 0.93    | 0.50    | 0.89    | 0.59    | **0.82725**  |
+--------------------------+---------+---------+---------+---------+---------+---------+--------------+
| Random Forest Classifier | 0.93    | 0.57    | 0.87    | 0.73    | 0.90    | 0.64    | **0.8417**   |
+--------------------------+---------+---------+---------+---------+---------+---------+--------------+
