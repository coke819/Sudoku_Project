
def initialize_board():
	list = []
    for i in range(9):
        line = []
        for j in range(9):
            line.append(0)
        list.append(line)
    return list
	
