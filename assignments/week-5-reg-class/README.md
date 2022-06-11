# Electronics Purchase Prediction
Today you are a machine learning engineer in the Department of Marketing and Inventory at Walmart Labs. You have access to the Walmart server data, specifically the Electronics section. However, there is no customer facing information, but you do have access to timestamped data regarding product viewing/carting/purchasing. We will use this data to build a model of whether a not some product will be purchased.

Data is adapted from [e-commerce behavior data on Kaggle](https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store). 

This file contains behavior data from a large multi-category store. Each row in the file rerepresents an event. All events are related to products and users. Each event is like many-many relation between users and products. 

## Learning Objectives
At the end of this session, you will be able to
- Detect data imbalance
- Practice more on preprocessing features
- Build logistic regression / SVM / Gradient Boosting / Random Forest models
- Evaluate models with proper metrics
- Interpret black box models

## Pre-Work
The assignment depends on a few python packages:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `sklearn`
- `shap` (will be used for optional task)

You've encountered the first five packages from previous weeks. Installing `shap` following instructions [here](https://shap.readthedocs.io/en/latest/index.html)

In addition, for task "Analyze importance of data sample balancing using a Random Forest" to render the graph properly, it requires `Graphviz`. Check [Download](https://graphviz.org/download/) for installation information.

For MacOS, you can install these packages using the following command:
```
brew install graphviz # it can take a while
```

