map_sokoban = {
    "size_x": 5,
    "size_y": 5
}
player = {
    "x": 4,
    "y": 0
}
boxes = [
    {
        'x': 1,
        'y': 1
    }, 
    {
        'x': 2,
        'y': 2
    },
    {
        'x': 3,
        'y': 3
    }
]
destination = [
    {
        'x': 2,
        'y': 1
    }, 
    {
        'x': 3,
        'y': 2
    },
    {
        'x': 4,
        'y': 3
    }
]
playing = True
while playing:
    for y in range(map_sokoban['size_y']):
        for x in range(map_sokoban['size_x']):
            box_is_here = False
            for box in boxes:
                if y == box['y'] and x == box['x']:
                    # print("B ", end = "")
                    box_is_here = True    
            player_is_here = False
            if y == player['y'] and x == player['x']:
                # print("P", end = "")
                player_is_here = True
            # elif box_is_here is False:
            #     # print("- ", end = "")
            destination_is_here = False
            for dessss in destination:
                if y == dessss['y'] and x == dessss['x']:
                    destination_is_here = True 
            if player_is_here:
                print("P ", end = "")
            elif box_is_here:
                print("B ", end = "")
            elif destination_is_here:
                print("D ", end="")
            else:
                print("- ", end = "")
        print()
    
    win = True        
    for box in boxes:
        if box not in destination:
            win = False
    if win :
        print("You win!")
        break      

    ym = input("Your move? ").lower()

    dx = 0
    dy= 0
    if ym == "w":
        dy = -1
    elif ym == "s":
        dy = 1
    elif ym == "a":
        dx = -1
    elif ym == "d":
        dx = 1
    else:
        player = False  
    if 0 <= player['x'] + dx < map_sokoban['size_x']\
      and 0 <= player['y'] + dy < map_sokoban['size_y']:
      player['x'] += dx
      player['y'] += dy
    
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy
     





   

