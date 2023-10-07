# COVID-19 and Weather Data Exploratory Data Analysis

## Description
This project provides an in-depth Exploratory Data Analysis (EDA) on a combined dataset of COVID-19 statistics and corresponding weather information across various countries. The aim is to uncover patterns, correlations, and insights that might hint at how weather conditions could influence the spread of the virus. Using advanced visualization techniques, including D3.js and standard Python libraries, this project offers a comprehensive view of the interplay between the pandemic and meteorological factors.

## Datasets
The project leverages two primary datasets:

- **COVID-19 Data**: This dataset encompasses daily updates on confirmed cases, fatalities, and recoveries for every country. It provides a granular view of how the pandemic evolved over time, enabling time-series analysis.
  
- **Weather Data**: Encompassing daily weather metrics like temperature, humidity, and wind speed, this dataset aids in understanding potential correlations between climatic conditions and virus spread.

- [Kaggle Dataset Link](https://www.kaggle.com/datasets/davidbnn92/weather-data-for-covid19-data-analysis)

## Observable Notebook
A significant portion of the EDA was executed on Observable, harnessing the interactive capabilities of D3.js for dynamic visualizations. The Observable notebook delves into country-specific trends, offering a global overview of the pandemic's progress.
- [View the Observable notebook here](https://observablehq.com/d/cf70720e5bc5640a).

## Colab Notebook
For a structured and detailed EDA, a Colab notebook was employed. This notebook walks through the entire data processing pipeline, from cleaning and preprocessing to advanced visualizations. Python libraries like geopandas and Matplotlib are extensively used here.
- [Access the Colab notebook here](https://colab.research.google.com/drive/1KrE846OdNHoh0sXwYP74symksgb3FGXF#scrollTo=6ejbIE-ifng3).

## Visualizations
A variety of visualizations were crafted to represent the data effectively:

- **Time Series Analysis**: Plotting confirmed cases and fatalities over time.
- **Choropleth Maps**: Geospatial representation of data, showcasing COVID-19 spread across the globe.
- **Bar Charts**: Highlighting top countries based on different metrics.
- **Line Charts with Dual Axes**: Utilizing D3.js to represent confirmed cases against average temperature.

## Interactivity Features
Throughout the visualizations, a strong emphasis has been placed on user interactivity to provide a richer exploration experience:

- **Tooltips**: Hovering over various data points, be it on maps, bar charts, or line charts, will display detailed information in a tooltip. This allows users to glean specific data values and other insights without cluttering the main visualization.

- **Zoom**: Especially in time-series visualizations, users have the capability to zoom into specific timeframes to get a closer look at the data. This is particularly useful for analyzing short-duration trends or anomalies.

- **Dynamic Updates**: Some visualizations provide the ability to dynamically update based on user input or selections. This offers a customized view of the data based on specific criteria or filters.

These interactive elements not only enhance the visual appeal of the analysis but also make the data exploration process more intuitive and insightful.



# IPL 2023 Data: Automated Exploratory Data Analysis (Auto EDA)

## Description
This repository showcases an automated exploratory data analysis (Auto EDA) of the IPL 2023 datasets, highlighting detailed batting and bowling statistics for each match. Through this analysis, we aim to provide a swift and comprehensive overview of the datasets, uncovering patterns, distributions, and potential insights.

## Datasets
We analyze two primary datasets for the IPL 2023 season:

- **Batting Data**: Match-wise batting statistics that include metrics such as runs scored, balls faced, strike rates, and more.
  
- **Bowling Data**: Match-wise bowling data offering insights into overs bowled, wickets taken, economy rates, among other statistics.

- [Kaggle Dataset Link](https://www.kaggle.com/datasets/adityaazad79/ipl-2023-dataset/code)

## Auto EDA Tool Used
The analysis was carried out using pandas profiling, renowned for delivering interactive and in-depth insights into various datasets with ease.

## Reports
Detailed HTML reports generated from the Auto EDA tool can be accessed below:

- [Batting EDA Report](https://drive.google.com/file/d/1eNSp8LgrbXOmklZcIJnJYRGFi-np3xZ2/view?usp=drive_link)
  
- [Bowling EDA Report](https://drive.google.com/file/d/10a5JQL_NikVDUls5SUPG9dBZlVqe3Ycy/view?usp=drive_link)

## Notebook
For a detailed walkthrough of the Auto EDA process, you can explore the [AUTO_EDA.ipynb](https://colab.research.google.com/drive/18AYyz1hERO3zhwAL6KoR2MFttZS2sNAf#scrollTo=6z1ocz2CjD5F) notebook.


# Apache Beam Data Processing

This project delves deep into the data processing capabilities of Apache Beam, taking the user on a journey from rudimentary data reading and transformations to mastery of advanced features like windowing, triggers, and BeamML for machine learning tasks.

## Datasets Used:

- [`log_inf.csv`](https://www.kaggle.com/datasets/deeiip/1m-real-time-stock-market-data-nse): Contains log information with timestamps, aiding in windowing demonstrations.


## Key Features Demonstrated:

- **Composite Transforms**: Bundling multiple transformations into a single, reusable component for cleaner and modular code.
- **Windowing**: Organizing data into time-based windows, enabling temporal analysis.
- **Timestamp Assignment**: Essential for windowed operations, where each data point gets a timestamp.
- **Custom Metrics Calculation**: Using `ParDo` transform for parallel processing and computing custom metrics for each record.
- **Triggers**: Demonstrating advanced triggering mechanisms to control when the results of a windowed PCollection are computed.

## Output Files:

- [`output.txt`](https://drive.google.com/file/d/12VO4WTKYGL_ouvtPKhre4-hoUiSUWxQU/view?usp=drive_link): Contains processed data showcasing the various transformations applied.
- [`output2.txt`](https://drive.google.com/file/d/1Quy1vSwj7oskA8HytPb8w5KtkmCevHjr/view?usp=drive_link): An enriched output that highlights windowed aggregations.

## Notebooks:

- [Apache Beam Comprehensive Data Processing Notebook](https://colab.research.google.com/drive/1BGeG3U0-2R3shsrc797YqEA2BH8BZIhy#scrollTo=X-KbMzI9p19x): A Jupyter notebook that contains all the code, explanations, and visual outputs of the Apache Beam processing pipeline.