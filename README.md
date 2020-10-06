# Magic_money 💰
Generates a list of banking transactions for designers to use in their prototypes and user tests.

# Installation
Copy the Magic_money_vX.X.py script to a folder on your computer. Using Terminal (or OS equivalent), navigate to the folder's location and run the script with 'python3 Magic_money_vX.X.py'. The script must be run in Python 3, it will not work with Python v2.

# Usage
Magic Money will create any number of transactions (£), ordered across a random range of dates and keep a running balance. It will also match those dates so they correspond with your future user testing session. Currently account starting balance is fixed at £1500.

Your generated transaction list will exported into a CSV file (found in the same location as the script). You can copy and paste the values from here into your prototypes.
If your product uses different date format, you can change this with `.strftime()` [More info](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) 

# Updates
I've planned some updates which will include transaction descriptions, +/- transactions, alt currency symbols...

# Questions or comments
Drop me a line on twitter: @Swain0.
