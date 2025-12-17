#!/usr/bin/env python3
import sys
from collections import defaultdict

def parse(lines):
	g = defaultdict(list)
	for line in lines:
		line = line.strip()
		if not line or ':' not in line:
			continue
		name, rest = line.split(':', 1)
		name = name.strip()
		outs = [tok.strip() for tok in rest.strip().split() if tok.strip()]
		if outs:
			g[name].extend(outs)
	return g

def count_paths(graph, src='you', dst='out'):
	sys.setrecursionlimit(10000)

	def dfs(node, seen):
		if node == dst:
			return 1
		if node in seen:
			return 0
		seen.add(node)
		total = 0
		for nb in graph.get(node, []):
			total += dfs(nb, seen)
		seen.remove(node)
		return total

	return dfs(src, set())

with open('input.txt', 'r') as f:
	lines = f.readlines()

graph = parse(lines)
print(count_paths(graph))

