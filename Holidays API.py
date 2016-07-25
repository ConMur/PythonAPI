import requests
import json

#API Key
key = "5b4eb360-0397-415e-b0a9-e38738177f6e"

#List of countries supported by the API and their short forms
countryList = {"BE": "Belgium","BG": "Bulgaria", "BR": "Brazil", "CA": "Canada", "CZ": "Czech Republic", "DE" :"Germany", "ES": "Spain", "FR": "France", "GB":"United Kingdom", "GT":"Guatemala","HR":"Croatia", "HU":"Hungary", "ID":"Indonesia", "IN":"India", "IT":"Italy", "NL":"Netherlands", "NO":"Norway", "PL":"Poland", "PR":"Puerto Rico", "SI":"Slovenia", "SK":"Slovakia", "US":"United States"}

#List of months
monthList = ["01", "02","03","04","05","06","07","08","09","10","11","12"]

#ITS [CURRENT YEAR]
year = "2016"

#Get the country from the user
country = input("Enter a country: ")

#Check to see if they entered the country code instead of the country's common name
if len(country) is 2 and country in countryList:
    countryCode = country
else:
    try:
        countryCode = countryList[country]
    except:
        print("Invalid country, using Canada as default.")
        countryCode = "CA"

#Get the month from the user
month = input("Enter a month: ")

monthNumber = "12"

#Validate the month
if len(month) is 1:
    month = "0" + month

if(month not in monthList):
    print("Invalid month, using December as default.")
else:
    monthNumber = month

#Form the API Request and send it
apiRequest = "https://holidayapi.com/v1/holidays?country=" + str(countryCode) + "&year=" + str(year) + "&month=" + str(monthNumber) + "&key=" + key

response = requests.get(apiRequest)

json_data = json.loads(response.text)

#Parse the status of the response and display result to user if there is an error
status = str(json_data["status"])
if status != "200":
    if "4" in status:
        print("Something wrong on this end (Status Code - " + status + ")")
    elif "5" in status:
        print("Something wrong with the server (Status Code - " + status + ")")
    else:
        print("Unknown status code (Status Code - " + status + ")")

print("")#Blank line

numHolidays = 0

#List each holiday for this month
for holiday in json_data["holidays"]:
    numHolidays += 1
    #Print data about the holiday
    print("Holiday Name: " + holiday["name"])
    print("Holiday Date: " + holiday["date"])
    print("Date Observed: " + holiday["observed"])
    print("")#Blank line
    public = (holiday["public"] == "True")

#Display a message if there are no holidays this month
if numHolidays is 0:
    print("No holidays this month")

