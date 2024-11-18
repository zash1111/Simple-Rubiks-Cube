# simple text-based rubik's cube

front_face = [['W' for i in range(3)] for j in range(3)]
top_face = [['R' for i in range(3)] for j in range(3)]
bottom_face = [['G' for i in range(3)] for j in range(3)]
left_face = [['B' for i in range(3)] for j in range(3)]
right_face = [['Y' for i in range(3)] for j in range(3)]
back_face = [['O' for i in range(3)] for j in range(3)]

def print_cube():
    #print blank top blank
    for i in range(3):
        print("    ", end='')
        for j in range(3):
            print(top_face[i][j], end='')
        print()
    
    #print left, front, right
    for i in range(3):
        for j in range (3):
            print(left_face[i][j], end='')
        print(' ', end='')
        for j in range (3):
            print(front_face[i][j], end='')
        print(' ', end='')
        for j in range (3):
            print(right_face[i][j], end='')
        print()

    #print blank, bottom, back
    for i in range(3):
        print("    ", end='')
        for j in range(3):
            print(bottom_face[i][j], end='')
        print(' ', end='')
        for j in range (3):
            print(back_face[i][j], end='')
        print()
    
    print()

def spin_row_right(row):
    temp = front_face[row]
    front_face[row] = left_face[row]
    left_face[row] = back_face[row]
    back_face[row] = right_face[row]
    right_face[row] = temp

def spin_row_left(row):
    temp = front_face[row]
    front_face[row] = right_face[row]
    right_face[row] = back_face[row]
    back_face[row] = left_face[row]
    left_face[row] = temp

def spin_col_up(col):
    temp = [front_face[0][col], front_face[1][col], front_face[2][col]]
    for i in range(3):
        front_face[i][col] = bottom_face[i][col]
        bottom_face[i][col] = back_face[i][col]
        back_face[i][col] = top_face[i][col]
        top_face[i][col] = temp[i]

def spin_col_down(col):
    temp = [front_face[0][col], front_face[1][col], front_face[2][col]]
    for i in range(3):
        front_face[i][col] = top_face[i][col]
        top_face[i][col] = back_face[i][col]
        back_face[i][col] = bottom_face[i][col]
        bottom_face[i][col] = temp[i]

def spin_face_clockwise(depth):
    temp = top_face[depth]
    for i in range(3):
        top_face[depth][i] = right_face[i][depth]
        right_face[i][depth] = bottom_face[depth][i]
        bottom_face[depth][i] = left_face[i][depth]
        left_face[i][depth] = temp[i]

def spin_face_counterclockwise(depth):
    temp = top_face[depth]
    for i in range(3):
        top_face[depth][i] = left_face[i][depth]
        left_face[i][depth] = bottom_face[depth][i]
        bottom_face[depth][i] = right_face[i][depth]
        right_face[i][depth] = temp[i]

def print_choices():
    print("Use Capital Letters to indicate a request to rotate that face clockwise")
    print("   (U)pper face   (D)own face   (R)ight face   (L)eft face   (F)ront face   (B)ack face")
    print("Send a face with a 2 after it two make that move twice")
    print("Send a face with a single apostraphe (') to rotate in a counter clockwise direction ")
    print("Send a lower case letter to rotate the middle layer in conjuction with the other face")
    print("Send x y or z to rotate the face that is facing toward you")
    print("Send M E or S to preform a slice (moving only the middle layer)")


next_choice = ""


