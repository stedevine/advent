class LightGrid:
    def count_on_neighbors(x,y,matrix):
        #Check all neighbours starting at top-left, moving clockwise
        # assume a square matrix (the problem space is square)

        n = len(matrix[0])
        on_count = 0
        if y - 1 >= 0 and x - 1 >= 0 and matrix[x-1][y-1]==1:
            on_count += 1

        if y - 1 >= 0 and matrix[x][y-1]==1:
            on_count += 1

        if y - 1 >= 0 and x + 1 < n and matrix[x+1][y-1]==1:
            on_count += 1

        if x + 1 < n and matrix[x+1][y]==1:
            on_count += 1

        if y + 1 < n and x + 1 < n and matrix[x+1][y+1]==1:
            on_count += 1

        if y + 1 < n and matrix[x][y+1]==1:
            on_count += 1

        if y + 1 < n and x - 1 >= 0 and matrix[x-1][y+1]==1:
            on_count += 1

        if x - 1 >= 0 and matrix[x-1][y]==1:
            on_count += 1

        return on_count

    def has_exactly_three_neighbors_on(x,y,matrix):
        return LightGrid.count_on_neighbors(x,y,matrix) == 3

    def has_two_or_three_neighbors_on(x,y,matrix):
        count = LightGrid.count_on_neighbors(x,y,matrix)
        return count == 2 or count == 3

    def get_switch_list(matrix):
        switchList =[]
        n = len(matrix[0])
        for i in range(0, n):
            for j in range(0, n):
                if (matrix[i][j] == 1 and not LightGrid.has_two_or_three_neighbors_on(i,j, matrix) and not LightGrid.is_corner(i,j, len(matrix[0]))):
                    switchList.append({'x': i, 'y': j})
                elif (matrix[i][j] == 0 and LightGrid.has_exactly_three_neighbors_on(i,j, matrix) and not LightGrid.is_corner(i,j, len(matrix[0]))):
                    switchList.append({'x': i, 'y': j})
        return switchList

    def apply_switches(switchList, matrix):
        for s in switchList:
            if matrix[s['x']][s['y']] == 0 :
                matrix[s['x']][s['y']] = 1
            else:
                matrix[s['x']][s['y']] = 0

    def is_corner(x,y, n):
        if (x == 0 and y == 0):
            return True

        if (x == 0 and y == n-1):
            return True

        if (x == n-1 and y==0):
            return True

        if (x == n-1 and y == n-1):
            return True

        return False;


    def create_matrix(filename):
        f = open(filename,'r')
        n = len(f.readline().strip('\n'))
        print(n)
        matrix = [[0 for x in range(n)] for x in range(n)]
        f.seek(0)
        j = 0
        for line in f:
            line = line.strip('\n')
            i = 0
            for c in line:
                #print("{i} {j}".format(i=i,j=j))
                matrix[i][j] = 0 if c == '.' else 1
                i += 1
            j += 1

        # corner lights are always on
        matrix[0][0] = 1
        matrix[0][n-1] = 1
        matrix[n-1][0] = 1
        matrix[n-1][n-1] = 1

        return matrix

    def print_matrix(matrix):
        n = len(matrix[0])
        for i in range(n):
            text = ""
            for j in range(n):
                text += str(matrix[i][j])
            print(text)

    def count_on_lights(matrix):
        count = 0
        n = len(matrix[0])
        for i in range(n):
            count += matrix[i].count(1)

        print(count)

matrix = LightGrid.create_matrix('input.txt')
LightGrid.print_matrix(matrix)
for i in range(100):
    switches = LightGrid.get_switch_list(matrix)
    LightGrid.apply_switches(switches, matrix)
    print("")
    LightGrid.print_matrix(matrix)


LightGrid.count_on_lights(matrix)
