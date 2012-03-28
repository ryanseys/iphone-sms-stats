#! /usr/bin/env python
from sqlite3 import dbapi2 as sqlite
import shutil

### Created by Ryan Seys (http://www.github.com/ryanseys) ###
### This script parses the sqlite database from an iPhone ###
### It allows for statistical analysis on the messages 	  ###
### that are contained within the database. This script   ###
### is meant to be edited and not to be run without any   ###
### modification. In fact, it will throw errors if it is  ###
### not changed. Please adjust the code to your needs.	  ###

#for progress
print "Copying SQLite database from backup."
shutil.copyfile('<sms_database_goes_here>', 'smsdb_copy.db')
shutil.copyfile('<address_database_goes_here>', 'addressdb_copy.db')
print "Copying complete."
SMS_DB = 'smsdb_copy.db'
ADD_DB = 'addressdb_temp.db'

### FLAGS ### SET THESE TO 1 CHOOSE WHAT YOU WANT TO PRINT ###
all_messages 				= 1
total_word_count = 1
word_occurrence_count 		= 1
word						= "lol"
total_character_count 		= 1
total_alphabet_count		= 1
alphabet_breakdown_count 	= 0
sorted_alphabet_breakdown	= 0
total_unknown_char_count	= 1
total_alphabet_plus_unknown	= 1

#prints out all of the messages in the database. Conversation style needs revising.
def run_commands(all_messages, total_word_count, word_occurrence_count, total_character_count, total_alphabet_count, total_unknown_char_count, total_alphabet_plus_unknown):
	message_step = 1
	t_w_count = 0
	w_count	  = 0
	chars	  = 0
	letters   = {'a': 0, 'b': 0, 'c': 0, 
	'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 
	'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 
	'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
	's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 
	'x': 0, 'y': 0, 'z': 0}
	unknowns  = 0
	alphabet_counter = 0
	for i in msgs:
		if i[0] != None:
			#text, address, flag
			if all_messages == 1:
				printmsg(i[0], i[1], i[2])
			if total_word_count == 1:
				t_w_count = t_w_count + len(i[0].strip().split(' '))
			if (word_occurrence_count == 1) or (total_character_count == 1):
				for j in i[0].strip().split(' '):
					j = j.lower()
					
					if word_occurrence_count == 1:
						if j == word:
							w_count+=1
					if total_character_count == 1:
						chars = chars + len(j)
					if (total_alphabet_count == 1) or (total_alphabet_plus_unknown == 1):
						for k in list(j):
							if k in letters:
								letters[k] = letters[k] + 1
							else:
								if (total_unknown_char_count == 1) or (total_alphabet_plus_unknown == 1):
									unknowns+=1
	print "Calculations complete.\n"
	print "Number of messages: " + str(len(msgs))
	if (total_alphabet_count == 1) or (total_alphabet_plus_unknown == 1):
		for letter in letters.items():
			alphabet_counter+=letter[1] #add the number of characters counted together
		if total_alphabet_count == 1:
			print "Total alphabet count: " + str(alphabet_counter)
	if alphabet_breakdown_count == 1:
		print "Alphabet breakdown count"
		for letter in letters:
			print str(letter) + ": " + str(letters[letter])
	if sorted_alphabet_breakdown == 1:
		print "Sorted alphabet breakdown count"
		import operator
		sletters = sorted(letters.iteritems(), key=operator.itemgetter(1))
		sletters.reverse()
		for letter in sletters:
			print letter[0] + ": " + str(letter[1])
	if total_character_count == 1:
		print "Total character count: " + str(chars)
	if word_occurrence_count == 1:
		print "Total word occurence of \"" + word + "\": " + str(w_count)
	if total_word_count == 1:
		print "Total word count: " + str(t_w_count)
	if total_unknown_char_count == 1:
		print "Total unknown character count: " + str(unknowns)
	if total_alphabet_plus_unknown == 1:
		print "Total alphabet + unknown character count: " + str(unknowns + alphabet_counter)
#Return the number of words (strings delimited by a single space) in the messages.	
def f_total_word_counter():
	count = 0
	for i in msgs:
		if i[0] != None:
			count = count + len(i[0].strip().split(' '))
	
	return count

def f_word_occurance_count(word):
	count = 0
	for i in msgs:
		if i[0] != None:
			for j in i[0].strip().split(' '):
				j = j.lower()
				if j == word:
					count+=1
	print "Total word occurence of \"" + word + "\": " + str(count)
	return count

