dict1 = {'Newfoundland': 'A',
        'Nova Scotia': 'B',
        'Prince Edward Island': 'C',
        'New Brunswick': 'E',
        'Quebec': 'G',
        'Quebec': 'H',
        'Quebec' : 'J',
        'Ontario': 'K',
        'Ontario': 'L',
        'Ontario': 'M',
        'Ontario': 'N',
        'Ontario': 'P',
        'Manitoba': 'R',
        'Saskatchewan': 'S',
        'Alberta': 'T',
        'British Columbia': 'V',
        'Nunavut': 'X',
        'Northwest Territories': 'X',
        'Yukon': 'Y'
        }
index = input("Enter the postal code in the format D#R:")
index = index.upper()
if len(index) == 3:
    if index[0].isalpha() and index[1].isdigit() and index[2].isalpha():
        region_num = index[0]
        region_code = index[1]
        region_name = dict1.get(region_num)
        if region_name:
            if region_code == '0':
                region_area = "rural"
            else:
                region_area = "urban"
                print(f"The addressee is located in {region_area} area of the province {region_name}.")
        else:
            print("The entered index does not correspond to any of the provinces.")
    else:
        print("Error!The index format you entered is incorrect! Enter a letter, number, and letter.")        
else:
    print("Error! Enter three characters.")
    
    
    #Не розібралась з тим, чому не виводить правильний результат, а показує лише те, що немає такої провінції.