# Uplift Modeling 
 
## Background
The data for this exercise consists of about 120,000 data points split in a 2:1 ratio among training and test files. 
In the experiment simulated by the data, an advertising promotion was tested to see if it would bring more customers to 
purchase a specific product priced at $10. Since it costs the company 0.15 to send out each promotion, it would be best 
to limit that promotion only to those that are most receptive to the promotion. Each data point includes one column 
indicating whether or not an individual was sent a promotion for the product, and one column indicating whether or not 
that individual eventually purchased that product. Each individual also has seven additional features associated with 
them, which are provided abstractly as V1-V7.

Our task is to use the training data to understand what patterns in V1-V7 to indicate that a promotion should be 
provided to a user. Specifically, our goal is to maximize the following metrics:

- **Incremental Response Rate (IRR)**:   
IRR depicts how many more customers purchased the product with the promotion, as compared to if they didn't receive the 
promotion. Mathematically, it's the ratio of the number of purchasers in the promotion group to the total number of 
customers in the purchasers group (_treatment_) minus the ratio of the number of purchasers in the non-promotional group 
to the total number of customers in the non-promotional group (_control_). 
<img src="https://render.githubusercontent.com/render/math?math=IRR = \frac{purch_{treat}}{cust_{treat}} - \frac{purch_{ctrl}}{cust_{ctrl}}">

- **Net Incremental Revenue (NIR)**:  
NIR depicts how much is made (or lost) by sending out the promotion. Mathematically, this is 10 times the total number 
of purchasers that received the promotion minus 0.15 times the number of promotions sent out, minus 10 times the number 
of purchasers who were not given the promotion. 
<img src="https://render.githubusercontent.com/render/math?math=NIR = (10\cdot purch_{treat} - 0.15 \cdot cust_{treat}) - 10 \cdot purch_{ctrl}">

For a full description of what Starbucks provides to candidates see the [instructions available here](https://drive.google.com/open?id=18klca9Sef1Rs6q8DW4l7o349r8B70qXM).

## Approaches
- **Two-model approach**: This approach consists building two seperate models for treatment and control groups. 
These models tell us the likelihood of a customer to purchase when they receive the promotion offers and when they don't, 
respectively. After these two classifiers are constructed, we score all customers using both models. Thus, each customer 
now has two probabilities and the difference between these two is the uplift score.   
- **Class transformation approach**: This approach includes creating a new target variable which corresponds to the 
group of customers who will buy if receive promotions. Specifically, the new response variable is equal to one if the 
customer belongs to the treatment group and they do purchase. In all other cases, the target takes on value zero. 
Our problem could then be solved with a standard binary classification model. We'll want to send promotions to customers 
whose target is one in this case.  
- **Treatment indicator variable approach**: In order to incorporate the information of whether one receives promotion or 
not while building one single model, we use the treatment column itself as a predictor in our classifier in addition 
to other features. Then, to predict whether a new individual is likely to respond favorably to the promotions, we set this 
treatment dummy indicator to be both 0 and 1. Specifically, for each unseen customer, we apply the trained model on the 
observation assuming they are in the treatment group (i.e. treatment dummy = 1) to predict the probability of purchase 
when receiving promotion and apply the model again, but this time, assuming they are in the control group 
(i.e. treatment dummy = 0) to predict the probability of purchase when not receiving promotion. The difference between 
these two probabilities is the lift value for the particular customer. In this exercise, we decide to send promotions to 
those whose lift value is positive. 

## Conclusion
| MODEL                                  | IRR    | NIR      |
|----------------------------------------|--------|----------|
| Current assignment (treatment column)  | 0.0096 | -1132.20 |
| Starbucks benchmark                    | 0.0188 | 189.45   |
| Two-model approach                     | 0.0091 | -496.15  |
| Class transformation approach          | 0.0198 | 416.20   |
| Treatment indicator approach           | 0.0124 | -444.54  |

Based on the result on the test set, class transformation is the best approach which is able to outperform the 
Starbucks benchmark. Furthermore, the model achieves this performance while using only two out of the originally 
given seven features.



