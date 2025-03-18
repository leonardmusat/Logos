import requests
import urllib.request
import pandas as pd
import os

def read_parquet(path, folder = "logo_image"):
    df = pd.read_parquet(path)
    lst = df.values.tolist()
    flat_list = [el[0] for el in lst]
    for el in flat_list:
        logo_url = get_company_logo(el)

        if logo_url:
            filename = os.path.join(folder, f"{el.replace('.', '_')}.png")  
            try:
                urllib.request.urlretrieve(logo_url, filename)
                print(f"Downloaded: {filename}")
            except urllib.error.HTTPError as e:
                print(f"Error downloading {el}: {e}")
            except Exception as e:
                print(f"Error downloading {el}: {e}")
        else:
            print(f"Logo not found for: {el}")

def get_company_logo(domain):
    url = f"https://logo.clearbit.com/{domain}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return url  
    else:
        return None
    
read_parquet("logos.snappy.parquet")

