# Data Science Salary Investigation

![](./cloud.png)
- word cloud from job summary

### Overview

In this project, I collected salary information on data science jobs in a variety of markets from [Indeed.com](https://www.indeed.com). Then using the location, title, and summary of the job, I tried to predict a corresponding salary range (lower or higher than median) for that job.

The data I scraped from Indeed includes over 50000 records and following columns:
* company name
* location
* Job Title
* Job summary
* Salary

Most of the records does not have salary information. After dropped records without salary, only 294 records were used to build models.

---

### Challenges

The main challenges of this project are:

* Web scraping
* Data cleaning
* Feature engineering
* Natural language processing
* Small dataset

---

### Methodology

In this project, I made use of BeautifulSoup to scrape data from Indeed, conduct heavy data cleaning and feature engineering to prepare features, used Tableau to create a word cloud of the most common words in job summary, used TfidfVectorizer to process text features, and used random forest to select features.

Random Forest, Gradient Boosting and SVM were built to make prediction. For each model, confusion matrix, classification report and roc curve were used to evaluate model performance.
