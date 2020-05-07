# Airbnb Open Data

## Context
Since 2008, guests and hosts have used Airbnb to travel in a more unique, personalized way. As part of the Airbnb Inside initiative, the datasets describe the listing activities of homestays in Seattle, WA and Boston, MA.

This work attempts to explore homestays experience in Boston and Seattle from both the visitors' and hosts' perspectives, from the trends of number of visitors and number of listings over time as well as at specific time of the year, to how the price rates differ between cities and months of the year, to what factors seem to contribute the most to price prediction. We also did some fun exploration around what each city tends to characterize itself. 


## Data
There are 3 datasets that include similar information for each city:

- Listings, including full descriptions and average review score
- Reviews, including unique id for each reviewer and detailed comments
- Calendar, including listing id and the price and availability for that day

You can download data from https://www.kaggle.com/airbnb/seattle/data and https://www.kaggle.com/airbnb/boston.


## Folder structure
```
├── README.md               <- The top-level README for developers using this project.
├── blog.md                 <- Writing summary to communicate insights to non-technical audience.
├── data                    <- Folder that includes original data and miscellaneous images used in analysis.
│   ├── boston
│   │   ├── calendar.csv
│   │   ├── listings.csv
│   │   └── reviews.csv
│   ├── boston_map_outline.jpg
│   ├── seattle
│   │   ├── calendar.csv
│   │   ├── listings.csv
│   │   └── reviews.csv
│   └── seattle_map_outline.jpg
├── main.ipynb              <- The main notebook that includes source code for exploration and modeling work.
├── outputs                 <- Folder that includes figures from analysis
│   ├── bos_loc_wordcloud.png
│   ├── bos_neigh_wordcloud.png
│   ├── count_booked_listings.png
│   ├── num_visitors_by_month.png
│   ├── num_visitors_over_time.png
│   ├── price_over_time.png
│   ├── prop_booked_listings.png
│   ├── rf_feat_imp.png
│   ├── sea_loc_wordcloud.png
│   ├── sea_neigh_wordcloud.png
│   ├── tree.dot
│   └── tree.png
└── requirements.txt        <- Text file that lists libraries required to run notebook.
```

## Usage
To replicate work in the notebook:
1. Clone this repo
2. `brew install graphviz` (graphviz is the only used library that needs to be installed via `brew`; for the rest of the libraries in `requirements.txt`, you can install with `pip`)
3. Run all cells in `main.ipynb`

Otherise, you can view results from `main.ipynb` whose cells have already been executed.  


## Conclusion from analysis
1. There has been a general increase in travel demand to both Boston and Seattle over time. Both cities are especially busy around the summer and Seattle seems to welcome a larger number of travellers to the city each month, compared with Boston. 
2. Rental activity appears to be a long-term business for most hosts in the dataset. Neighborhood description of each listing tends to share similar qualities, i.e. advertising about the vicinity of key sightseeing spots and lively areas with coffee shops and restaurants. 
3. Boston appears to be pricier than Seattle and some main contributors for price prediction are number of bedrooms, number of bathrooms, property type and how reliable a host is in terms of number of reviews and number of associated listings.







