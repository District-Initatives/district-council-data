# -*- coding: utf8 -*-
# coding: utf8

# Usage: python ./aggregates.py [Output Path] [Output Format: json/csv]

import json, os, sys, fnmatch, unicodecsv

# Settings
headers =  [
		u'districtNum',
		u'districtName',
		u'districtPopulaton',
		u'district18',
		u'LCtotalDemoVotes', 
		u'LCtotalGovVotes', 
		u'LCtotalUnclassVotes',
		u'LCtotalVotes'
	]
# End Settings

def readJSON(filename):
	with open(filename, 'r') as f:
		data = json.load(f)
	return data

def sortList(list):
	return sorted(list, key=lambda k: k['districtNum'])

def find(lst, key, value):
	for i, dic in enumerate(lst):
		if dic[key] == value:
			return i
	return -1

def merge(tables):
	for row in tables[0]:
		for table in tables[1:]: # Save the first table as template, then update it with other tables
			index = find(table, "districtNum", row["districtNum"])
			row.update(table[index])
	return tables[0]

def writeCSV(source):
	f = unicodecsv.writer(open("test.csv", "wb+"))
	f.writerow(headers)
	for x in source:
		print x
		f.writerow([x[header] for header in headers])


def main(argv):
	files = os.listdir(os.getcwd())
	print(files)
	tables = []
	for file in files:
		if fnmatch.fnmatch(file, '*.json'):
			tables.append(sortList(readJSON(file)))
	writeCSV(merge(tables))


if __name__ == "__main__":
	main(sys.argv)