while (next_choice != "Q"):
    print_cube()
    next_choice = input("What move would you like to perform (H to see moves Q to quit): ")
    match next_choice:
        case "H":
            print_choices()

        case "U":
            spin_row_left(0)
            
        case "U2":
            spin_row_left(0)
            spin_row_left(0)

        case "U'":
            spin_row_right(0)

        case "u":
            spin_row_left(0)
            spin_row_left(1)

        case "u2":
            spin_row_left(0)
            spin_row_left(1)
            spin_row_left(0)
            spin_row_left(1)

        case "u'":
            spin_row_right(0)
            spin_row_right(1)

        case "D":
            spin_row_right(2)

        case "D2":
            spin_row_right(2)
            spin_row_right(2)

        case "D'":
            spin_row_left(2)

        case "d":
            spin_row_right(2)
            spin_row_right(1)

        case "d2":
            spin_row_right(2)
            spin_row_right(1)
            spin_row_right(2)
            spin_row_right(1)

        case "d'":
            spin_row_left(2)
            spin_row_left(1)

        case "R":
            spin_col_up(2)

        case "R2":
            spin_col_up(2)
            spin_col_up(2)

        case "R'":
            spin_col_down(2)

        case "r":
            spin_col_up(2)
            spin_col_up(1)

        case "r2":
            spin_col_up(2)
            spin_col_up(1)
            spin_col_up(2)
            spin_col_up(1)

        case "r'":
            spin_col_down(2)
            spin_col_down(1)

        case "L":
            spin_col_down(0)

        case "L2":
            spin_col_down(0)
            spin_col_down(0)

        case "L'":
            spin_col_up(0)

        case "l":
            spin_col_down(0)
            spin_col_down(1)

        case "l2":
            spin_col_down(0)
            spin_col_down(1)
            spin_col_down(0)
            spin_col_down(1)

        case "l'":
            spin_col_up(0)
            spin_col_up(1)

        case "F":
            spin_face_clockwise(0)

        case "F2":
            spin_face_clockwise(0)
            spin_face_clockwise(0)

        case "F'":
            spin_face_counterclockwise(0)

        case "f":
            spin_face_clockwise(0)
            spin_face_clockwise(1)

        case "f2":
            spin_face_clockwise(0)
            spin_face_clockwise(1)
            spin_face_clockwise(0)
            spin_face_clockwise(1)

        case "f'":
            spin_face_counterclockwise(0)
            spin_face_counterclockwise(1)

        case "B":
            spin_face_counterclockwise(2)

        case "B2":
            spin_face_counterclockwise(2)
            spin_face_counterclockwise(2)

        case "B'":
            spin_face_clockwise(2)

        case "b":
            spin_face_counterclockwise(2)
            spin_face_counterclockwise(1)

        case "b2":
            spin_face_counterclockwise(2)
            spin_face_counterclockwise(1)
            spin_face_counterclockwise(2)
            spin_face_counterclockwise(1)

        case "b'":
            spin_face_clockwise(2)
            spin_face_clockwise(1)

        case "M":
            spin_col_down(1)

        case "M2":
            spin_col_down(1)
            spin_col_down(1)

        case "M'":
            spin_col_up(1)

        case "E":
            spin_row_right(1)

        case "E2":
            spin_row_right(1)
            spin_row_right(1)

        case "E'":
            spin_row_left(1)

        case "S":
            spin_face_clockwise(1)

        case "S2":
            spin_face_clockwise(1)
            spin_face_clockwise(1)

        case "S'":
            spin_face_counterclockwise(1)

        case "x":
            spin_col_up(0)
            spin_col_up(1)
            spin_col_up(2)

        case "x2":
            spin_col_up(0)
            spin_col_up(1)
            spin_col_up(2)
            spin_col_up(0)
            spin_col_up(1)
            spin_col_up(2)

        case "x'":
            spin_col_down(0)
            spin_col_down(1)
            spin_col_down(2)

        case "y":
            spin_row_left(0)
            spin_row_left(1)
            spin_row_left(2)

        case "y2":
            spin_row_left(0)
            spin_row_left(1)
            spin_row_left(2)
            spin_row_left(0)
            spin_row_left(1)
            spin_row_left(2)

        case "y'":
            spin_row_right(0)
            spin_row_right(1)
            spin_row_right(2)

        case "z":
            spin_face_clockwise(0)
            spin_face_clockwise(1)
            spin_face_clockwise(2)

        case "z2":
            spin_face_clockwise(0)
            spin_face_clockwise(1)
            spin_face_clockwise(2)
            spin_face_clockwise(0)
            spin_face_clockwise(1)
            spin_face_clockwise(2)

        case "z'":
            spin_face_counterclockwise(0)
            spin_face_counterclockwise(1)
            spin_face_counterclockwise(2)

        case "Q":
            print("Exiting now")

        case _:
            print("Not a recognized move")


