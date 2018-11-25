import sys

def print_file(file_name):
	f=open(file_name)
	for line in f:
		print line
	f.close

if __name__ == "__main__":
	file=(sys.argv[1])
	print_file()
