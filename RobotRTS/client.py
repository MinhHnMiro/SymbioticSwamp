import pygame, time, keyboard, socket

pygame.init()
wn = pygame.display.set_mode((800, 800))
pygame.display.set_caption('RobotRTS')
clock = pygame.time.Clock()

HEADER = 64
PORT = 32383
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '29.ip.gl.ply.gg'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

class Sprite:
    def __init__(self, x, y, shape, color, name='Dummy', size=[1, 1, None], heading=90, team='s', give_energy=50): # team: s=self, f=friendly, e=enemy, n=neatral
        self.x = x
        self.y = y
        self.heading = heading
        self.shape = shape
        self.color = color
        self.size = size
        self.name = name
        self.energy = 100
        self.team = team
        self.surface = pygame.Surface(self.size)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(HEADER).decode(FORMAT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(send(DISCONNECT_MESSAGE))
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
