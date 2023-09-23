## SEMMA Data Science Project

This project adopts the SEMMA (Sample, Explore, Modify, Model, Assess) methodology for a data-driven exploration and analysis.

### File Descriptions
- **SEMMA.ipynb**: Comprehensive Jupyter notebook with analysis, visualizations, and detailed explanations following the SEMMA methodology.
- **SEMMA.tex**: LaTeX source of the research paper/report detailing the project.
- **SEMMA.pdf**: Compiled PDF version of the LaTeX report.
- **Medium Article**: [Emotion Detection from Text: A SEMMA Methodology Approach](https://medium.com/@moukthikareddy.vuyyuru/title-emotion-detection-from-text-a-semma-methodology-approach-eddf2797a67a)
- **Colab Notebook**: [View on Google Colab](https://colab.research.google.com/drive/1L-iWwqCv7Em4RG4ZQKJAHuqy_a6RD8zD#scrollTo=kmSY9isl9fKW)

### Project Overview

In this project, we leveraged the SEMMA methodology to delve into emotion detection from textual data. The dataset appears to contain snippets of text that likely represent users' sentiments or emotions.

**Key Steps**:
- **Sample**: A subset of the textual data was selected to facilitate efficient analysis without compromising the depth of insights.
- **Explore**: Preliminary explorations were conducted on the textual snippets to identify patterns, frequent terms, and potential emotional indicators.
- **Modify**: The data underwent preprocessing to handle any inconsistencies, clean the text, and prepare it for modeling.
- **Model**: Models, potentially sentiment analysis or emotion detection algorithms, were applied to discern the underlying emotions or sentiments in the textual snippets.
- **Assess**: The model's performance was evaluated, ensuring that it accurately captures the emotions or sentiments expressed in the texts.

**Challenges**:
- **Data Complexity**: Textual data, being unstructured, poses unique challenges in terms of preprocessing and extraction of meaningful features.
- **Scalability**: The high dimensionality of text data, especially when converted to features, poses computational challenges.
- **Model Interpretability**: With textual data, ensuring that the model's predictions align with human interpretation is crucial.

**Solutions Implemented**:
- **Text Preprocessing**: Techniques like tokenization, stemming, and stopword removal were potentially employed to prepare the text for modeling.
- **Feature Extraction**: Methods like TF-IDF or word embeddings might have been used to convert text into numerical features.
- **Model Selection**: The project employed a variety of models as part of the AutoML process, including:
  - Deep Learning models: `DeepLearning_grid_3_AutoML_1_20230922_172321_model_1`
  - Stacked Ensembles: `StackedEnsemble_BestOfFamily_1_AutoML_1_20230922_172321` and `StackedEnsemble_AllModels_1_AutoML_1_20230922_172321`
  - Generalized Linear Models (GLM): `GLM_1_AutoML_1_20230922_172321`
  - XGBoost models: `XGBoost_grid_1_AutoML_1_20230922_172321_model_3`, `XGBoost_grid_1_AutoML_1_20230922_172321_model_1`, `XGBoost_grid_1_AutoML_1_20230922_172321_model_2`, and `XGBoost_2_AutoML_1_20230922_172321`


### GIF Walkthrough
Get a swift visual overview of the essential sections and outputs in the Jupyter notebook:

![GIF Walkthrough](https://drive.google.com/uc?export=view&id=1kpj0eCwW_ksT4ox0LDHy76Tys8Wajyin)
