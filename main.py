import pygame

from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw
from forbiddenKey import all_keys_filtered

# setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# create fonts
MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# global variables
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGIN = {'top': 200, 'bottom': 100, 'left': 100, 'right': 100}
GAP = 150

INPUT = ""
OUTPUT = ""
PATH = []

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard
KB = Keyboard()
PB = Plugboard(["PB", "JL", "MN", "OU"])

AVAILABLE_ROTORS = {"I": I, "II": II, "III": III, "IV": IV, "V": V}
AVAILABLE_REFLECTORS = {"A": A, "B": B, "C": C}

# defaults
selected_reflector = "B"
selected_rotors = ["I", "II", "III"]
ROT1 = AVAILABLE_ROTORS[selected_rotors[0]]
ROT2 = AVAILABLE_ROTORS[selected_rotors[1]]
ROT3 = AVAILABLE_ROTORS[selected_rotors[2]]
REFL = AVAILABLE_REFLECTORS[selected_reflector]

ENIGMA = Enigma(REFL, ROT1, ROT2, ROT3, PB, KB)
ENIGMA.set_rings((0, 0, 0))
ENIGMA.set_key("AAA")

# dropdown variables
dropdown_open = [False, False, False, False]
rotor_options = list(AVAILABLE_ROTORS.keys())
reflector_options = list(AVAILABLE_REFLECTORS.keys())
font = pygame.font.SysFont("Arial", 20)
rotors_locked = False


def draw_dropdowns(screen):
    # dropdown variables position
    dropdown_width, dropdown_height = 100, 30
    spacing = 120
    tab = 100
    start_x, start_y = tab, HEIGHT-80

    # reflector dropdown
    rect = pygame.Rect(start_x, start_y, dropdown_width, dropdown_height)
    pygame.draw.rect(screen, (50, 50, 50), rect)
    pygame.draw.rect(screen, (200, 200, 200), rect, 2)
    text = font.render(selected_reflector, True, (255, 255, 255))
    screen.blit(text, (rect.x+5, rect.y+5))

    if dropdown_open[0]:
        for j, option in enumerate(reflector_options):
            oy = rect.y-(j+1) * dropdown_height
            opt_rect = pygame.Rect(rect.x, oy, dropdown_width, dropdown_height)
            pygame.draw.rect(screen, (70, 70, 70), opt_rect)
            pygame.draw.rect(screen, (200, 200, 200), opt_rect, 1)
            opt_text = font.render(option, True, (255, 255, 255))
            screen.blit(opt_text, (opt_rect.x+5, opt_rect.y+5))

    rotor_start_x = start_x + dropdown_width + 2*tab-40
    for i in range(3):
        rect = pygame.Rect(rotor_start_x + i*spacing,
                           start_y, dropdown_width, dropdown_height)
        pygame.draw.rect(screen, (50, 50, 50), rect)
        pygame.draw.rect(screen, (200, 200, 200), rect, 2)

        text = font.render(selected_rotors[i], True, (255, 255, 255))
        screen.blit(text, (rect.x+5, rect.y+5))

        if dropdown_open[i+1]:
            filtered_options = [
                o for o in rotor_options if o not in selected_rotors or o == selected_rotors[i]]
            for j, option in enumerate(filtered_options):
                oy = rect.y - (j+1) * dropdown_height
                opt_rect = pygame.Rect(
                    rect.x, oy, dropdown_width, dropdown_height)
                pygame.draw.rect(screen, (70, 70, 70), opt_rect)
                pygame.draw.rect(screen, (200, 200, 200), opt_rect, 1)
                opt_text = font.render(option, True, (255, 255, 255))
                screen.blit(opt_text, (opt_rect.x+5, opt_rect.y+5))


def handle_dropdown_click(pos):
    global ROT1, ROT2, ROT3, REFL, ENIGMA, selected_reflector

    dropdown_width, dropdown_height = 100, 30
    spacing = 120
    tab = 100
    start_x, start_y = tab, HEIGHT-80

    # reflector dropdown
    rect = pygame.Rect(start_x, start_y, dropdown_width, dropdown_height)
    if rect.collidepoint(pos):
        dropdown_open[0] = not dropdown_open[0]
        return
    if dropdown_open[0]:
        for j, option in enumerate(reflector_options):
            oy = rect.y-(j+1) * dropdown_height
            opt_rect = pygame.Rect(rect.x, oy, dropdown_width, dropdown_height)
            if opt_rect.collidepoint(pos):
                selected_reflector = option
                REFL = AVAILABLE_REFLECTORS[selected_reflector]
                ENIGMA = Enigma(REFL, ROT1, ROT2, ROT3, PB, KB)
                ENIGMA.set_rings((0, 0, 0))
                ENIGMA.set_key("AAA")
                dropdown_open[0] = False
                return
        dropdown_open[0] = False

    # rotor dropdowns
    rotor_start_x = start_x+250
    for i in range(3):
        rect = pygame.Rect(rotor_start_x + i*spacing,
                           start_y, dropdown_width, dropdown_height)
        if rect.collidepoint(pos):
            dropdown_open[i+1] = not dropdown_open[i+1]
            return
        if dropdown_open[i+1]:
            filtered_options = [
                o for o in rotor_options if o not in selected_rotors or o == selected_rotors[i]]
            for j, option in enumerate(filtered_options):
                oy = rect.y - (j+1)*dropdown_height
                opt_rect = pygame.Rect(
                    rect.x, oy, dropdown_width, dropdown_height)
                if opt_rect.collidepoint(pos):
                    selected_rotors[i] = option
                    ROT1 = AVAILABLE_ROTORS[selected_rotors[0]]
                    ROT2 = AVAILABLE_ROTORS[selected_rotors[1]]
                    ROT3 = AVAILABLE_ROTORS[selected_rotors[2]]
                    ENIGMA = Enigma(REFL, ROT1, ROT2, ROT3, PB, KB)
                    ENIGMA.set_rings((0, 0, 0))
                    ENIGMA.set_key("AAA")
                    dropdown_open[i+1] = False
                    return
            dropdown_open[i + 1] = False


animating = True
while animating:
    SCREEN.fill("#161616")

    # text input
    text = BOLD.render(INPUT, True, "white")
    SCREEN.blit(text, text.get_rect(center=(WIDTH/2, MARGIN['top']/3)))

    # text output
    text = MONO.render(OUTPUT, True, "white")
    SCREEN.blit(text, text.get_rect(center=(WIDTH/2, MARGIN['top']/3+25)))

    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGIN, GAP, BOLD)

    draw_dropdowns(SCREEN)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not rotors_locked:
            handle_dropdown_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if rotors_locked:
                    continue
                ROT2.rotate()
            elif event.key == pygame.K_LEFT:
                if rotors_locked:
                    continue
                ROT1.rotate()
            elif event.key == pygame.K_RIGHT:
                if rotors_locked:
                    continue
                ROT3.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "
                rotors_locked = True
            elif event.key in all_keys_filtered:
                continue
            else:
                key = event.unicode
                letter = key.upper()
                INPUT += letter
                cipher, PATH = ENIGMA.encipher(letter)
                OUTPUT += cipher
                rotors_locked = True