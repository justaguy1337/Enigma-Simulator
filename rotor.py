import pygame


class Rotor:

    def __init__(self, wiring, turn):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.turn = turn

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def show(self):
        print(self.left)
        print(self.right)
        print("")

    def rotate(self, n=1, forward=True):
        for _ in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, n):
        # rotate the rotor backwards
        self.rotate(n-1, forward=False)
        # adjust the turnover turn in relationship to the wiring
        n_turn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.turn)
        self.turn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_turn-n) % 26]

    def draw(self, screen, x, y, w, h, font):

        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        # letters
        for i in range(26):

            # left hand side
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w/4, y+(i+1)*h/27))

            # highlight top letter
            if i == 0:
                pygame.draw.rect(screen, "teal", text_box, border_radius=10)

            # highlgiht turnover
            if self.left[i] == self.turn:
                letter = font.render(self.turn, True, "#161616")
                pygame.draw.rect(screen, "white", text_box, border_radius=10)

            screen.blit(letter, text_box)

            # right hand side
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)
