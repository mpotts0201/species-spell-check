# species-spell-check

##Installation
You will need `pyenchant` to run the spell checker.
Installation guide: https://pyenchant.github.io/pyenchant/install.html#installation

##About
This repo is an experimental way to spell check species names in taxonomy.

You will need to aquire a tsv of species names from GBIF:

https://hosted-datasets.gbif.org/datasets/backbone/current/

and download backbone.zip.

Unzip the file and place Taxon.tsv into the root of this project.

run `python3 generate_dict.py` in terminal, or whatever you use for python to run that script to build a dict.

The dict will be named `species_dict.txt` and will be created at the root of the project.

In `species_spell_check.py` there is an experimental script to spell check a hardcoded value. Run this script to see an example of output of the spell checker with a hardcoded intentionally misspelled species name.

Ideally in the future you could use a local tsv or csv to pipeline all entries into the spell checker. Or change it to take one name at a time from user input with pythons `input()` method.

`GBIFLookup.py` is another experimental method to try to spell check against their api, but would not be practical with 1000's of spell checks at a time.
