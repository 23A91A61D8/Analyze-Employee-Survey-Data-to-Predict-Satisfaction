\# Employee Satisfaction and Attrition Analysis Report



\## Project Overview



This project analyzes employee satisfaction and attrition patterns using IBM HR Analytics data and employee review text data. The objective was to identify factors affecting employee satisfaction, predict attrition, and provide actionable recommendations for HR leadership.



\## Data Sources



1\. IBM HR Employee Attrition Dataset

2\. Employee Reviews Dataset



\## Data Preparation



\* Removed duplicate records

\* Verified missing values

\* Created Composite Satisfaction Score

\* Processed employee review text for NLP analysis



\## Exploratory Data Analysis



Key findings:



\* Monthly Income strongly correlates with Job Level.

\* Years at Company correlates with Years in Current Role.

\* Attrition varies across departments.



\## Statistical Analysis



\### Chi-Square Test



Department and Attrition showed a statistically significant relationship (p < 0.05).



\### Kruskal-Wallis Test



Monthly income differs significantly across departments (p < 0.05).



\## NLP Analysis



Performed:



\* Text Cleaning

\* Stopword Removal

\* Lemmatization

\* Sentiment Analysis

\* TF-IDF Feature Extraction

\* Word Cloud Visualization



Sentiment Results:



\* Positive Reviews: 4304

\* Negative Reviews: 563

\* Neutral Reviews: 133



\## Machine Learning



\### Logistic Regression



Used to predict satisfaction categories.



\### Random Forest



Used to predict employee attrition.



Accuracy Achieved:



\* Random Forest Accuracy: 86.39%



Important Features:



1\. Monthly Income

2\. Age

3\. Years At Company

4\. Environment Satisfaction

5\. Job Satisfaction



\## Dashboard



Developed an interactive Streamlit dashboard featuring:



\* Employee KPIs

\* Attrition Analysis

\* Satisfaction Analysis

\* Department Filters

\* Correlation Matrix

\* HR Insights



\## Recommendations



1\. Improve compensation strategies for lower-income employees.

2\. Increase employee engagement programs.

3\. Focus on improving work-life balance.

4\. Enhance workplace environment and satisfaction initiatives.

5\. Monitor attrition trends across departments.



\## Conclusion



Employee satisfaction and attrition are strongly influenced by compensation, experience, and workplace satisfaction factors. Data-driven HR interventions can significantly improve employee retention and engagement.



