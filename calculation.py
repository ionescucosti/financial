import datetime

from datetime import datetime
from database import get_instrument_modifier


# Function to calculate statistics based on instrument type
def calculate_statistics(file):
    results = {}
    instruments_data = {}
    
    for line in file.split():
        # Parse the line from the file
        instrument_name, date, value = line.strip().split(",")
        value = float(value)

        # Get the instrument modifier from the database
        modifier = get_instrument_modifier(instrument_name)

        # Apply the modifier to the original value
        value = value * modifier

        # INSTRUMENT1 update sum and total, at the end we can calculate mean
        if instrument_name == 'INSTRUMENT1':
            if instrument_name not in instruments_data.keys():
                instruments_data[instrument_name] = {'sum': value, 'total': 1}
            else:
                instruments_data[instrument_name]['sum'] += value
                instruments_data[instrument_name]['total'] += 1

        # INSTRUMENT2 update sum and total for Nov-2014 dates, at the end we can calculate mean
        elif instrument_name == 'INSTRUMENT2':
            if date.endswith("-Nov-2014"):
                if instrument_name not in instruments_data.keys():
                    instruments_data[instrument_name] = {'sum': value, 'total': 1}
                else:
                    instruments_data[instrument_name]['sum'] += value
                    instruments_data[instrument_name]['total'] += 1

        # INSTRUMENT3 get lowest and highest elements, at the end we can calculate mean
        elif instrument_name == 'INSTRUMENT3':
            if instrument_name not in instruments_data.keys():
                instruments_data[instrument_name] = {'lowest': None, 'highest': value}
            else:
                if value >= instruments_data[instrument_name]['highest']:
                    instruments_data[instrument_name]['highest'] = value
                elif instruments_data[instrument_name]['highest'] is None \
                        or value < instruments_data[instrument_name]['highest']:
                    instruments_data[instrument_name]['lowest'] = value

        # Others INSTRUMENT get newest 10 elements, at the end we calculate the sum
        else:
            date_object = datetime.strptime(date, '%d-%b-%Y').date()
            if instrument_name not in instruments_data.keys():
                instruments_data[instrument_name] = {date_object: value}
            elif len(instruments_data[instrument_name].keys()) < 10:
                instruments_data[instrument_name].update({date_object: value})
            else:
                oldest = min(instruments_data[instrument_name].keys())
                if date_object > oldest:
                    del instruments_data[instrument_name][oldest]
                    instruments_data[instrument_name].update({date_object: value})

    # Apply final calculations related to each instrument
    for k, v in instruments_data.items():
        if k in ['INSTRUMENT1', 'INSTRUMENT2', 'INSTRUMENT3']:
            results[k] = instruments_data[k]['sum']/instruments_data[k]['total']
        else:
            results[k] = sum(instruments_data[k].values())
            
    return results
