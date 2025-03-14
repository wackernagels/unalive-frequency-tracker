# unalive-frequency-tracker

A project tracking usage and mentions of 'unalive' and other killing-related words on r/offmychest, from 2019-2024!

# Usage Instructions

## Required Packages
* Selenium ([documentation](https://www.selenium.dev/documentation/))
* Pandas ([documentation](https://pandas.pydata.org/docs/))
* NumPy ([documentation](https://numpy.org/doc/stable/))
* Plotly ([documentation](https://plotly.com/python/))
*    Note that Plotly documentation will also talk about Dash. This project did NOT use Dash, and the time slider feature on the posts visualization is NOT supported on Dash!

## Webscraping
All of our webscraping scripts will be in the scraping-scripts directory. We have one Jupyter Notebook script for each of 'unalive', 'kill', 'murder', and 'suicide', and each of these will generate a CSV file with post metadata from December 31 2018 to January 1 2025.

## Preprocessing
This happens in the data-preprocess.ipynb file! It will remove, clean and reorganize our data into a more accessible format. You will need to have the raw data first for the script to work.

## Graphing
This happens in vis.py. Make sure you have the processed data, then run the script to see the visual!

# Documentation
## Data 
All of our data was scraped from the [PullPush Reddit API](https://pullpush.io/). The scraping process is mostly documented in 'data collection unalive.ipynb' (the other scraping scripts are copies of this script, adjusted for the load of the other words). Since we are looking at every post mentioning killing-related words from 2019-2024 we need to, well, find every post!
The data cleaning and preprocessing is described in data-preprocess.ipynb. Basically, we want to take our raw data and organize all of the text within these posts by keyword and date. This makes it a lot easier to look up (and graph).

## Our Visualization

## Limitations

# FAQs
### I'm just here for the graph. What do I do?
* Pull the repository and download the cleaned dataset from below. Then run vis.py!

### Where are the datasets?
* The datasets are too big for GitHub! You can access them here: [https://drive.google.com/drive/folders/1x9BlMWjyv8oDJ-HwZ9wzPe9eCyeId_vY?usp=sharing](https://drive.google.com/drive/folders/1x9BlMWjyv8oDJ-HwZ9wzPe9eCyeId_vY?usp=sharing)
*   data: containing the raw data for each word
*   cleaned_data: the data post-processing

### Why are you doing this?
* Prototyping and getting practice in for a bigger project!

### My IP address got blocked! What now?
* Find a proxy! I accessed mine from here: [https://free-proxy-list.net/](https://free-proxy-list.net/)

### How long will it take to scrape/preprocess the data?
* Each word may take up to eight hours to scrape. The preprocessing may take up to 12 hours! If you have access to multiple computers I would recommend running these scripts on a machine you don't often use.

### Can I use this code for other words/subreddits/etc?
* Yes! You can find instructions on querying with the PullPush Reddit API on their website: [https://pullpush.io/](https://pullpush.io/)

### Can I use this code for different websites?
* Yes! Be aware however that different websites have different HTML structures, so the scraping logic will need to be rewritten if you choose to use a different website!
