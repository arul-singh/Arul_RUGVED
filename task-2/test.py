import math

pos = (0.0, 0.0, 0.0)  
history = [pos]


def path(current_pos, command, value):
    x, y, theta = current_pos

    if command == "forward":
        
        x += value * math.cos(math.radians(theta))
        y += value * math.sin(math.radians(theta))

    elif command == "left":
        
        theta += value

    elif command == "right":
        
        theta -= value

    new_pos = (x, y, theta)
    history.append(new_pos)
    return new_pos


pos = path(pos, "forward", 10)
pos = path(pos, "left", 10)
pos = path(pos, "forward", 10)

print(history)