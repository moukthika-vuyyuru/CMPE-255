# Clustering Assignment


### Credit Card Customer Segmentation
- **Problem Statement:** Classify credit card customers into distinct segments based on their credit card usage and interaction with the bank.
- **Dataset:** The dataset, available on [Kaggle](https://www.kaggle.com/datasets/aryashah2k/credit-card-customer-data), includes features like Average Credit Limit, Total Number of Credit Cards, Total Visits to Bank, Online Visits, and Calls Made.
- **Solution & Modeling Approach:** Implemented K-Means clustering algorithm from scratch for customer segmentation, incorporating data preprocessing techniques like normalization.
- **Results:** Successfully segmented customers into four distinct groups, offering insights for targeted marketing and personalized customer service strategies.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lZ3Tp3BKXr9Wo66ezBXer3x1feHYkvoB#scrollTo=1sW_2Oqzs92P)


### Hierarchical Clustering of UCI Datasets
- **Problem Statement:** Group the UCI Machine Learning Repository's datasets to uncover patterns based on dataset size and complexity.
- **Dataset:** The "UCI Top 250 Datasets" collection, available on [Kaggle](https://www.kaggle.com/datasets/khushipitroda/uci-dataset), featuring a variety of datasets with details like the number of instances and attributes.
- **Solution & Modeling Approach:** Applied Hierarchical Clustering to analyze and segment datasets based on their normalized 'Instances' and 'Attributes'. The clustering process included data preprocessing, feature extraction, and dendrogram analysis to determine the optimal number of clusters.
- **Results:** Identified three distinct clusters representing varying dataset characteristics:
  - Cluster 1: Large datasets with fewer attributes, indicating high volume but lower complexity.
  - Cluster 2: Datasets with moderate size but high attribute count, suggesting higher complexity.
  - Cluster 3: Moderately sized datasets with fewer attributes, balancing size and complexity.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bydd4PRKQzmwt3UfIYUJ8p1M2Wuf5eLd#scrollTo=4KXyTDybX2IG)


### Gaussian Mixture Models Clustering Analysis
- **Objective:** Apply GMM clustering to understand and segment our dataset, potentially for enhancing customer targeting, product recommendations, or other strategic initiatives.
- **Methodology:**
  - Data Preprocessing: Standard scaling applied to normalize the dataset.
  - Optional PCA: Applied for dimensionality reduction to simplify the data structure.
  - GMM Clustering: Implemented Gaussian Mixture Models to identify clusters within the data.
- **Key Findings:**
  - Cluster Characteristics: Detailed profiles for each cluster were developed, highlighting key differentiators and patterns.
  - Feature Importance: Analysis conducted to identify features that significantly influence cluster formation.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bDYUaDMoIdGw2evItNScHhfjFenm1dmJ#scrollTo=TlE7fQZ4klZy)


### DBSCAN Clustering of Grocery Store Customers
- **Problem Statement:** Cluster grocery store customers to manage offers and discounts more effectively.
- **Dataset:** The dataset [Kaggle](https://www.kaggle.com/datasets/samanehkorlou/customer-segmentation)Includes features like Customer ID, Status, Geographical ID, Net Purchase, Average Invoice Rows, Waste Rate, Rejected Rate, Average Monthly Purchases, and Dates related to customer activity.
- **Solution & Modeling Approach:** Implemented DBSCAN clustering using the PyCaret library. Explored different `eps` values to optimize clustering. Features included numerical customer activity and purchase metrics.
- **Results:** 
  - First Attempt (eps=0.5): Achieved moderate cluster separation (Calinski-Harabasz: 21.7999), but clusters were not well-defined (Silhouette: -0.1549).
  - Second Attempt (eps=0.9): Similar results with slight parameter tuning (Silhouette: -0.1568, Calinski-Harabasz: 21.6333).
  - The DBSCAN algorithm struggled to find well-separated clusters, indicating potential overlap or complex data distribution.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PxUBbeZvPNSQ9M8mtHtIGknAo2IPexiE#scrollTo=AOOVQI8bdTak)


### Clustering of NYC Taxi Passenger Time Series Data
- **Objective:** Identify patterns in NYC taxi passenger counts using time series clustering techniques.
- **Dataset Description:** Aggregated data on the number of NYC taxi passengers in 30-minute intervals, with anomalies during events like the NYC marathon, holidays, and a snowstorm.
- **Methodology:**
  - Data Preprocessing: Converted timestamps to datetime format and set as the index. Dropped unnecessary columns.
  - Feature Extraction: Calculated rolling mean and standard deviation; extracted time-based features such as hour of the day and day of the week.
  - Clustering: Applied K-Means clustering on the extracted features.
- **Results:**
  - Five clusters were identified, each representing different patterns in passenger counts:
    - Cluster 0: High passenger counts, predominantly in the late afternoon on weekends.
    - Cluster 1: Moderately high counts, mainly in the late afternoon on weekdays.
    - Cluster 2: High counts during early morning hours.
    - Cluster 3: Lower counts in the early morning, mostly on weekdays.
    - Cluster 4: Lowest counts around noon.
  - The clusters reflect variations in passenger volume across different times of the day and week.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10Nh8IkPgXobBuDqVucrl02-NCLZd4mLC#scrollTo=cxwulQu0tixF)


### Anomaly Detection in Stock Market Data using PyOD
- **Objective:** Identify unusual patterns in stock market data (price and volume) using PyOD's Isolation Forest algorithm.
- **Dataset Description:** Time series data of a stock (e.g., AAPL), including daily closing prices, trading volumes, and high/low prices.
[Kaggle](https://www.kaggle.com/datasets/khushipitroda/stock-market-historical-data-of-top-10-companies)
- **Methodology:**
  - Data Preprocessing: Converted price fields to numeric and parsed dates.
  - Anomaly Detection: Applied Isolation Forest from PyOD to detect anomalies in multivariate data.
- **Results:** 
  - Identified anomalies marked in the dataset, potentially indicating unusual market activities or significant events.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10sLBzIdXCaQMy1DuBUnaxCBI57TpV5NI#scrollTo=QsjRhbuN5QCb)
- 

### Document Clustering with LLM Embeddings
- **Objective:** Categorize news articles into five distinct topics using advanced LLM embeddings.
- **Dataset Description:** A collection of 2225 news articles from the BBC News website, spanning across five categories: business, entertainment, politics, sport, and tech.
  [Kaggle](https://www.kaggle.com/datasets/dimasmunoz/bbc-articles-cleaned)
- **Methodology:**
  - Data Preprocessing: Text cleaning and preparation for embedding.
  - Embeddings: Generated document embeddings using the `all-MiniLM-L6-v2` model.
  - Clustering: Applied K-Means clustering to the embeddings.
- **Results:** 
  - Successfully clustered documents into five groups corresponding to their respective news categories, as visualized with t-SNE.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DeF2TWz5De_iS2mKatKOW2Jch-c-S5Im#scrollTo=pfa7I3jlkvul)



### Clustering of Images Using ImageBind LLM Embeddings

- **Objective:** Demonstrate the clustering of a diverse set of images (dogs, cats, family, alone, food) using advanced ImageBind LLM embeddings.
- **Dataset Description:** The dataset comprises 80 photos across five categories: dogs (10), cats (10), family (20), alone (20), and food (20). The images are not labeled, but they exhibit clear categorical distinctions.
  [Kaggle](https://www.kaggle.com/datasets/heavensky/image-dataset-for-unsupervised-clustering#:~:text=URL%3A%20https%3A%2F%2Fwww.kaggle.com%2Fdatasets%2Fheavensky%2Fimage)
- **Methodology:**
  - Image Preprocessing: Converted images to a consistent size and RGB format.
  - Embedding Generation: Utilized ImageBind LLM embeddings to transform images into high-dimensional vectors.
  - Clustering: Applied K-Means clustering on the generated embeddings.
- **Results:** 
  - Successfully clustered images into distinct groups, reflecting their categorical similarities.
- **Colab Notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LOUuFf_ATjn4gJYyKM5Lis2mSBB5m_Mn#scrollTo=p5OpdgmyvIc1)


