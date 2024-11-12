# Description Extractor

A short script that takes a specific CSV file with descriptions of our offers (from Allegro marketplace) and extracts HTML parts out of it using Regular Expressions (because the data is not a valid JSON). It then puts each part in separate columns and saves to an Excel file.

If you need the newest descriptions, you need to export the file, save it as 'offers.csv' and replace the current with the new one.

Beware: It works for a specific .csv file with hardcoded column names that we download from the marketplace.

The code is being used in our e-commerce company Pancernik.eu to help us create offers on other marketplaces more easily.
