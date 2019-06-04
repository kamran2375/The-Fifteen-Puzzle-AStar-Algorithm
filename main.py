from puzzle import Puzzle
import os

def play_game():
    puzzle = Puzzle()
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        puzzle.display()
        if(puzzle.check()):
            print("You win!")
            break
        _in = input("Enter number or x for exit: ")
        if _in == 'x': break
        matrix = puzzle.get()
        for i in range(4):
            if int(_in) in matrix[i]:
                puzzle.move(i, matrix[i].index(int(_in)))
                break

def heuristic(matrix, end, number):
    t = 0

    ## Heuristic 1 ##
    if number == 1:
        for i, j in zip(matrix, end):
            for k, l in zip(i, j):
                if k != l: t += 1
        return t
    
    ## Heuristic 2 ##
    if number == 2:
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if matrix[i][j] in end[k]:
                        t += abs(i-k) + abs(j-end[k].index(matrix[i][j]))
        return t

    ## Heuristic 3 ##
    if number == 3:        
        for i, j in zip(matrix, end):
            for k, l in zip(i, j):
                if k != l: t += 1 + (1 if i.index(k) < 2 else 0)
        return t

def astar(puzzle, heuristicNumber):
    nodes = []
    route = [puzzle.matrix]
    number_of_nodes = 0
    
    while True:
        if route[-1] == puzzle.end: break

        for i in puzzle.moves():
            
            if i not in route: 
                t = route.copy()
                t.append(i)
                nodes.append(t)

        route = nodes[0]
        for i in nodes:
            if heuristic(i[-1], puzzle.end, heuristicNumber) + len(i) < heuristic(route[-1], puzzle.end, heuristicNumber) + len(route): route = i

        nodes.remove(route)
        puzzle.set(route[-1])
        number_of_nodes += 1

    return [number_of_nodes, route]


if __name__ == '__main__':
    _in = input('\n0.Play game \n1.Heuristic 1 \n2.Heuristic 2 \n3.Heuristic 3 \n\nEnter number: ')
        
    if _in == '0':
        play_game()
    else:
        puzzle = Puzzle([[4, 1, 6, 2], [5, 0, 9, 3], [8, 13, 10, 7], [12, 14, 15, 11]])
        puzzle.display()
        res = astar(puzzle, int(_in))
        print("\nNumber of nodes: " + str(res[0]), "\nSolution: ")
        for i in res[1]: print(i)