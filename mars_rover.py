# Rotation list 90 degree right->
rotation_list = ['n','e','s','w']

class Rover:
    """
    Rover class to handle Rover and it's actions
    """
    def __init__(self,max_x,max_y):
        self.x = 0
        self.y = 0
        self.max_x = max_x
        self.max_y = max_y
        self.compass_point = None

    def set_initial_position(self,x,y,compass_point):
        """
        set the initial point of the rover
        :param x:
        :param y:
        :param compass_point:
        :return:
        """
        self.x = x
        self.y = y
        self.compass_point = compass_point.lower()

    def __move_rover(self,x,y, is_rotate):
        """
        This function will move the rover according to the command send to it
        :param x:
        :param y:
        :param is_rotate:
        :return:
        """
        if x > 0 and x !=0 and x <= self.max_x:
            self.x = x
        if y> 0 and y !=0 and y <= self.max_y:
            self.y = y
        if is_rotate == 'r':
            current_index = rotation_list.index(self.compass_point)
            new_index = current_index + 1
            if new_index >= len(rotation_list):
                self.compass_point = rotation_list[0]
            else:
                self.compass_point = rotation_list[new_index]
        elif is_rotate == 'l':
            current_index = rotation_list.index(self.compass_point)
            new_index = current_index - 1
            if new_index < 0:
                self.compass_point = rotation_list[len(rotation_list)-1]
            else:
                self.compass_point = rotation_list[new_index]


    def send_command(self,command:str):
        """
        This function will process the input command
        :param command:
        :return:
        """
        # Rotations
        # lr -> left mapped to a
        # lm->right mapped to b
        # Replace lm and lr with something meaningful

        sanitised_command = command.lower().replace('lm','b')
        sanitised_command = sanitised_command.lower().replace('lr','a')
        for value in sanitised_command:
            if value == 'l':
                self.__move_rover(0,self.y-1,'n')
            elif value == 'm':
                if self.compass_point == 'n':
                    self.__move_rover(0,self.y+1,'n') #upward
                elif self.compass_point == 's':
                    self.__move_rover(0,self.y-1,'n') #downward
                elif self.compass_point == 'e':
                    self.__move_rover(self.x+1,0,'n') #right
                else:
                    self.__move_rover(self.x-1,0,'n')
            elif value == 'r':
                if self.compass_point == 'n':
                    self.__move_rover(self.x+1,0,'n') #right
                elif self.compass_point == 's':
                    self.__move_rover(self.x+1, 0, 'n') #right
                elif self.compass_point == 'e':
                    self.__move_rover(0,self.y-1,'n') #est right is down
                else:
                    self.__move_rover(0,self.y+1,'n') #west right is up
            elif value == 'b':
                self.__move_rover(0,0,'r')
            elif value == 'a':
                self.__move_rover(0,0,'l')
            else:
                raise Exception('Unknown command')

    def get_position(self):
        """
        This function will return the current positions as
        x,y,compass point
        :return:
        """
        return self.x,self.y,self.compass_point.upper()



if __name__ == "__main__":
    obj = Rover(5,5)
    obj.set_initial_position(1,2,'N')
    obj.send_command('LMLMLMLMM')
    print(obj.get_position())
    obj.set_initial_position(3,3,'E')
    obj.send_command('MMRMMRMRRM')
    print(obj.get_position())