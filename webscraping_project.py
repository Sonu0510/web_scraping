
from bs4 import BeautifulSoup
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)
# print(type(response))
# print(dir(response)) #-- to get methods for this class object

# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
# print(dir(soup))
# print(soup.prettify())

# To print all the text of given HTML page
entire_body_text = soup.select("body")
# print(entire_body_text) 


# entire_body_text gives data in a list that is why we are using indexing
# print(entire_body_text[0].getText())

world_data = soup.find("tbody").find_all("tr") # world_data is a list-contains all the rows table body
# print(world_data[8].getText()) # getting text of 8th item from world_data list
# world_data = soup.find("tbody").find("tr")

# print(world_data[9].getText())

# for data in world_data:
#     print(data)
#     break

# print(len(world_data))


complete_data = []
for i in range(8, len(world_data)):
    data = []
    list_data = world_data[i].find_all("td")
    # print(list_data)
    # print(len(list_data))
    # break

    for col in list_data:
        data.append(col.getText())

    complete_data.append(data)

# print(complete_data[:2])

# for item in complete_data:
#     print(item)
# print(complete_data)


# print(complete_data[0])

cleaned_data = list(map(lambda x: x[1:10] + [x[12]] + [x[14]], complete_data))
# print(len(cleaned_data))
# print(cleaned_data[0])
# print(len(cleaned_data[0]))


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


# list_2d = [[1,2],[3,4]]
df = pd.DataFrame(cleaned_data, columns= column_name)
# print(df)

first_five_row = df.head()
# print(first_five_row)


df.to_csv("covid_data.csv", index=	False)

# Read csv file
df_read = pd.read_csv("covid_data.csv")
# print(df_read.head())

# print(df_read.isnull().sum())

missing_data = df_read.isnull().sum()
# print(missing_data)

# Visulaization
# print(df_read.isnull())


# sns.heatmap(df_read.isnull().T)
# plt.show()

# missing_data.plot(kind="barh") # h is added for horizontal bar graph
# plt.title("Show missing data")
# plt.xlabel("Number of missing data country")
# plt.ylabel("Category")
# plt.show()

# print(missing_data.values)
# print(missing_data.index)

# Bar Diagram
# fig = px.bar(x = missing_data.index, y = missing_data.values)
# fig.show()

# pie-chart
# fig = px.pie(values = missing_data.values, names = missing_data.index)
# fig.show()


""" Country wise total cases """

# print(df_read)

# Check daty_types before plotting
# print(df_read.dtypes)


# Data preparation - typecast object to integer
# total_cases_in_int_data = df_read["total_cases"].map(lambda x: int(x.replace(",", "")))
# print(total_cases_in_int_data)


x = df_read["names"]
y = df_read["total_cases"].map(lambda x: int(x.replace(",", "")))

fig = px.bar(x=x, y =y)
fig.show()





