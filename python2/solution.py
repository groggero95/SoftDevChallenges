#!/usr/bin/python
import socket
import sys
import pickle
import re
import datetime
import calendar

one=	'   #     ##    # #      #      #      #    ##### '
two=	' ##### #     #      # ##### #      #      #######'
three=	' ##### #     #      # #####       ##     # ##### '
four=	'#      #    # #    # #######     #      #      # '
five=	'########      #       #####       ##     # ##### '
six=	' ##### #     ##      ###### #     ##     # ##### '
seven=	'########    #     #     #     #      #      #    '
eight=	' ##### #     ##     # ##### #     ##     # ##### '
nine=	' ##### #     ##     # ######      ##     # ##### '
zero=	'  ###   #   # # #   ##  #  ##   # # #   #   ###  '

fig_dict={}

fig_dict[one]=1
fig_dict[two]=2
fig_dict[three]=3
fig_dict[four]=4
fig_dict[five]=5
fig_dict[six]=6
fig_dict[seven]=7
fig_dict[eight]=8
fig_dict[nine]=9
fig_dict[zero]=0



name_id='jollyroger\n'
TCP_IP = 'localhost'
TCP_PORT = 9999
secret = '8389c07265822f7388b8baf33652339f\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
fs=s.makefile('rw', 0)

s.recv(100)
s.send(name_id)
s.recv(100)
s.send(secret)
s.recv(100)


# launch a binary search here
status_in = 0
low_bound=0
up_bound=10000
while (True):
	index = (low_bound + up_bound) // 2		
	s.send(str(index)+'\n')
	received = s.recv(1000)
	if (received == 'nope. Try something smaller\n'):
		up_bound = index - 1
	elif (received == 'nope. Try something bigger\n'):
		low_bound = index + 1
	else:
		break

mat=[[' ']*39 for i in range(7)]
#cont=s.recv(1000)
for i, line in enumerate(fs):
	if i < 7:
		print line
		for j, char in enumerate(line):
			if char == '#':
				mat[i][j]=char
	#elif (i == 9):
	#	print line
	#	break
	else:
		print line
		break

#fs.close()
#print mat
string=''
char1=''
char2=''
char3=''
s.recv(100)

for j,line in enumerate(mat):
	for i, element in enumerate(line):
		if (element=='#'):
			string += '#'
		else:
			string += ' '
		if (i < 7):
			char1 += element
		elif (i > 15) and (i <23):
			char2 += element
		elif (i>31) and (i<40):
			char3 += element	

#print "%d%d%d\n" %(fig_dict[char1], fig_dict[char2], fig_dict[char3])
s.send("".join([str(fig_dict[char1]), str(fig_dict[char2]), str(fig_dict[char3])]) +'\n')
emp=''


print s.recv(100)
all_lines=s.recv(1000)
x=all_lines.split('\n')
print all_lines
for i,line in enumerate(x):
	if (i>0) and (i<9):
		emp += (line+'\n')

unpick = pickle.loads(emp)
s.send(str(unpick)[20:]+'\n')
s.recv(1000)
string_date = s.recv(1000)
print string_date
day, month_name, year = string_date[25:27], string_date[28:31], '20'+ string_date[32:34]
month=list(calendar.month_abbr).index(month_name)
day_int=int(day)
year_int=int(year)
print day_int, month, year_int, type(month)

deltatime= datetime.date.today() - datetime.date(year_int, month, day_int)
print deltatime.days
s.send(str(deltatime.days) + '\n')

msg = s.recv(100)
if len(msg) < 12:
	final_msg=s.recv(100).split(':')
else:
	final_msg=msg.split(':')

print final_msg[1]
s.send(final_msg[1])
fs.close()
s.close()
