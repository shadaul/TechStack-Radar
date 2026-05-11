import pandas as pd

df = pd.read_json('raw_data.json')

df_clean = df[['title','company_name', 'location', 'remote']]
print(df_clean.head())
df_clean.to_csv('silver_jobs.csv', index=False)