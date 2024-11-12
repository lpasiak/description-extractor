import pandas as pd
import re

# Products that need to be removed
GSHEETS_BUNDLES = "https://docs.google.com/spreadsheets/d/1mVBRLkJe4XSVbzWxvK6Hz4hJqBo8hJLF-8D909X5YuY/export?format=csv&gid=1937940390"
OFFERS_FILE = "offers.csv"

try:
    df1 = pd.read_csv(OFFERS_FILE, encoding='utf-8', usecols=['id', 'external_id', 'name', 'description_sections'])
except FileNotFoundError:
    print(f"No file {OFFERS_FILE} found.")
else:

    df2 = pd.read_csv(GSHEETS_BUNDLES, encoding='utf-8', usecols=["Numer aukcji"])

    df2['Numer aukcji'] = df2['Numer aukcji'].fillna(0).astype(int).astype(str)
    df1['id'] = df1['id'].fillna(0).astype(int).astype(str)
    filt = ~(df1['id'].isin(df2['Numer aukcji']))
    final_df = df1[filt].drop_duplicates(subset='external_id')

    def retrieve_htmls(item):
        item = item.replace('\\xa0', ' ').replace('&nbsp', ' ').replace('\\xa', ' ').replace('\\n', ' ')
        content_pattern = r"(?<='content':\s')[^']+"
        contents = re.findall(content_pattern, item)
        
        return contents

    final_df['description_sections'] = final_df['description_sections'].apply(retrieve_htmls)

    new_cols = final_df['description_sections'].apply(pd.Series)
    new_cols = new_cols.rename(lambda x: f"description_{x+1}", axis=1)
    final_df = pd.concat([final_df, new_cols], axis=1)
    final_df.drop(['description_sections', 'id'], axis=1, inplace=True)

    final_df.to_excel('descriptions.xlsx', sheet_name='Sheet1', index=None)
