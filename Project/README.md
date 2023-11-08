# **Hotel Recommendation System**

## **Overview**

This repository contains the work for our CMPE-255 data mining project, where we aim to develop a hotel recommendation system. Our goal is to help users find their ideal hotel based on their preferences and previous user data. We are utilizing the publicly available Expedia dataset, which we will enhance with synthetic data to train our models.

## Problem Statement

The complexity of choosing from countless available hotels makes it challenging for travelers to find the perfect match for their preferences. Expedia has recognized the need for a more personalized hotel recommendation system. Our project addresses this by predicting the likelihood that a user will book a hotel from a specific cluster, based on their search behavior and other relevant attributes.

## Input

Our primary dataset is a subset of Expedia's hotel booking data, which includes:

- Customer search and booking logs
- Click and booking events
- Travel package interactions
- Hotel cluster information based on historical data

We'll also incorporate `destinations.csv`, which contains latent features extracted from hotel review text, to enhance our predictions.

Data Sources:

- [Expedia Hotel Recommendations Dataset](https://www.kaggle.com/competitions/expedia-hotel-recommendations/data)

## Output

Our system will predict the hotel cluster that a user is likely to book, considering their search parameters and other associated attributes. The predictions will be outputted as a ranked list of hotel clusters, accessible via a user-friendly web interface.

## Methodology

We follow the CRISP-DM process, encompassing the phases of Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.

## Artifacts

Our project will produce a comprehensive set of artifacts, each aligning with the CRISP-DM process steps:

- **EDA**: Jupyter notebooks detailing exploratory data analysis.
- **Data Preparation**: Scripts for data cleaning, integration, and feature engineering.
- **Modeling**: Training pipelines, model selection, tuning, and evaluation.
- **Deployment**: Cloud deployment architecture, excluding Colab, with a user interface.

## Deployment and UI

The system will be cloud-deployed, with a simple web UI for real-time user interactions. Details for usage will be provided upon completion.

## MLOps

We will employ MLOps practices to ensure efficient model development, deployment, and maintenance, focusing on versioning, testing, and automation.