from random import randint


class Generator(object):
    data = []
    data_size = 32
    rooms = []
    
    def randomizer(self, low,high):
        return randint(low, high)
    
    def collision(self, room, ignore):
        for i in range(1, len(self.rooms)):
            if i == ignore:
                continue
            
            check = self.rooms[i]
            if not ((room['x'] + room['h'] < check['x']) or (room['x'] > check['x'] + check['w']) 
                    or (room['y'] + room['h'] < check['y'])
                    or (room['y'] > check['y'] + check['h'])):
                return True 
            return False
    
    def squash(self):
        for i in range(0,10):
            for j in range(0, len(self.rooms)):
                room = self.rooms[j]
                while True:
                    old_position = {
                        'x': room['x'],
                        'y': room['y']
                        }
                    if room['x'] > 1:
                        room['x'] -= 1
                    if room['y'] > 1:
                        room['y'] -= 1
                    if room['x'] == 1 and room['y'] == 1:
                        break
                    if self.collision(room, j):
                        room['x'] = old_position['x']
                        room['y'] = old_position['y']
                        break
    
    def find_closest(self, room):
        middle = {
            'x': room['x'] + (room['w']/2),
            'y': room['y'] + (room['h']/2),
            }
        closest = None
        closest_distance = 1000
        for i in range(0, len(self.rooms)):
            check = self.rooms[i]
            check_mid = {
                'x': check['x'] + (check['w']/2),
                'y': check['y'] + (check['h']/2),
                }
            if check == room:
                continue
            distance = min(abs(middle['x'] - check_mid['x']) - (room['w']/2) - (check['w']/2), 
                           abs(middle['y'] - check_mid['y']) - (room['h']/2) -(check['h']/2))
            if distance < closest_distance:
                closest_distance = distance
                closest = check
        return closest 
        
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
        
        for k in range (0, room_count):
            room = {}
            room['x'] = self.randomizer(1, (self.data_size-max_size-1))
            room['y'] = self.randomizer(1, (self.data_size-max_size-1))        
            room['w'] = self.randomizer(min_size, max_size)
            room['h'] = self.randomizer(min_size, max_size)
            
            if self.collision(room,k):
                k -= 1
                continue
            
            room['w'] -= 1
            room['h'] -= 1
            self.rooms.append(room)  
        self.squash()
        
#         list index out of range
        for l in range(0, room_count):
            roomA = self.rooms[l]
            roomB = self.find_closest(roomA)
            
            
            pointA = {
                'x': self.randomizer(roomA['x'], roomA['x'] + roomA['w']),
                'y': self.randomizer(roomA['y'], roomA['y'] + roomA['h'])}
            pointB = {
                'x': self.randomizer(roomB['x'], roomB['x'] + roomB['w']),
                'y': self.randomizer(roomB['y'], roomB['y'] + roomB['h'])
                }
            
            while pointB['x'] != pointA['x'] or pointB['y'] != pointA['y']:
                if pointB['x'] != pointA['x']:
                    if pointB['x'] > pointA['x']:
                        pointB['x'] -= 1
                    else:
                        pointB['x'] += 1
                elif pointB['y'] != pointA['y']:
                    if pointB['y'] > pointA['y']:
                        pointB['y'] -= 1
                    else:
                        pointB['y'] += 1
                self.data[pointB['x']][pointB['y']] = 1
        
        for m in range(0,room_count):
            room = self.rooms[m]
            for x in range (room['x'], room['x'] + room['w']):
                for y in range (room['y'], room['y'] + room['h']):
                    self.data[x][y] = 1
        
        for X in range (0, self.data_size):
            for Y in range (0, self.data_size):
                if self.data[X][Y] == 1:
                    for xWall in range(X-1, X+1):
                        for yWall in range(Y-1, Y+1):
                            if self.data[xWall][yWall] == None:
                                self.data[xWall][yWall] = 2
        
        return self.data
    


def main():
    g = Generator().room_gen()
    print(g)

if __name__ == "__main__":
    main()


 
        