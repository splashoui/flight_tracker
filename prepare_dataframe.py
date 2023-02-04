import json
import pandas as pd
import datetime
today = datetime.date.today().strftime("%Y-%m-%d")


def prepare_dataframe(json_result):
    """Takes the json response from the Flights API and converts it into a pandas dataframe

    Returns:
        dataframe: Returns a pandas dataframe with the flights information

    Parameters:
        json_result: Json response from the Flights API

    """

    result = json.loads(json_result)['itineraries']['buckets'][0]['items']
    df = pd.DataFrame(result, columns=["id", "price", "legs"])
    df['price_formatted'] = df['price'].apply(lambda x: x['raw'])
    df['currency'] = df['price'].apply(lambda x: x['formatted'].split(' ')[-1])

    # Choosing index 0 inside 'legs' key which is the best flight option.
    # 0 Best
    # 1 Cheapest
    # 2 Fastest

    df['transfer_num'] = df['legs'].apply(lambda x: x[0]['stopCount'])
    df['duration'] = df['legs'].apply(
        lambda x: round(x[0]['durationInMinutes']/60, 2))
    df['departure_time'] = df['legs'].apply(lambda x: x[0]['departure'])
    df['arrival_time'] = df['legs'].apply(lambda x: x[0]['arrival'])

    df['departure_location'] = df['legs'].apply(
        lambda x: x[0]['origin']['name'])
    df['arrival_location'] = df['legs'].apply(
        lambda x: x[0]['destination']['name'])

    df['departure_airport_1'] = df['legs'].apply(
        lambda x: x[0]['segments'][0]['origin']['flightPlaceId'])
    df['departure_time_1'] = df['legs'].apply(
        lambda x: x[0]['segments'][0]['departure'])

    df['arrival_airport_1'] = df['legs'].apply(
        lambda x: x[0]['segments'][0]['destination']['flightPlaceId'])
    df['arrival_time_1'] = df['legs'].apply(
        lambda x: x[0]['segments'][0]['arrival'])
    try:
        df['departure_airport_2'] = df['legs'].apply(
            lambda x: x[0]['segments'][1]['origin']['flightPlaceId'])
        df['departure_time_2'] = df['legs'].apply(
            lambda x: x[0]['segments'][1]['departure'])

        df['arrival_airport_2'] = df['legs'].apply(
            lambda x: x[0]['segments'][1]['destination']['flightPlaceId'])
        df['arrival_time_2'] = df['legs'].apply(
            lambda x: x[0]['segments'][1]['arrival'])
    except:
        # If there is no transfer. There will not be second departure or arrival airport
        df['departure_airport_2'] = None
        df['arrival_airport_2'] = None
    df.drop(['price', 'legs'], axis=1, inplace=True)
    df['query_date'] = today

    return df
