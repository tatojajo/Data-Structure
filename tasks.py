from main import Queue, Stack


# elements = "()[]{}"

def valid_parentheses(elments):
    stack = Stack()
    
    for char in elments:
        if char in [')', '}', ']']:
            if stack.size() == 0:
                return False
            last_element = stack.pop()
            if last_element == '(' and char == ')' or last_element == '[' and char == ']' or last_element == '{' and char == '}':
                continue
            return False
        else:
            stack.push(char)
    
    return stack.size() == 0

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

def numIslands(grid):
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        neighbours = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        visited = set()
        que = Queue()

        def bfs(row, col):
            que.enQueue((row, col))
            while not que.isEmpty():
                r, c = que.deQueue()
                if (r, c) not in visited:
                    visited.add((r, c))
                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        que.enQueue((nr, nc))
                        visited.add((nr, nc))
             
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    bfs(i, j)
        return islands
    
    
    
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens):
        stack = Stack()
        
        for token in tokens:
            if token.isdigit() or (token.lstrip('-').isdigit() and token.count('-') <= 1):
                stack.push(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                result = eval(str(second) + token + str(first))
                stack.push(int(result))

        return int(stack.top())