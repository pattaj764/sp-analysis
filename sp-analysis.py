# --- read a file to obatin a list of numbers ------
import csv

file_path = input(str("Please write the file path of the CSV file:     "))
file_path = str(file_path)

def read_file(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        spy = []
        for row in csv_reader:
                spy.append(row[1])

    return list(map(float, spy)) 
    
spy = read_file(file_path)
# ---------------------------------------------------
# Please download the CSV file and initial code from this Github Link Links to an external site.. The CSV file is the SPDR S&P 500 ETF Trust (SPY)

# Links to an external site. closing price from 1/2/2024 through 6/28/2024. Please create Python script to answer the following questions. (You are not allowed to import any built-in or external libraries) 

#     Let's define a rising day as the day when the closing price is higher than the previous day.
#         (3 pts) Try to obtain the number of rising days from 1/2/2024 through 6/28/2024. You need to print out the number of rising days.
#         (8 pts) How many days did the rise last at most?
#     Moving Averages (MA) are the means for sequences of consecutive time-series values for a time duration L. For example, given the daily values, 10, 9, 11, 12, 19, the 3-day moving averages are 10.00, 10.67, and 14.00, where the first MA value, 10.00, is the mean of the first three values (10, 9, and 11) and so on so forth. 
#         (5 pts) Try to calculate 5-day moving averages.
#         (3 pts) Obtain the number of rising days in the 5-day moving averages.
#         (8 pts) How many days did the 5-day moving averages rise last at most?
#         (5 pts) How many days were the SPY closing prices lower than the 5-day moving averages. 
# ---------------------------------------------------

# ----------------- A. rising days -------------------- #

# i. number of rising days
# return total count of rising days
def count_RisingDays( price ):
    count = 0
    for i in range( 1, len( price ) ):
        #   compare to previous day, start with index 1
        if price[i] > price[i - 1]: 
            count += 1
    return count

# ii. rising days streak
def streak_RisingDays( price ):
    streak = 0
    topStreak = 0
    i = 1
    while i < len( price ):
        if price[i] > price[i - 1]:
        # loops to compare previous price to determine rising day
            streak += 1
            # adds to streak if true
            topStreak = max( topStreak, streak )
            # updates top streak
        else:
             streak = 0
        i += 1
    return topStreak

# --------------- B. moving averages ------------------ #


# i. 5-day moving averages
def ma_FiveDay( price ):
    period = 5
    mAvg = []
    # stores moving averages in list
    for i in range( len( price ) - period + 1 ):
        mAvg.append(sum( price[ i : i + period]) / period )
        # appends list 5-day period
    return mAvg

# ii. rising days in moving averages
count_RisingDaysMA = count_RisingDays( ma_FiveDay( spy ) )

# iii. rising moving average streak
streak_RisingDaysMA = streak_RisingDays( ma_FiveDay( spy ) )

# iv. closing below moving average
def count_BelowMA(price, mAvg):
    count = 0
    for i in range(len( mAvg )): 
        if price[i + 4] < mAvg[i]:
        # checks if end of moving average is below moving average
            count += 1
    return count


# -------------------- OUTPUTS ------------------------ #
print("Jack Pattarini\nProfessor Devin Wong\nFoundations of Business Programming Project 1\n22 November, 2024")
print("------------------------------------------------------------------------")
print("                               PART A")
print("------------------------------------------------------------------------")
print(f"i.      number of rising days from 1/2/2024 through 6/28/2024:      {count_RisingDays(spy)}")
print(f"ii.     longest rising period:                                      {streak_RisingDays(spy)}")
print("------------------------------------------------------------------------")
print("                               PART B")
print("------------------------------------------------------------------------")
# print(f"i.    moving averages:                                              {ma_FiveDay( spy )}")
# this prints a massive list, I don't know what you meant for this question but it is properly calculated
print(f"ii.   number of rising 5-day moving averages:                       {count_RisingDaysMA}")
print(f"iii.  longest streak for rising days in 5-day moving averages:      {streak_RisingDaysMA}")
print(f"iv.   number of days closing below 5-day averages:                  {count_BelowMA(spy, ma_FiveDay( spy ))}")