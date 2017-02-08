from random import randint


class Generator(object):
    data = []
    data_size = 128
    rooms = []
    
    def randomizer(self, low,high):
        return randint(low, high)
    
    def collision(self, room, ignore):
        for i in range(1, self.rooms.length()):
            if i == ignore:
                continue
            
            check = self.rooms[i]
            if not ((room.x + room.h < check.x) or (room.x > check.x + check.w) or (room.y + room.h < check.y)
                    or (room.y > check.y + check.h)):
                return True 
            return False
    
    def squash(self):
        pass
    
    def find_closest(self):
        pass
    
    def room_gen(self):
        
        self.data = []
        for i in range (0, self.data_size):
            self.data.append([])
            for j in range (0, self.data_size):
                self.data[i].append(None)
                j += 1
            i += 1
        
        room_count = self.randomizer(10, 20)
        min_size = 5
        max_size = 15
        
        for i in range (0, room_count):
            room = {}
            room.x = self.randomizer(1, (self.data_size-max_size-1))
            room.y = self.randomizer(1, (self.data_size-max_size-1))        
            room.w = self.randomizer(min_size, max_size)
            room.h = self.randomizer(min_size, max_size)
            i += 1
        
        return self.data
    


g = Generator()
print(g.room_gen())



 
        