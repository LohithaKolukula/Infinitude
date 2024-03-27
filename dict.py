dict = {'Id':1, 'Name':'Lohitha', 'Phone':99999, 'Marks':50, 'City':'Hyd'}
print(dict.keys())
print(dict.values())

dict.pop('City')
print(dict)

dict['car'] = 'Tesla'
print(dict)

print(list(dict))
print(list(dict.keys()))
print(list(dict.values()))