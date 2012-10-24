[![Build Status](https://secure.travis-ci.org/Hydriz/GlobalPageEdit.png)](http://travis-ci.org/Hydriz/GlobalPageEdit)

This is a bot that is written in python that edits Wikimedia wikis in the [beta cluster](http://deployment.wikimedia.beta.wmflabs.org) and creates global user pages for anyone.

This tool depends on:
1. Python 2.7 and above (not Python 3)
2. [wikitools](https://code.google.com/p/python-wikitools/) (SVN checkout the wikitools directory in trunk in the same folder as the script)

### Setting up the script
This script needs a list of URLs in a separate file (called listofwikis.txt in the same directory). You would have to manually generate it so that the bot knows where to edit. Please omit the ".org" suffix as it is already included in the script.

Edit the required configuration in globalpageedit.py with the relevant information before you run the script. Double-check, triple-check before running this script as the effects of mistakes is tremendous (and may carry a ban following it). **YOU HAVE BEEN WARNED**!

Disclaimer: The author (Hydriz) accepts no liability for damages incurred by third-parties running this script.

More information is available in this repository's wiki.
