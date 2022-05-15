import pandas as pd
import numpy as np

LIBRE_DATA = 'data/SamDysch_glucose_2-5-2022.csv'
PUMP_DATA = 'data/Samuel Dysch 06-05-2022.csv'

def get_combined_libre_pump_data(libre_data=LIBRE_DATA, pump_data=PUMP_DATA):

    # open libre data and sort
    libre_data = pd.read_csv(LIBRE_DATA, skiprows=[0])
    libre_data['Device Timestamp'] = pd.to_datetime(libre_data['Device Timestamp'], format="%d-%m-%Y %H:%M")
    libre_data = libre_data.sort_values('Device Timestamp')

    # open pump data and sort
    pump_data = pd.read_csv(PUMP_DATA, parse_dates=[['Date', 'Time']])
    pump_data = pump_data.dropna(how='all')
    pump_data['Date_Time'] = pd.to_datetime(pump_data['Date_Time'])
    pump_data = pump_data.sort_values('Date_Time')

    # merge on nearest timestamp
    merged = pd.merge_asof(pump_data, libre_data, left_on='Date_Time', right_on='Device Timestamp', direction='nearest')

    merged.index = merged['Date_Time']
    merged = merged.drop(['Date_Time', 'Index'], axis='columns')

    return merged


def combine_libre_readings(scan, historic):
    ''' scan glucose = SG when libre was scanned, historic = libre's historical readings when there was no scan.
    Aggregate these into a combined 'Libre glucose' column '''

    # have preference for scan glucose
    value = scan if np.isnan(historic) else historic

    return value

