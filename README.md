# data-representation-project
## Data Representation 52957
## Part of HDip Data Analytics GMIT

### Shane Austin G00318488

## Description:

Write a program that demonstrates that you understand creating and consuming RESTful APIs.

Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data.

Project URL: http://shanepaustin.pythonanywhere.com/

## Contents:

#### Python
File | Description
-----|-------------
Server.py | Main program to establish login and Flask commands
RNLIDao.py | Program that processes connection and mySQL queries
rnliScrapeCSV.py | Program that web scrapes a table from Wikipedia and imports a csv from third party API
dbconfig.py | Program to set mySQL login details

#### HTML
File | Description
-----|-------------
homepage.html | Landing page for the site
login.html | User login page
profile.html | Home page for logged in users
fleet.html | Auto generated html of third party API
locations.html | Auto generated html of webscraped data
boatsdb.html | RESTful API page that handles CRUD operations
locationsdb.html |	RESTful API page that handles CRUD operations
to_login.html | Redirect page to login page

#### Data
File | Description
-----|-------------
boats.csv | CSV file of boatsdb page
stations.csv | CSV file of locationsdb page
fleet.csv | CSV file from third-party API
locations.csv | CSV file of web scrape data

