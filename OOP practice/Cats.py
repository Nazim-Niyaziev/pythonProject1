from ClassCat import Cat

baron = Cat("Baron", 2, "male")
sam = Cat("Sam", 2, "male")
susana = Cat("Susana", 1, "female")

Baron_atr = [baron.name, baron.age, baron.gender]

Sam_atr = [sam.name, sam.age, sam.gender]

Susana_atr = [susana.name, susana.age, susana.gender]

print(f"Cat Baron\nname: {Baron_atr[0]}\nage: {Baron_atr[1]}\ngender: {Baron_atr[2]}\n")
print(f"Cat Sam\nname: {Sam_atr[0]}\nage: {Sam_atr[1]}\ngender: {Sam_atr[2]}\n")
print(f"Cat Susana\nname: {Susana_atr[0]}\nage: {Susana_atr[1]}\ngender: {Susana_atr[2]}")

