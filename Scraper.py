# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from csv import writer
import json
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize an empty list to store the records
records = []

# Define a function to filter HTML tags
def tag_filter(tag):
    # Return True if the tag name is 'h3' or 'p' and its class starts with 'offer-price'
    return (tag.name in ['h3', 'p']) and (tag.get('class', [None])[0] or '').startswith('offer-price')

# Define another function to filter HTML tags
def tag_filter2(tag):
    # Return True if the tag name is 'p' and its text contains 'ID'
    return tag.name == 'p' and 'ID' in tag.get_text()


# acces LINKS from dotenv
LINK1 = os.getenv("LINK1")
LINK2 = os.getenv("LINK2")
# Loop over a range of numbers
for i in range(1, 10):
    try:
        # Construct the URL
        url = f'{LINK1}{i}'

        # Initialize the webdriver
        driver = webdriver.Firefox()
        driver.get(url)
        sleep(5)

        # Find all 'a' tags on the page
        a_tags = driver.find_elements(By.TAG_NAME, "a")
        urls = []

        # Loop over each 'a' tag
        for a in a_tags:
            # Try to get the 'href' attribute of the 'a' tag
            try:
                href = a.get_attribute('href')

                # If the 'href' attribute is not None and it starts with the specified prefix, append it to the list of URLs
                if href is not None and href.startswith(f'{LINK2}'):
                    urls.append(href)
            except StaleElementReferenceException:
                # Print a message if a StaleElementReferenceException is raised
                print("StaleElementReferenceException")

        # Remove duplicates from the list of URLs
        urls = list(set(urls))

        # Print the number of URLs
        print(f'Number of urls: {len(urls)}')

        # Loop over each URL in the list
        for url in urls:
            print(url)
            driver.get(url)
            sleep(5)

            # Find the div with data-testid="content-details-section"
            div = driver.find_element(By.XPATH, '//div[@data-testid="content-details-section"]')

            # Parse the HTML content of the div with BeautifulSoup
            soup = BeautifulSoup(div.get_attribute('outerHTML'), 'html.parser')

            # Parse the entire page source with BeautifulSoup
            soup2 = BeautifulSoup(driver.page_source, 'html.parser')
            # Find all the <p> and <a> tags in the div
            tags = soup.find_all(['p', 'a'])
            
            # Find all the <h3> and <p> tags in the soup2 that have a class starting with 'offer-price'
            tags2 = soup2.find_all(lambda tag: (tag.name in ['h3', 'p']) and (tag.get('class', [None])[0] or '').startswith('offer-price'))
            
            # Find the <p> tag in the soup2 that contains 'ID' in its text
            tag3 = soup2.find(lambda tag: tag.name == 'p' and 'ID' in tag.get_text())
            data = []
            
            # Loop over each tag in tag3
            for tag in tag3:
                # Print the text of the tag
                print(tag.get_text())
            
                # If the text of the tag is empty, append 'NA' to the data list, otherwise append the text of the tag
                if(tag.get_text() == ""):
                    data.append("NA")
                else:
                    data.append(tag.get_text())
            
            # Print a separator for readability
            print("**********************************")
            
            # Loop over each tag in tags2
            for tag in tags2:
                # Print the text of the tag
                print(tag.get_text())
            
                # If the text of the tag is empty, append 'NA' to the data list, otherwise append the text of the tag
                if(tag.get_text() == ""):
                    data.append("NA")
                else:
                    data.append(tag.get_text())
            
            print("==================================")
            k = 0
            flag = False
            
            # Loop over each tag in tags
            for tag in tags:
                k += 1
                label = ""
            
                # If the text of the tag is one of the specified labels, set the label to the text of the tag and set the flag to True
                if tag.get_text() in ["Marka pojazdu", "Model pojazdu", "Rok produkcji", "Przebieg", "Pojemność skokowa", "Rodzaj paliwa", "Moc", "Skrzynia biegów", "Typ nadwozia", "Kolor"]:
                    label = tag.get_text()
                    flag = True
                    continue
            
                # If the flag is True, print the text of the tag and append it to the data list, then set the flag to False
                if flag == True:
                    print(tag.get_text())
                    if(tag.get_text() == ""):
                        data.append("NA")
                        flag = False
                    else:
                        data.append(tag.get_text())
                        flag = False
            
            # Print a separator for readability
            print("####################################")
            records.append(data)
        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()
        records = []
        continue
    with open('car_listings.csv', 'a', encoding='utf-8') as f_object:
        writer_object = writer(f_object)
        for record in records:
            writer_object.writerow(record)
        f_object.close()
    records = []