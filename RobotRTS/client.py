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

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(HEADER).decode(FORMAT)

lentities = {}

surface = pygame.Surface((200, 200))

text = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            send(DISCONNECT_MESSAGE)
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                text += 'w'
            if event.key == pygame.K_a:
                text += 'a'
            if event.key == pygame.K_s:
                text += 's'
            if event.key == pygame.K_d:
                text += 'd'
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                text.remove('w')
            if event.key == pygame.K_a:
                text.remove('a')
            if event.key == pygame.K_s:
                text.remove('s')
            if event.key == pygame.K_d:
                text.remove('d')

    print(text)
    entities = send(''.join(text))
    entit = entities.split('\t')
    enti = []
    # Fix client handling Server info with multiple Objects
    '''for e in entit:
        enti.append(e.split(','))
        ent = enti[0].split('.')
        en = []
        for e in ent:
            en.append(int(e))
        en = tuple(en)
        
        surface.fill(enti[1])
        wn.blit(surface, en)
'''
    pygame.display.update()
    clock.tick(60)

    wn.fill('black')
