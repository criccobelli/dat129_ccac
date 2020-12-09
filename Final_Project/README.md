# Python 2 Final Project: Describing and Analyzing the *1001 Movies You Must See Before You Die*
&nbsp;
My first attempt at API code was to pull movie data using the Open Movie Database ([OMDb]) API. OMDb uses data from IMDb, and can be searched in two ways: with the Title and Year, or with the IMDb ID number (each entry in IMDb is given a unique identifier). Below is an example for what the API returns in JSON:

![Star Wars API search](pic1.png)

However, I was stumped at first because I could only search for one movie at a time, unless I looped through a list of titles/years and the API to get a large dataset. I decided that I could use the popular reference book *1001 Movies You Must See Before You Die* to get a large list of films that cover a wide range of years, genres and countries.


## Web Scraping

First, I had to find a way to use Python to get the *1001* list into Python list. I found the 2018 version of the *1001* list on the website http://www.rinkworks.com/checklist/list.cgi?u=crimsong&U=crimsong&p=1001movies. This is one of the many editions of the book, which gets revised each year to include new films.

Initially I tried to scrape the title and the year from the website, put the titles in one list and the years in another list, then loop both through the API code to obtain the IMDb data. However, this proved to cause errors. Some titles did not search through the API correctly, and some years did not match from the list to the IMDb data. 

![year and titles lists code](pic2.png)

![api search error](pic3.png)

I thought I would have to fix each film that was incorrect manually, but then I realized that the most accurate way to search the API was through the IMDb id number, and thankfully my scraping website linked to the IMDb page of each film. These links therefore included the id numbers.

![href imdb id](pic4.png)

My final scraping code and output example: 

![scraping code](pic5.png)

## API Code
Below is a snippet of my API function and the resulting data. I included ways to capture if any of the IMDb IDs did not successfully pull the movie's data. The results were that one IMDb ID was incorrect. I also initially ran into a request limit and had to wait a day to re-run. Once these two things were resolved I did not encounter any API errors.

![API function and results](pic6.png)

## Opening a CSV and creating a pandas DataFrame

In opening a CSV file and reading in the API movie data, I used all of the Keys from the API dictionaries as field names. I then iterated through the list of dictionaries and added the data to the file. I cleaned up the data in the CSV by deleting columns I didn't need, removing spaces from the data in some columns, and other things to make it easier to work with. 

![opening file and dataframe](pic7.png)

## Conclusions based on analysis
 - The list is havily focused on movies from the "West", especially the USA.
 - The IMDb ratings did not vary must throughout the years.
 - Average runtime seems to have slowly increased, though further analysis is needed.
 - Drama is the most popular genre designation.
 - Of the data available, December is the most common month of release.

![country count](pic8.png)
![runtime by year](pic9.png)
![genre piechart](pic10.png)

## Ideas on how to expand and continue the project
   - I really wanted to separate the films be decade and analyze that way but I got stuck on trying to isolate the decades in the dataframe. This is something I will look into in the future. 
   - I can analyze characteristics by director, by genre, by rating, etc.


[OMDb]: <http://www.omdbapi.com/>

### Links
https://en.wikipedia.org/wiki/1001_Movies_You_Must_See_Before_You_Die
http://www.omdbapi.com/
http://www.rinkworks.com/checklist/list.cgi?u=crimsong&U=crimsong&p=1001movies


