    onboard = True
    if red.xc >= track.get_width():
        onboard = False
    if red.xc < 0:
        onboard = False
    if red.yc >= track.get_height():
        onboard = False
    if red.yc < 0:
        onboard = False

    if onboard:
        clr = track.get_at((red.xc, red.yc))  # машина на треке
    else:
        clr = trk  # машина за пределами трека

    ###################################################################
    # выехали за пределы трека
    ###################################################################
    keys = pygame.key.get_pressed()

    if clr == trk:
        red.speed -= 0.3
        if red.speed < 2:
            red.speed = 2
    elif clr == barer or clr == barer1:
        if red.speed < 5:
            pass
        else:
            red.speed -= 0.1
    elif clr == stena:
        red.speed = 0

    if keys[K_LEFT]:
        red.view = (red.view + 2) % 360
    elif keys[K_RIGHT]:
        red.view = (red.view + 358) % 360
    if keys[K_UP]:
        red.speed += 0.05
        if red.speed > 99:
            red.speed = 99
    elif keys[K_DOWN]:
        red.speed -= 0.05
        if red.speed < 0:
            red.speed = 0

    f1.write(str(red.xc) + ' ' + str(red.yc) + ' ' + str(red.view) + ' ' + str(red.speed) + '\n')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k += 1

f1.close()

    Up = 0
    Right = 0
    Down = 0
    Left = 0

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        Up = 1
    if keys[K_RIGHT]:
        Right = 1
    if keys[K_LEFT]:
        Left = 1
    if keys[K_DOWN]:
        Down = 1

    if Up and speed < maxSpeed:
        if speed < 0:
            speed += dec
        else:
            speed += acc

    if Down and speed > -maxSpeed:
        if speed > 0:
            speed -= dec
        else:
            speed -= acc

    if not Up and not Down:
        if speed - dec > 0:
            speed -= dec
        else:
            if speed + dec < 0:
                speed += dec
            else:
                speed = 0

    if Right and speed != 0:
        angle -= turnSpeed * speed / maxSpeed

    if Left and speed != 0:
        angle += turnSpeed * speed / maxSpeed

    car[0].speed = speed
    car[0].angle = angle

    [400, 730],
    [500, 834],
    [585, 743],
    [590, 318],
    [665, 240],
    [1325, 243],
    [1366, 311],
    [1377, 479],
    [1294, 552],
    [878, 565],
    [785, 644],
    [872, 738],
    [1292, 745],
    [1362, 814],
    [1371, 1283],
    [1266, 1372],
    [1136, 1271],
    [1126, 1040],
    [979, 948],
    [816, 1014],
    [795, 1292],
    [725, 1392],
    [617, 1334],
    [215, 930],
    [205, 641]