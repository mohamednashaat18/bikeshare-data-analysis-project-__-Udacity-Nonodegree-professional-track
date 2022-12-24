import time 
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday
   
    
    city=str(input('select the City that you want to work with(chicago ~ new york city ~ washington): ')).lower()
    month=str(input('select month that you want to filter(january,february ,....,june) or print "all" if you want all months')).title()
    day=str(input('select day(monday,tuesday,....,sunday) or print "all" if you want all day')).title()
    if city=='new york':
        city+=' city'
    while city in CITY_DATA.keys():
        break
    else:    
        print('invalid city name, please try agian')
        get_filters()
    
    months = ['January', 'February', 'March', 'April', 'May', 'June','All']
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    
    while month in months:
        break
    else:
        print('invalid month name, please try agian')
        get_filters()
    while day in days:
        break
    else:
        print('invalid day name, please try agian')
        get_filters()


    

    print('-'*40)
    return city,month,day

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df=pd.read_csv(CITY_DATA[city])
    #with converting columns start and end time to date time formating
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    
    #we will insert two new column named by "month" "day of weak" 
    df['month']=df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month!='All':
        
    
        df = df[df['month'] == month]
        
    
    if day!='All':
        
        df = df[df['day_of_week'] == day]
    


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
   
        
    most_month=df['Start Time'].dt.month_name().mode()
    print('the most common month: ',most_month.values[0])


    # display the most common day of week
    
        
    most_day=df['Start Time'].dt.day_name().mode()
    print('the most common day: ',most_day.values[0])
    


    # display the most common start hour
    most_hour=df['Start Time'].dt.hour.mode()
    print("the most common hour: ",most_hour.values[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_stat=df['Start Station'].mode()
    print('the most commonly used start station: ',most_start_stat.values[0])


    # display most commonly used end station
    most_end_stat=df['End Station'].mode()
    print('the most most commonly used end station',most_end_stat.values[0])


    # display most frequent combination of start station and end station trip
    most_start_to_stop=df['Start Station'] +' to '+ df['End Station']
    print('most frequent combination of start station and end station:',most_start_to_stop.mode().values[0])

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=df['End Time']-df['Start Time']
    print('the total travel time: ',total_travel.sum())
    
    
    # display mean travel time
    print('average of travel time: ',total_travel.mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type=df['User Type'].value_counts()
    print(user_type)


    # Display counts of gender
    if 'Gender' in df.keys():
         print(df['Gender'].value_counts())
         
        
    # Display earliest, most recent, and most common year of birth

         earliest_year=(df['Birth Year'].dropna(axis=0).min())
         print('the earliest year of our subscribers is: {}'.format(round(earliest_year)))
               
         most_recent=(df['Birth Year'].dropna(axis=0).max())
         print('the most recent birth year of our subscribers is:{}'.format(round(most_recent)))
         common_year=(df['Birth Year'].dropna(axis=0).mode())
         print('the common birth year of our subscibers is:{}'.format(round(common_year)))      
    else:
              print('washington has no information about gender or birth year of users')
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_head_data(df):
    
    """
    Displays head data that contain the frist 5 rows.
    
    
    
    
    """
   
    row = 0
        
    sample_row_data = input('\nWould you like to see sample row data ? yes or no.\n')
    while sample_row_data.lower() == 'yes':
        
        part=df.iloc[row:row+5]
        # check if we reached to last data
        if part.empty:
            print('no more data to display!')
            break
        else:            
            print(part)
            show_more_data = input('\nType yes if you would you like to see more data or type no\n')                
            if show_more_data.lower() !='yes':
                break
            else:
                row+= 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_head_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()    