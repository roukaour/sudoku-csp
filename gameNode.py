from itertools import product

def chunk(s, n):
	for i in xrange(0, len(s), n):
		yield s[i:i+n]

class gameNode():

	def __init__(self):
		self.board = None
		self.N = self.M = self.K = 0
		self.num_checks = 0

	def __str__(self):
		return ('\n' + '-'*(3 * self.N + 2 * self.M - 3) + '\n').join(
			'\n'.join(t) for t in chunk([' | '.join(' '.join(s) for s in chunk([
			str(x).rjust(2) for x in r], self.K)) for r in self.board], self.M))

	def __getitem__(self, pos):
		i, j = pos
		assert 0 <= i < self.N and 0 <= j < self.N
		return self.board[i][j]

	def __setitem__(self, pos, value):
		assert 0 < value <= self.N
		i, j = pos
		assert 0 <= i < self.N and 0 <= j < self.N
		self.board[i][j] = value

	def __delitem__(self, pos):
		i, j = pos
		assert 0 <= i < self.N and 0 <= j < self.N
		self.board[i][j] = 0

	def solved(self):
		return all(self.board[i][j] for i in xrange(self.N) for j in xrange(self.N))

	def solution(self):
		return (self.board, self.num_checks)

	def load_game(self, filename):
		assert self.board is None
		self.board = []
		try:
			f = open(filename, 'r')
			metadata = f.readline().strip().rstrip(';').split(',')
			self.N, self.M, self.K = (int(t) for t in metadata)
			assert self.N == self.M * self.K
			for i in xrange(self.N):
				line = f.readline()
				elements = line.strip().rstrip(';').split(',')
				elements = [0 if x == '-' else int(x) for x in elements]
				self.board.append(elements)
			f.close()
			return True
		except IOError as e:
			print("Error:", e)
			print("Error: fail to load the testcase from file %s" % filename)
			self.board = None
			return False

	def get_unassigned_positions(self):
		for pos in product(xrange(self.N), xrange(self.N)):
			if not self[pos]:
				yield pos

	def get_valid_moves(self, pos):
		assert self.board is not None
		self.num_checks += 1
		if self[pos]:
			return ()
		i, j = pos
		invalid_moves = set()
		# block
		bi = i // self.M * self.M
		bj = j // self.K * self.K
		for k in xrange(self.N):
			invalid_moves.add(self[i, k])
			invalid_moves.add(self[k, j])
			invalid_moves.add(self[bi + k // self.K, bj + k % self.K])
		return (m for m in xrange(1, self.N + 1) if m not in invalid_moves)
