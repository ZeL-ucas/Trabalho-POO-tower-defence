import pygame

def load_sprite_sheet(image_path:str, rows:int, cols:int)->list:
    sprite_sheet = pygame.image.load(image_path).convert_alpha()
    sheet_rect = sprite_sheet.get_rect()
    sprite_width = sheet_rect.width // cols
    sprite_height = sheet_rect.height // rows
    sprites = []

    for row in range(rows):
        row_sprites = []
        for col in range(cols):
            rect = pygame.Rect(col * sprite_width, row * sprite_height, sprite_width, sprite_height)
            image = sprite_sheet.subsurface(rect)
            row_sprites.append(image)
        sprites.append(row_sprites)

    return sprites
