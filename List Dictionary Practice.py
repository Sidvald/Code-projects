

list = [
    {
        "id": 0,
        "First Name": "Sarah",
        "Last Name": "Lastname",
        "Address": "51B Address lane",

    },

    {
        "id": 1,
        "First Name": "Mike",  
        "Last Name": "Lastname",
        "Address": "41A Address Street",
    },

    {
        "id": 2,
        "First Name": "Trevor", 
        "Last Name": "Lastname",
        "Address": "31 Address venue",
    },
    
]

new_id = len(list)
new_first_name = input("Enter your first name: ")
new_last_name = input("Enter your last name: ")
new_address = input("Enter your address: ") 

new_dictionary = {
    "id": new_id,
    "First Name": new_first_name,
    "Last Name": new_last_name,
    "Address": new_address, 
}

list.append(new_dictionary)
print(list)