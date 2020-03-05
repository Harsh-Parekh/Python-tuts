dict={'key':'value','name':'Nimesh',"marks":99,'k6':"Harshal","k7":88.8}

print(dict)
#{'key': 'value', 'name': 'Nimesh', 'marks': 99, 'k6': 'Harshal', 'k7': 88.8}

print(dict['k6'])
#Harshal

dict['k7']=99

print(dict)
#{'key': 'value', 'name': 'Nimesh', 'marks': 99, 'k6': 'Harshal', 'k7': 99}

print(type(dict))
#<class 'dict'>