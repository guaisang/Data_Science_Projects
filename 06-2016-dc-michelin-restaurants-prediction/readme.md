# Washington D.C. Michelin Star Restaurants Prediction

# Overview

On 10/13/2016, Michelin announced the Michelin star restaurants list of D.C. for the first time. In this project, I tried to collect information of restaurants and predict which restaurants in D.C. would get star based on the Michelin starred restaurants in New York, Chicago and San Fransisco.

---

# Challenges

The main challenges of this project are:

* Study design
* Data Collection

---

# Methodology

### Data Collection Source and Method:

The restaurants in the training dataset are scraped from the following websites:

Chicago: http://www.chicagonow.com/chicago-food-snob/2013/12/chicagos-top-85-restaurants/

NYC: https://www.timeout.com/newyork/en_US/paginate?page_number={}&pageId=35907&folder=&zone_id=1202678

San Fransisco: http://projects.sfchronicle.com/2016/top-100-restaurants/

The restaurants list of DC is scraped from the following websites:
https://www.washingtonian.com/2016/02/08/100-very-best-restaurants/
https://www.washingtonpost.com/news/going-out-guide/wp/2016/10/10/these-are-the-d-c-restaurants-that-insiders-predict-will-get-michelin-stars/

If there are Michelin star restaurants that are not in the list, I added them manually into the list.

See ‘restaurants_scraper.ipynb’ for details.

The next step, I used the scraped list to make requests to Yelp API to get res  information as my features, including price, rating, cuisine category, and review counts. For some restaurants information that cannot be requested from Yelp API, I searched Yelp manually and added to my dataset.

See ‘Yelp_API_requests.ipynb’ for details.

* Question: Why not just scrape restaurants from Yelp?

Answer: Thus I will have too much data, and most of which will be non Michelin starred restaurants. A highly unbalanced dataset may make it harder to train my models. So I need some sort of pre-filtered list.

* Question: Why Yelp?

Answer: There is an empirical work on this problem on fivethirtyeight.com shows that the Yelp data is highly correlated to the Michelin starred restaurants of NYC in 2015:
http://fivethirtyeight.com/features/yelp-and-michelin-have-the-same-taste-in-new-york-restaurants/

I assume that in the other cities in the US, the relationship between Yelp and Michelin star would hold.

* Question: Why not use reviews / text data?

Answer: There is no Michelin official reviews on any DC restaurant yet. If I use Michelin official reviews for my training set and reviews from other professional  for DC restaurants, I will not have consistent features. The Yelp reviews are less reliable since they are not professional food reviews.

### Models:

Four models were built: Random Forest, Gradient Boosting, SVM and Neural Network. Grid search was performed to optimize F1-score. Models were evaluated based on the score on the testing set.

The final prediction was determined by a majority vote: only restaurants that are predicted by at least 3 models are included. The number of star was equal to the highest number predicted by any model.

See ‘models.ipynb’ for details.

### Prediction / Results

10 restaurants are predicted and 5 of them are in the actual Michelin list.

Predicted Resaurants | Predicted Star | Michelin Restaurants | Michelin Star
 --- | --- | --- | ---
Komi | 1 | The Inn at Little Washington | 2
Plume | 1 | Minibar | 2
The Inn at Little Washington | 1 | Pineapple & Pearls | 2
Masseria | 1 | Blue Duck Tavern | 1
Marcel's | 1 | The Dabney | 1
Minibar | 1 | Fiola | 1
Obelisk | 1 | Kinship | 1
Pineapple & Pearls | 1 | Masseria | 1
Metier | 1 | Plume | 1
Kinship | 1 | Rose's Luxury | 1
 | | Sushi Taro | 1
 | | Tail Up Goat | 1
