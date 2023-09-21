import numpy as np
import pandas as pd

__author__ = "TODO"
__date__ = "TODO"
__assignment = "SER*94: Homework 2 Q4 Programming"


def web_scrapping(url, classname):
    # Import Requests, Beautiful Soup
    import requests
    from bs4 import BeautifulSoup
    
    """
    :param url: URL for web scrapping
    :param classname:  classname string of the element with reviews
    :return: list 

    Request data for the url. 
    Create a soup (parse the html data).
    Manually: go to inspect element on the reviews and check the class of the element.
    Get and return the plain text (preferably in list format).
    """
    # TODO

    # Return the plain text (list)
    return []  # TODO


def preprocessing(reviews):
    # Import nltk - only use nltk library to perform all the following processing.
    import nltk
    """
    :param reviews: Reviews list
    :return: Dataframe with processed reviews

    Lower-case all words.
    Remove all punctuations.
    Remove stopwords. (Stopwords are the lists in the nltk library that are trivial and not relevant to the context/text.)
    Perform lemmatization on the data.
    """
    # TODO

    # Return the dataframe with the processed data
    return None  # TODO


if __name__ == '__main__':
    # give your desired urls and classnames, preferably from yelp
    url1, url2 = "", ""
    classname1, classname2 = "", ""

    # Part 1
    review_list1 = web_scrapping(url1, classname1)
    review_list2 = web_scrapping(url2, classname2)

    # Create a pandas dataframe from array
    df1 = pd.DataFrame(np.array(review_list1), columns=['review'])
    df2 = pd.DataFrame(np.array(review_list2), columns=['review'])

    # Part 2
    processed_review1 = preprocessing(df1)
    processed_review2 = preprocessing(df2)
