import sys
import re

def print_file(file_name):
	f=open(file_name)
	for line in f:
		print line
		result = re.search('from ([0-9\.]+) port', line)
		print result.group(1)
	f.close

if __name__ == "__main__":
	file=(sys.argv[1])
	print_file(file)
