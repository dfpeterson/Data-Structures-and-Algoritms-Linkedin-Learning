maze = ['******', '* *  *', '*  * *', '* ****','*    *', '******']

for row in maze:
    print(row)


with open(r'..\Exercise Files\02_03_challenge\mazes\challenge_maze.txt', 'r') as amaze:
    ing = amaze.readlines()
    for row in ing:
        print(list(row))