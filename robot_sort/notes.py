##Notes

def pick_up(self):
        #FIX
        self._item = self._position

def sort(self):
    """
    Sort the robot's list.
    """
    # Fill this out
    #first swap None with value at position 0
        #if comparing and position item is None, swap
    if self._position == 0:
        # self.pick_up()
        print(f'switching None at position {self._position}')

    while self.light_is_on() == False:   
        print('WHILE LIGHT: FALSE')
        if self.can_move_right() == True:
            print('can move right, moving right')
            #if yes, move right
            self.move_right()
            #compare: > check then move right
            print(f'holding: {self._item}')
            self.compare_item()
            print(f'comparing {self._item} to {self._position}')
            if self.compare_item() == 1: #checking if greater than
                if self.can_move_right() == True:
                    print('held item is greater, ')
                    return self.sort()
            if self.compare_item == -1: #then its less than
                # < swap then check and move right
                self.swap_item()
                print('held item is less, swapping item')
                if self.can_move_right() == True:
                    print('item swapped, sorting again')
                    return self.sort()
        
        else:
            print("CAN'T MOVE RIGHT, TURNING LIGHT ON")
            self.set_light_on()
            return self.sort()

#if no, can move left?
    print('WHILE LIGHT: TRUE')
        #if yes, first compare
    self.compare_item()
    print(f'comparing {self._item} to {self._position}')

    if self.compare_item() == 1: #is greater
        #if > swap then check and move left
        print('From Left: item is greater, swapping item')
        self.swap_item()
        if self.can_move_left() == True:
            print('moving left after swapping')
            self.move_left()
            return self.sort()
    if self.compare_item() == -1: #is less than
        print('From Left: item is less, moving left and sorting again')
        if self.can_move_left() == True:
            self.move_left()
            return self.sort()
    else:
        self.set_light_off()
        # return self.sort()


""" 
VERSION TWO --> COULDN'T DO SPLICING IN RECURSION, 
TRYING TO MOVE LEFT. WORKS THEN MAXES
"""

 if self._position == 0 and self._item == None:
            self.pick_up()
            print(f'Robot has picked up number: {self._item}')
        #pickup first item
        #can move right? YES
        while self.can_move_right() == True:
            #move right
            print("Can--> Moving right")
            self.move_right()
            #compare
            print(f'Comparing--> Held: {self._item} Compared: {self._position}')
            self.compare_item()
            #if held item is < compared item, SWAP
            if self.compare_item() == -1:
                print("Held is LESS than compared item. SWAPPING")
                self.swap_item()
            #if held item is > compare item, REPEAT 106-110
            elif self.compare_item() == 1:
                print("Held item is GREATER than compared. SORTING AGAIN")
                return self.sort()
        #can move right? NO!
        while self.can_move_right() == False:
            print("CAN'T move right --> comparing items")
            print(f'Comparing--> Held: {self._item} Compared: {self._position}')
            #compare item
            self.compare_item()
            #if held item is > compared item, SWAP
            if self.compare_item() == 1:
                print("Held item is GREATER--SWAPPING n=and SORTING AGAIN")
                self.swap_item()
                self.sort()
            #if held item is < compare item, recursive sort[:-1]
            elif self.compare_item() == -1:
                print("Held item is LESS than --> moving left")
                self.move_left()
                self.compare_item()
                print(f'Comparing--> Held: {self._item} Compared: {self._position}')
                #if held item is > compared item, SWAP
                if self.compare_item() == 1:
                    print("Held item is GREATER than, SWAPPING")
                    self.swap_item()
                    self.sort()
                elif self.compare_item() == -1:
                    print("Held item is LESS than. SORTING AGAIN")
                    self.sort()
        #if [:-1] = [1] OR if # goes through all and is < all #'s, switch again at position 0
