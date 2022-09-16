from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*

janela = Window(600,600)
janela.set_title("Bolinha n°2")
janela.set_background_color((210,210,210))

bola = Sprite("png/bola.png",1)

bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

#valores que representam de quantos em quantos "velocidades" o objeto se locomove
velX = 200
velY = 500

while True:
	
	#convertendo a velocidade no tempo do jogo (não me pergunte pq)
	bola.x += velX * janela.delta_time()
	bola.y += velY * janela.delta_time()
	
	#impedindo a bola sair da tela // resolvendo o bug da bola sair escoregando na parede
	if (bola.x <= 0):
		bola.x = 0
		velX *= (-1) 
	if (bola.x + bola.width >= janela.width):
		bola.x = janela.width - bola.width
		velX *= (-1)
	if (bola.y <= 0):
		bola.y = 0
		velY *= (-1) 
	if (bola.y + bola.height >= janela.height):
		bola.y = janela.height - bola.height
		velY *= (-1)
	
	janela.set_background_color((210,210,210))

	bola.draw()
	janela.update()

