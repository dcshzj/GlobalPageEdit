#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012-2013 Hydriz
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
import sys
import time
import wikitools

class GlobalPageEdit:
	def __init__(self):
		self.action = settings.action
		self.username = settings.username
		self.password = settings.password
		self.page = settings.page
		self.text = settings.text
		self.summary = settings.summary
		self.wikilist = settings.wikilist
		self.skipwikis = settings.skipwikis
		# Please do not change this unless you take responsibility on what you are doing
		self.suffix = ".beta.wmflabs.org"
		self.apiurl = ""
		self.numberofwikis = 0

	def welcome(self):
		# Welcomes the user and checks for essential parameters given in settings.py
		if ( ( self.username == "" ) or ( self.password == "" ) ):
			print "You have yet to tell me what username/password to use!"
			sys.exit(1)

		if ( ( self.page == "" ) or ( self.action == "" ) ):
			print "You have yet to tell me what page to edit and what to do about it!"
			sys.exit(1)

		if ( ( self.action not in [ 'overwrite', 'create', 'delete', 'append', 'prepend' ] ) ):
			print "Invalid action was provided, please provide an action that I understand."
			sys.exit(1)

		if ( self.summary == "" ):
			print "Please provide a summary of your action."
			sys.exit(1)

		print "Welcome to the Global Page Edit tool!"

	def bye(self, number):
		# Bid goodbye to the user and give an overall statistics on the number of wikis edited
		if ( self.action == "delete" ):
			action = "deleted"
		else:
			action = "edited"

		if ( number == 1 ):
			print "Done! The page \"%s\" was %s on 1 wiki." % ( self.page, action )
		else:
			print "Done! The page \"%s\" was %s on %d wikis." % ( self.page, action, number )

	def run(self):
		# Main runner of the script
		self.welcome()
		wikis = open( self.wikilist, 'r' ).read().splitlines()
		for wiki in wikis:
			if wiki in self.skipwikis:
				print "Skipping %s%s (in skip list)" % ( wiki, self.suffix )
			else:
				self.numberofwikis += 1
				print "Modifying %s%s..." % ( wiki, self.suffix )
				self.apiurl = "http://%s%s/w/api.php" % ( wiki, self.suffix )
				if ( self.action == "overwrite" ):
					self.overwrite( wiki )
				elif ( self.action == "create" ):
					self.create( wiki )
				elif ( self.action == "delete" ):
					self.delete( wiki )
				elif ( self.action == "append" ):
					self.append( wiki )
				elif ( self.action == "prepend" ):
					self.prepend( wiki )
		self.bye( self.numberofwikis )

	def overwrite(self, wiki):
		# The overwrite function.
		# This function overwrites existing pages with the new content given in the text file.
		# It also creates non-existent pages with the provided content.
		# TODO: Check if the site actually exists before continuing (usually because of a typo or the server is offline)
		wikie = wikitools.Wiki( self.apiurl )
		# TODO: Check if the user is actually logged in before continuing (usually because account does not exist)
		wikie.login( self.username, self.password )
		pagefunct = wikitools.Page( wikie, self.page )
		page_text = self.text.encode( 'utf-8' )
		pagefunct.edit( page_text, summary=self.summary )

	def create(self, wiki):
		# The create function.
		# This function creates the page on the wiki with the content given in the text file.
		# If the page exists, it would be skipped.
		print "Creating new pages is not yet supported, sorry."
		# TODO: Add code here.

	def delete(self, wiki):
		# The delete function.
		# This function deletes the page on the wiki, regardless of what the page used to contain.
		domain = "%s%s" % ( wiki, self.suffix )
		loginfailed = False

		# TODO: Exception handler cannot catch the errors raised by urllib2, and continues retrying forever...
		try:
			wikie = wikitools.Wiki( self.apiurl )
		except:
			print "Server is slow, retrying in 5 seconds..."
			time.sleep(5)
			try:
				wikie = wikitools.Wiki( self.apiurl )
			except URLError:
				print "ERROR: The website at %s is not accessible, skipping..." % ( domain )

		wikie.login( self.username, self.password )
		try:
			if ( wikie.isLoggedIn( self.username ) == False ):
				loginfailed = True
		except wikitools.api.APIError:
			loginfailed = True

		if ( loginfailed == True ):
			print "ERROR: Your authentication credentials are incorrect! Please check your username and password again!"
			print "The page \"%s\" was NOT deleted on %s" % ( self.page, domain )
			self.numberofwikis -= 1
		else:
			pagefunct = wikitools.Page( wikie, self.page )
			page_text = self.text.encode( 'utf-8' )
			try:
				pagefunct.delete( reason=self.summary )
			except KeyError:
				domain = "%s%s" % ( wiki, self.suffix )
				print "ERROR: Your account does not have sufficient rights to delete pages on %s!" % ( domain )
				self.numberofwikis -= 1

	def append(self, wiki):
		# The append function.
		# This function appends onto existing pages with the content given in the text file.
		# TODO: The function also creates non-existent pages with the provided content.
		# A check should be made to avoid creating ugly pages with a newline at the beginning of the page.
		# TODO: Check if the site actually exists and if the user logged in successfully.
		wikie = wikitools.Wiki( self.apiurl )
		wikie.login( self.username, self.password )
		pagefunct = wikitools.Page( wikie, self.page )
		page_text = self.text.encode( 'utf-8' )
		existingtext = pagefunct.getWikiText()
		result_text = "%s\n\n%s" % ( existingtext, page_text )
		pagefunct.edit( result_text, summary=self.summary )

	def prepend(self, wiki):
		# The prepend function.
		# This function prepends onto existing pages with the content given in the text file.
		# TODO: The function also creates non-existent pages with the provided content.
		# A check should be made to avoid creating pages with a newline at the ending of the page.
		# TODO: Check if the site actually exists and if the user logged in successfully.
		wikie = wikitools.Wiki( self.apiurl )
		wikie.login( self.username, self.password )
		pagefunct = wikitools.Page( wikie, self.page )
		page_text = self.text.encode( 'utf-8' )
		existingtext = pagefunct.getWikiText()
		result_text = "%s\n\n%s" % ( page_text, existingtext )
		pagefunct.edit( result_text, summary=self.summary )

if __name__ == "__main__":
	GlobalPageEdit = GlobalPageEdit()
	GlobalPageEdit.run()
