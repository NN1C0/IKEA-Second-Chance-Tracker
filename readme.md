# Ikea Second Chance Search
[Demo](https://second-chance.apps.nicomeier.de)

Can be used to search for an item across multiple coountries.

## How To
### API Scraper
This tool should run periodically. Like every hour.
It's scrapes the IKEA second chance API for the supplied countries and creates a copy of it in a local database.
This increases the searchability of the API, especially in cross-country searches. This might be helpful if you live somewhat close to a bordering country.
 
### Frontend
List the current data from a postgres database. Written using Flask and HTMX

### Todo
- Make frontend prettier. Add images and savings in percent
- Build User area for:
    - Subscribe to searches, receive notifications
    - Configure preferred stores
