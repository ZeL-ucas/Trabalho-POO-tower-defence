import pygame

def loadAnimation(sprite_sheet:pygame.Surface, frames:int) -> list:
    """
    Carrega as imagens de animação a partir de um spritesheet.
    """
    height = sprite_sheet.get_height()
    width = sprite_sheet.get_width()
    frame_width = width // frames
    animation_list = []
    for x in range(frames):
        temp_img = sprite_sheet.subsurface(pygame.Rect(x * frame_width, 0, frame_width, height))
        animation_list.append(temp_img)
    return animation_list

def playAnimation(animation_list: list, frame_index: int, angle: float, position: pygame.math.Vector2, update_time: int, animation_speed: int) -> tuple[pygame.Surface, int, int]:
    """
    Atualiza a animação e retorna a imagem atual da animação.
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