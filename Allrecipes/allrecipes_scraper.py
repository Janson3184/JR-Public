import time
import pandas as pd
import re
from concurrent import futures
import requests
from selenium import webdriver
import numpy as np

import urllib.request

'''
br = webdriver.Firefox() #open firefox
br.get('https://www.allrecipes.com/recipe/271046/') #'https://www.allrecipes.com/recipe/271046/'
'''
page = 'https://www.allrecipes.com/recipe/000000'

# Lovingly stolen from https://stackoverflow.com/questions/14329381/regular-expression-to-get-quantity-and-names-of-ingredients
pattern = '/(([0-9][\s+]*[\-]*[0-9]*[\s+]*)(teaspoon|tablespoons|cup|cups)*)([a-z0-9\s]+)/'


def check_page_error(page):
    '''This is a MUCH faster way to check for valid pages that doesn't require a webdriver.'''

    try:
        fp = urllib.request.urlopen(page)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        title = mystr.split('<title>')[1].split('</title>')[0]

        fp.close()
        return page, title

    except:
        return 'Invalid Page.'





def get_urls_from_generic_search(generic_search):
    pass


def get_ingredients(br):
    try:
        if br.find_element_by_class_name("error-page__404"):
            return [None]
    except:

        ingred = br.find_elements_by_class_name("checkList__item")

        #Go through all ingredients and collect text
        ingredients = []

        for x in np.arange(len(ingred)-1):
            ingredients.append(str(ingred[x].text))
            #.encode('ascii', 'ignore')

        return ingredients

#for ingredient in get_ingredients(br):
#    print(ingredient)

for i in range(100000,100999):
    output = check_page_error('https://www.allrecipes.com/recipe/' + str(i))
    if output == 'Invalid Page.':
        pass
    else:
        print(output)

'''
def main(generic_search):
    recipe_urls = get_urls_from_generic_search(generic_search)
    
    recipe_ingredients = pd.DataFrame()
    
    # with concurrent...
    for url in recipe_urls:
        recipe_ingredients.append(get_recipe_ingredients(url))
    
    recipe_ingredients.to_csv('allrecipes.csv')



if __name__ == '__main__':
    main()

################    Test  ###################




def get_wall_street_journal(site):
    try:
        r = requests.get(site)
        dfs = pd.read_html(r.content)
        number_buys = dfs[8].loc[0,'Current']
        consensus = dfs[8].loc[5, 'Current']
        print(number_buys, consensus, site)
        print(total_stocks)
        total_stocks -= 1
        return number_buys, consensus, site
    except:
        total_stocks -= 1
        return "None", "None", site


with futures.ThreadPoolExecutor() as executor:

    the_street_results = executor.map(get_the_street, tickers_dataframe['thestreet_URL'])
    the_street_results = pd.DataFrame(the_street_results)
    the_street_results.columns = ['street_consensus', 'street_rating', 'thestreet_URL']
    the_street_results.to_csv('TheStreet.csv')
'''


