
import gameNode

###########################################
# you need to implement five funcitons here
###########################################

def backtrackingHelper(node):
    if node.solved():
        # node.p()
        return True

    for i in range(node.size):
        for j in range(node.size):
            if node.gameStatus[i][j] == 0:
                valid_values = node.get_valid_moves(i, j)
                for k in valid_values:
                    node.set_value(i, j, k)
                    if backtrackingHelper(node):
                        return True
                    node.set_empty(i, j)

                return False
    return False


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

    if backtrackingHelper(node):
        return node.solution()

    return ("Error: No Solution", 0)

def backtrackingMRVHelper(node):
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

    if backtrackingMRV(node):
        return node.solution()

    return ("Error: No Solution", 0)

def backtrackingMRVfwdHelper(node):
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

    if backtrackingMRVfwdHelper(node):
        return node.solution()
    
    return ([[],[]], 0)

def backtrackingMRVcp(filename):
    ###
    # use backtracking + MRV + cp to solve sudoku puzzle here,
    # return the solution in the form of list of 
    # list as describe in the PDF with # of consistency
    # checks done
    ###
    
    return ([[],[]], 0)

def minConflict(filename):
    ###
    # use minConflict to solve sudoku puzzle here,
    # return the solution in the form of list of 
    # list as describe in the PDF with # of consistency
    # checks done
    ###
    
    return ([[]], 0)