# Analysis of the Supply, Demand and Prices for Airbnb Listings


## Introduction
Since 2008, guests and hosts have used Airbnb to travel in a more unique, personalized way. As part of the Airbnb Inside initiative, the datasets describe the listing activities of homestays in Seattle, WA and Boston, MA.

This work attempts to explore homestays experience in Boston and Seattle from both the visitors' and hosts' perspectives, from the trends of number of visitors and number of listings over time as well as at specific time of the year, to how the price rates differ between cities and months of the year, to what factors seem to contribute the most to price prediction. We also did some fun exploration around what each city tends to characterize itself. 


## Part 1: Travel demand to Boston and Seattle

### 1) What are the busiest times of the year to visit each city? What city among the two seem to be more popular?

Using number of unique reviewers as a proxy for number of visitors, we want to compare travel demand between cities (Boston vs Seattle) at different points in time. We understand this might be an underestimation since not all travelers write Airbnb reviews and not all travellers choose Airbnb for their homestay accommodation, but this is the closest estimation we could get based on the data we have access to. That said, given the growing presence of Airbnb among hosts and travellers and how the site incentivizes guests to write reviews, this estimation still provides solid insights and is helpful to visitors. 

<p align="center">
  <img src="/outputs/num_visitors_by_month.png">
</p>

Number of unique visitors in both Boston and Seattle follows a unimodal distribution. Boston is popular to travellers during the summer months from May to August, with the peak in August. Seattle is also busy around the same time, from June to September, with the highest demand in August. This follows our intuition since summer months allow just about any vaction activities without weather-based interruptions in both cities. In general, Seattle is more popular than Boston in terms of number of visitors around the year, except for the month of April and May. This is also expected because Seattle offers a warmer weather all year round whereas Boston could be bitterly cold in the winter. In April and May, however, Boston features spring-like weather that is less humid and drier than Seattle, which might explain the difference in travel demand. 

### 2) Is there a general upward trend of number of visitors over time?

<p align="center">
  <img src="outputs/num_visitors_over_time.png">
</p>

From 2009 to 2016, there is a general upward trend of number of visitors in both cities, given some seasonal variations. The figure also aligns with Q1 which indicates that Seattle is more popular than Boston as a travel destination. 


## Part 2: Homestay accommodation supply 

### 1) What is the general trend of number of listings over time?

In the dataset, we only have 1 year of listings data from 2016 to 2017 and the number of distinct listings in both cities stays consistent, specifically, 3585 for Boston and 3818 for Seattle. This means to most of the hosts appearing in this dataset, rental activity is their long-term business, at least for a year. 

### 2) Does the number of booked listings align with travel demands found in Part 1?

Out of all the listed properties, we examine the monthly number of booked ones, both in terms of absolute count and proportion, to see if this trend aligns with the travel demand insight we extracted from Part 1.

<p align="center">
  <img src="outputs/count_booked_listings.png">
</p>

<p align="center">
  <img src="outputs/prop_booked_listings.png">
</p>

Based on the count number of booked listings, Boston seems to do better than Seattle, especially in the fall and early winter months. Except for January and February, where Seattle has the spike in unavailable listings, the hub city of Massachusetts is consistently more popular in terms of number of bookings for the rest of the year. Given that the number of lisitings is not exactly the same between two cities, we also look at the proportion of this metric. On average, 50% and 36% of listings are booked on a monthly basis in Boston and Seattle, respectively. And the trend in proportion of bookings is similar to when we use absolute count.  

There are multiple reasons which might explain the difference of trend in number of booked listings and number of visitors between two cities (i.e. between this question and Part 1 Q1). A notable one is that a listing can have different number of bedrooms and can accommodate different number of visitors. Thus, the number of booked listings is not directly related to number of visitors to the city. 

### 3) What is the vibe of each city based on neighborhood description?

To get a sense of the vibe of each city, we look into how hosts in each city tend to describe the neighborhood around their listings. 

<p align="center">
  <img src="outputs/bos_neigh_wordcloud.png">
</p>

<p align="center">
  <img src="outputs/sea_neigh_wordcloud.png">
</p>

We see that most of these listings are advertised to be around key sightseeing areas of each city, for example: Public Garden, Back Bay and Beacon Hill of Boston or Capitol Hill and Queen Anne of Seattle. Walkability, public transportation, coffee shops and restaurants are also talked about frequently in these descriptions for both cities.


## Part 3: Pricing

### 1) How different is the price rate between two cities at different time points in the year?

<p align="center">
  <img src="outputs/price_over_time.png">
</p>

Average price rate of available listings in Boston is consistently higher than that in Seattle all year round. On average, the mean listing price in Boston is around $200. In the fall, from September to December, you can expect this rate to be over $200. On the other hand, the mean listing price in Seattle is about $138. This rate is pretty stable throughout the year with just a slight increase in summer months.  

### 2) What listing properties might contribute to price prediction? 

We are interested in what listing properties could help us predict price of these accommodations. Thus, we build a simple random forest model. We choose this model since random forest is easy to explain, intuitive and still guarantees a decent performance. Note that this predictive question alone can stand as its own project, however, given that we include it as just a part of a supply/demand analysis, we did not go through the process of hyperparameter tuning or model selection.

Despite that, this model provides an R-squared score of 0.859 on the test set, which means 85.9 percent of the variation in the price could be explained by this model. Since the model performs well, it is meaningful for us to take a look at the feature importance as well as a visualization of a single tree in the forest.

Below are the 10 most important features suggested by random forest. Number of bedrooms, number of bathrooms, whether the listing is an entire apartment or not, month of the year, location, number of reviews per month are some factors that contribute the most to the price.    

<p align="center">
  <img src="outputs/rf_feat_imp.png">
</p>

A visualization of one tree in the forest could help us get an idea of the decision path the model makes. In the first three levels of the tree, we can see that listings with fewer than 1.5 bedrooms tend to be cheaper, then the price is further reduced if the room is not an entire home, and etc. 

<p align="center">
  <img src="outputs/tree.png">
</p>


## Conclusion
In this analysis, we explore homestays experience in Boston and Seattle from both the visitors' and hosts' perspectives and draw some inference about the prices between cities. 

1. There has been a general increase in travel demand to both Boston and Seattle over time. Both cities are especially busy around the summer and Seattle seems to welcome a larger number of travellers to the city each month, compared with Boston. 
2. Rental activity appears to be a long-term business for most hosts in the dataset. Neighborhood description of each listing tends to share similar qualities, i.e. advertising about the vicinity of key sightseeing spots and lively areas with coffee shops and restaurants. 
3. Boston appears to be pricier than Seattle and some main contributors are number of bedrooms, number of bathrooms, property type and how reliable a host is in terms of number of reviews and number of associated listings.