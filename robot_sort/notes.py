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