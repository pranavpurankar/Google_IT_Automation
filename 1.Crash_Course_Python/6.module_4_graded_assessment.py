'''
A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list
of students in the order they arrived in the classroom. Aniyah was the first one to note which
students arrived, and then Imani took over. After class, they each entered their lists into 
the computer and emailed them to the professor. The professor wants to combine the two lists 
into one and sort it in alphabetical order.

Complete the code by combining the two lists into one and then sorting the new list. 
This function should:

1.accept two lists through the function’s parameters;,

2.combine the two lists;

3.sort the combined list in alphabetical order;

4.return the new list.

'''
def alphabetize_lists(list1,list2):
    new_list = [] # Initialize a new list
    combined_list = list1+list2 # Combine the lists.
    cobined_list = combined_list.sort() # Sort the combined lists.
    new_list = combined_list # Assign the combined lists to the "new_lists"
    return new_list

Aniyahs_list = ["Jacomo","Emma","Uli","Nia","Imani"]
Imanis_list = ["Loik","Gabriel","Ahmed","Soraya"]


print(alphabetize_lists(Aniyahs_list,Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
