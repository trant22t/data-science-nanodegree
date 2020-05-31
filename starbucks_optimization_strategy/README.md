# Starbucks Optimization Strategy

This folder consists two independent pieces of work related to Starbucks optimization strategies for promotional offers: 
one provides multiple uplift models to determine whether a user should be given a promotion based on Incremental Response 
Rate and Net Incremental Revenue; the other builds a customer segmentation model to determine which demographic groups 
respond best to which offer types. 

## Folder structure
```
├── README.md               
├── customer_segmentation
│   ├── README.md
│   ├── data                    <- Raw data files used for customer segmentation project.
│   │   ├── portfolio.json
│   │   ├── profile.json
│   │   └── transcript.json
│   └── main.ipynb              <- The main notebook that includes source code for exploration and modeling work 
│                                    related to customer segmentation.
└── uplift_models
    ├── README.md
    ├── data                    <- Raw data files used for uplift modeling project.
    │   ├── test.csv
    │   └── training.csv
    └── main.ipynb              <- The main notebook that includes source code for uplift modeling work.

```
## Instructions
To replicate work in the notebook, you can clone this repo and run all cells in `main.ipynb` in each project folder.
Otherise, you can view results from `main.ipynb` whose cells have already been executed.

