#coding=UTF-8

'''
Joguinho:
Lucas S. Avila
Gabriela Suita
'''
from graphics import *
import random
import time


# Janela de configuração da resolução do jogo
winresolu = GraphWin("Configuração", 500, 500)
presolucao = Text(Point(250, 150), "Digite a resolução desejada:")
presolucao.draw(winresolu)
textox = Text(Point(250, 250), "x")
textox.draw(winresolu)
entrada1 = Entry(Point(150, 250), 10)
entrada2 = Entry(Point(350, 250), 10)
entrada1.draw(winresolu)
entrada2.draw(winresolu)
pontob1 = Point(225, 400)
pontob2 = Point(275, 425)
botaop1 = Rectangle(pontob1, pontob2)
botaop1.draw(winresolu)
botaop2 = Text(botaop1.getCenter(), "Ok!")
botaop2.draw(winresolu)
click = winresolu.getMouse()
while(click.getX() < pontob1.getX() or click.getX() > pontob2.getX() or click.getY() < pontob1.getY() or click.getY() > pontob2.getY()):
	click = winresolu.getMouse()
winresolu.close()

resolu1 = eval(entrada1.getText())
resolu2 = eval(entrada2.getText())

# Arquivo de instruções
objinstrucoes = open("instr.txt", 'r')
instrucoes = objinstrucoes.read()
objinstrucoes.close()

# Janela principal
wingame = GraphWin("Joguinho", resolu1, resolu2)
textoinstru = Text(Point(resolu1/2, resolu2/2), instrucoes)
textoinstru.draw(wingame)
pontob1 = Point(resolu1/2 - 50, resolu2 - 105)
pontob2 = Point(resolu1/2 + 50, resolu2 - 80)
botaop1 = Rectangle(pontob1, pontob2)
botaop1.draw(wingame)
botaop2 = Text(botaop1.getCenter(), "Começar!")
botaop2.draw(wingame)
click = wingame.getMouse()
while(click.getX() < pontob1.getX() or click.getX() > pontob2.getX() or click.getY() < pontob1.getY() or click.getY() > pontob2.getY()):
	click = wingame.getMouse()
textoinstru.undraw()
botaop1.undraw()
botaop2.undraw()

#Waves
nivel = 1
while(nivel <= 20 and nivel != -1):
	#Contador 
	cont = 3
	contador = Text(Point(resolu1/2, resolu2/2), str(cont))
	contador.setSize(36)
	contador.draw(wingame)
	if(nivel == 1):
		texto = "O jogo começa em: "
	else:
		texto = "O nivel " + str(nivel) + " começa em: "
	textoqualquer = Text(Point(resolu1/4, resolu2/2), texto)
	textoqualquer.setSize(36)
	textoqualquer.draw(wingame)
	while(cont > 0):
		time.sleep(1)
		cont = cont - 1
		contador.setText(str(cont))
	contador.undraw()
	textoqualquer.undraw()
	if(nivel % 5 == 0):
		#Wave com chefe
		print "oi"
		nivel += 1
	else:
		#Wave sem chefe
		tempo = 0
		ncorruptos = random.randint(1+nivel/4, 4+nivel/4)
		n_inimigos = ncorruptos
		corruptos = []
		vidacorruptos = []
		#desenhando os inimigos
		cont = 0
		click = wingame.checkMouse()
		while(cont < ncorruptos):
			pontoa = Point(random.randint(0, resolu1-200), random.randint(0, resolu2-200))
			pontob = Point(pontoa.getX()+200, pontoa.getY()+200)
			corruptos.append(Rectangle(pontoa, pontob))
			corruptos[cont].draw(wingame)
			vidacorruptos.append(random.randint(1+nivel/4, 3+nivel/4))
			cont += 1
		#começo da wave
		while(tempo < 9.0 - nivel/4 and n_inimigos != 0):
			click = wingame.checkMouse()
			cont = 0
			while(cont < ncorruptos and cont != -1):
				if(click != None):	
					pontoa = corruptos[cont].getP1()
					pontob = corruptos[cont].getP2()
					if(click.getX() >= pontoa.getX() and click.getX() <= pontob.getX() and click.getY() >= pontoa.getY() and click.getY() <= pontob.getY()):
						if(vidacorruptos[cont] != 0):
							vidacorruptos[cont] += -1
							if(vidacorruptos[cont] == 0):
								corruptos[cont].undraw()
								n_inimigos += -1
							cont = -1
						else:
							cont += 1
					else:
						cont += 1
				else:
					cont = -1
			time.sleep(0.01)
			tempo += 0.01
		if(n_inimigos != 0):
			nivel = -1
		else:
			nivel += 1

if(nivel >= 20):
	print("ganhou")
	
else:
	print("perdeu")


'''
	- PNG com a caras dos inimigos;
	- Fazer lista de objetos GraphWin, reutilizar;
	- inimigos por wave min: 3, max: 9;
	- Tempos dos corruptos max: 8s, min: 3s;
	- Chefes no levels 5, 10, 15, 20. 20 é o "primeiramente";
	- Janelas tem vidas que dimínuem com o número de clicks;
	- Janela com o tempo(Retangulo que diminui conforme o tempo que passa);
	- Tempo com contadores;
	- O lugar onde as janelas aparecem deve ser aleatório também!!
	- Arrumar as janelas auxiliares;
	- Arrumar o cursor;
	- Pegar fotos de x políticos;
	- Transformar as fotos em ppm ou gif; 
	- Recortar os rostos;
	- Diminuir as resoluções;
'''
