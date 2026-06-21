# Employee Satisfaction and Attrition Analysis Report

## Executive Summary

This project analyzes employee satisfaction and attrition patterns using IBM HR Analytics data and employee review text data. The primary objective was to identify key factors influencing employee satisfaction, predict employee attrition, and provide data-driven recommendations to improve workforce engagement and retention.

The analysis combines statistical techniques, natural language processing (NLP), machine learning models, and interactive dashboard visualizations to support HR decision-making.

---

## Project Objectives

* Analyze employee satisfaction factors.
* Identify relationships between employee demographics and attrition.
* Perform statistical hypothesis testing.
* Apply NLP techniques to employee reviews.
* Develop predictive machine learning models.
* Create an interactive HR analytics dashboard.
* Generate actionable recommendations for HR leadership.

---

## Data Sources

### 1. IBM HR Employee Attrition Dataset

Contains employee demographic information, job-related attributes, satisfaction scores, and attrition status.

### 2. Employee Reviews Dataset

Contains employee review comments used for sentiment analysis and text mining.

---

## Data Preparation

The following preprocessing steps were performed:

* Verified missing values across all columns.
* Removed duplicate records.
* Examined data types and distributions.
* Created a Composite Satisfaction Score using:

  * Job Satisfaction
  * Environment Satisfaction
  * Relationship Satisfaction
  * Work-Life Balance
* Prepared processed datasets for analysis and modeling.

---

## Exploratory Data Analysis (EDA)

Exploratory analysis revealed several important trends:

### Key Findings

* Monthly Income shows a strong relationship with Job Level.
* Employees with higher experience tend to have higher salaries.
* Years at Company strongly correlates with Years in Current Role.
* Satisfaction-related variables exhibit moderate positive relationships.
* Attrition patterns vary across departments and employee groups.

---

## Statistical Analysis

### Chi-Square Test

**Objective:** Determine whether employee attrition is associated with department membership.

**Result:**

* Chi-Square Statistic: 10.796
* P-Value: 0.0045

**Interpretation:**

Since the p-value is less than 0.05, a statistically significant relationship exists between department and employee attrition.

---

### Kruskal-Wallis Test

**Objective:** Compare satisfaction levels across employee groups.

**Result:**

* Test Statistic: 42.619
* P-Value: 5.56e-10

**Interpretation:**

Significant differences exist among employee groups regarding satisfaction levels.

---

## Natural Language Processing (NLP)

Employee review text data was analyzed using several NLP techniques.

### NLP Pipeline

* Text Cleaning
* Lowercasing
* Stopword Removal
* Lemmatization
* Sentiment Analysis
* TF-IDF Feature Extraction
* Word Cloud Generation

### Sentiment Analysis Results

| Sentiment | Count |
| --------- | ----: |
| Positive  |  4304 |
| Negative  |   563 |
| Neutral   |   133 |

### Key Review Themes

Frequently occurring employee review themes included:

* Work Environment
* Management
* Salary
* Benefits
* Team Collaboration
* Work-Life Balance
* Career Growth Opportunities

Overall employee sentiment was predominantly positive.

---

## Machine Learning Models

### Logistic Regression

Used to classify employee satisfaction categories.

### Random Forest Classifier

Used to predict employee attrition.

### Model Performance

| Metric   | Value  |
| -------- | ------ |
| Accuracy | 86.39% |

### Important Features

The most influential variables affecting employee attrition were:

1. Monthly Income
2. Age
3. Years At Company
4. Environment Satisfaction
5. Job Satisfaction
6. Relationship Satisfaction
7. Job Involvement
8. Work-Life Balance
9. Job Level

---

## Interactive Dashboard

A Streamlit dashboard was developed to support interactive exploration of employee data.

### Dashboard Features

* KPI Cards
* Attrition Analysis
* Satisfaction Analysis
* Department-wise Analysis
* Work-Life Balance Analysis
* Monthly Income Analysis
* Correlation Matrix
* HR Insights
* Interactive Filters

### Available Filters

* Department
* Job Role
* Gender

The dashboard enables HR teams to explore employee trends in real time.

---

## Business Recommendations

Based on the analysis, the following recommendations are proposed:

### 1. Improve Compensation Strategies

Monthly income emerged as the strongest predictor of employee attrition. Compensation structures should be reviewed to improve retention.

### 2. Strengthen Employee Engagement Programs

Implement initiatives that promote employee recognition, career development, and professional growth.

### 3. Improve Work-Life Balance

Encourage flexible work arrangements and wellness programs to enhance employee satisfaction.

### 4. Enhance Workplace Environment

Focus on leadership quality, communication, and employee-manager relationships.

### 5. Monitor Attrition Trends Continuously

Utilize HR dashboards and predictive analytics to proactively identify retention risks.

---

## Conclusion

This project demonstrates how statistical analysis, natural language processing, machine learning, and interactive visualization can be combined to generate meaningful HR insights.

The findings indicate that compensation, workplace satisfaction, and employee experience are major contributors to employee retention and engagement.

By leveraging data-driven HR strategies, organizations can improve employee satisfaction, reduce attrition, and support long-term organizational success.
