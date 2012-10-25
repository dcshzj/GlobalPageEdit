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

# Globalising the settings in settings.py
action = settings.action
username = settings.username
password = settings.password
page = settings.page
text = settings.text
summary = settings.summary
wikilist = settings.wikilist
skipwikis = settings.skipwikis

# Nothing to change below...
wikis = open(wikilist, 'r').read().splitlines()
def welcome():
	# Welcome message, but includes some checks...
	if (username == "") or (password == "") or (page == "") or (action == ""):
		print "ERROR (1): Essential parameters undefined!"
	elif (action != "overwrite") or (action != "create") or (action != "delete") or (action != "append") or (action != "prepend"):
		print "ERROR (2): Action is invalid!"
	else:
		print "Welcome to the Global Page Edit tool!"

def bye():
	print "Done! Please check the amount of devastation as a result of this script. :D"

def runthru():
	# Function to run through the list of wikis and edit them (skipping the skipwikis list)
	global skipwikis, wikis
	for wiki in wikis:
		if wiki in skipwikis:
			print "Skipping %s.beta.wmflabs.org (in skip list)" % (wiki)
		else:
			print "Modifying %s.beta.wmflabs.org..." % (wiki)
			if (action == "overwrite"):
				overwrite(wiki)
			elif (action == "create"):
				create(wiki)
			elif (action == "delete"):
				delete(wiki)
			elif (action == "append"):
				append(wiki)
			elif (action == "prepend"):
				prepend(wiki)

# The overwrite function. Overwrites existing pages with new content and create non-existent pages with the set content.
def overwrite(wiki):
	global page, password, summary, text, username
	apiurl = "http://%s.beta.wmflabs.org/w/api.php" % (wiki)
	wikie = wikitools.Wiki(apiurl)
	wikie.login(username, password)
	pagefunct = wikitools.Page(wikie, page)
	page_text = text.encode('utf-8')
	pagefunct.edit(page_text, summary=summary)

def create(wiki):
	global page, password, summary, text, username
	# Foobar

def delete(wiki):
	global page, password, summary, username
	apiurl = "http://%s.beta.wmflabs.org/w/api.php" % (wiki)
	wikie = wikitools.Wiki(apiurl)
	wikie.login(username, password)
	pagefunct = wikitools.Page(wikie, page)
	page_text = text.encode('utf-8')
	pagefunct.delete(reason=summary)

def append(wiki):
	global page, password, summary, text, username
	apiurl = "http://%s.beta.wmflabs.org/w/api.php" % (wiki)
	wikie = wikitools.Wiki(apiurl)
	wikie.login(username, password)
	pagefunct = wikitools.Page(wikie, page)
	page_text = text.encode('utf-8')
	existingtext = pagefunct.getWikiText()
	result_text = existingtext + "\n" + page_text
	pagefunct.edit(result_text, summary=summary)

def prepend(wiki):
	global page, password, summary, text, username
	apiurl = "http://%s.beta.wmflabs.org/w/api.php" % (wiki)
	wikie = wikitools.Wiki(apiurl)
	wikie.login(username, password)
	pagefunct = wikitools.Page(wikie, page)
	page_text = text.encode('utf-8')
	existingtext = pagefunct.getWikiText()
	result_text = page_text + "\n" + existingtext
	pagefunct.edit(result_text, summary=summary)

def main():
	welcome()
	runthru()
	bye()

if __name__ == "__main__":
	main()
