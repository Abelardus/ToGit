
# author: Abelardo Lopez
# date: 8/22/15
# description: 
from urllib2 import urlopen

# Reference (base) region
template = 'https://us.api.battle.net/wow/item/{}?locale=en_US&apikey=79ed54vhzynrw7cuwspdaya3nf8qee7r'
deep_earth_vestments = '[78775,78785,78805,78755,78835]'
deepEarthVestments = {
	'Deep Earth Handwraps' : '78775',
	'Deep Earth Helm' : '78785',
	'Deep Earth Legwraps' : '78805',
	'Deep Earth Robes' : '78755',
	'Deep Earth Mantle' : '78835',
	}
handwraps = deepEarthVestments['Deep Earth Handwraps']

# Test cases region
'''Test case #1
Using the World Warcraft Item Set Web API, verify that the items provided are all the existing items in the 'Deep
Earth Vestments'.
'''

def items_in_deep_earth_vestments_set():
	print ''
	print 'Items in the Deep Earth Vestments Set'
	url = template.format(handwraps)
	webtarget = urlopen(url)
	for line in webtarget:
		if deep_earth_vestments in line:
			print deep_earth_vestments + " are the items in Deep Earth Vesments --> pass" 
		else:
			print deep_earth_vestments + " are NOT the items in Deep Earth Vesments --> fail"
	
'''Test case #2
Using the World Warcraft Item Set Web API, retrieve the item names for all items in the 'Deep
Earth Vestments' set and verify that the item name for each item matches that which is returned by the Item Web API.
'''

def deep_earth_vestments_name():
	print ''
	print "Deep Earth Vestments Names:"
	for name, id in deepEarthVestments.iteritems():
		url = template.format(id)
		webtarget = urlopen(url)
		for line in webtarget:
			if name in line:
				print name + " id:[" + id + "]  --> pass"
			else:
				print name + " id:[" + id + "]  --> fail"
	
	
'''Test case #3
Using the World Warcraft Item Set Web API, retrieve the item ids for all items in the 'Deep
Earth Vestments' set and verify that the item id for each item matches that which is returned by the Item Web API.
'''

def deep_earth_vestments_id():
	print ''
	print "Deep Earth Vestments ID:"
	for name, id in deepEarthVestments.iteritems():
		url = template.format(id)
		webtarget = urlopen(url)
		for line in webtarget:
			if id in line:
				print "[" + name + "] id:" + id + " --> pass"
			else:
				print "[" + name + "] id:" + id + " --> fail"
	

'''Test case #4
Using the World Warcraft Item Set Web API, verify that the 'Deep Earth Vestments' set name appears in all 
the set items.
'''	

def idIn_deep_earth_vestments(itemset):
	print ''
	print "ID in Deep Earth Vestments Set"
	for name, id in deepEarthVestments.iteritems():
		url = template.format(id)
		webtarget = urlopen(url)
		for line in webtarget:
			if itemset in line:
				print "id:" + id + "is in " + itemset + " --> pass"
			else:
				print "id:" + id + "is Not in " + itemset + " --> fail"

'''Test case #5
 Negative Test: Using the World Warcraft Item Set Web API, verify that the item set name provided does 
NOT belong to the set items in the 'Deep Earth Vestments' set.
'''	

def setNameIn_deep_earth_vestments(itemset):
	print ''
	print "Negative Test Deep Earth Vestments Set"
	for name, id in deepEarthVestments.iteritems():
		url = template.format(id)
		webtarget = urlopen(url)
		for line in webtarget:
			if itemset not in line:
				print "id:" + id + "is in " + itemset + " --> pass"
			else:
				print "id:" + id + "is Not in " + itemset + " --> fail"				
				


items_in_deep_earth_vestments_set()
deep_earth_vestments_name()
deep_earth_vestments_id()
idIn_deep_earth_vestments("Deep Earth Vestments")
setNameIn_deep_earth_vestments("Deep Earth Battlegarb")

