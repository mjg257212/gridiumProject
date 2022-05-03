from bs4 import BeautifulSoup
import requests

LOCATIONS = [
              'Half Moon Bay, California\n'   ,
              'Huntington Beach, California\n',
              'Providence, Rhode Island\n'    ,
              'Wrightsville Beach, North Carolina\n'
            ]

LOW_TIDE_KEY = 'Low Tide'

URLS = [
         'https://www.tide-forecast.com/locations/Half-Moon-Bay-California/tides/latest'   ,
         'https://www.tide-forecast.com/locations/Huntington-Beach-California/tides/latest',
         'https://www.tide-forecast.com/locations/Providence-Rhode-Island/tides/latest'    ,
         'https://www.tide-forecast.com/locations/Wrightsville-Beach-North-Carolina/tides/latest'
       ]

if __name__ == '__main__':

  nUrl = -1

  for url in URLS:

    nUrl = nUrl + 1

    result = requests.get( url )

    doc = BeautifulSoup( result.text, 'html.parser' )

    rows = doc.find_all( [ 'tr' ] )

    print( "\nLow Tide Stats for " + LOCATIONS[ nUrl ] )

    for row in rows:
      txt = row.text

      if( txt.find( LOW_TIDE_KEY ) >= 0 ):
        print( txt )
