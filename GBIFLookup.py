import requests

# Playing around with GBIF's free name matching API

print("Input Kingdom: ")

kingdom = input()

print("Input Species name: ")

species_name = input()

response = requests.get("https://api.gbif.org/v1/species/match?verbose=true&kingdom=" + kingdom + "&name=" + species_name).json()

print(response)
print(response["canonicalName"])