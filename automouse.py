import pyautogui as pag


def move_by_landmark(width_screen: int, height_screen: int, lm):
    """
    :param width_screen: Largura total da tela.
    :param height_screen: Altura total da tela.
    :param lm: Objeto de marcação contendo a posição x e y da marcação reastreada.
    :return: movimenta o mouse relativo ao tamanho da tela e a posição do objeto reastreado.
    """
    pos_int_lm_x = int(lm.x * width_screen)
    pos_int_lm_y = int(lm.y * height_screen)
    print("Objeto detectado!")
    print("Movendo o mouse para:")
    print(f"|x -> {pos_int_lm_x} \n|y -> {pos_int_lm_y}\n")
    pag.moveTo(pos_int_lm_x, pos_int_lm_y, 0.01)
