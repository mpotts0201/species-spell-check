from enchant import DictWithPWL
from enchant.checker import SpellChecker

# use generated .txt file as new dictionary for pyenchant
my_dict = DictWithPWL("en_US", "species_dict.txt")
my_checker = SpellChecker(my_dict)


# This is where you would want to brign in a csv/tsv of data to check
# with open("Taxon.tsv") as fd:
#     rd = csv.reader(fd, delimiter="\t", quoting=csv.QUOTE_NONE)
#     # skip first row not to add header name
#     iterrows = iter(rd)
#     next(iterrows)

#     # iterate the cloned list with skipped first row
#     for row in iterrows:
#         if row[7]:
#             print("Writing line... " + row[7])
#             txt_file.writelines(row[7]+'\n')


# txt_file.close()

print("Checking...")

print("Suggested spelling: ")
print(my_checker.suggest("Bombusa Vulgarus"))

print('Done.')