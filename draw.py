import pygame


def draw(enigma, path, screen, width, height, margin, gap, font):

    # width and height component
    w = (width - margin['left'] - margin['right'] - 5*gap)/6
    h = height-margin['top'] - margin['bottom']

    #  path coordinates
    y = [margin['top']+(signal+1)*h/27 for signal in path]
    x = [width-margin['right']-w/2]  # keybaord

    for i in [4, 3, 2, 1, 0]:  # forward pass
        x.append(margin['left']+i*(w+gap)+w*3/4)
        x.append(margin['left']+i*(w+gap)+w*1/4)
    x.append(margin['left']+w*3/4)  # reflector

    for i in [1, 2, 3, 4]:  # backward pass
        x.append(margin['left']+i*(w+gap)+w*1/4)
        x.append(margin['left']+i*(w+gap)+w*3/4)
    x.append(width-margin['right']-w/2)  # lamboard

    # draw path
    if len(path) > 0:
        for i in range(1, 21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"

            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # base oordinates
    x = margin['left']
    y = margin['top']

    # enigma components
    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w+gap

    # add names
    names = ['Reflector', 'Left', 'Middle', 'Right', 'Plugboard', 'Keyboard']
    y = margin['top']*0.8
    for i in range(6):
        x = margin['left'] + w/2 + i*(w+gap)
        title = font.render(names[i], True, 'white')
        text_box = title.get_rect(center=(x, y))
        screen.blit(title, text_box)
