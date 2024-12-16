# README



### Project Overview

This repository contains the work completed as part of a group project for the **2024 Applied Machine Learning** course at the University of Edinburgh.



### Description of the Task

Music has become an increasingly important part of people's daily lives. This has led to the emergence of popularity charts for songs and artists on music streaming platforms. Hence, this work aims to figure out which artists or genres are going to be popular in 2024 based on historical data from 2017. The problem is addressed from two distinct perspectives: artists and genres. For artists, the prediction problem is tackled using two independent approaches: time-series forecasting and classification analysis with lagged features capturing time-related information. For genres, clustering methods are applied to identify underlying attributes that contribute to popularity, and proceed to further predict or forecast their popularity using time-series forecasting and classification approaches as well.



### Project Folder Structure

```
.
├── README.md
├── code
│   └──(hidden)
```

```
.
├── data
├── data_preprocessing.ipynb
├── exploratory_data_analysis.ipynb
├── figures
├── requirements.txt
├── task_1_Artist_Popularity
│   ├── 1_classification
│   │   ├── classification.ipynb
│   │   ├── song_to_artist_popularity_demo
│   │   │   ├── artist_popularity_rf_demo.ipynb
│   │   │   └── preprocess.ipynb
│   │   └── statistical_testing.ipynb
│   └── 2_arima_forcast
│       └── arima-airtist forcast.ipynb
└── task_2_Genre_Popularity
    ├── 1_classification
    │   ├── classification.ipynb
    │   ├── data_preprocessing.ipynb
    │   ├── popularity_prediction.ipynb
    │   └── statistical_testing.ipynb
    ├── 2_forecasting
    │   └── forecasting.ipynb
    └── clustering
        └── clustering.ipynb
```



### what software / packages are needed

The following software and Python packages are required for this project: `seaborn` ,  `umap` , `scipy` ,  `statsmodels` , `numpy` ,  `pandas` ,  `matplotlib`, `scikit-learn` ,  `tqdm`, `pmdarima` ,`tensorflow`.

For a detailed list, please refer to the requirements.txt file.



### where the data needs to be put

1. **Location of raw data**: The raw data needs to be manually placed in the `16/code/data` directory.
2. **Task-specific data organization**: Data required for specific tasks (e.g., for `/Users/ming./Desktop/16/code/task_2_Genre_Popularity/2_forecasting/forecasting.ipynb`) has already been organized and placed in the corresponding task directories (e.g., `/Users/ming./Desktop/16/code/task_2_Genre_Popularity/2_forecasting/`).



### how to run the notebooks

1. Place the raw data file (`Spotify_Dataset_V3.csv`) into the `data` directory. 
2. Open and run `data_preprocessing.ipynb` and `exploratory_data_analysis.ipynb`. These notebooks will automatically generate the necessary data for the tasks. 
3. Once the preprocessing is complete, you can proceed to run the notebooks in `task_1_Artist_Popularity` and `task_2_Genre_Popularity`. 
   1. For `task_2_Genre_Popularity`, ensure that the code in the `clustering` notebook is executed first, as subsequent steps depend on its output.
   2. ⁠For ⁠ `1_classification` ⁠ in ⁠` task_2_Genre_Popularity` ⁠, please run ⁠ `data_preprocessing.ipynb` ⁠ before running the other notebooks to prepare the data needed for the subsequent steps.
