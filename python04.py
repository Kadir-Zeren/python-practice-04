num1 = 25
num2 = float(num1)
print(type(num2))

fruit = 'Orange'
print( 'Word: ', fruit)
print('First letter: ', fruit[0])
print('Second letter:', fruit[1])
print("3rd to 5th letters:", fruit[2:5])
print("Letter all after 3rd:", fruit[2:])

text = 'Clarusway'
text[3]
text[4:7]

city = 'Phoenix'
print(city[1:])# starts from index 1 to the end
print(city [ :6])# starts from zero to 5th index
print(city[ :: 2]) # starts from zero to end by 2 step
print(city[1 :: 2])# starts from index 1 to the end by 2 step
print(city[-3:])# starts from index -3 to the end
print(city[ ::- 1]) # negative step starts from the end to zero

text = 'kayak'
text == text[: :- 1]
yeni_text = 'abcdef'
yeni_text == yeni_text[ ::- 1]

animal = "hippopotamus"
print(animal[1:])
print(animal [ :6])
print(animal[ :: 2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[ ::- 1])

vegetable = "Tomato"
print('length of the word', vegetable, 'is :', len(vegetable))