#!/usr/bin/python

import heapq
import sys

# Input =======================================================================
def make_pairs(line):
  a = line.split('\t')
  return (int(a[1]), a[0])

def read_pairs(instream):
  return map(make_pairs, filter(lambda x: x != '', instream.read().split('\n')))

# Create a new name
def rename(a, b):
  return '(' + a[1] + b[1] + ')'

# Huffman Tree ================================================================
def huffman_tree(items, combine = rename):
  heapq.heapify(items)

  while len(items) != 1:
    sm1 = heapq.heappop(items)
    sm2 = heapq.heappop(items)

    new_name = combine(sm1, sm2)

    heapq.heappush(items, (sm1[0] + sm2[0], new_name))

  return items[0]

# Graphviz output =============================================================
class graph_tree:
  def __init__(self):
    self.__next = 0
    self.__total = 1.0

  def prologue(self, data):
    print 'digraph {'

    for freq, item in data:
      self.__total += freq
      print '  %s [label = "%s"];' % (item, item)

  def epilogue(self):
    print '}'

  def new_name(self, a, b):
    ident = self.__next
    self.__next += 1

    print '  n_%s [label = ""];' % (ident)
    return 'n_%s' % ident

  def edge_proportion(self, count):
    return 100 * count / self.__total

  def print_edge(self, src, dest, n):
    print '  %s -> %s [label = "%d\n%.3f%%"];' % (src[1], dest, n, self.edge_proportion(src[0]))
    
  def draw_link(self, a, b):
    new_name = self.new_name(a, b)
    self.print_edge(a, new_name, 0)
    self.print_edge(b, new_name, 1)
    return new_name

  def treeify(self, data):
    self.prologue(data)
    huffman_tree(data, self.draw_link)
    self.epilogue()

# Main ========================================================================
if __name__ == '__main__':
  raw = read_pairs(sys.stdin)

  gt = graph_tree()

  gt.treeify(raw)
