# financial


Description:
Read time series from the file provided and pass all of them to the "calculation module".

Calculation engine needs to calculate:
For INSTRUMENT1 – mean
For INSTRUMENT2 – mean for November 2014
For INSTRUMENT3 – mean for min and max
For any other instrument from the input file - sum of the newest 10 elements (in terms of the date).

Now, we want to emulate the fact that in the real life there are often multiple factors influencing calculations
performed on the instrument prices. So as part of your task we would like you to set up a database with only one table,
called INSTRUMENT_PRICE_MODIFIER with the following columns:
    ID (primary key)
    NAME (instrument name as read from the input file)
    MULTIPLIER - double value that specifies the factor by which the original instrument price should be multiplied.

So in order to determine the final value of a given instrument price for a given date you should do the following:
1. read the line from the input file;
2. query the database to see if there is an entry for the <INSTRUMENT_NAME> you read in the 1st step;
3. if there is - multiply the original <VALUE> by the factor you found in the step 2;
4. if there is no entry - simply use the original <VALUE> from the file.

Please assume that the values in the INSTRUMENT_PRICE_MODIFIER table can change frequently independently of the process you're implementing, 
but not more often than once every 5 seconds.

Install requirements:
pip install -r requirements.txt

How to run program:
python main.py

How to run tests:
python -m unittest tests.py
