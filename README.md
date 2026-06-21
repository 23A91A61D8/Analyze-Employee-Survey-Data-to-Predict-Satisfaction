# Analyze-Employee-Survey-Data-to-Predict-Satisfaction



 Project Overview



This project analyzes employee satisfaction, engagement, and attrition using HR survey data and employee review text data. The objective is to identify key drivers of employee satisfaction, uncover patterns related to attrition, and provide actionable recommendations for HR leadership.



The project combines data cleaning, exploratory data analysis, statistical hypothesis testing, natural language processing (NLP), machine learning, and interactive dashboard development.



\---



\## Objectives



\* Analyze employee satisfaction factors.

\* Identify relationships between employee demographics and attrition.

\* Perform statistical hypothesis testing.

\* Apply NLP techniques to employee reviews.

\* Build predictive models for employee satisfaction and attrition.

\* Develop an interactive dashboard for HR analytics.

\* Provide business recommendations to improve employee engagement and retention.



\---



\## Dataset Information



\### 1. IBM HR Employee Attrition Dataset



Contains employee demographic information, job-related attributes, satisfaction scores, and attrition status.



\### 2. Employee Reviews Dataset



Contains employee review comments used for NLP analysis, sentiment analysis, TF-IDF feature extraction, and word cloud generation.



\---



\## Project Workflow



\### Data Preparation



\* Loaded employee survey dataset.

\* Checked for missing values.

\* Removed duplicate records.

\* Created a Composite Satisfaction Score.

\* Saved cleaned datasets for further analysis.



\### Exploratory Data Analysis



Performed:



\* Summary statistics

\* Distribution analysis

\* Correlation analysis

\* Attrition analysis

\* Monthly income analysis

\* Satisfaction analysis



\### Statistical Analysis



\#### Chi-Square Test



Used to determine whether attrition is associated with employee departments.



\*\*Result:\*\* Significant relationship found between department and attrition.



\#### Kruskal-Wallis Test



Used to compare monthly income distributions across departments.



\*\*Result:\*\* Significant differences found among departments.



\---



\## Natural Language Processing (NLP)



The following NLP techniques were applied:



\* Text Cleaning

\* Tokenization

\* Stopword Removal

\* Lemmatization

\* Sentiment Analysis

\* TF-IDF Feature Extraction

\* Word Cloud Generation



\### Sentiment Analysis Results



| Sentiment | Count |

| --------- | ----- |

| Positive  | 4304  |

| Negative  | 563   |

| Neutral   | 133   |



\---



\## Machine Learning Models



\### Logistic Regression



Used to classify employee satisfaction categories.



\### Random Forest Classifier



Used to predict employee attrition.



\### Model Performance



\*\*Random Forest Accuracy:\*\* 86.39%



\### Important Features



The most influential features affecting employee attrition were:



1\. Monthly Income

2\. Age

3\. Years At Company

4\. Environment Satisfaction

5\. Job Satisfaction

6\. Relationship Satisfaction

7\. Job Involvement

8\. Work-Life Balance

9\. Job Level



\---



\## Interactive Dashboard



A Streamlit dashboard was developed to visualize:



\* Employee KPIs

\* Attrition Analysis

\* Department-wise Analysis

\* Work-Life Balance Analysis

\* Monthly Income Analysis

\* Correlation Matrix

\* HR Insights



\### Dashboard Features



\* Department Filter

\* Job Role Filter

\* Gender Filter

\* Interactive Charts

\* KPI Cards

\* Real-Time Filtering



\---



\## Technologies Used



\* Python

\* Pandas

\* NumPy

\* Matplotlib

\* Seaborn

\* Plotly

\* Scikit-Learn

\* SciPy

\* NLTK

\* Streamlit

\* WordCloud

\* Jupyter Notebook



\---



\## Project Structure



```text

Analyze Employee Survey Data to Predict Satisfaction/



├── data/

│   ├── WA\_Fn-UseC\_-HR-Employee-Attrition.csv

│   ├── clean\_employee\_data.csv

│   ├── employee\_satisfaction\_processed.csv

│   └── all\_reviews.csv

│

├── dashboard/

│   └── app.py

│

├── notebooks/

│   └── employee\_satisfaction\_analysis.ipynb

│

├── report/

│   └── final\_report.md

│

├── README.md

├── requirements.txt

└── .gitignore

```



\---



\## Installation



\### Clone Repository



```bash

git clone <repository-url>

cd Analyze-Employee-Survey-Data-to-Predict-Satisfaction

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Run Dashboard



```bash

streamlit run dashboard/app.py

```



\---



\## Key Findings



\* Monthly Income is the strongest predictor of employee attrition.

\* Employee satisfaction is strongly influenced by work-life balance and workplace environment.

\* Attrition rates vary significantly across departments.

\* Positive employee sentiment dominates review data.

\* Long-term employee retention is associated with higher satisfaction levels.



\---



\## Recommendations



1\. Improve compensation strategies for lower-income employees.

2\. Enhance employee engagement programs.

3\. Promote better work-life balance initiatives.

4\. Improve workplace environment and management support.

5\. Monitor attrition trends using data-driven HR strategies.



\---



\## Conclusion



This project demonstrates how statistical analysis, NLP, machine learning, and interactive visualization can be combined to generate actionable HR insights. The results provide valuable guidance for improving employee satisfaction, reducing attrition, and supporting organizational decision-making.



