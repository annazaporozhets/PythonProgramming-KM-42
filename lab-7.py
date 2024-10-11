from datetime import datetime
data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, '2020-01-30T11:45:33.654357'),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, '1985-04-02T22:45:45.045385'),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, '2010-10-10T10:00:00.000000'),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, '2008-02-28T23:33:33.000000'),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, '2021-09-29T07:34:01.000143'),
]

title = "|-----------+---------------------+-----------+-----------+---------------------+--------+------+----------------------------|"

#List to format column titles for table headers
list1 = list(data[0])   
elem1 = '|{:^11}|'.format(list1[0])
elem2 = '{:^21}|'.format(list1[1])
elem3 = '{:^11}|'.format(list1[2]) 
elem4 = '{:^11}|'.format(list1[3])
elem5 = '{:^21}|'.format(list1[4])
elem6 = '{:^8}|'.format(list1[5])
elem7 = '{:^6}|'.format(list1[6])
elem8 = '{:^28}|'.format(list1[7])

#Combine all title elements into a single row string and print
elem = elem1 + elem2 + elem3 + elem4 + elem5 + elem6 + elem7 + elem8
print(elem)
print(title)
for line in data[1:]:
    (post_code, cost, country, city, street, build, app, dt) = line
    cost_thousand = cost / 1000    #Convert cost from units to thousands
    cost_thousand_form = f"{cost_thousand:.3f}"      #Format cost to 3 decimal places
    dates = datetime.fromisoformat(dt).isoformat(timespec = 'microseconds')    #Format the date to include microseconds
    '|{:<27}|'.format(dates)
    print(f"| {post_code:<10}| {cost_thousand_form:>19} | {country:<9} | {city:<10}| {street:<20}|{build:>7} | {app:>5}| {dates} |" )
    





