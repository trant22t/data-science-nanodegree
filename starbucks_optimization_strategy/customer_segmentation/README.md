# Customer Segmentation based on Demographics and Promotional Offers' Responses

## Background
The data set used in this challenge contains simulated data that mimics customer behavior on the Starbucks rewards 
mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an 
advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Some users might not 
receive any offer during certain weeks. Not all users receive the same offer, and that is the challenge to solve with 
this data set. 

This data set is a simplified version of the real Starbucks app because the underlying simulator only has one product 
whereas Starbucks actually sells dozens of products. Every offer has a validity period before the offer expires. 
As an example, a BOGO offer might be valid for only 5 days. We'll see in the data set that informational offers have a 
validity period even though these ads are merely providing information about a product; for example, if an informational 
offer has 7 days of validity, we can assume the customer is feeling the influence of the offer for 7 days after receiving 
the advertisement. We'll be given transactional data showing user purchases made on the app including the timestamp of 
purchase and the amount of money spent on a purchase. This transactional data also has a record for each offer that a 
user receives as well as a record for when a user actually views the offer. There are also records for when a user 
completes an offer. Keep in mind as well that someone using the app might make a purchase through the app without having 
received an offer or seen an offer. To give an example, a user could receive a discount offer buy 10 dollars get 2 off 
on Monday. The offer is valid for 10 days from receipt. If the customer accumulates at least 10 dollars in purchases 
during the validity period, the customer completes the offer. 

However, there are a few things to watch out for in this data set. 
- Customers do not opt into the offers that they receive; in other words, a user can receive an offer, never actually 
view the offer, and still complete the offer. For example, a user might receive the buy 10 dollars get 2 dollars off offer, 
but the user never opens the offer during the 10 day validity period. The customer spends 15 dollars during those ten days. 
There will be an offer completion record in the data set; however, the customer was not influenced by the offer because 
the customer never viewed the offer. This makes cleaning especially important and tricky.   
- We'll also want to take into account that some demographic groups will make purchases even if they don't receive an 
offer. From a business perspective, if a customer is going to make a 10 dollar purchase without an offer anyway, 
we wouldn't want to send a buy 10 dollars get 2 dollars off offer. We'll want to try to assess what a certain demographic 
group will buy when not receiving any offers. 

We are free to analyze the data any way we see fit. For example, we could build a machine learning model that predicts 
how much someone will spend based on demographics and offer type. Or we could build a model that predicts whether or 
not someone will respond to an offer. Or, we don't need to build a machine learning model at all. We could develop a 
set of heuristics that determine what offer you should send to each customer (i.e., 75 percent of women customers who 
were 35 years old responded to offer A vs 40 percent from the same demographic to offer B, so send offer A).

## Main task
Combining transaction, demographic and offer data, we build an unsupervised machine learning model 
(**PCA** plus **k-means clustering**) coupled with a lot of **feature engineering** to determine which demographic groups 
respond best to which offer types. 

## Data 
The data is contained in three files:  
    - `portfolio.json` - containing offer ids and meta data about each offer (duration, type, etc.),  
    - `profile.json` - demographic data for each customer,  
    - `transcript.json` - records for transactions, offers received, offers viewed, and offers completed,  

Here is the schema and explanation of each variable in the files:  
   - **portfolio.json**:  
        - id (string) - offer id,  
        - offer_type (string) - type of offer ie BOGO, discount, informational,  
        - difficulty (int) - minimum required spend to complete an offer,  
        - reward (int) - reward given for completing an offer,  
        - duration (int) - time for offer to be open, in days,  
        - channels (list of strings)       
   - **profile.json**:
        - age (int) - age of the customer,  
        - became_member_on (int) - date when customer created an app account,  
        - gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F),  
        - id (str) - customer id,  
        - income (float) - customer's income  
   - **transcript.json**:   
        - event (str) - record description (ie transaction, offer received, offer viewed, etc.),  
        - person (str) - customer id,  
        - time (int) - time in hours since start of test. The data begins at time t=0,  
        - value - (dict of strings) - either an offer id or transaction amount depending on the record  

## Conclusion
After building a k-means clustering model, we are able to identify three main customer segments:
- **The Big Spenders**: They actively engage with BOGO offers and seem to be the most valuable group to Starbucks since they 
spend the highest amount of money and make a good number of transactions. Their gender ratio between male and female is 
almost 1:1. Mean age of these spenders are 56 years old and they earn about 70K/year averagely.  
- **The Discount Lovers**: They are highly responsive to discount offers and tend to make the most number of purchases 
compared with the other two groups. They also spend a decent amount of money on Starbucks over time, despite not being 
the highest. They have a fair distribution of males and females. The average age of customers in the group is 54 and 
average income is about 65K/year.  
- **The Lurkers**: Although they do not participate much in BOGO and discount offers' activities, they tend to keep up-to-date 
with informational messages. However, this group doesn't significantly contribute to Starbucks' revenue since they make 
the fewest number of transactions, spend the least amount of money, and take the longest time between purchases compared 
with the rest. The group is composed of 70% males. Average age of customers in this segment is 51 and average income is 
about 57K/year.
