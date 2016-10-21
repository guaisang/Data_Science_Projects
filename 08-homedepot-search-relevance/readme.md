# Predict the relevance of search results on homedepot.com

### Overview

This project is from a Kaggle competition: https://www.kaggle.com/c/home-depot-product-search-relevance.

In this project, I was trying to predict how relevant the suggested product is to user search terms based on the product name, description and search terms. The relevance is a number between 1 (not relevant) to 3 (highly relevant).

This is a pure text analysis project. The datasets contain a number of products and real customer search terms from Home Depot's website. Following features are included in the datasets:

* id - a unique Id field which represents a (search_term, product_uid) pair
* product_uid - an id for the products
* product_title - the product title
* product_description - the text description of the product (may contain HTML content)
* search_term - the search query
* relevance - the average of the relevance ratings for a given id

---

### Challenges

The main challenges of this project are:

* Natural language processing
* Dimensional reduction

---

### Methodology

In this project, I utilized TextBlob to lemmatize text, used TfidfVectorizer to tokenize lemmas as features, and built a Bayesian Ridge Regression model to make prediction. I also conduct PCA to reduce feature dimensions. 
