# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={'Maths':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
total=sum(courses.values())
print(total)
percentage=total/5
print(percentage)
# Insert percentage formula

# Print the percentage




# Create the Dictionary
mathematics={"Geoffrey Hinton":78,'Andrew Ng':95,'Sebastian Raschka':65,"Yoshua Bengio":50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

topper=max(mathematics,key=mathematics.get)
print(topper)

# Given string

first_name=topper.split()[0]
last_name=topper.split()[1]
# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string
full_name=last_name+" "+first_name
# print the full_name
certificate_name=full_name.upper()
# print the name in upper case
print('certificate_name is',certificate_name)
# Code ends here


