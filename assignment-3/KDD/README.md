## KDD Data Science Project

This project employs the KDD (Knowledge Discovery in Databases) methodology to extract insights and knowledge from a dataset detailing credit card usage.

### File Descriptions

- **Enhanced_KDD.ipynb**: Comprehensive Jupyter notebook with analysis, visualizations, and detailed explanations following the KDD methodology. [View on Google Colab](https://colab.research.google.com/drive/1jFiV6LR-GqQmP_FQ17XLjzY-IA6VxrF0).

- **KDD.tex**: LaTeX source of the research paper/report detailing the project.

- **KDD.pdf**: Compiled PDF version of the LaTeX report.

- **Medium Article**: [Segmenting Credit Card Users: The Power of Clustering](https://medium.com/@moukthikareddy.vuyyuru/segmenting-credit-card-users-the-power-of-clustering-a431336c71a0)

### Project Overview

In this KDD project, the primary objective was to derive insights and possibly make predictions based on a dataset detailing credit card usage.

**Key Steps**:
- **Data Understanding**: The dataset encompasses various features related to credit card usage such as `BALANCE`, `PURCHASES`, `ONEOFF_PURCHASES`, `CASH_ADVANCE`, and more, offering a comprehensive view of cardholder behavior.

- **Data Exploration**: Initial steps involved loading the dataset and understanding its structure. Various statistics were calculated to provide an overview of the data distribution and characteristics.

- **Data Preprocessing**: The dataset had missing values, notably in the `CREDIT_LIMIT` and `MINIMUM_PAYMENTS` columns. Addressing these missing values would be critical for any subsequent analysis or modeling.

- **Modeling**: While the specific modeling techniques aren't clear from the provided snippets, the dataset's nature suggests potential applications like customer segmentation or behavior prediction.

**Challenges**:
- **Data Quality**: Addressing missing values is paramount to ensure reliable insights and predictions.

- **Data Volume**: The dataset's size might introduce computational challenges, especially during modeling or clustering phases.

- **Interpretability**: Ensuring that insights and potential predictions are interpretable and actionable would be essential.

**Solutions Implemented**:

- **Data Imputation**: 
  - Identified missing values in the dataset.
  - Filled missing values using the median of the respective columns for simplicity.

- **Efficient Processing**: 
  - Applied feature scaling using `StandardScaler` to normalize the data.
  - Addressed outliers using the IQR method.
  - Employed Principal Component Analysis (PCA) for data reduction, understanding the variance explained by principal components.

- **Model Selection**: 
  - Utilized the `H2OAutoML` framework, which automatically explored various models and ranked them based on performance.
  - Employed models like GBM and XGBoost.
  - Applied K-means clustering for data segmentation. Determined the optimal number of clusters using the elbow curve method.
  - Tested the "k-means++" variation of K-means clustering.
  - Explored DBSCAN as an alternative clustering technique, a density-based approach.


### GIF Walkthrough
Get a swift visual overview of the essential sections and outputs in the Jupyter notebook:

![GIF Walkthrough](https://drive.google.com/uc?export=view&id=1jK0doyRKyD9d4MMWDXPJVRRnaraLGnlL)
