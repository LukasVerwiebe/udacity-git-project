import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# New function to check if input is correct
def input_checking(str_input, dtype_input):
    while True:
        read_input = input(str_input).lower()
        try:
            if read_input in ["chicago", "new york city", "washington"] and dtype_input == 1:
                break
            elif read_input in ["all", "january", "february", "march", "april", "may", "june", "juli", "august", "september", "october", "november", "december"] and dtype_input == 2:
                break
            elif read_input in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] and dtype_input == 3:
                break
            else:
                if dtype_input == 1:
                    print("not the correct city!")
                if dtype_input == 2:
                    print("not the corrrect month!")
                if dtype_input == 3:
                    print("not the corrrect day!")
        except ValueError:
            print("Input is not correct!")
    return read_input

# Seting filters
def get_filters():

    """
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Asks user to specify a city, month, and day to analyze.

     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    city = input_checking("Specify a city: chicago, new york city or washington: ",1)

     # TO DO: get user input for month (all, january, february, ... , june)
    month = input_checking("Specify a month: ",2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_checking("Specify a day: ",3)

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df["month"].mode()[0]
    print("Most popular month:", popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df["day_of_week"].mode()[0]
    print("Most day of week:", popular_day_of_week)


    # TO DO: display the most common start hour
    popular_common_start_hour = df["hour"].mode()[0]
    print("Most common start hour:", popular_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df["Start Station"].mode()[0]
    print("Most Start Station:", commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df["End Station"].mode()[0]
    print("Most End Station:", commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station','End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time:', travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # TO DO: Display counts of gender
        print('Gender stats:')
        print(df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth year stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display Raw Data
def display_data(city):
    a = 0
    b = 5
    while True:
        choice = input('\nDo you want to see raw Data: Enter yes or no.\n').lower()
        print('')
        if choice != 'yes':
            break
        else:
           df = pd.read_csv(CITY_DATA[city])
           print(df.iloc[a:b, :])
           a = a + 5
           b = b + 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        while True:
            print('1: time_stats, 2: station_stats, 3: trip_duration_stats, 4: user_stats, all: All Stats, stop: End of programm')
            choice = input('Wich Result want you to View: ').lower()
            print('-'*40)
            if choice == '1':
                time_stats(df)
            elif choice == '2':
                station_stats(df)
            elif choice == '3':
                trip_duration_stats(df)
            elif choice == '4':
                user_stats(df,city)
            elif choice == 'all':
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df,city)
            elif choice == 'stop':
                restart = input('\nWould you like to Enter another result: Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break
            else:
                print('')
                print('Wrong input!')
                print('')

            display_data(city)
            #print('test')
            #os = pd.read_csv('washington.csv')
            #print(os.head(5))


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
