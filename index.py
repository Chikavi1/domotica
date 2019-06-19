from firebase import firebase

firebase = firebase.FirebaseApplication('https://domotica-2020.firebaseio.com/',None)

# post data


# data = {
# 	'Name':'chikavi',
# 	'RollNo':1,
# 	'Percentage' : 76.02
# }
# result = firebase.post('/python-sample-ed7f7/students/',data)
# print(result)

# get data

#result = firebase.get('/python-sample-ed7f7/students/','')
#print(result)

# update data

#firebase.put('/python-sample-ed7f7/students/-Lh7FcmOAqM_6ONwtxP7','Name','Luis Rojas')
#print('updated')

#delete data
#firebase.delete('/python-sample-ed7f7/students','Lh7FcmOAqM_6ONwtxP7')
#print('deleted')

result = firebase.get('/temperatura','')
print(result)