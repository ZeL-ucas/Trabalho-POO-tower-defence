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
def load_animation(sprite_sheet:pygame.Surface, frames:int) -> list:
    """
    Carrega as imagens de animação a partir de um spritesheet.
    
    :param sprite_sheet: A superfície do spritesheet.
    :param frames: O número de frames na animação.
    :return: Uma lista de superfícies de cada frame.
    """
    height = sprite_sheet.get_height()
    width = sprite_sheet.get_width()
    frame_width = width // frames
    animation_list = []
    for x in range(frames):
        temp_img = sprite_sheet.subsurface(pygame.Rect(x * frame_width, 0, frame_width, height))
        animation_list.append(temp_img)
    return animation_list

def play_animation(animation_list: list, frame_index: int, angle: float, position: pygame.math.Vector2, update_time: int, animation_speed: int) -> tuple[pygame.Surface, int, int]:
    """
    Atualiza a animação e retorna a imagem atual da animação.
    
    :param update_time: Tempo da última atualização da animação.
    :param animation_speed: Velocidade da animação em milissegundos.
    :return: Imagem atual da animação, novo índice do frame, novo tempo de atualização.
    """
    current_time = pygame.time.get_ticks()
    if current_time - update_time > animation_speed:
        frame_index = (frame_index + 1) % len(animation_list)
        update_time = current_time
    image = pygame.transform.rotate(animation_list[frame_index], angle)
    rect = image.get_rect()
    rect.center = position
    return image, frame_index, update_time