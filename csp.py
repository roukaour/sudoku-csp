import random
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
	node.num_checks += 1
	if node.solved():
		print node
		return True
	unassigned = node.get_unassigned_positions()
	if not unassigned:
		return False
	pos = unassigned[0]
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
	node.num_checks += 1
	if node.solved():
		print node
		return True
	unassigned = node.get_unassigned_positions()
	if not unassigned:
		return False
	mrv_pos = min(unassigned, key=lambda p: len(node.get_valid_moves(p)))
	lcv_moves = sorted(node.get_valid_moves(mrv_pos),
		key=lambda m: node.count_constraints(mrv_pos, m))
	for move in lcv_moves:
		node[mrv_pos] = move
		if backtrackingMRV_helper(node):
			return True
		del node[mrv_pos]
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

def backtrackingMRVcp_helper(node):
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

def minConflict_helper(node, max_steps=1000):
	# initial complete assignment
	# greedy minimal-conflict values for each variable
	for pos in node.get_positions():
		if not node.is_given(pos):
			node[pos] = min(node.get_values(),
				key=lambda m: node.count_conflicts(pos, m))
	print node
	for _ in xrange(max_steps):
		if node.solved():
			print node
			return True
		con_pos = random.choice(node.get_conflicted_positions())
		lcv_move = min(node.get_values(),
			key=lambda m: node.count_conflicts(con_pos, m))
		node[con_pos] = lcv_move
	return False
