import sys

class position:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.movement = list()
		self.old_path = list()
	def N(self):
		self.y += -1
		self.movement.append('N')
		self.old_path.append(position(self.x,self.y))
	def S(self):
		self.y += 1
		self.movement.append('S')
		self.old_path.append(position(self.x,self.y))
	def W(self):
		self.x += -1
		self.movement.append('W')
		self.old_path.append(position(self.x,self.y))
	def E(self):
		self.x += 1
		self.movement.append('E')
		self.old_path.append(position(self.x,self.y))
	def undo_move(self):
		# Undo position
		try:
			if self.movement[-1] == 'N':
				self.y += 1
			elif self.movement[-1] == 'S':
				self.y += -1
			elif self.movement[-1] == 'W':
				self.x += 1
			elif self.movement[-1] == 'E':
				self.x += -1
			self.movement.pop()
			self.old_path.pop()
		except IndexError:
			pass
	def distance(self,other):
		if isinstance(other, self.__class__):
			return (abs(self.x-other.x) + abs(self.y-other.y))
		else:
			return False
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return ((self.x==other.x) and (self.y==other.y))
		else:
			return False
	def __ne__(self, other):
		return not self.__eq__(other)

def rec_call(iteration_max,y=None):
    if iteration_max == 0:
        return y
    elif iteration_max == 2:
        rec_call(iteration_max-1,list(y))
    elif iteration_max == 4:
        rec_call(iteration_max-1,list(y))
    if y is None:
        y = []
    y.append(iteration_max)
    print iteration_max, y
    return rec_call(iteration_max-1,y)

def open_map(filename):
    map_init=[]
    with open(filename) as file:
        for j,line in enumerate(file):
            single_line=[]
            for i, char in enumerate(line):
                if char == 'S':
                    start_pos=position(i,j)
                    single_line.append('.')
                elif char == 'E':
                    end_pos=position(i,j)
                    single_line.append('.')
                else:
                    single_line.append(char)
            map_init.append(single_line[:16])
    return map_init, start_pos, end_pos


def find_position(current, end, maps):
	#contatore iterazioni maggiore 22
	if (len(current.movement) <= 21):
		#print len(current.movement), current.movement
		if(current==end):
			print ''.join(current.movement)
			current.undo_move()
			return True
		else:
			#reachability for optim
			if (current.distance(end) < 22 - len(current.movement)):
				if (current.y-1>=0):
					if (maps[len(current.movement)+1][current.y-1][current.x] != '&' ) and (maps[len(current.movement)][current.y-1][current.x] != '&' ) and not(position(current.x, current.y-1) in current.old_path):
						current.N()
						#print current.x, current.y, current.movement
						found=find_position(current, end, maps)
						if found == True:
							return True
				if (current.x+1<=15):
					if (maps[len(current.movement)+1][current.y][current.x+1] != '&' ) and (maps[len(current.movement)][current.y][current.x+1] != '&' ) and not(position(current.x+1, current.y) in current.old_path):
						current.E()
						#print current.x, current.y, current.movement
						found=find_position(current, end, maps)
						if found == True:
							return True
				if (current.y+1<=11):
					if (maps[len(current.movement)+1][current.y+1][current.x] != '&' ) and (maps[len(current.movement)][current.y+1][current.x] != '&' ) and not(position(current.x, current.y+1) in current.old_path):
						current.S()
						#print current.x, current.y, current.movement
						found=find_position(current, end, maps)
						if found == True:
							return True
				if (current.x-1>=0) :
					if (maps[len(current.movement)+1][current.y][current.x-1] != '&' ) and (maps[len(current.movement)][current.y][current.x-1] != '&' ) and not(position(current.x-1, current.y) in current.old_path):
						current.W()
						#print current.x, current.y, current.movement
						found=find_position(current, end, maps)
						if found == True:
							return True
				#current.undo_move()
				#return

	#print 'returning'
	current.undo_move()
	return


def create_maps(map_begin):
    map_cycles={0: map_begin}
    for i in range(1,23):
        map_cycles[i]=update_map(map_cycles[i-1])
    return map_cycles

def update_map(old_map):
    new_map=[['.' for _ in range(16)] for _ in range(12)]
    for i, row in enumerate(old_map):
        for j, element in enumerate(row):
            count = 0
            if (i-1 >= 0):
                for t in range(j-1, j+2):
                    if (t>=0) and (t<=15):
                        if(old_map[i-1][t]=='&'):
                            count += 1
            if (i+1 < 12):
                for t in range(j-1, j+2):
                    if (t>=0) and (t<=15):
                        if(old_map[i+1][t]=='&'):
                            count += 1
            if (j-1 >=0) and (old_map[i][j-1]=='&'):
                count+=1
            if (j+1 <=15) and (old_map[i][j+1]=='&'):
                count+=1
            #Can now update the map
            if (element=='&') and ((count==2) or (count==3)):
                new_map[i][j]='&'
            elif (element=='.') and (count>2):
                new_map[i][j]='&'
            else:
                new_map[i][j]='.'
    return new_map



if __name__ == '__main__':
	in_map, start, end = open_map(sys.argv[1])
	maps=create_maps(in_map)
	find_position(start, end, maps)
