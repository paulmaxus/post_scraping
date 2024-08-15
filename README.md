
# Instructions

The script uses [this library](https://github.com/moda20/facebook-scraper) which is a fork of [that library](https://github.com/kevinzg/facebook-scraper).

## Setup

### Required software

First of all, we need [Python](https://www.python.org/downloads/).
We also need [git](https://git-scm.com/downloads)

### File system

Start by creating a project folder: something like *facebook_scraper* in your home directory.

Now, we need the command line, if you're not familiar with it, check out [this Carpentry lesson](https://swcarpentry.github.io/shell-novice/02-filedir.html).
On Mac, open the Terminal application.

Navigate to the project folder with `cd`.

### Virtual environment

Assuming you have Python installed, create a virtual environment:
`python -m venv venv`

Activate the environment:
`source venv/bin/activate`

Let's install the necessary packages:
`pip install git+https://github.com/moda20/facebook-scraper.git@master pandas lxml_html_clean`

Done

### Cookies

The tool needs your facebook cookies in a file called *cookies.json*.

The easiest way to get those is by using this Chrome plugin: 
https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc

Open facebook in Chrome, log in, then click on the plugin, it will ask if you would like to save your cookies:
Make sure to click on format=json, then save the cookies.json in the project folder.

## Running the tool

Put the pages you want to scrape into *pages.txt*.

Now run the tool:
`python script.py`

The results will be in *posts.csv*