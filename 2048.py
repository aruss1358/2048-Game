#2048 movements

#Define a function for what happens when the player swipes from right to left
def left_swipe(playing_field):
    new_field=[]
    for line in playing_field:
        new_line=[]
        condensed_line=[]
        for ch in line:
            #get rid of blanks to give the appearance of numbers shifting left
            if ch!=" ":
                new_line.append(ch)
        # combine numbers starting from the left
        #copy numbers from the left unless they will condense
        index=0
        while index<len(new_line)-1:
            #just copy if they are not equal
            if new_line[index]!=new_line[index+1]:
            
                condensed_line.append(new_line[index])
                index+=1
            #condense squares 
            else:
                condensed_line.append(new_line[index]*2)
                index+=2
            #account for the last one being added if the last 2 are not equal
            if index==len(new_line)-1:
                    condensed_line.append(new_line[-1])
       
        #handle a single input
        if len(new_line)==1:
            condensed_line.append(new_line[0])
            
        #add spaces to the end to fill in each line
        while len(condensed_line)!=5:
            condensed_line.append(" ")

        new_field.append(condensed_line)
        

    return (new_field)

#Define a function for  right swipe
def right_swipe(playing_field):
    new_field=[]
    for line in playing_field:
        new_line=[]
        #this differs from the left swipe. This allows assignment from the right and gets rid of the add spaces statement
        condensed_line=[" "]*5
        for ch in line:
            #get rid of blanks to give the appearance of numbers shifting right
            if ch!=" ":
                new_line.append(ch)
        index=-1
        while index>(-len(new_line)):
            #just copy if not equal
            if new_line[index]!=new_line[index-1]:
                for i in range(1,len(condensed_line)):
                    if condensed_line[-i] == " ":
                        condensed_line[-i]=new_line[index]
                        break
                
                index-=1
                              
            #condense squares
            else:
                for i in range(1,len(condensed_line)):
                    if condensed_line[-i] == " ":
                        condensed_line[-i]=new_line[index]*2
                        break
                index-=2
            #account for the last one being added if the two are not equal
            if index==-len(new_line):
                for i in range(1,len(condensed_line)):
                    if condensed_line[-i] == " ":
                        condensed_line[-i]=new_line[index]
                        break
        #Handle a line with only one input
        if len(new_line)==1:
            condensed_line[-1]=new_line[0]
            
        new_field.append(condensed_line)
        
    return(new_field)

#define a function to make up and down display horizontally
def retrieve_for_up_and_down(playing_field):
    rotated_field=[]
    #read the place in each line and add them to a list so we can treat it like an up or down swipe
    for place in range(0,5):
        new_line=[]
        for line in playing_field:
            new_line.append(line[place])
        rotated_field.append(new_line)
    return(rotated_field)

def read_out(rotated_field):
    new_field=[]
    for i in range(0,5):
        new_line=[]
        for line in rotated_field:
            new_line.append(line[i])
        new_field.append(new_line)
    return(new_field)
    
            

#define a function for up swipe
def up_swipe(playing_field):
    new_field=[]
    rotated_field=retrieve_for_up_and_down(playing_field)
    rotated_field=left_swipe(rotated_field)
    new_field=read_out(rotated_field)
    return(new_field)

#define a function for down swipe 
def down_swipe(playing_field):
    new_field=[]
    rotated_field=retrieve_for_up_and_down(playing_field)
    rotated_field=right_swipe(rotated_field)
    new_field=read_out(rotated_field)
    return(new_field)

# define a function to disply the numbers among a field of stars
def format_playing_field(playing_field):
    print("*"*32)
    print("*"*32)
    #go through each line in the playing field
    for line in playing_field:
        string="**"
        # center the numbers in the slots
        for space in line:
            str_space=str(space)
            if len(str_space)==1:
                str_space="  "+str_space+" "
            elif len(str_space)==2:
                str_space=" "+str_space+" "
            elif len(str_space)==3:
                str_space=str_space+" "
            #add the number to the line
            string+=str_space
            string+="**"
        print(string)
        print("*"*32)
        print("*"*32)
def check_win(playing_field):
    for line in playing_field:
            for number in line:
                if number==2048:
                    print("You Won!!")
                    return(True)
    return(False)
def main():

    while check_win(playing_field) True:
        #check for a win
        
        #ask user how they want to move
        move=input("How would you like to move?")
        #process the change in the playing field
        if move=="up" or move=="Up":
            playing_field=up_swipe(playing_field)
        elif move=="down" or move=="Down":
            playing_field=down_swipe(playing_field)
        elif move=="left" or move=="Left":
            playing_field=left_swipe(playing_field)
        elif move=="right" or move=="Right":
            playing_field=right_swipe(playing_field)
        else:
            print("You have put an invalid input")
            
        #print the plaing field in a human readable format  
        format_playing_field(playing_field)
        
        



playing_field=[[2," ",2,4,4],[2,2,4,4,8],[4,8,16," "," "],[" ",4,4,4,4],[4," ",8,8,8]]




  
            
