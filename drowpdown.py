import pygame


class Dropdown:
    def __init__(self, x, y, w, h, font, options, title=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (50, 50, 50)
        self.font = font
        self.options = options
        self.active = False
        self.selected = None
        self.title = title
        self.locked = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        label = self.title if not self.selected else self.selected
        text = self.font.render(label, True, "white")
        surface.blit(text, (self.rect.x + 5, self.rect.y + 5))

        if self.active and not self.locked:
            for i, option in enumerate(self.options):
                opt_rect = pygame.Rect(
                    self.rect.x, self.rect.y + (i+1)*self.rect.height,
                    self.rect.width, self.rect.height
                )
                pygame.draw.rect(surface, (70, 70, 70),
                                 opt_rect, border_radius=5)
                opt_text = self.font.render(option, True, "white")
                surface.blit(opt_text, (opt_rect.x + 5, opt_rect.y + 5))

    def handle_event(self, event):
        if self.locked:
            return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            elif self.active:
                for i, option in enumerate(self.options):
                    opt_rect = pygame.Rect(
                        self.rect.x, self.rect.y + (i+1)*self.rect.height,
                        self.rect.width, self.rect.height
                    )
                    if opt_rect.collidepoint(event.pos):
                        self.selected = option
                        self.active = False
                        self.locked = True
                        return self.selected
                self.active = False
        return None
