items=[{'id':1,'name':'mobile','cost':12000,'rating':4.2,'brand':'Redmi','category':'Electronics','discount':10},{'id':2,'name':'tablet','cost':300,'rating':4.7,'brand':'Dolo','category':'Medicines','discount':30},{'id':3,'name':'laptop','cost':52000,'rating':4.0,'brand':'HP','category':'Electronics','discount':15},{'id':4,'name':'bat','cost':12000,'rating':4.5,'brand':'Li-Ning','category':'Sports','discount':30}]
print('''1.Sort by Name\n2.Sort by Brand\n3.Sort by discount\n4.Sort by rating\n5.Sort by price\n''')
value=int(input('Enter your choice\n'))
setV=['name','brand','discount','rating','price']
print('''\n1.High to low\n2.Low to high''')
order=int(input())
(items.sort(key=lambda el:el[setV[value-1]]))
print("-------------------------------------------")
print("Item","---",setV[value-1])
print("-------------------------------------------")
if order==1:
    items.reverse()
for item in items:
    print(item['name'],"---",item[setV[value-1]])