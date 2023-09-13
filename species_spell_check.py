from enchant import DictWithPWL
from enchant.checker import SpellChecker

# use generated .txt file as new dictionary for pyenchant
my_dict = DictWithPWL("en_US", "species_dict.txt")
my_checker = SpellChecker(my_dict)

print("Checking...")

print("Suggested spelling: ")
print(my_checker.suggest("Bombusa Vulgarus"))

print('Done.')