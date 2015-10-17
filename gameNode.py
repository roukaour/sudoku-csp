from itertools import product

def chunk(s, n):
	for i in xrange(0, len(s), n):
		yield s[i:i+n]

class cell(object):

	def __init__(self, i, j, value, N):
		self.i = i
		self.j = j
		self.given = value > 0
		self.domain = {value} if self.given else set(xrange(1, N + 1))

	def value(self):
		return list(self.domain)[0] if len(self.domain) == 1 else 0

class gameNode(object):

	def __init__(self):
		self.board = None
		self.N = self.M = self.K = 0
		self.num_checks = 0

	def __str__(self):
		w = len(str(self.N))
		return ('\n' + '-'*(3 * self.N + 2 * self.M - 3) + '\n').join(
			'\n'.join(t) for t in chunk([' | '.join(' '.join(s) for s in chunk([
			str(c.value()).rjust(w) for c in r], self.K)) for r in self.board], self.M))

	def __getitem__(self, pos):
		i, j = pos
		assert 0 <= i < self.N and 0 <= j < self.N
		return self.board[i][j]

	def __setitem__(self, pos, value):
		assert 0 < value <= self.N
		i, j = pos
		assert 0 <= i < self.N and 0 <= j < self.N and not self[pos].given
		self[pos].domain = {value}

	def __delitem__(self, pos):
		i, j = pos
		assert 0 <= i < self.N and 0 <= j < self.N
		self[pos].domain = set(self.get_values())

	def solved(self):
		return (all(self[pos].value() for pos in self.get_positions()) and
			not any(self.count_conflicts(pos) for pos in self.get_positions()))

	def solution(self):
		return ([[c.value() for c in r] for r in self.board], self.num_checks)

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
				tokens = line.strip().rstrip(';').split(',')
				row = [cell(i, j, 0 if v == '-' else int(v), self.N)
					for (j, v) in enumerate(tokens)]
				self.board.append(row)
			file.close()
			return True
		except IOError as e:
			print('Error:', e)
			print('Error: fail to load the testcase from file %s' % filename)
			self.board = None
			return False

	def get_values(self):
		return xrange(1, self.N + 1)

	def get_positions(self):
		return list(product(xrange(self.N), xrange(self.N)))

	def get_unassigned_positions(self):
		return [pos for pos in self.get_positions() if not self[pos].value()]

	def get_conflicted_positions(self):
		return [pos for pos in self.get_positions()
			if self[pos].value() and not self[pos].given and
			self[pos].value() in (self[n].value() for n in self.get_neighbors(pos))]

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
		if self[pos].value():
			return []
		invalid_moves = {self[n].value() for n in self.get_neighbors(pos)}
		return [m for m in self.get_values() if m not in invalid_moves]

	def count_constraints(self, pos, value=None):
		if value is None:
			value = self[pos].value()
		return len([n for n in self.get_neighbors(pos)
			if not self[n].value() and value in self.get_valid_moves(n)])

	def count_conflicts(self, pos, value=None):
		if value is None:
			value = self[pos].value()
		return len([n for n in self.get_neighbors(pos) if self[n].value() == value])
