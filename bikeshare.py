import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = ''
    while city_input.lower() not in CITY_DATA:
        city_input = input("What is the name of the city you want to analyze? Please select one. (chicago, new york city, or washington)\n")
        if city_input.lower() in CITY_DATA:
            city_input = city_input.lower()
            city = CITY_DATA[city_input]

        else:
            print("Please input the correct name of the city, we are not able to get the city data\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = ''
    while month_input.lower() not in MONTH_DATA:
        month_input = input("What is the month you want to analyze? July is not included. (Either input all or name of the month)\n")

        if month_input.lower() in MONTH_DATA:
            month = month_input.lower()

        else:
            print("Please input the correct name of the month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = ''
    while day_input.lower() not in DAY_DATA:
        day_input = input("What is the day you want to analyze? (Either input all or name of the day)\n")

        if day_input.lower() in DAY_DATA:
            day = day_input.lower()

        else:
            print("Please input the correct name of the day")

    print('-'*40)
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

    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Month_Name'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.weekday
    df['Day_Name'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour


    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df[df['Month'] == month]
    
    if day != 'all':
        day = DAY_DATA.index(day) - 1
        df = df[df['Day'] == day]


    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df['Month_Name'].mode()[0]
    print("The most common month in the data is {}".format(month_mode))
    # TO DO: display the most common day of week
    day_mode = df['Day_Name'].mode()[0]
    print("The most common day in the data is {}".format(day_mode))

    # TO DO: display the most common start hour
    hour_mode = df['Hour'].mode()[0]
    print("The most common hour in the data is {} o'clock".format(hour_mode))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most common start station in the data is {}".format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most common end station in the data is {}".format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combine_station = (df['Start Station'] + ' AND ' + df['End Station']).mode()[0]
    print("The most common combine station in the data is {}".format(combine_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day    
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel = df['Trip Duration'].sum()
    print("The total travel duration is {} seconds".format(sum_travel))

    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print("The total travel duration is {} seconds".format(avg_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.
        
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
        city - city input by user
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_count = str(df['User Type'].value_counts())
    print("The user type counts are {}\n" + user_count + "\n")

    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender_count = str(df['Gender'].value_counts())
        print("The gender counts are {} \n" + gender_count + "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = str(df['Birth Year'].min())
        recent = str(df['Birth Year'].max())
        common = str(df['Birth Year'].mode()[0])
        print("The earliest birth year is {}".format(earliest))
        print("The recent birth year is {}".format(recent))
        print("The common birth year is {}".format(common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Displays statistics on bikeshare users.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        df - Five rows of the dataframe
    """
    raw_input = input("Do you want to see next 5 rows of the data (Yes or No)\n")
    i = 0
    while True:
        if raw_input.lower() == 'yes':
            print(df.iloc[i:i+5])
            i += 5
            raw_input = input("Do you want to see next 5 rows of the data (Yes or No)\n")
        else:
            return
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
