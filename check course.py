import requests
import argparse
import json

#Read command line arguments to determine what to search
parser = argparse.ArgumentParser()
parser.add_argument("term", help="The term to search for")
parser.add_argument("subject", help="The subject code for the course")
parser.add_argument("coursenum", help="""The number of the course to search for. \
  Note: Include extra symbols such as 'R' for enriched courses""")
args = parser.parse_args()

#Get the API token from the config file
with open("config.txt", "r") as f:
   api_token = f.readline()

#Create the url to query the API with
endpoint = """https://api.uwaterloo.ca/v2/terms/{}/{}/{}/schedule.json?key={}\
""".format(args.term, args.subject, args.coursenum, api_token)

#Query the API
json = requests.get(endpoint).json()

#Ensure the response was received
status_code = json['meta']['status']

#Notify and exit if there are errors
if status_code is not 200:
    error_message = json['meta']['message']
    print("Error getting course data: {}".format(error_message))
    quit()

#Parse json response
for course in json['data']:
   course_section = course['section']
   if 'LEC' in course_section or 'LAB' in course_section:
       enrol_cap = course['enrollment_capacity']
       enrol_tot = course['enrollment_total']

       #Notify if there are empty spots
       if(enrol_cap > enrol_tot):
            empty_spots = int(enrol_cap) - int(enrol_tot)

            #Get the instructor's name
            professor = course['classes'][0]['instructors'][0]
            #Change from lastname, firstname to firstname lastname
            names = professor.split(',')
            professor = "{} {}".format(names[0], names[1])

            print("There are {} empty spots in {} with {} as the instructor".format(
            empty_spots, course_section, professor))
