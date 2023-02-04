import os
from dotenv import load_dotenv
import input_file
from prepare_dataframe import prepare_dataframe
from request_flight import request_flights
import pandas as pd
import datetime
import time
from date_range import choose_date_range
today = datetime.date.today().strftime("%Y-%m-%d")


def configure():
    load_dotenv()


def main():
    configure()
    # The API has 100 request limit per month. I exceeded the limit of 100 requests per month.
    # So this project is on hold.
    """
    Loop through each date range, get the flight information data for that date range.
    Create a dataframe and append to df_output.

    """

    date_range_list = choose_date_range(
        start_date=input_file.start_date, end_date=input_file.end_date)

    df_output = pd.DataFrame()

    count = 0
    for departure_date in date_range_list:
        count += 1
        print("------------------------------------------------")
        print(
            f'Request{count}: Starting to query for {departure_date.strftime("%Y-%m-%d")}.')
        print("------------------------------------------------")
        response, response_status = request_flights(api_key=os.getenv('api_key'),
                                                    api_host=os.getenv(
                                                        'api_host'),
                                                    num_people=input_file.num_people,
                                                    departure_location=input_file.departure_location,
                                                    destination_location=input_file.destination_location,
                                                    departure_date=departure_date,
                                                    currency=input_file.currency)

        if response_status != 200:
            if response_status == 429:
                raise ValueError(
                    f"Error: The user has sent too many requests in a given amount of time (10 requests per min).\nResponse status code: {response_status}")
            elif response_status == 401:
                raise ValueError(
                    f"Error: Unauthorized.\nResponse status code: {response_status}")
            elif response_status == 400:
                raise ValueError(
                    f"Error: The server cannot or will not process the request due to something that is perceived to be a client error.\nResponse status code: {response_status}")
            else:
                raise ValueError(
                    f"Error: response status code is not 200.\nResponse status code: {response_status}")

        else:

            print(f'Request{count}: Starting to prepare the dataframe.')

            # Prepare the dataframe
            df = prepare_dataframe(response)
            print(f'Request{count}: Dataframe has been prepared successfully.')
            # Concat the dataframes for each day.
            df_output = pd.concat([df_output, df], axis=0, ignore_index=True)

            # 10 requests per minute
            if count % 10 == 0:
                sleep_time = 120
                print(
                    f'Request limit {count} reached: Sleeping {sleep_time} seconds.')
                time.sleep(sleep_time)

    return df_output


if __name__ == '__main__':
    main()
