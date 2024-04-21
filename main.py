import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
WHITE = (222, 175, 132)
BLACK = (113, 68, 35)
FONT_SIZE = 36

# Load chess piece images
piece_images = {
    "wP": pygame.image.load("white_pawn.png"),
    "wR": pygame.image.load("white_rook.png"),
    "wN": pygame.image.load("white_knight.png"),
    "wB": pygame.image.load("white_bishop.png"),
    "wQ": pygame.image.load("white_queen.png"),
    "wK": pygame.image.load("white_king.png"),
    "bP": pygame.image.load("black_pawn.png"),
    "bR": pygame.image.load("black_rook.png"),
    "bN": pygame.image.load("black_knight.png"),
    "bB": pygame.image.load("black_bishop.png"),
    "bQ": pygame.image.load("black_queen.png"),
    "bK": pygame.image.load("black_king.png"),
}

# Create the chess board
chess_board = [
    "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
    "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP",
    "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"
]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# Function to draw the chess board
def draw_board():
    for row in range(8):
        for col in range(8):
            square_color = BLACK if (row + col) % 2 == 1 else WHITE
            pygame.draw.rect(screen, square_color, (col * WIDTH/8, row * HEIGHT/8, WIDTH/8, HEIGHT/8))

# Function to draw the pieces on the chess board
def draw_pieces():
    for i, piece in enumerate(chess_board):
        if piece:
            row, col = divmod(i, 8)
            image = piece_images[piece]
            image = pygame.transform.scale(image, (WIDTH // 8, HEIGHT // 8))
            screen.blit(image, (col * WIDTH/8, row * HEIGHT/8))

# Main game loop
selected_piece = None
selected_piece_position = None
dragging = False
offset_x = 0
offset_y = 0

def get_possible_moves():
    pass

def make_move():
    pass

def undo_move():
    pass


def eval():
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                x, y = pygame.mouse.get_pos()
                row, col = y // (HEIGHT // 8), x // (WIDTH // 8)
                piece_index = row * 8 + col
                if 0 <= piece_index < 64:
                    piece = chess_board[piece_index]
                    if piece:
                        selected_piece = piece
                        selected_piece_position = (row, col)
                        dragging = True
                        offset_x = col * (WIDTH // 8) - x
                        offset_y = row * (HEIGHT // 8) - y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and dragging:
                dragging = False
                x, y = pygame.mouse.get_pos()
                row, col = y // (HEIGHT // 8), x // (WIDTH // 8)
                target_index = row * 8 + col
                if (0 <= target_index < 64) and (selected_piece_position != (row, col)):
                    chess_board[selected_piece_position[0] * 8 + selected_piece_position[1]] = ""
                    chess_board[target_index] = selected_piece
                selected_piece = None
                selected_piece_position = None

    screen.fill(WHITE)
    draw_board()
    draw_pieces()

    if dragging and selected_piece:
        x, y = pygame.mouse.get_pos()
        image = piece_images[selected_piece]
        image = pygame.transform.scale(image, (WIDTH // 8, HEIGHT // 8))
        screen.blit(image, (x + offset_x, y + offset_y))

    pygame.display.flip()
