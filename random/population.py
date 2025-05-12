# Population Density
# Given a country name, return the population density of that country.
# Population density is defined as the number of people per unit area.
# Population density = population / area

import requests

def getPopulationDensity(name):
    
    url = f"https://jsonmock.hackerrank.com/api/countries?name={name}"

    
    resp =  requests.get(url).json()
    
    data = resp["data"]
    
    if data:
        population = data[0]["population"]
        
        area = data[0]["area"]
        
        populationDensity = round(population / area)
    
        return populationDensity
        
    return -1

# Test cases
print(getPopulationDensity("India")) # 388