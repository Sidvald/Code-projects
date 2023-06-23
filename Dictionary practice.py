#Dictionary practice (City info bot)

cities = {
    "City1": "Washington DC", "City2": "Oslo",
    "City3": "Istanbul", "City4": "Stockholm",
    "City5": "Seattle", "City6": "Paris"
}

#All the information was the first thing that appeared on google. Any tips on presenting information in a more tidy way would be appreciated! (Tips in general also)
information = {
"info1": "Washington, D.C., is the capital city of the United States, located between Virginia and Maryland on the north bank of the Potomac River. The city is home to all three branches of the federal government, as well as the White House, the Supreme Court and the Capitol Building",
"info2": "Oslo is the oldest of the Scandinavian capitals, and its history goes back 1000 years, to the time when the first settlements were built at the inlet of the Oslo fjord. The capital of Norway is also its largest city. Oslo has over 600,000 inhabitants and covers 454 square kilometres, 242 of which are forests.",
"info3": "Istanbul is a transcontinental city, straddling the Bosphorus strait in northwestern Turkey between the Sea of Marmara and the Black Sea. Founded on the Sarayburnu promontory around 660 BC as Byzantium, the city now known as Istanbul developed to become one of the most significant cities in history.",
"info4": "Stockholm is Sweden's leading industrial area. Its major industries include metal and machine manufacturing, paper and printing, foodstuffs, and chemicals. It is also the country's chief wholesale and retail centre and serves as the headquarters of many banks and insurance companies.",
"info5": "Seattle (/siˈætəl/ ( listen) see-AT-əl) is a seaport city on the West Coast of the United States. It is the seat of King County, Washington. With a 2022 population of 749,256 it is the largest city in both the state of Washington and the Pacific Northwest region of North America.",
"info6": "Paris is the capital of France; over 2,2 million people live in this city. Paris is famous for its many highlights: monuments, museums, restaurants, fashion and its city landscape at the Seine. Paris has many beautiful hotels, cosy bars and restaurants. While searching for an accommodation in Paris, you will quickly realize that there’s endless possibilities. Paris was conquered by Julius Caesar in 52 BC. Gradually, little villages developed around the little islands of the Seine, the people living there were called the Parissii.",
   
}

for city in cities.values():
    print(city)

city_choice = input("What city would you like to learn about?\n")

if city_choice == "Washington DC":
    print(information["info1"])
elif city_choice == "Oslo":
    print(information["info2"])
elif city_choice == "Istanbul":
    print(information["info3"])
elif city_choice == "Stockholm":
    print(information["info4"])
elif city_choice == "Seattle":
    print(information["info5"])
elif city_choice == "Paris":
    print(information["info6"])
else:
    print("Not a valid option")


    
        

    



