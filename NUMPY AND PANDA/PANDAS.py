import pandas as pd

# series = a pandas 1D labeled array that can hold any data type
    #      Its like a single column in spreadsheet

#data = [100,102,104,202,200]
#series = pd.Series(data, index = ["A","B","C","D","E"])
#series.loc["A"] = 6969
#print(series.iloc[0])
#print(series[series >= 199])

#EXAMPLE
#pokemon = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard"]

#List_pokemon = pd.Series(pokemon,index = [0,1,2,3,4,5])
#print(List_pokemon)


#dataframe = A tabular data structure with rows and columns (2 Dimensional)

data = {
    "Name" : ["A","B","C"],
    "Age" : [30,35,66]
}
df = pd.DataFrame(data, index= ["EMP 1","EMP 2","EMP 3"])

#ADD A NEW COLUMN
df["job"] = ["Cook","Cashier","Manager"]

#add a new rows
new_rows = pd.DataFrame([{"Name" : "sandy", "Age" : 27, "job" : "Scientist"}
                         ,{"Name" : "patrick", "Age" : 35, "job" : "Manager"}],
                       index = ["EMP 4","EMP 5"])
df = pd.concat([df, new_rows])


print(df)
