#oefening 1

# import csv

# with open('boeken.csv', 'r', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter= ",")
#     for line in csv_reader:
#          print(line)

# nieuwe_boeken = [
#     ['Book1', 'Author1', 'Genre1', '19.99'],
#     ['Book2', 'Author2', 'Genre2', '29.99'],
#     ['Book3', 'Author3', 'Genre3', '39.99']
# ]
# with open('boeken.csv', 'a', newline='') as csv_file:
#      csv_writer = csv.writer(csv_file, delimiter=',')
#      csv_writer.writerows(nieuwe_boeken)

#-------------------------------------------------------------------

# #oefening 2.1

# import csv

# def aantal_landen():

#     with open('landen.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         count = 0
#         for line in csv_reader:
#             count += 1  
#         print("aantal landen:", count)

# aantal_landen()

# # oefening 2.2
# def grootste_bevolking():
    
#     grootste_bevolking = 0
#     grootste_land = ""

#     with open('landen.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)  
#         #zeker next() doen want anders in for loop error, want verwacht int, maar eerste lijn is enkel strings
#         next(csv_reader)
#         for line in csv_reader:
#             land, Bevolking = line        
#             if int(Bevolking) > int(grootste_bevolking):
#                 grootste_bevolking = Bevolking
#                 grootste_land = land
#         print("Het land met de meeste inwoners is ",grootste_land,"met ",grootste_bevolking,"inwoners.")

# grootste_bevolking()

# # oefening 2.3

# def gemiddelde_bevolking():

#     with open("landen.csv", "r") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)

#         inwoners = 0
#         count = 0

#         for line in csv_reader:
#             land, bevolking = line
#             inwoners += int(bevolking)
#             count +=1
#         print("Het gemiddelde van alle inwoners over alle landen is: " ,inwoners/count)

# gemiddelde_bevolking()


#---------------------------------------------------------------------------
# # oefening 3
# import csv

# with open("schrijven.csv", "w") as new_file:
#     csv_writer = csv.writer(new_file, delimiter=",")

#     data=[
#         ["Land","Bevolking"],
#         ["Nederland",17000000],
#         ["België",11500000],
#         ["Duitsland",83000000],
#         ["Frankrijk",67000000],
#         ["Spanje", 47000000]
#     ]

#     csv_writer.writerows(data)

#-----------------------------------------------------------------------------
# #oef 4

# import csv
# def totale_verkoopwaarde():
#     with open("winkelverkocht.csv","r") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         waarde = 0

#         for line in csv_reader:
#             datum, product, hoeveelheid, verkoopwaarde = line
#             waarde += float(verkoopwaarde)
#         print(round(waarde,2))

# totale_verkoopwaarde()

# def meest_verkocht():
#     with open("winkelverkocht.csv","r") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
        
#         items = {}

#         for line in csv_reader:
#             datum, product, hoeveelheid, verkoopwaarde = line
#             if str(product) not in items:
#                 items[product] = int(hoeveelheid)
#             else:
#                 items[product] += int(hoeveelheid)
#         print(items)

#     #onderstaande = max zoeken in dictionary. mijn oplossing. Beter oplossing = met max() functie werken
#         meest = 0
    
#         for key, value in items.items():
#             if int(value) > meest:
#                 meest = int(value)
#             if value == meest:
#                 pr = key
#         print("Het meest verkochte product is ", pr, "met een aantal van ", meest)

# meest_verkocht()


# def Hoogste_verkoop():
#     with open("winkelverkocht.csv","r") as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         waarde = 0
#         dag = ""         

        
#         for line in csv_reader:
#             datum, product, hoeveelheid, verkoopwaarde = line
#             if float(waarde) < float(verkoopwaarde):
#                 waarde = verkoopwaarde
#                 dag = line[0]
#     print("De dag met meeste verkoop was ",dag)        
                  
# Hoogste_verkoop()

# def gemiddelde_verkoopwaarde_per_dag():
#     totaal=0
#     aantal=0
#     with open('winkelverkocht.csv','r') as csv_file:
#         csv_reader=csv.reader(csv_file)
#         next(csv_reader)
#         for line in csv_reader:
#             datum,product,hoeveelheid,verkoopwaarde=line
#             totaal+=float(verkoopwaarde)
#             aantal+=1
#     gemiddelde=totaal/aantal
#     print(f"Het gemiddelde van de dagelijkse totale verkoopwaarde is: {round(gemiddelde,2)}")
# gemiddelde_verkoopwaarde_per_dag()

#--------------------------------------------------------------------------------------------------------

#oefeningen JSON

# import json

# gebruiker_gegevens={
#     "naam": "John Doe",
#     "leeftijd": "25",
#     "stad": "New York",
#     "e-mail": "john@example.com"
# }
# with open("gebruiker.json",'w') as json_bestand:
#     json.dump(gebruiker_gegevens, json_bestand)

# with open('gebruiker.json','r') as json_bestand:
#     gegevens=json.load(json_bestand)
#     # print(gegevens)

# gegevens['stad']='San Francisco'
# with open('gebruiker.json','w') as json_bestand:
#     json.dump(gegevens, json_bestand)
# print(gegevens)