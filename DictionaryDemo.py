friends = {'tom' : "111-22-333",
           'jerry' : '222-33-444'}

print(friends)

#Reterving elements from the dictionary

print(friends['tom'])


#Adding elements into dictionay

friends['bob']='666-777-888'

print(friends)

#Modifying elements into dictionary

friends['bob']='666-777-999'

print(friends)


#Deleting elements from the dictionary

del friends['bob']

print(friends)