import csv

# Each header of the .tsv
# index 7 of row in file read of each row is canonicalName (row[7])
# headers = ['taxonID', 'datasetID', 'parentNameUsageID', 'acceptedNameUsageID', 'originalNameUsageID', 'scientificName', 'scientificNameAuthorship', 'canonicalName', 'genericName', 'specificEpithet', 'infraspecificEpithet', 'taxonRank', 'nameAccordingTo', 'namePublishedIn', 'taxonomicStatus', 'nomenclaturalStatus', 'taxonRemarks', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus']

txt_file = open("species_dict.txt", "a")

# Reading .tsv of file from GBIF to write into 1 word per line .txt for pyenchant (takes a few minutes to complete)
with open("Taxon.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quoting=csv.QUOTE_NONE)
    # skip first row not to add header name
    iterrows = iter(rd)
    next(iterrows)

    # iterate the cloned list with skipped first row
    for row in iterrows:
        if row[7]:
            print("Writing line... " + row[7])
            txt_file.writelines(row[7]+'\n')


txt_file.close()