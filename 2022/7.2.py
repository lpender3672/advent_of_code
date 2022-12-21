
commands = []
with open('2022/7.txt', 'r') as f:
    for l in f:
        commands.append(l.strip())

dirs = {"/home":0}
path = "/home"

for c in commands:
    command = c.split(" ")
    if command[0] == "$":
        if command[1] == "ls":
            pass

        elif command[1] == "cd":
            if command[2] == "/":
                path = "/home"

            elif command[2] == "..":
                path = path[0:path.rfind("/")]

            else:
                dir_name = command[2]
                path = path + "/" + dir_name
                dirs.update({path:0})

    elif command[0] == "dir":
        pass

    else:
        size = int(command[0])
        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]

# space required - space unused (total space - space used)
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []

# Iterate through every path
for dir in dirs:
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])

smallest = min(valid_dirs)
print(smallest)
