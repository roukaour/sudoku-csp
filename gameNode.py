class gameNode():

	def __init__(self):
		self.gameStatus = None
		self.num_check = 0
		self.size = 0
		self.height = 0
		self.width = 0

	def __str__(self):
		return '\n'.join(' '.join(str(x).rjust(2) for x in self.gameStatus[i])
			for i in xrange(self.size))

	def load_game(self, filename):
		assert self.gameStatus is None
		self.gameStatus = []
		try:
			f = open(filename, 'r')
			metadata = f.readline().strip().rstrip(';').split(',')
			self.size, self.height, self.width = (int(t) for t in metadata)
			assert self.size == self.height * self.width
			for i in xrange(self.size):
				line = f.readline()
				elements = line.strip().rstrip(';').split(',')
				elements = [0 if x == '-' else int(x) for x in elements]
				self.gameStatus.append(elements)
			f.close()
			return True
		except IOError as e:
			print("Error:", e)
			print("Error: fail to load the testcase from file %s" % filename)
			self.gameStatus = None
			return False

	def solved(self):
		return all(self.gameStatus[i][j] != 0
			for i in xrange(self.size) for j in xrange(self.size))

	def has_load_game(self):
		return self.gameStatus is not None

	def get_valid_moves(self, i, j):
		assert self.has_load_game()
		if self.gameStatus[i][j] != 0:
			return []
		self.num_check += 1
		invalid_moves = set()
		# block
		bi = i // self.height * self.height
		bj = j // self.width * self.width
		for k in xrange(self.size):
			invalid_moves.add(self.gameStatus[i][k])
			invalid_moves.add(self.gameStatus[k][j])
			invalid_moves.add(self.gameStatus[bi+k//self.width][bj+k%self.width])
		return (m for m in xrange(1, self.size+1) if m not in invalid_moves)

	def set_value(self, i, j, v):
		self.gameStatus[i][j] = v

	def set_empty(self, i, j):
		self.gameStatus[i][j] = 0

	def solution(self):
		return (self.gameStatus, self.num_check)
