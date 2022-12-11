import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore US bikeshare dataset!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\n Which cities date would you like to explore ? \n").title()
        if city not in CITY_DATA.keys():
            print("invalid input. Please enter a valid input")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\n Do you want details specific to a particular month? If yes, type month name from within first six months else type 'all'\n").title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("invalid input. Please enter a valid input")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nDo you want details specific to a particular day? If yes, type day name else type 'all'\n").title()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print("invalid input. Please enter a valid input")
            continue
        else:
            break

    print('\n')
    print(' * * ' * 10, '\n')

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.day)

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'All':
        # use the index of the days list to get the corresponding int
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = days.index(day) + 1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def T_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].apply(lambda x: x.hour)
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\n This took %s seconds." % (time.time() - start_time))

    print('\n')
    print(' * * ' * 10, '\n')


def S_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\n Most Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\n Most Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\n This took %s seconds." % (time.time() - start_time))

    print('\n')
    print(' * * ' * 10, '\n')


def trip_D_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time:', Total_Travel_Time / 86400, " Days")

    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time / 60, " Minutes")

    print("\n This took %s seconds." % (time.time() - start_time))

    print('\n')
    print(' * * ' * 10, '\n')


def U_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    # print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
        gender_types = df['Gender'].value_counts()
        print('\n Gender Types:\n', gender_types)

    except KeyError:
        print("\n Gender Types: \n No data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        Earliest_Year = df['Birth Year'].min()
        print('\n Earliest Year:', Earliest_Year)
    except KeyError:
        print("\n Earliest Year: \n No data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\n Earliest Year: \n No data available for this month.")


    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\n Most Common Year:', Most_Common_Year)
    except KeyError:
        print("\n Earliest Year: \n No data available for this month.")

    print("\n This took %s seconds." % (time.time() - start_time))

    print('\n')
    print(' * * ' * 10, '\n')
    
    
 
def show_data(df):
       row=0
       while True:
        view_raw_data = input("would you like see the raw data? if yes Enter 'Y' if no Enter 'N'.\n").lower() 
        if view_raw_data == "y":
            print( df.iloc[ row : row + 6] )
            row += 6
        elif view_raw_data == "n":
                      break
        else:
          print(" invalid input. Please enter a valid input")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

        T_stats(df)
        S_stats(df)
        trip_D_stats(df)
        U_stats(df)
        show_data(df)
        
 
        restart = input('\n Would you like to restart? Enter Yes or No.\n').title()
        if restart.title() != 'Yes':
            break


if __name__ == "__main__":
    main()