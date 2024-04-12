## Feito por Gabriel Juliani Segatto e Nícolas Sanson Giaboeski

import copy
import random

class Node:
    def __init__(self, data=[], f=0, g=0):
        self.data = data
        self.f = f
        self.g = g

    def f_calc(self):
        """ Return value of f(x) = h(x) + g(x)."""

        return (self.g + self.h_calc())
    
    def h_calc(self):
        """ Return value of h(x). """

        node_goal = Node(goal, 0, 0)
        distance = 0

        for i in range(3):
            for j in range(3):
                if self.data[i][j] != 0: 
                    x, y = self.find_number(self.data[i][j])
                    z, w = node_goal.find_number(self.data[i][j])
                    distance += abs(x - z) + abs(y - w)

        del node_goal
        return distance

    def find_number(self, number): 
        """ Return 'number' coordinates. """

        for i in range(3):
            for j in range(3):
                if self.data[i][j] == number:
                    return i,j
                
class Puzzle:
    def __init__(self, start):
        self.start = Node(start, 0, 0)
        self.open = []
        self.closed = [self.start]

    def print_node(self, node):
        """ Print the current node. """

        for i in node.data:
            print(i)
        print("\n")

    def actions(self, cur):
        """ Update the list 'open' with the possibilities of movement. """

        x, y = cur.find_number(0)

        """ Possibilities [left, right, up, down] respectively. """
        moves = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

        for i in moves:
            temp_data = copy.deepcopy(cur.data)

            if 0 <= i[0] < 3 and 0 <= i[1] < 3:
                number = cur.data[i[0]][i[1]]
                temp_data[x][y] = number
                temp_data[i[0]][i[1]] = 0
                new_node = Node(temp_data, 0, cur.g+1)
                new_node.f = new_node.f_calc()

                if not any(node.data == new_node.data for node in self.closed):
                    self.open.append(new_node)

        self.open.sort(key = lambda x: (x.f, x.h_calc()), reverse=False)
        
    def move(self):
        """ Method that moves the cell of the current node. """        
        
        if len(self.open) != 0:
            next_node = self.open[0]
            self.closed.append(self.open[0])
        else:
            print("\n O jogo iniciado é, provavelmente, impossível de se resolver. \n")

        self.open.clear()

        self.print_node(next_node)

        return next_node
    
    def solve(self):
        """ Method that solves the 8 - Puzzle. """

        cur = self.start
        print("\n\n")
        self.print_node(cur)

        while True:
            if cur.data == goal:
                print("Puzzle concluído em {} passos!".format(cur.g))
                break
            
            self.actions(cur)
            cur = self.move()

start = [[2, 3, 6], [1, 5, 0], [4, 7, 8]] 
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

puzzle = Puzzle(start)
puzzle.solve()
