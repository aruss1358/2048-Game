def rotated_field(playing_field):
    rotated_field=[]
    for position in range(0,5):
        new_line=[]
        for line in range(0,5):
            new_line.append((playing_field[(4-line)])[position])
        rotated_field.append(new_line)
    return(rotated_field)
