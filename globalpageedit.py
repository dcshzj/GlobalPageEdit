#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Hydriz
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Configuration goes into settings.py, not here!

import settings
import wikitools

# Nothing to change below...
wikis = open(wikilist, 'r').read().splitlines()
def welcome():
	# Welcome message, but includes some checks...
	if (username == "") or (password == "") or (page == ""):
		print "ERROR (1): Essential parameters undefined!"
	else:
		print "Welcome to the Global Page Edit tool!"

def bye():
	print "Done! Please check the amount of devastation as a result of this script..."

def runthru():
	# Function to run through the list of wikis and edit them (skipping the skipwikis list)
	global skipwikis, wikis
	for wiki in wikis:
		if wiki in skipwikis:
			print "Skipping %s.beta.wmflabs.org (in skip list)" % (wiki)
		else:
			print "Changing %s.beta.wmflabs.org..." % (wiki)
			edit(wiki)

def edit(wiki):
	# Function to edit a specific page
	global page, password, text, username
	apiurl = "http://%s.beta.wmflabs.org/w/api.php" % (wiki)
	wikie = wikitools.Wiki(apiurl)
	wikie.login(username, password)
	pagefunct = wikitools.Page(wikie, page)
	page_text = text.encode('utf-8')
	pagefunct.edit(page_text, summary=summary)

def main():
	welcome()
	runthru()
	bye()

if __name__ = "__main__":
	main()
