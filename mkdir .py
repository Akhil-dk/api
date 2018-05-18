# -*- coding: utf-8 -*-
import sys
import requests
import json

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

def main(isbn):
    isbn_path = "./isbn_data/" + isbn + ".json"
    buf01 = ''
    buf02 = ''
    try:
        with open(isbn_path, 'r') as f:
            data = json.load(f)
            try:
                buf01 += data['items'][0]['volumeInfo']['title'] 
                buf02 += data['items'][0]['volumeInfo']['description'] 
            except:
                print('None')
    except:
        req_url = url + isbn
        response = requests.get(req_url)
        with open(isbn_path, 'w') as f:
            json.dump(response.json(), f)
        with open(isbn_path, 'r') as f:
            data = json.load(f)
            try:
                buf01 += data['items'][0]['volumeInfo']['title'] 
                buf02 += data['items'][0]['volumeInfo']['description'] 
            except:
                print('None')
    return buf01, buf02

if __name__ == "__main__":
    while True:
        sys.stdout.write('input isbn >>>')       
        isbn_input = input()
        print(main(isbn_input))