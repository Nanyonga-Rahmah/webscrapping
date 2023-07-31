#LISTS
#1
names=["Rahmah","Mahad","Rahim","Akram","Hawah"]
print(names[1])
#2
names[0]="ZZiwa"
print(names)
#3
names.insert(5,"Azzawi")
print(names)
#4
names.insert(2,"Bathel")
print(names)
#5
names.pop(3)
print(names)
#6
print(names[-1])
#7
numbers=[1,2,3,4,5,6,7]
print(numbers[2:5])
#8
countries=["Uganda","Kenya","Albama","Congo"]
new_countries=countries.copy()
print(new_countries)
#9
for country in countries:
    print(country)
#10
animals=["dog","cat","cow","goat","sheep"]
   #sorting in ascending
animals.sort()
print(animals)
   #sorting in descending
animals.reverse()
print(animals)
#11
for animal in animals:
    if "a" in animal:
        print(animal)
#12
first_name=["Nanyonga"]    
Last_name=["Rahmah"]  
result=first_name + Last_name    
print(result)

#TUPLES
#1
x=("samsung","iphone","tecno","redmi")
print(x[1])
#2
print(x[-2])
#3
x=list(x)
x[1]="itel"
x=tuple(x)
print(type(x))
print(x)
#4
x=list(x)
x.append("Huawei")
x=tuple(x)
print(x)
#5
for phone in x:
    print(phone)
#6
x=list(x) 
x.pop(0)
x=tuple(x) 
print(x)  
#7
cities=tuple(["Kampala","Mukono","Mbarara","Nairobi","Dodoma"])
#8
(Uganda,Dubai,Tahoma,Tanzania,Kenya)=cities
print(Uganda)
#9
print(cities[1:4])
#10
my_first_name=("Nanyonga")
my_last_name=("Rahmah")
my_name=my_first_name + my_last_name
print(my_name)
#11
colors=("red","yellow","green")
print(colors*3)

#12
thistuple=(1,3,7,8,7,5,6,8,5)
count=0
for i in thistuple:
    if i==8:
        count+=1
        continue
print(count)    

#SETS
#1
drinks=set(("oner","mirinda","coke"))
#2
drinks.add(("water"))
drinks.add(("beer"))
print(drinks)
#3
mySet={"oven","kettle","microwave","refrigerator"}
print("microwave" in mySet)
#4
mySet.remove("kettle")
print(mySet)
#5
for item in mySet:
    print(item)
#6
set_items={1,2,3,4} 
list_items=[5,6,7,8]
set_items.update(list_items) 
print(set_items)  
#7
ages={21}
names={"Nanyonga Rahmah"}
ages.update(names)
print(ages)

#STRINGS
#1
your_name="Nanyonga Rahmah"
your_age=21
print(f"My name is {your_name} and my age is {your_age}")
#2
txt="   Hello,  Uganda!"
print(txt.strip())
#3
print(txt.upper())
#4
print(txt.replace("U","V"))
#5
y="I am proudly Ugandan"
print(y[1:5])
#6
x='All "Data Scientists" are cool'
print(x)




#DICTIONARIES
#1 Output value of the shoe size
Shoes = {"brand": "Nick", "color": "black", "size": 40}
s_size = Shoes["size"]
print(s_size)

#2 Change Nick to Adidas
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes["brand"] = "Adidas"
print(Shoes)

#3 Add key/value pair type = sneakers
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes["type"] = "sneakers"
print(Shoes)

#4 Return a list of all keys
Shoes = {"brand": "Nick", "color": "black", "size": 40}
keys = list(Shoes.keys())
print(keys)

#5 Return a list of all values
Shoes = {"brand": "Nick", "color": "black", "size": 40}
values = list(Shoes.values())
print(values)

#6 Check if size exists in the dictionary
Shoes = {"brand": "Nick", "color": "black", "size": 40}
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

#7 Loop through the dictionary
Shoes = {"brand": "Nick", "color": "black", "size": 40}
for key, value in Shoes.items():
    print(key, ":", value)

#8 Remove color from the dictionary
Shoes = {"brand": "Nick", "color": "black", "size": 40}
del Shoes["color"]
print(Shoes)

#9 Emptying the dictionary
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes.clear()
print(Shoes)

#10 Write a dictionary and make a copy of it
orgnl = {
    "name": "Nanyonga Rahmah", 
    "age": 21, 
    "regNO": "21/U/11530", 
    "stdtNo": 2100711530
    }
cpy = orgnl.copy()
print(cpy)

#11  Nested Dictionaries
person = {
    "name": "Gray",
    "age": 40,
    "address": {
        "District": "Wakiso",
        "city": "Kampala",
        "country": "Uganda"
    }
}
print(person)