def f_total_character_count():
	chars = 0
	for i in msgs:
		if i[0] != None:
			for j in i[0].strip().split(' '):
				chars = chars + len(j)
	print "Total character count: " + str(chars)
	return chars

def f_total_alphabet_count(FROM=None):
	unknowns = 0
	letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
	'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 
	'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 
	'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 
	'x': 0, 'y': 0, 'z': 0}
	for i in msgs:
		if i[0] != None:
			if FROM != None:
				if i[1] == FROM and i[2] == 3: #SENT BY THIS GIVEN NUMBER
					for j in i[0].strip().split(' '):
						j = j.lower()
						for k in list(j):
							if k in letters:
								letters[k] = letters[k] + 1
			else:
				for j in i[0].strip().split(' '):
						j = j.lower()
						for k in list(j):
							if k in letters:
								letters[k] = letters[k] + 1
							else:
								unknowns+=1
	import operator
	sletters = sorted(letters.iteritems(), key=operator.itemgetter(1))
	sletters.reverse()
	alphabet_counter = 0
	for letter in sletters:
		alphabet_counter+=letter[1]
		print letter[0] + ": " + str(letter[1])
	print "Total alphabet count: " + str(alphabet_counter)
	print "Total unknown characters: " + str(unknowns)
	print "Total alphabet count + unknowns: " + str(alphabet_counter+unknowns)

#didn't write this, and don
def message_read(flags):
    """reimplementation of an sqlite user defined function called by a trigger
    on the messages table.

    the trigger checks the message flags to see if a message has been read to
    see if the counter of unread messages in another needs to be updated when
    a message is deleted.
    """
    # second bit is the "was read" flag
    return (int(flags) & 0x02) >> 1

def printmsg(text, address, flag):
	if flag == 2:
		print getContact(address) + ":\t" + text
	elif flag == 3:
		print "Ryan Seys:\t" + text
	elif flag == 129:
		print "Deleted:\t" + text
	elif flag == 33:
		print "Message send failure:\t" + text
# temporary contact list. Should be made to extract from address book db but don't have one.
def getContact(number):
	if number == "+12345678910":
		return "Test Contact"
	else:
		return number

def unique_word_count():
	unique = []
	for i in msgs:
		if i[0] != None:
			for j in i[0].strip().split(' '):
				j = j.lower()
				j = strip_punc(j)
				if j not in unique:
					unique.append(j)
	return len(unique)

def strip_punc(word):
	exceptions = [':)', ':(']
	if word in exceptions:
		return word
	word = word.strip("~`!@#$%^&*()_+-={}|:\"<>?/.,';\][ ")
	return word
	
def last_message():
	return msgs[len(msgs)-1][0]
	
db = sqlite.connect(SMS_DB)
#add_db = sqlite.connect(ADD_DB)



# register the user-defined function used by delete trigger
db.create_function('read', 1, message_read)
c = db.cursor()
#add_c = add_db.cursor()
#add_c.execute("SELECT ROWID, First, Last, ABMultiValue.value FROM ABPerson, ABMultiValue WHERE ABPerson.ROWID=ABMultiValue.record_id;")

#addressbook = add_c.fetchall()


def prepare_addressbook(add_book):
	names = {}
	add_book = list(add_book)
	count = 0
	list_of_tuples = []
	for instance in add_book:
		list_of_tuples.append(instance)
		list3 = list(instance)
		add_book.append(list3)
	for instance in list_of_tuples:
		add_book.remove(instance)
	for instance in add_book:
		print instance
			
		
#prepare_addressbook(addressbook)

#select the defined tables
c.execute("SELECT text,address,flags FROM message;")

print "Getting messages..."
#get all the entries in those tables
msgs = c.fetchall()
print "Messages retrieved."
print_all_messages()
total_word_count()
total_alphabet_count()
total_character_count()
word_occurance_count("lol")

'''
Calculations!
'''
print "Running calculations..."

run_commands(all_messages, total_word_count, word_occurrence_count, total_character_count, total_alphabet_count, total_unknown_char_count, total_alphabet_plus_unknown)

### TO DO: MERGE THIS INTO RUN_COMMANDS() ###
print "Total unique word count: " + str(unique_word_count())
print "Last message: " + "\"" + last_message() + "\""