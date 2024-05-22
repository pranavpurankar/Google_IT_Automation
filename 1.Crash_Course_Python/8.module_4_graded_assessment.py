'''
Tessa and Rick are hosting a party. Both sent out invitations to their friends, and each one 
collected responses into dictionaries, with names of their friends and how many guests each 
friend was bringing. Each dictionary is a partial guest list, but Rick's guest list has more 
current information about the number of guests.

Complete the function to combine both dictionaries into one, with each friend listed only 
once, and the number of guests from Rick's dictionary taking precedence, if a name is 
included in both dictionaries. Then print the resulting dictionary. This function should:

1.accept two dictionaries through the function’s parameters;

2.combine both dictionaries into one, with each key listed only once;

3.the values from the “guests1” dictionary taking precedence, if a key is included in both dictionaries;

4.then print the new dictionary of combined items.
'''

def combine_guests(guests1,guests2):
    guests2.update(guests1)# Use a dictionary method to combine the dictionaries
    return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}
