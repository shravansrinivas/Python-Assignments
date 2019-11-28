class product:
    def __init__(self,id,name,price,rating,discount,brand,category):
        self.name=name
        self.id=id
        self.price=price
        self.rating=rating
        self.discount=discount
        self.brand=brand
        self.category=category
    def display(self):
        print(self.name,"\t",self.brand,"\t",self.discount)
p1=product(1,"Note 4 pro",12500,4.3,40,"Redmi","Mobiles")
p2=product(2,"Badminton Raquet",2500,4.6,30,"Yi-Ning","Sports")
p3=product(3,"Pavilion",52000,4.5,20,"HP","Laptops")

products=[p1,p2,p3]

sort=['name','price','rating','discount']
print('''1.Sort by Name\n2.Sort by price\n3.Sort by rating\n4.Sort by discount\n''')
value=int(input('Enter your choice\n'))
x=[]
for i in products:
    x.append(getattr(i,sort[value-1]))

(products.__getattribute__().sort(key=lambda el:el[sort[value-1]]))

for item in items:
    print(item['name'],"---",item[sort[value-1]])