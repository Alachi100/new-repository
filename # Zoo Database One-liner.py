# Zoo Database One-liner
print(f"Zoo's Animals: {(zoo_animals := [input('Enter an animal species: ') for _ in range(5)])}\nThere are {zoo_animals.count('lion')} lions\nThere are {zoo_animals.count('panda')} pandas\nThere are {zoo_animals.count('bear')} bears")

# Colour Converter One-liner
print(f"Hex Code: {'#{:02X}{:02X}{:02X}'.format(*(int(input(f'Enter a value for {color} (0-255): ')) for color in ['red', 'green', 'blue']))}")

