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
		return (all(self[pos] for pos in self.get_positions()) and
			not any(self.count_conflicts(pos, self[pos]) for pos in self.get_positions()))

	def solution(self):
		return (self.board, self.num_checks)

	def load_game(self, filename):
		self.board = []
		try:
			file = open(filename, 'r')
			metadata = file.readline().strip().rstrip(';').split(',')
			self.N, self.M, self.K = (int(t) for t in metadata)
			if self.N != self.M * self.K:
				raise IOError('N != M * K')
			for i in xrange(self.N):
				line = file.readline()
				elements = line.strip().rstrip(';').split(',')
				elements = [0 if x == '-' else int(x) for x in elements]
				self.board.append(elements)
			file.close()
			return True
		except IOError as e:
			print('Error:', e)
			print('Error: fail to load the testcase from file %s' % filename)
			self.board = None
			return False

	def get_positions(self):
		return list(product(xrange(self.N), xrange(self.N)))

	def get_unassigned_positions(self):
		return [pos for pos in self.get_positions() if not self[pos]]

	def get_conflicted_positions(self):
		return [pos for pos in self.get_positions()
			if self[pos] and self.count_conflicts(pos, self[pos])]

	def get_neighbors(self, pos):
		i, j = pos
		bi = i // self.M * self.M
		bj = j // self.K * self.K
		neighbors = set()
		for k in xrange(self.N):
			neighbors.add((i, k))
			neighbors.add((k, j))
			neighbors.add((bi + k // self.K, bj + k % self.K))
		neighbors.remove(pos)
		return list(neighbors)

	def get_valid_moves(self, pos):
		if self[pos]:
			return []
		invalid_moves = {self[n] for n in self.get_neighbors(pos)}
		return [m for m in xrange(1, self.N + 1) if m not in invalid_moves]

	def count_constraints(self, pos, value):
		return len([n for n in self.get_neighbors(pos)
			if not self[n] and value in self.get_valid_moves(n)])

	def count_conflicts(self, pos, value):
		return len([n for n in self.get_neighbors(pos) if self[n] == value])
