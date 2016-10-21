# West Nile Virus Spread Prediction
![demo](spread.gif)
made with Tableau

### Overview

This project is from a Kaggle competition: https://www.kaggle.com/c/predict-west-nile-virus.

West Nile virus is most commonly spread to humans through infected mosquitos. Around 20% of people who become infected with the virus develop symptoms ranging from a persistent fever, to serious neurological illnesses that can result in death.

In 2002, the first human cases of West Nile virus were reported in Chicago. By 2004 the City of Chicago and the Chicago Department of Public Health (CDPH) had established a comprehensive surveillance and control program that is still in effect today.

Every week from late spring through the fall, mosquitos in traps across the city are tested for the virus. The results of these tests influence when and where the city will spray airborne pesticides to control adult mosquito populations.

Given weather, location, testing, and spraying data, I tried to predict when and where different species of mosquitos will test positive for West Nile virus.

There are four datasets used in this project: the train.csv dataset includes the test records 2007, 2009, 2011, and 2013. The weather.csv datset includes weather data from 2007 to 2014 of Chicago. The Spray dataset includes GIS data of spraying efforts in 2011 and 2013. The test dataset is used to make prediction and submit to Kaggle for score.

This is also a class group competition, which we won with an auc score of 0.71.

### Challenges

The main challenges of this project are:

* Highly unbalanced data
* Data cleaning
* Feature engineering and data transformation
* Model optimization

### Methodology

In this project, I conduct feature engineering and data transformation to utilize all of the available datasets to create useful features, built KNN, random forest, boosting, SVM, Naive Bayes, and neural network to make prediction. Grid search was used to optimize roc-auc score. Confusion matrix and roc curve were used to evaluate models.

The neural network I built generated the highest auc score on test set. 
