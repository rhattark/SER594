import numpy as np
import pandas as pd
import re
import string

__author__ = "Rhishabh Suhas Hattarki"
__date__ = "25 September 2023"
__assignment = "SER594: Homework 2 Q4 Programming"


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

    print(f'Fetching data from {url} with class {classname}')
    review_list = []
    r = requests.get(url)

    if r.status_code == 200:
        print('code 200, so far so good')
        soup = BeautifulSoup(r.text, 'html.parser')
        reviews = soup.findAll(class_=classname)

        for review in reviews:
            review_list.append(review.get_text())

    print(f'Fetched data from {url}')
    return review_list


def preprocessing(reviews):
    # Import nltk - only use nltk library to perform all the following processing.
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer

    """
    :param reviews: Reviews list
    :return: Dataframe with processed reviews

    Lower-case all words.
    Remove all punctuations.
    Remove stopwords. (Stopwords are the lists in the nltk library that are trivial and not relevant to the context/text.)
    Perform lemmatization on the data.
    """
    
    print('Initiating preprocessing')
    nltk.download('stopwords')
    nltk.download('wordnet')
    processed = pd.DataFrame()
    processed['review'] = reviews['review'].str.lower()
    processed['review'] = processed['review'].str.replace(f'[{string.punctuation}]','', regex=True)
    stop_words = set(stopwords.words('english'))

    def remove_stopwords(given_str):
        words = given_str.split(' ')
        new_str = []
        for word in words:
            if word not in stop_words and len(word) > 0:
                new_str.append(word)
        return ' '.join(new_str)
    
    processed['review'] = processed['review'].apply(remove_stopwords)
    lemmatizer = WordNetLemmatizer()
    
    def lemmatize(given_str):
        words = given_str.split(' ')
        new_str = []
        for word in words:
            new_str.append(lemmatizer.lemmatize(word))
        return ' '.join(new_str)

    processed['review'] = processed['review'].apply(lemmatize)
    reviews['cleaned_review'] = processed['review']
    
    print('Done preprocessing')
    print(reviews)
    return reviews


if __name__ == '__main__':
    # give your desired urls and classnames, preferably from yelp
    url1, url2 = "https://www.yelp.com/biz/the-peppersauce-cafe-phoenix", "https://www.yelp.com/biz/wtf-burgers-phoenix?osq=Burgers"
    classname1, classname2 = "comment__09f24__D0cxf css-qgunke", "comment__09f24__D0cxf css-qgunke"

    # Part 1
    review_list1 = web_scrapping(url1, classname1)
    review_list2 = web_scrapping(url2, classname2)

    # Create a pandas dataframe from array
    df1 = pd.DataFrame(np.array(review_list1), columns=['review'])
    df2 = pd.DataFrame(np.array(review_list2), columns=['review'])

    # Part 2
    processed_review1 = preprocessing(df1)
    processed_review2 = preprocessing(df2)
