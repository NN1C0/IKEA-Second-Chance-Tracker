# How To
## API Scraper
This tool should run periodically. Like every hour.
It's scrapes the IKEA second chance API for the supplied countries and creates a copy of it in a local database.
This increases the searchability of the API, especially in cross-country searches. This might be helpful if you live somewhat close to a bordering country.
This include:
- Stores
    - All Stores from supplied countries
    - ID
    - Name
    - Display Name
- Offers
  - All offers per country for all stores. Connected to the store which is offering
  - ID
  - Title
  - Desciption
  - Price(New, Old)
  - Currency
  - Reason for discount
  - Link to a hero image