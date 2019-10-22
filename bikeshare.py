import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # gettng the user input for city (chicago, new york, washington).I used .lower to get input in any format and the while loop to handle invalid inputs
    city = input('\nWould you like to see the data for Chicago, New York or Washington ?\n').lower()
      
    while(True):
        if(city == 'chicago' or city == 'new york' or city == 'washington'):
            break
        else:
            city = input('Enter Correct city: ').lower()
    print('\nGreat you choosed: ',city.title())
    
    
    # getting the  user to input for month (all, january, february, ... , june).Using .lower to get input in any format and the while loop to handle invalid inputs
    month = input('\nfor which month?(January, February, March, April, May, June or all?\n').lower()
    
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower()
    print('\nSo, you want the data for the month of: ',month.title())
    # getting the user to input for day of week (all, monday, tuesday, ... sunday). using lower to get input in any format and the while loop to handle invalid inputs
    day = input('\nWhich day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all to display the data of all days:\n').lower()
    
    while(True):
        
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter Correct day: ').lower()
            
    print('\nand for the day you selected:',day.title())


    print('*'*50)
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
    # To read the file I used the pd.read_csv:
    df = pd.read_csv(CITY_DATA[city])
    # The to_datetime is used to covert the date into date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month] #
        
        
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()] 
    
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month,by using the dt.month.valule().idxmax
    if(month == 'all'):
        common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('The Most Commn month is ',common_month)
        

    # TO DO: display the most common day of week,by using the dt.weekday_name.value_counts().idxmax()
    if (day == 'all'):
        common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most Common day is ', common_day)

    # display the most common start hour,by dt.hour.value_counts().idxmax()
    common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most common hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station, by using the .value_counts().idxmax()
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most common start station is: ', common_start_station)

    # Display most commonly used start station, by using the .value_counts().idxmax()
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most common end station is:', common_end_station)
          
    # display most frequent combination of start station and end station trip, by using the .value_counts().idxmax()
    comb_stations =  df['Start Station'] + "-" + df['End Station']
    comb_stations_value = comb_stations.value_counts().idxmax()
    print('Most frequent combination are {} to {}'.format(comb_stations_value.split('-')[0],comb_stations_value.split('-')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Creating a function for convert the seconds to days, minutes and seconds
    def convert_to_d_m_s(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return(' {} Days, {} Hours, {} Mins:, {} Secs:'.format(days, hours, minutes, seconds))
              
         
    #display total travel time.by the sum()
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time is: ', convert_to_d_m_s(total_time))

    #display mean travel time.by the mean()
    mean_time = df['Trip Duration'].mean()
    print('The mean travel Time is: ',mean_time, ' sec')
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types by using  value_count()
    user_types = df['User Type'].value_counts()
    print('The count of the users are:')
    print(user_types)
    #Display counts of gender by using str.count().sum()
    if('Gender' in df.columns):
        male = df['Gender'].str.count('Male').sum()
        female = df['Gender'].str.count('Female').sum()
        print('Counts of Male users are: ', int(male))
        print('Counts of Female users are: ',int(female))
    else:
        print('There is no information about the gender')
    #Display earliest, most recent, and most common year of birth by using max(),min() and .value_counts().idxmax()
    if('Birth Year' in df.columns):
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('Earliest year of birth is {}, while the most recent one is {} and the most common year of birth is {}'.format(int(earliest),int(recent),int(common_birth_year)))
    else:
        print('There is no information about the birth year')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)
    
    
    #a function made to display raw data shape and size and checking if the user want to see by using the iloc[].
def display(df):
    print('\nThe size of the data is {} cells and it have a shape of {}'.format(df.size,df.shape))
    user = input('\nDo you like to see the raw data? Enter yes or no\n')
    n = 0
    # the loop was uesed to increase the number by 5 
    while True:
        if user.lower() != 'no':
            print(df.iloc[n : n + 5])
            n += 5
            user = input('Do you like to see more data? Enter yes or no\n')
        else:
            break
    print('*'*50)
    
    

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('*'*50)
            print('Have a Good Day!')
            print('*'*50)
            break     

if __name__ == "__main__":
	main()
