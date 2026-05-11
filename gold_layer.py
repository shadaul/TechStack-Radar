import pandas as pd

df = pd.read_csv('silver_jobs.csv')

gold_df = df.groupby('location')['title'].count().reset_index()

gold_df = gold_df.rename(columns={'title':'job_count'})

gold_df = gold_df.sort_values(by='job_count', ascending=False)

print(gold_df.head())

gold_df.to_csv('gold_top_locations.csv', index=False)