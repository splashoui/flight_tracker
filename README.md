# Flights Information Tracker & Analysis

This project were created to do the following steps. 



1. Send request to Skyscanner API through RapidAPI, fetch the response for flights information that user choses the following inputs:
  - Departure location
  - Arrival Location
  - Number of adults who will travel
  - Currency of the prices
2. Get the responses for all the flights between today and next 60 days.
3. Using the response, creating a dataframe to store relevant information to track historical data.
  - Departure location
  - Arrivial location
  - Price
  - Currency
  - Number of transfer
  - Departure airport code 1 
  - Arrival airport code 1 
  - Departure time 1
  - Arrival time 1
  
  - If number of transfer is more than 0:
    - Departure airport code 2 
    - Departure time 2 
    - Arrival airport code 2
    - Arrival time 2
  - Query date: The date when this code has been ran, so the information and the prices would belong to that date.
  
  Note: I was using Skyscanner API through RapidAPI to fetch the data but after building the code I have seen that in the free user plan there is a limit of 100 requests per month , so can not continue with the next part until next month when I am able to send more requests to API.
  
  
  4. The idea of the next step was to run this project daily to store the changing prices in a database.
  5. Later, connecting that database to a BI tool to get insights about the prices and flights between these 2 location.
