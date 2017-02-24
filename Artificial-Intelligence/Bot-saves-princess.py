#!/usr/bin/python
def displayPathtoPrincess(n,grid):
#print all the moves here
	for idx, row in enumerate(grid):
		if 'p' in row:
			princess = (idx, row.index('p'))
		if 'm' in row:
			mario = (idx, row.index('m'))
	moves = []
	moves += ["DOWN"]*(princess[0]-mario[0]) if princess[0]>mario[0] else ["UP"]*(mario[0]-princess[0])
	moves += ["RIGHT"]*(princess[1]-mario[1]) if princess[1]>mario[1] else ["LEFT"]*(mario[1]-princess[1])
	for move in moves:
		print(move)

m = int(input())
grid = [] 
for i in range(0, m): 
	grid.append(input().strip())

displayPathtoPrincess(m,grid)