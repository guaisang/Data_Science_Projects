# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Choose Your Own Adventure

![](./assets/alpaca.jpg)

### Overview
This week we learned how to use scikit-learn to run logistic regression models and also how to optimize these models. Now we're going to use these skills to dig into a rich set of data!

We're going to be working with a dataset detailing the defaults of credit card owners. You're job is the understand and predict whether someone is going to default based on the available data. You're going to working through the entire data science workflow, including presentation, so get ready!

This project is going to be a "mini" project, in that the scope is a bit different than the typical project. You'll have a choice of methods/options you can use. 

---

### The "Menu Options"

Below is a rough approximation of all of the techniques that we have made this week. You can use any of the following below, it's up to you to determine what is the best path! 

#### Import Your Data

First Things First, import your data and take a good visual look at it. 

#### EDA/Cleaning

* `displot/histogram`
* `dtypes`
* `isnull` 
* `get_dummies`
* `map`
* `labelencoder`

#### Model Prep 

* Regularization
* Standardization
* Feature Scaling
* Feature Engineering (Making new features from existing features)
* Train Test, Split

#### Model 

* Linear Regression
* Logistic Regression
* KNN

#### Optimization 

* GridSearch
* Select K Best
* Recursive Feature Elimination

#### Results

* Classification Report
* Confusion Matrix
* Accuracy Score 
* ROC/AUC 
* Presicion/Recall 
* `Cross_Val_Score`
* Error

---

###  Requirements

Using a provided dataset, predict whether a credit card client will default or not. 

Your work must:
**Identify the problem**
- Write a high quality problem statement
- Describe the goals of your study and criteria for success

**Acquire the data**
- Load in the data

**Explore the data**
- Perform exploratory analysis methods with visualization and statistical analysis
- State the risks and assumptions of your data

**Clean the Data**


**Build a data model**
- Build a model using the method of your choosing. 

**Present the results**
- Create a Jupyter writeup hosted on GitHub that provides a dataset overview with visualizations, statistical analysis, data cleaning methodologies, and models
- Create a slide deck on the interpretation of findings including an executive summary with conclusions and next steps


### Necessary Deliverables / Submission

- Materials must be in a clearly labeled Jupyter notebook
 

---

### Dataset

The datasets utilizes a binary variable, default on payment (Yes = 1, No = 0) in column 24, as the response variable. There are 23 features in this set: 

* 1 Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit. 
* 2 Gender (1 = male; 2 = female). 
* 3 Education (1 = graduate school; 2 = university; 3 = high school; 4 = others). 
* 4 Marital status (1 = married; 2 = single; 3 = others). 
* 5 Age (year). 
* 6 = the repayment status in September, 2005
* 7:11 = the repayment status in August, 2005; . . .;X11 = the repayment status in April, 2005. The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above. 
* 12 = amount of bill statement in September, 2005; 
* 13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005. 
* 18 = amount paid in September, 2005
* 19 = amount paid in August, 2005
* 20 = amount paid in July, 2005
* 21 = amount paid in June, 2005
* 22 = amount paid in May, 2005
* 23 = amount paid in April, 2005


---


**General suggestions:**
- Write pseudocode before you write actual code. Thinking through the logic of something helps.  
- Read the docs for whatever technologies you use. Most of the time, there is a tutorial that you can follow, but not always, and learning to read documentation is crucial to your success!
- Document **everything**.  

---

### Project Feedback + Evaluation

[Attached here is a complete rubric for this project.](./project-03-rubric.md)

Your instructors will score each of your technical requirements using the scale below:

    Score | Expectations
    ----- | ------------
    **0** | _Incomplete._
    **1** | _Does not meet expectations._
    **2** | _Meets expectations, good job!_
    **3** | _Exceeds expectations, you wonderful creature, you!_

 This will serve as a helpful overall gauge of whether you met the project goals, but __the more important scores are the individual ones__ above, which can help you identify where to focus your efforts for the next project!
