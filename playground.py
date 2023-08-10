
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

world_data = soup.find("tbody").find_all("tr")


complete_data = []
for i in range(8, len(world_data)):
    data = []
    list_data = world_data[i].find_all("td")

    for col in list_data:
        data.append(col.getText())

    complete_data.append(data)

cleaned_data = list(map(lambda x: x[1:10] + [x[12]] + [x[14]], complete_data))

column_name = [
    "names", 
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_recovered",
    "new_recovered",
    "active_cases",
    "serious_cases",
    "total_tests",
    "population"
]

df = pd.DataFrame(cleaned_data, columns= column_name)

df.to_csv("covid_data.csv", index=	False)

