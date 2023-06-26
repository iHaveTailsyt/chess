import os 
import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, filename, cols, rows):
        pygame.sprite.Sprite.__init__(self)
        self.pieces = {
            "white pawn": 5,
            "white knight": 3,
            "white bishop": 2,
            "white rook": 4,
            "white king": 0,
            "white queen": 1,
            "black pawn": 11,
            "black knight": 9,
            "black bishop": 8,
            "black rook": 10,
            "black king": 6,
            "black queen": 7
        }
        self.spritesheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.cell_count = cols * rows

        self.rect = self.spritesheet.get_rect()
        w = self.cell_width = self.rect.width // self.cols
        h = self.cell_height = self.rect.height // self.rows

        self.cells = list([(i % cols * w, i // cols * h, w, h) for i in range(self.cell_count)])

    def draw(self, surface, piece_name, coords):
        piece_index = self.pieces[piece_name]
        surface.blit(self.spritesheet, coords, self.cells[piece_index])