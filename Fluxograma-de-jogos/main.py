def celular():
  print("Legal adoro jogos de celular também")
  print("Agora vamos escolher um tipo de jogo que você mais gosta. Temos jogos de: ")
  print("1 - Score")
  print("2 - Tiro")
  print("3 - Tabuleiro")
  print("Digite o número: ", end="")
  tipo = int(input());
  if(tipo==1):
    score()
  elif(tipo==2):
    tiro()
  elif(tipo==3):
    tabuleiro()
  else:
    print("Ops, opção inválida")

def score():
  print("Eu amo jogos de score também")
  print("Voce gostaria de qual tipo de score:")
  print("1 - Com passaros")
  print("2 - Com galinhas")
  print("Digite o número: ", end="")
  score_op = int(input());
  if(score_op==1):
    print("Escolhemos o jogo perfeito para você: Flappy Bird")
  elif(score_op==2):
    print("Escolhemos o jogo perfeito para você: Crossy Road")
  else:
    print("Ops, opção inválida")

def tiro():
  print("Eu amo jogos de tiro também")
  print("Voce gostaria de qual tipo de tiro:")
  print("1 - Terceira pessoa")
  print("2 - Primeira pessoa")
  print("Digite o número: ", end="")
  tiro_op = int(input());
  if(tiro_op==1):
    print("Escolhemos o jogo perfeito para você: FF")
  elif(tiro_op==2):
    print("Escolhemos o jogo perfeito para você: COD Mobile")
  else:
    print("Ops, opção inválida")

def tabuleiro():
  print("Eu amo jogos de tabuleiro também")
  print("Voce gostaria de qual tipo de tabuliro:")
  print("1 - Dificil")
  print("2 - Facil")
  print("Digite o número: ", end="")
  tabuleiro_op = int(input());
  if(tabuleiro_op==1):
    print("Escolhemos o jogo perfeito para você: Xadrez")
  elif(tabuleiro_op==2):
    print("Escolhemos o jogo perfeito para você: Dama")
  else:
    print("Ops, opção inválida")

def PC():
  print("Legal adoro jogos de PC também")
  print("Agora vamos escolher um tipo de jogo que você mais gosta. Temos jogos de: ")
  print("1 - Fantasia")
  print("2 - Diversão em grupo")
  print("3 - Tiro")
  print("Digite o número: ", end="")
  tipo = int(input());
  if(tipo==1):
    fantasia()
  elif(tipo==2):
    diversao()
  elif(tipo==3):
    tiro()
  else:
    print("Ops, opção inválida")

def fantasia():
  print("Eu amo jogos de fantasia também")
  print("Voce gostaria de qual tipo de fantasia:")
  print("1 - Partidas")
  print("2 - História")
  print("Digite o número: ", end="")
  fantasia_op = int(input());
  if(fantasia_op==1):
    print("Escolhemos o jogo perfeito para você: LOL")
  elif(fantasia_op==2):
    print("Escolhemos o jogo perfeito para você: WOW")
  else:
    print("Ops, opção inválida")

def diversao():
  print("Eu amo jogos de diversao também")
  print("Voce gostaria de qual tipo de diversão:")
  print("1 - Inteligncia")
  print("2 - Mecanica")
  print("Digite o número: ", end="")
  diversao_op = int(input());
  if(diversao_op==1):
    print("Escolhemos o jogo perfeito para você: Among Us")
  elif(diversao_op==2):
    print("Escolhemos o jogo perfeito para você: Fall Guys")
  else:
    print("Ops, opção inválida")

def tiro():
  print("Eu amo jogos de tiro também")
  print("Voce gostaria de qual tipo de tiro:")
  print("1 - Aberto")
  print("2 - Turno")
  print("Digite o número: ", end="")
  tiro_op = int(input());
  if(tiro_op==1):
    print("Voce prefere jogos realistas?")
    print("1 - Sim")
    print("2 - Não")
    print("Digite o número: ", end="")
    tiro_op2 = int(input());
    if(tiro_op2==1):
      print("Escolhemos o jogo perfeito para você: PUBG")
    elif(tiro_op2==2):
      print("Escolhemos o jogo perfeito para você: Fortinite")
    else:
      print("Ops, opção inválida")
  elif(tiro_op==2):
    print("Voce prefere jogos realistas?")
    print("1 - Sim")
    print("2 - Não")
    print("Digite o número: ", end="")
    tiro_op2 = int(input());
    if(tiro_op2==1):
      print("Escolhemos o jogo perfeito para você: CSGO")
    elif(tiro_op2==2):
      print("Escolhemos o jogo perfeito para você: Valorant")
    else:
      print("Ops, opção inválida")






def console():
  print("Legal adoro jogos de console também")
  print("Agora vamos escolher um tipo de jogo que você mais gosta. Temos jogos de: ")
  print("1 - Esportes")
  print("2 - Luta")
  print("3 - FPS")
  print("Digite o número: ", end="")
  tipo = int(input());
  if(tipo==1):
    esportes()
  elif(tipo==2):
    luta()
  elif(tipo==3):
    fps()
  else:
    print("Ops, opção inválida")

def esportes():
  print("Eu amo jogos de esportes também")
  print("Voce gostaria de qual tipo de esporte:")
  print("1 - Futebol")
  print("2 - Basquete")
  print("Digite o número: ", end="")
  esportes_op = int(input());
  if(esportes_op==1):
    print("Escolhemos o jogo perfeito para você: FIFA")
  elif(esportes_op==2):
    print("Escolhemos o jogo perfeito para você: NBA")
  else:
    print("Ops, opção inválida")

def luta():
  print("Eu amo jogos de luta também")
  print("Voce gostaria de qual tipo de luta:")
  print("1 - Realista")
  print("2 - Não tão realista")
  print("Digite o número: ", end="")
  luta_op = int(input());
  if(luta_op==1):
    print("Escolhemos o jogo perfeito para você: MK")
  elif(luta_op==2):
    print("Escolhemos o jogo perfeito para você: Street Fighter")
  else:
    print("Ops, opção inválida")

def fps():
  print("Eu amo jogos de fps também")
  print("Voce gostaria de qual tipo de fps:")
  print("1 - Realista")
  print("2 - Com poderes")
  print("Digite o número: ", end="")
  fps_op = int(input());
  if(fps_op==1):
    print("Escolhemos o jogo perfeito para você: COD")
  elif(fps_op==2):
    print("Escolhemos o jogo perfeito para você: Paladins")
  else:
    print("Ops, opção inválida")



print("Olá seja bem vindo ao decididor de jogos, de acordo com suas respostas vamos escolher um jogo legal para você se divertir :)")
print("A primeira coisa que preciso saber é se você prefere jogos de:")
print("1 - Console")
print("2 - PC")
print("3 - Celular")
print("Digite o número: ", end="")

op = int(input());

if(op==1):
  console()
elif(op==2):
  PC()
elif(op==3):
  celular()
else:
  print("Ops, opção inválida")

