import numpy as np
import pandas as pd
from GoogleSheetDownloader import downloader


# https://old.reddit.com/r/dataengineering/comments/y5bhzg/when_to_use_object_oriented_programming_in_de/

class ActivityStats:
    """
    Give filepath to a time/activity .CSV (like from aTimeLogger) and return a DataFrame for basic descriptive statistics for each of those activities, for a total activities statistics DataFrame, and for use in plotly dashboards (time/activity chart, scatterplots, histograms, correlation heatmap, etc.
    """

    # def download(self):
    #     downloader.run()
    #     # or d = Downloader()
    #     # d.run()
    
    def get_df_from_csv_filepath(filepath=filepath):
        df = pd.read_csv(filepath)
        return df
        
    def transform_df(df=df):
        original_df = df = df[['Group', 'Activity type', 'From', 'To']]
        original_df = df = df.rename(columns={'Activity type':'Activity', 
                                              'From':'Start', 
                                              'To':'End'})
        df['Day'] = original_df['Start'].str[0:10]
        original_df['Start'] = df['Start'] = pd.to_datetime(df['Start'])
        original_df['End'] = df['End'] = pd.to_datetime(df['End'])
        replace_activity_name(df)
        replace_activity_name(original_df)
        
        original_df['Duration in Seconds'] = df['Duration in Seconds'] = pd.to_timedelta(df['End'] - df['Start']).astype('timedelta64[s]')
        original_df['Duration'] = pd.to_datetime(df["Duration in Seconds"], unit='s').dt.strftime("%H:%M:%S")
        
        edges = pd.date_range(df.Start.min().normalize() - pd.Timedelta(days=1), 
                              df.End.max().normalize() + pd.Timedelta(days=1), freq='D')
        l = []
        for edge in edges:
            m = df.Start.lt(edge) & df.End.gt(edge)            # Rows to modify
            l.append(df.loc[m].assign(End=edge))               # Clip end of modified rows
            df.loc[m, 'Start'] = edge                          # Fix start for next edge
            
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
        df = pd.concat(l+[df], ignore_index=True).sort_values('Start')
        
        df['Day'] = df['Start'].dt.date
        df['Start'] = pd.to_datetime(df.Start)
        df["Start"] = df["Start"].apply(lambda x: x.replace(year=1970, month=1, day=1))
        df['Start'] = pd.to_datetime(df.Start)

        df['End'] = pd.to_datetime(df.End)
        df["End"] = df["End"].apply(lambda x: x.replace(year=1970, month=1, day=1))
        df['End'] = pd.to_datetime(df.End)
        
        m = dt(year=1970, month=1, day=1, hour=0, minute=0, second=0)
        new = dt(year=1970, month=1, day=1, hour=0, minute=0, second=1)
        df['Start'] = df['Start'].mask(df['Start'] == m, new)
        m = dt(year=1970, month=1, day=1, hour=0, minute=0, second=0)
        new = dt(year=1970, month=1, day=1, hour=23, minute=59, second=59)
        df['End'] = df['End'].mask(df['End'] == m, new)
        df['Duration in Seconds'] = pd.to_timedelta(df['End'] - df['Start']).astype('timedelta64[s]')
        df['Duration'] = pd.to_datetime(df["Duration in Seconds"], unit='s').dt.strftime("%H:%M:%S")
        
        df.to_csv('data/split_activities.csv', index=None, encoding='utf-8')
        original_df.to_csv('data/activities.csv', index=None, encoding='utf-8')
        return original_df, df
    
def replace_activity_name(df=df):
        for activity in df['Activity'].unique():
            print(activity)
        print()

        while True:
            replace = input("Do you want to replace any activity's names with something else? (y/n): \n")
            try:
                if replace == 'y' or replace == 'Y' or replace == 'yes' or replace == 'Yes' :
                    replacement_activity = input('What activity do you want to replace?: ')
                    replaced_with = input('And what do you want to replace it with?: ')
                    df.loc[df['Activity'].str.contains(replacement_activity), 'Activity'] = replaced_with
                    original_df.loc[df['Activity'].str.contains(replacement_activity), 'Activity'] = replaced_with
                    print(f'Replaced: {replacement_activity} with {replaced_with}')
                    continue
                elif replace == "n" or replace == "N" or replace == "no" or replace == "No" or replace == "" or replace == " ":
                    print("Finished replacing activity names.")
                else:
                    raise Exception("Answer must be some variation of 'yes' or 'no.'")

            except Exception as e:
                print(e)

            else:
                for activity in df['Activity'].unique():
                    print(activity)
                break
        
    def lower_replace(string):
        return string.lower().replace('/', '_').replace(' ', '_')
        
    def __init__(self, filepath=filepath):
        
        self.df = get_df(filepath)
        self.transform_df
        
        
        self.unique_activities = self.df['Activity'].unique().tolist()
        self.days_in_df = pd.DataFrame(self.df['Day'].unique(), columns=['Day'])
        self.num_days_in_df = len(self.days_in_df) - 1
        self.seconds_in_df = self.num_days_in_df * 86400