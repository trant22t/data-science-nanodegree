# Figure Eight Disaster Response Pipeline 

## Context
Partnering with Udacity, Figure Eight provides us with data sets containing real messages that were sent during disaster events. In this project, you will find an ETL pipeline that processes these data and a machine learning pipeline to categorize these events so that messages can be sent to an appropriate disaster relief agency.  

When it comes to using text in a machine learning model, one of the main challenges is how to represent texts as numerical inputs so that we can feed them into the model. This project experiments with two methodologies to represent text messages, which are TF-IDF and Doc2Vec embedding models.
## Folder structure
```
├── README.md           <- The top-level README for developers using this project.
├── data                <- The original, immutable data dump.
│   ├── categories.csv
│   └── messages.csv
├── main.py             <- The main script to execute for both ETL and ML pipelines in this project.
└── src                 <- Scripts to process data and then validate this process.
    ├── data
    │   ├── process_data.py
    │   └── processed_data_validation.py
    └── models          <- Scripts to train classifiers and create utility functions and custom
        │                  transformers for this process.
        ├── DocumentTransformer.py
        ├── train_classifier.py
        └── utils.py
```

## Instructions
Run the following commands in the project's root directory to set up your database and model.

   - To run ETL pipeline that cleans data and stores in database
        `python main.py process_data data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
   - To run ML pipeline that trains a TF-IDF model whose outputs are fed into a random forest classifier and saves this final model
        `python train_classifier data/DisasterResponse.db tfidf_rf`
   - To run ML pipeline that trains a Doc2Vec model whose outputs are fed into a random forest classifier and saves this final model
        `python train_classifier data/DisasterResponse.db d2v_rf`

## Notes to self / Takeaways
1. **Method chaining and ML pipelines are the "apple of my eye."**  
  
    Originally an R user and a fan of `tidyverse`, I adore method chaining functions due to their readability, their ability to help me write less error-prone codes, and how they relieve the burden of naming variables when it comes to working with the same dataset through multiple steps. Switiching to Python, I realize that `Pandas` does not provide as many "ready-made" methods to use in method chaining as `dplyr` or `margrittr` in R. To make up for that, it supports `Pipe` which enables user-defined methods in method chains. `Pipe` comes in very handy when building ML pipeline, from feature transformation to hyperparameter tuning to model training. Using pipeline helps optimize the entire workflow and especially prevents data leakage (think: cross validation). I've become a fan girl for method chaining, especially all these pipes, all over again.  
  
    That said, I admit that the readable style and convenience of pipes (or method chains in general) come at an expense of harder-to-debug. My workaround right now is to first start with each smaller piece in the pipe and make sure it works before chaining them altogether.     

2. **`great_expectations` data validation tool is a gem.**  
    I have heard repeatedly from software developers that you should write tests for your code. I know I should do it but I have never really done that since I find data science code to involve a fair share of exploration work and tend to have different use cases than software engineering. However, I make it a goal for myself to write unit tests for this project, no matter how simple, but there should be a start. While learning more about this, I came across `great_expectations` that solves the exact problem I'm having - writing tests to validate your data pipeline. `src/data/processed_data_validation.py` is a very simple script that I write to experiment with this tool. Tldr: `great_expectations` has a lot of potential and more people should know about this tool. You can check it out [here](https://github.com/great-expectations/great_expectations).  
    
3. **A large-scale solution for a small-scale problem is an overkill.**  
   When I started this Udacity Data Scientist Nanodegree, my main goals are to practice writing tests for ML models, organizing code structure and developing a mental model for designing an automated system. Essentially, I want to work on my data/software engineering skills given that I come from a pure math background. However, these projects/assignments of this Nanodegree are too small-scope and short-lived that when I attempt to experiment with these areas listed above, my solution becomes an overkill. I realize that to practice large-scale solutions, I should work on a long-term and scalable problem. Hence, another goal for myself :).     