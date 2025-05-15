numbers: list[int] = [1, 10, 5, 3]
sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers) #OUTPUT: [1, 3, 5, 10]
# It will not return to us a sorted object.
# It just returns to us the numbers directly.
# And what it does by default is sort the elements in ascending order.

# To sort the elements in descending order.
print(sorted(numbers, reverse=True)) #OUTPUT: [10, 5, 3, 1]

people: list[str] = ['Anna', 'Bob', 'Betty', 'James', 'John']
sorted_names: list[str] = sorted(people)
print(sorted_names) #OUTPUT: ['Anna', 'Betty', 'Bob', 'James', 'John']
# Strings are sorted by their Ascii value.

print(sorted(people, reverse=True)) #OUTPUT: ['John', 'James', 'Bob', 'Betty', 'Anna']

people: list[str] = ['Mario', 'James', 'Anna', 'Tom']
sorted_names: list[str] = sorted(people, key=lambda x: len(x))
print(sorted_names) #OUTPUT: ['Tom', 'Anna', 'Mario', 'James']
# Mario and James are going to remain where they are because it has no information regarding how those
# should be sorted.

class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name} = {self.weight}kg'

cat: Animal = Animal('Cat', 10)
dog: Animal = Animal('Dog', 5)
kangaroo: Animal = Animal('Kangaroo', 50)

sorted_animals = sorted([cat, dog, kangaroo], key=lambda animal: animal.weight)
print(sorted_animals) #OUTPUT: [Dog = 5kg, Cat = 10kg, Kangaroo = 50kg]

sorted_animals = sorted([kangaroo, cat, dog], key=lambda animal: animal.name)
print(sorted_animals) #OUTPUT: [Cat = 10kg, Dog = 5kg, Kangaroo = 50kg]






