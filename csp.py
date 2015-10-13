from itertools import product

import gameNode

###########################################
# you need to implement five funcitons here
###########################################

def backtracking(filename):
	###
	# use backtracking to solve sudoku puzzle here,
	# return the solution in the form of list of
	# list as describe in the PDF with # of consistency
	# checks done
	###
	node = gameNode.gameNode()
	if not node.load_game(filename):
		return ("Error: Fail Load", 0)
	if backtracking_helper(node):
		return node.solution()
	return ("Error: No Solution", 0)

def backtracking_helper(node):
	if node.solved():
		print node
		return True
	try:
		pos = next(node.get_unassigned_positions())
	except StopIteration:
		return False
	for move in node.get_valid_moves(pos):
		node[pos] = move
		if backtracking_helper(node):
			return True
		del node[pos]
	return False

def backtrackingMRV(filename):
	###
	# use backtracking + MRV to solve sudoku puzzle here,
	# return the solution in the form of list of
	# list as describe in the PDF with # of consistency
	# checks done
	###
	node = gameNode.gameNode()
	if not node.load_game(filename):
		return ("Error: Fail Load", 0)
	if backtrackingMRV_helper(node):
		return node.solution()
	return ("Error: No Solution", 0)

def backtrackingMRV_helper(node):
	return False

def backtrackingMRVfwd(filename):
	###
	# use backtracking +MRV + forward propogation
	# to solve sudoku puzzle here,
	# return the solution in the form of list of
	# list as describe in the PDF with # of consistency
	# checks done
	###
	node = gameNode.gameNode()
	if not node.load_game(filename):
		return ("Error: Fail Load", 0)
	if backtrackingMRVfwd_helper(node):
		return node.solution()
	return ("Error: No Solution", 0)

def backtrackingMRVfwd_helper(node):
	return False

def backtrackingMRVcp(filename):
	###
	# use backtracking + MRV + cp to solve sudoku puzzle here,
	# return the solution in the form of list of
	# list as describe in the PDF with # of consistency
	# checks done
	###
	node = gameNode.gameNode()
	if not node.load_game(filename):
		return ("Error: Fail Load", 0)
	if backtrackingMRVcp_helper(node):
		return node.solution()
	return ("Error: No Solution", 0)

def backtrackingMRVcp_helper(filename):
	return False

def minConflict(filename):
	###
	# use minConflict to solve sudoku puzzle here,
	# return the solution in the form of list of
	# list as describe in the PDF with # of consistency
	# checks done
	###
	node = gameNode.gameNode()
	if not node.load_game(filename):
		return ("Error: Fail Load", 0)
	if minConflict_helper(node):
		return node.solution()
	return ("Error: No Solution", 0)

def minConflict_helper(filename):
	return False
