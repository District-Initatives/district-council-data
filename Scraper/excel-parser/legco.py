# -*- coding: utf8 -*-
# coding: utf8

# Usage: python ./legco.py [Exeels Path] [Output Path]

import os, locale, sys, xlrd, json, fnmatch, re
locale.setlocale(locale.LC_ALL, 'zh_TW.UTF-8')

# Settings
districtNumIndex = 0
LCtotalVotesIndex = 25
LCtotalDemoVotesIndex = 26
LCtotalGovVotesIndex = 27
LCtotalUnclassVotesIndex = 28

filename = "legco.json"
# End Settings

def readExcels(path):
	files = os.listdir(path)
	os.chdir(path)
	tables = []
	for file in files:
		if fnmatch.fnmatch(file, '*.xls'):
			tables.append(xlrd.open_workbook(file).sheets()[0])
	return tables

def parseRow(row):
	if re.search(r'[A-Z]\d\d\d\d', row[districtNumIndex]) is None: # Not information row
		return None
	else:
		return {
			"districtNum": row[districtNumIndex][:3], # First 3 characters
			"LCtotalVotes": row[LCtotalVotesIndex],
			"LCtotalDemoVotes": row[LCtotalDemoVotesIndex],
			"LCtotalGovVotes": row[LCtotalGovVotesIndex],
			"LCtotalUnclassVotes": row[LCtotalUnclassVotesIndex]
		}

def save(result, path):
	os.chdir(path)
	with open(filename, 'w') as outfile:
		json.dump(result, outfile, indent=2)

def removeDuplicates(table):
	lastDistrictNum = ""
	newArray = []
	for row in table:
		if row["districtNum"] == lastDistrictNum:
			newArray[-1]["LCtotalVotes"] += row["LCtotalVotes"]
			newArray[-1]["LCtotalDemoVotes"] += row["LCtotalDemoVotes"]
			newArray[-1]["LCtotalGovVotes"] += row["LCtotalGovVotes"]
			newArray[-1]["LCtotalUnclassVotes"] += row["LCtotalUnclassVotes"]
		else:
			newArray.append(row)
			lastDistrictNum = row["districtNum"]
	return newArray

def main(argv):
	print(argv)
	result = []
	tables = readExcels(argv[1])
	for table in tables:
		for i in range(table.nrows):
			row = table.row_values(i)
			if (parseRow(row) is not None):
				result.append(parseRow(row))
	result = removeDuplicates(result)
	save(result, argv[2])

if __name__ == "__main__":
	main(sys.argv)
