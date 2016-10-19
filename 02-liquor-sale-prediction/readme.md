# Iowa Liquor Sales Prediction

### Overview

The state of Iowa provides many data sets on their website, including [this dataset](https://www.dropbox.com/sh/pf5n5sgfgiri3i8/AACkaMeL_i_WgZ00rpxOOcysa?dl=0) which contains transactions for all stores that have a class E liquor license.
This project is to predict sales for liquor stores based on the previous transaction information.

Due to computational expense, I used [this 10% dataset version of Iowa liquor sales](https://drive.google.com/file/d/0Bx2SHQGVqWaseDB4QU9ZSVFDY2M/view?usp=sharing). to build my model.

The dataset includes the following features for every transaction of liquor sales:
* Transaction dataset
* Store number
* City
* Zip Code
* Country Number
* Category
* Category name
* Vender Number
* Item Number
* Item description
* Bottle volume
* State bottle cost
* State bottle retail
* Bottles sold
* Sale(Dollars)
* Volume sold(Gallons)

---

### Challenges

The main challenges of this project are:
* Feature engineering and data transformation
* Handling outliers
* Handling categorical features
* Linear model implementation
---

###  Methodology

In this project, I group transaction data by stores, locations and time period to create features, used EDA (plotting) to identify outliers, create dummy variables to handle categorical features, and implement Lasso regularization with linear regression to handle redundant dummies.
