# Webscrapping

## HW 3: Scraping from Ebay
 This is homework assignment where the instructions are listed below. In this assignment I am gathering information from 
 search results from ebay and compiling them into json files. The code goes through your search result and finds certain indicators to 
 identify items name, price, status, shipping cost, return value, and number of items sold.
<br />

### Link to Instructions: [instructions ](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)


## Running the Code
To start off, you have to run the code in a compatible programming editor. Then open the terminal and input the following command:
<br />

```
$python ebay-dl.py "search term"
```
<br />
Input your search term into the "search term" to find your listed results. 

By default, the code will go through the first 10 pages of ebay. 
By adding `--page_number` to the input code, you may edit the number of pages. 

<br />
<br />


**For my inputs, I selected the following terms for the json files listed in my repository:**

``` 
python3 ebay_dl.py "nintendo switch" 
```

``` 
python3 ebay_dl.py "playstation 5" 
```

``` 
python3 ebay_dl.py laptop 
```
