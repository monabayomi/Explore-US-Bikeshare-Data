import time
import pandas as pd

CITY_DATA={ 'chicago':'chicago.csv',
            'new york city':'new_york_city.csv',
            'washington':'washington.csv'}
city = ('chicago' , 'new york city' , 'washington' )
months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
days = ('saturday','sunday','monday','tuesday','wednesday','thursday','friday','all')
def get_filters():
  
    print('welcome to us bike share ptoject')
    city_name=" "
    for cite in city:
         city_name += cite +" , "

    c = input ("\n please choose one city \n"+ city_name +":").lower()
    while c not in CITY_DATA :
        print('\n wrong choice \n')
        c = input ("\n please choose one city \n"+ city_name +":").lower()
    month_name=" "
    for month in months :
        month_name += month + ","

    m = input ('\n enter the month:\n ' + month_name + ', or "all" ').lower()
    while m not in month_name:
        print('\n wrong choice \n')
        m = input ('\n enter the month:\n ' + month_name + ', or "all" ').lower()

    day_name= " "
    for da in days :
       day_name += da + ", "
    d= input('\n please choose the day name:\n ' + day_name + ', or "all"').lower()
    while d not in days :
        print('\n wrong choice \n')
        d= input('\n please choose the day name:\n ' + day_name + ', or "all"').lower()

    print('-'*50)
    print (c+ "-" + m + "-" + d)
    print('-'*50)
    return c, m, d


def load_data(c, m, d):

    df = pd.read_csv(CITY_DATA[c])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day Of The Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    if m!= 'all':
        month_name= ['january', 'february', 'march', 'april', 'may', 'june']
        m = month_name.index(m) + 1
        df = df[df['Month'] == m]
    if d != 'all':
        df = df[df['Day Of The Week'] == d.title()]
    return df

def time_stats(df):
  
    print('\nCalculate The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['Month'].mode()[0]
    print('Most Popular Month:', popular_month)
    popular_day = df['Day Of The Week'].mode()[0]
    print('Most Popular Day Of The Week:', popular_day)
    popular_hour = df['Hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    
    print('\nCalculateThe Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_Start_Station = df['Start Station'].mode()[0]
    print('Most Popular Start Station is:', popular_Start_Station)

    popular_End_Station = df['End Station'].mode()[0]
    print('Most Popular End Station is:', popular_End_Station)
    df['combination'] = 'from ( ' + df['Start Station'] + ' ) station, to ( ' + df['End Station' ] + ' ) station '
    comp_Station = df['combination'].mode()[0]
    print('Most frequent combination of start station and end station trip : \n', comp_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculate Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Trip Duration = '+ str(total_travel_time) + ' sec.')
    travel_time_mean = df['Trip Duration'].mean()
    print('travel time mean  = '+ str(travel_time_mean) + ' sec.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print( user_types )
    if 'Gender' in df :
      gender = df['Gender'].value_counts()
      print( gender )
    else :
        print('no available data in tis city')

    if 'Birth Year' in df :
        earliest_y = df['Birth Year'].min()
        print( earliest_y )
        recent_y = df['Birth Year'].max()
        print( recent_y )
        common_y = df['Birth Year'].mode()[0]
        print( common_y )
    else :
        print('no available data in tis city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    print('\nCalculate User Stats...\n')
    start_time = time.time()

    view_data = input("Would you like to view 5 rows of  data? Enter yes or no?").lower()
    start_loc = 5
    while (view_data == 'yes'):
        print(df.iloc[0:start_loc])
        start_loc += 5
        display = input("doyou want to complete viewing data")
        if display.lower() != 'yes':
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def main():
    while True:
        c,m,d = get_filters()
        df = load_data(c,m,d)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()