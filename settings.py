# Configuration file for globalpageedit.py
# More information is available at the repository's wiki on GitHub.

# What to do? Options:
# overwrite - Overwrite existing pages with the new set content (and create non-existent pages with the set text)
# create - Create new pages with the set content, leaving existing pages intact. (NOT SUPPORTED)
# delete - Delete existing pages.
# append - Add the content set below to the bottom of existing pages (and creating non-existent pages with it)
# prepend - Add the content set below to the top of existing pages (and create non-existent pages with it)
action = ""

# Login information
username = ""
password = ""

# Page text
page = "" # The user page to edit
text = u'''
''' # Copy verbatim into this box. Add a backslash (\) in front of (''') whereever necessary
summary = "" # The edit summary (or delete reason)
wikilist = "listofwikis.txt" # List of wikis to edit.

# Wikis to skip
########## DANGER!!! ##### DANGER!!! ##### DANGER!!! ##########
# IMPORTANT: WILL OVERWRITE EVERYTHING, PLEASE ADD WIKIS THAT SHOULD BE SKIPPED IN HERE!
skipwikis = []
