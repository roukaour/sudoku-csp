
class gameNode():
    def __init__(self):
        self.gameStatus = None
        self.num_check = 0

        self.size = 0
        self.height = 0
        self.width = 0

    def load_game(self, filename):
        assert(self.gameStatus is None)
        self.gameStatus = []
        try:
            with open(filename, 'r') as f:
                firstline = f.readline()
                self.size, self.height, self.width = [int(x) for x in firstline.strip()[:-1].split(',')]
                assert(self.size == self.height * self.width)
                for i in range(self.size):
                    line = f.readline()
                    elements = line.strip()[:-1].split(',')
                    elements = [0 if x == '-' else int(x) for x in elements]
                    self.gameStatus.append(elements)

        except IOError as e:
            print("Error:", e)
            print("Error: fail to load the testcase from file %s" % (filename))
            self.gameStatus = None
            return False

        return True

    def solved(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.gameStatus[i][j] == 0:
                    return False
        return True

    def has_load_game(self):
        return self.gameStatus is not None

    def get_valid_moves(self, i, j):
        assert(self.has_load_game())
        if self.gameStatus[i][j] != 0:
            return []

        self.num_check += 1

        unvalid_moves = set()

        # block
        block_i = i // self.height * self.height
        block_j = j // self.width * self.width

        for x in range(self.size):
            unvalid_moves.add(self.gameStatus[i][x])
            unvalid_moves.add(self.gameStatus[x][j])
            unvalid_moves.add(self.gameStatus[block_i+x//self.width][block_j+x%self.width])

        valid_moves = [x for x in range(self.size+1) if x not in unvalid_moves]
        return valid_moves

    def set_value(self, i, j, v):
        self.gameStatus[i][j] = v

    def set_empty(self, i, j):
        self.gameStatus[i][j] = 0

    def p(self):
        for i in range(self.size):
            print ' '.join([(' ' + str(x)) if x < 10 else str(x) for x in self.gameStatus[i]])

    def solution(self):
        return (self.gameStatus, self.num_check)
