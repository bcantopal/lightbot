''''
mylist = [1,2,3,4,5,6,7]
mylist.append(mylist[0])
mylist[0]=mylist[-2]
mylist.pop(mylist[-3])


print(mylist)
'''
class LightBotKernel:
    def __init__(self, width=10, height=10):
        # Initialize the 10x10 terrain grid with flat blue squares (height=1, light off)
        self.terrain = [[{'height': 1, 'light': False} for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

        # Bot starting position and direction (0,0) facing up
        self.bot_x = 0
        self.bot_y = 10
        self.direction = 'UP'

    def print_state(self):
        """Prints the current state of the bot and terrain for debugging."""
        print(f"Bot position: ({self.bot_x}, {self.bot_y})")
        print(f"Bot direction: {self.direction}")
        print("Terrain state:")
        row_num = 0
        for y, row in enumerate(self.terrain):
            row_state = ""

            row_num=row_num+1
            for x, cell in enumerate(row):
                light_state = 'On' if cell['light'] else 'Off'
                row_state += f"({light_state}) "
            print(row_state,row_num)
        print("\n")

    def turn_right(self):
        """Turns the bot 90 degrees to the right."""
        directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_left(self):
        """Turns the bot 90 degrees to the left."""
        directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        self.direction = directions[(directions.index(self.direction) - 1) % 4]

    def move_forward(self):
        """Moves the bot forward in the direction it is currently facing."""
        if self.direction == 'UP' and self.bot_y > 0:
            self.bot_y -= 1
        elif self.direction == 'DOWN' and self.bot_y < self.height - 1:
            self.bot_y += 1
        elif self.direction == 'LEFT' and self.bot_x > 0:
            self.bot_x -= 1
        elif self.direction == 'RIGHT' and self.bot_x < self.width - 1:
            self.bot_x += 1

    def light_up(self):
        """Lights up the current square."""
        self.terrain[self.bot_y][self.bot_x]['light'] = True

    def execute_instructions(self, instructions):
        """Executes a series of instructions on the bot."""
        for instruction in instructions:
            if instruction == '^':
                self.move_forward()
            elif instruction == '>':
                self.turn_right()
            elif instruction == '<':
                self.turn_left()
            elif instruction == '@':
                self.light_up()

            # Print state after each instruction for debugging
            self.print_state()



kernel = LightBotKernel()
instructions = "^@^@>@^@<@^@"
kernel.execute_instructions(instructions)
#print(self.matrix)