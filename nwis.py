import dataretrieval.nwis as nwis
from datetime import datetime, timedelta
BATT = '70969'
N_DAYS_AGO = 1
FILE_NAME = "sites.txt"
today = datetime.now()    
n_days_ago = today - timedelta(days=N_DAYS_AGO)
startDate=str(n_days_ago)[0:10]
site_file = open(FILE_NAME, "r")
sites =  site_file.readlines()

for site in sites:
    site=site.rstrip() #remove newline
    stuff = nwis.get_record(site=site,service="site")
    station_name = stuff.station_nm[0]
    print(station_name, end =": ")
    df = nwis.get_record(sites=site, service='iv', start=startDate,parameterCd=BATT)
    if not (BATT in df): 
        print("no "+BATT+" parm")
    else:  
        min_volts=99  
        for v in df[BATT]:
            volts = float(v)
            if volts < min_volts:
                min_volts=volts
        print(min_volts)
