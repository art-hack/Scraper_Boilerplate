import csv
from bs4 import BeautifulSoup
import requests


# function to scrape smartybro
def scrape(string):
    page_response = requests.get(string, timeout=15)
    if page_response.status_code == 200:
    	page_content = BeautifulSoup(page_response.content, "html.parser")
        # Do with the response
    else:
        print("Error Fetching the Data")


# Main driver Program

# Uncomment if you want to clear out the output from the output file everytime you run this
# listFile2 = open('output.csv', 'w')
# listFile2.close()


with open('input.txt') as openfileobject:
    for line in openfileobject:
        page_link = line
        scrape(page_link)