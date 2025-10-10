import pygame

pygame.init()
window=pygame.display.set_mode(size=(600,480)) #cria a janela do jogo


while True: #precisa de um loop pra janela se manter aberta
   for event in pygame.event.get():    #retorna todos os eventos
       if event.type ==pygame.QUIT:    #evento de fechar janela
           pygame.quit() #fecha a janela
           quit()