from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*

janela = Window(720,400)
janela.set_title("Ping-Pong de dois")

controle = janela.get_keyboard()

#criação dos pads esquerdo e direito respectivamente
pad = Sprite("png/raquete.png",1)
pad.x = pad.width * 2
pad.y = janela.height / 2 - pad.height / 2

pad2 = Sprite("png/raquete.png",1)
pad2.x = janela.width - pad.width * 3
pad2.y = janela.height / 2 - pad2.height / 2

velP = 200

bola = Sprite("png/bola.png",1)
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

bX = 300
bY = 300

#pontuação de cada pad
esquerda = 0
direita = 0

while True:
        
        #bola com movimentos atualizados
        bola.x += bX * janela.delta_time()
        bola.y += bY * janela.delta_time()

        if (controle.key_pressed("w")):
                pad.y -= velP * janela.delta_time()
        elif (controle.key_pressed("s")):
                pad.y += velP * janela.delta_time()

        if (controle.key_pressed("up")):
                pad2.y -= velP * janela.delta_time()
        elif (controle.key_pressed("down")):
                pad2.y += velP * janela.delta_time()
                        
        #impedir que pads e bola saiam da tela
        if (pad.y <= 0):
                pad.y = 0
        if (pad.y + pad.height >= janela.height):
                pad.y = janela.height - pad.height
        if (pad2.y <= 0):
                pad2.y = 0
        if (pad2.y + pad2.height >= janela.height):
                pad2.y = janela.height - pad2.height

        if (bola.y <= 0):
                bola.y = 0
                bY *= (-1) 
        if (bola.y + bola.height >= janela.height):
                bola.y = janela.height - bola.height
                bY *= (-1)
		
        #define a pontuação do jogador 
        if (bola.x + bola.width >= janela.width):
                esquerda += 1
                bX *= -1
                bola.x = janela.width / 2 - bola.width / 2
                bola.y = janela.height / 2 - bola.height / 2
        if (bola.x <= 0):
                direita += 1
                bX *= -1
                bola.x = janela.width / 2 - bola.width / 2
                bola.y = janela.height / 2 - bola.height / 2

        #reação da bola ao entrar em contato com os pads // correção da bolinha passando por dentro do pad
        if (pad.collided(bola)):
                bX *= (-1)
                bola.x = pad.x + pad.width
        if (pad2.collided(bola)):
                bX *= (-1)
                bola.x = pad2.x - bola.width

        janela.set_background_color((219, 210, 81))

		#pontuação de cada pad
        janela.draw_text("{} esquerdo x {} direito".format(esquerda,direita), janela.width / 2 - 120, 30, 20, (94, 44, 14), "Arial", True, False)
	
        pad.draw()
        pad2.draw()
        bola.draw()

        janela.update()
