# Subscription Prediction with PySpark and MLlib
During this session, from data collected from direct marketing campaigns of a Portuguese banking institution, you will build a logistic regression model to predict whether a client will subscribe to a term deposit using [PySpark](https://databricks.com/glossary/pyspark) and [MLlib](https://spark.apache.org/docs/latest/ml-guide.html).

## Learning Objectives
At the end of this session, you will be able to 

- Explore data with Spark DataFrames 
- Build a pipeline in MLlib for machine learning workflow
- Fit a logistic regression model, make predictions, and evaluate the model

## Pre-Work
### Option I: Databricks Community Edition
Sign up Databricks Community Edition following [official documentation](https://docs.databricks.com/getting-started/community-edition.html). Make sure you follow through ALL six steps. 

For a video demo how to set up Databricks Community Edition, [watch this short video](https://www.youtube.com/watch?v=x3n0bixfP_4&feature=youtu.be&ab_channel=FourthBrainAI). 

Note: It is NOT the same as Free Trial. Free trial lasts 14 days and Databricks uses compute and S3 storage resources in your own AWS account ( or Azura / GCP ).

### Option II: Google CoLab
If the first option takes too long, one alternative is to use Google CoLab. Following this [Medium article](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c) to the section **Get coding**. 

Test it by running this [notebook](https://colab.research.google.com/drive/1u6gYTJ_5dZOudWpkQNXmpk9xdbyoNPbG?usp=sharing) in Google Colab.


(This notebook is taken from this [tutorial](https://colab.research.google.com/github/asifahmed90/pyspark-ML-in-Colab/blob/master/PySpark_Regression_Analysis.ipynb#scrollTo=lh5NCoc8fsSO). Please don't use the notebook mentioned in the tutorial as spark version used is outdated.)


For the live session, upload the notebooks under nb folder to your Google Drive, make sure you install `Colaboratory` Add-ons, open the notebook with `Google Colaboratory`, and you are ready to go. Check if all dependencies are met by running the imports.ipynb notebook.


### Option III: Locally
If you are up for a challenge, to run the notebook locally, follow instructions: 
 
- MacOS [(Reference)](https://sparkbyexamples.com/pyspark/how-to-install-pyspark-on-mac/). Spark was written in Scala, but for our purpose (i.e., run `PySpark`), you can skip Scala installation. 

    The following has been tested on macOS Monterey 12.0.1 with M1 chip:
    ```
    # Install OpenJDK 11 (java)
    brew install openjdk@11

    # Install Apache Spark
    brew install apache-spark

    # Activate environment
    conda activate py39_12
    pip install pyspark 
    ```

    If `which pip` is not pointing to your env, then find the path to the correct env, and run the following to finish the installation.
    ```
    /usr/local/Caskroom/miniforge/base/envs/py39_12/bin/python -m pip install pyspark 
    ```

    To verify that you have installed `pyspark`, run notebook [imports](nb/imports.ipynb) and make sure no error messages are displayed when importing the packages. 


- Windows [Reference](https://sparkbyexamples.com/pyspark/how-to-install-and-run-pyspark-on-windows/). 
