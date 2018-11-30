import sys
import re
# In order not to check if an entry is already present in the dict, I took advantage
# of the following:
# https://stackoverflow.com/questions/26367812/appending-to-list-in-python-dictionary
from collections import defaultdict


def scan_file(file_name):
	f=open(file_name)
	accepted_dict = defaultdict(list)
	failed_dict=defaultdict(list)
	for line in f:
		status_a=re.search('Accepted password', line)
		status_f=re.search('Failed password', line)
		if status_a:
			address = re.search('from ([0-9\.]+) port', line).group(1)
			user=re.search('for (.*) from', line).group(1)
			accepted_dict[address].append(user)
		elif (status_f):
			address = re.search('from ([0-9\.]+) port', line).group(1)
			user_tmp=re.search('for (.*) from', line)
			del_user = re.compile('invalid user ([a-zA-Z0-9_]+)')
			user=del_user.sub(r'\1', user_tmp.group(1))
			failed_dict[address].append(user)

	f.close

	ip_both = [x for x in accepted_dict if (x in failed_dict) and (len(failed_dict[x]) > len (accepted_dict[x]))]
	for i in ip_both:
		print "%s - %d failed for %d users - %d accepted for %d users" %(i, len(failed_dict[i]), len(set(failed_dict[i])), len(accepted_dict[i]), len(set(accepted_dict[i])))

if __name__ == "__main__":
	file=(sys.argv[1])
	scan_file(file)
