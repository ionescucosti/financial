import time
import sqlite3
import threading

# Global variable to store the latest instrument modifiers
instrument_modifiers = {}


# Function to fetch instrument modifier from the database periodically
def update_instrument_modifiers():
    while True:
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        query = "SELECT NAME, MULTIPLIER FROM INSTRUMENT_PRICE_MODIFIER"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()

        # Update the global variable with the latest modifiers
        instrument_modifiers.update(dict(result))

        # Sleep for 5 seconds before the next query
        time.sleep(5)


# Start the instrument modifiers update thread
instrument_modifiers_thread = threading.Thread(target=update_instrument_modifiers)
instrument_modifiers_thread.daemon = True
instrument_modifiers_thread.start()


# Function to fetch instrument modifier from the global variable
def get_instrument_modifier(instrument_name):
    return instrument_modifiers.get(instrument_name, 1.0)
