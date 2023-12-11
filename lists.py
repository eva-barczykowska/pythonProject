languages = ['english', 'hindi', 'spanish', 'italian', 'german', 'russian', 'french']

had_at_school = languages[-1]
print(had_at_school)

really_good_at = languages[0]
print(really_good_at.title())

message = f"My favourite languages are {languages[0].title()} and {languages[4].title()}."

print(message)

languages.append("czech")
print(languages)

print('\t')
cars = ['bugatti', 'maserati', 'fiat', 'opel', 'volvo', 'fiat126p']
print(cars)
del cars[0]
print(cars)

my_car = cars.pop()
print(my_car)

too_expensive = 'maserati'
cars.remove(too_expensive) #remove deletes only THE FIRST OCCURENCE of value we specify
print(cars)

print('\t')
bikes = ['harley davidson', 'suzuki', 'vespa', 'ducati', 'enfield']
print(bikes)
bikes.sort() #sort is mutating in python
print(bikes)

bikes.sort(reverse=True)
print(bikes)

bikes = ['harley davidson', 'suzuki', 'vespa', 'ducati', 'enfield']
print(sorted(bikes)) #it is possible to use SORTED to sort temporarily

print('\t')
animals = ['fox', 'dog', 'cat', 'crocodile', 'zebra', 'pyton']
animals.reverse() # I need to call it on the list first and then only I can print
print(animals)
print(len(animals))




