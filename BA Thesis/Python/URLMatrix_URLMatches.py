

import pandas as pd
import numpy as np

#################################################################

firms = pd.read_csv(r"COMPLETE_URLS_SALES.csv")
sdc = pd.read_csv(r"SDC_ACQUIROR_URLs.csv")

#################################################################

firms_names = firms['conml'].tolist()
sdc_names = sdc['AcquirorName'].tolist()

main_urls = firms['url'].tolist()
sdc_urls = sdc['url'].tolist()

#################################################################

firm_url_store = []

sdc_url_store = []

for index, url in enumerate(main_urls):
    url = str(url)
    url = url.split("'")
    for location, rawurl in enumerate(url):
        if len(rawurl) < 5:
            del url[location]

    firm_url_store.append(url)

for index, url in enumerate(sdc_urls):
    url = str(url)
    url = url.split("'")
    for location, rawurl in enumerate(url):
        if len(rawurl) < 5:
            del url[location]

    sdc_url_store.append(url)

#################################################################

url_matches = np.zeros((int(len(firm_url_store)),int(len(sdc_url_store))))

counter = 0

for frim_index, firm_url in enumerate(firm_url_store):

    for sdc_index, sdc_url in enumerate(sdc_url_store):

        intersection = set(sdc_url).intersection(firm_url)

        url_matches[frim_index,sdc_index] = len(intersection)

    counter = counter + 1

    if counter%50 == 0:
        print("At index: ", counter, " ", round(counter*100/len(firm_url_store),2), " %" )

#################################################################

named_matches = []

counter = 0

for firm_index, firm_name in enumerate(firms_names):

    for sdc_index, sdc_name in enumerate(sdc_names):

        matchcount = url_matches[firm_index,sdc_index]

        if matchcount > 0:
            match = [firm_name,sdc_name,matchcount]
            named_matches.append(match)

    counter = counter + 1

    if counter%50 == 0:
        print("At index: ", counter, " ", round(counter*100/len(firm_url_store),2), " %" )


#################################################################

matches_array = np.array(named_matches)

matches_df = pd.DataFrame(matches_array)

matches_df.to_csv("URLMatchesV1.csv", encoding = "utf-8")