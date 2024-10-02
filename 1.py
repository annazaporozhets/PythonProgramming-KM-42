#Start of the data entry block
name = input("Enter first name:")      #Entering a first name
surname = input("Enter last name:")      #Entering a last name
tel_number = input("Enter phone number:")     #Entering s phone number
num_street = input("Enter the street name:")   #Entering a street name
num_house = input("Enter the house number:")    #Entering a house number
num_apart = input("Enter the apartment number:")   #Entering an apartment number
city = input("Enter city:")      #Entering city
city_index = input("Enter the city index:")    #Entering a city index
country = input("Enter country:")    #Entering country
#Finish of the data entry block

#Data output block
print(name , surname, '\n' ,       
    tel_number, '\n' ,
    "Str." , num_street , num_house , "ap." , num_apart , city, '\n' ,
    city_index, '\n' ,
    country)      