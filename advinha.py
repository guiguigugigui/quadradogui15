import random
# precisa ter dois espaço em branco entre os import.
# e o inicio da função, fora os comentarios.
# as linhas do código podem ter apenas 79 caracteres.


def jogo_advinhacao() :
 # Gera um número aleatório  entre 1 e 100
   numero_aleatorio = random.randint(1, 10)  # Gera um número aleatório 
   max_tentativas = 8                         # entre 1 e 10
   
   print("Bem-vindo ao jogo de Adivinhação")
   print("Tente adivinhar o número entre 1 e 100.")
   
   for tentativa in range(max_tentativas):
       palpite = int(input("Digite sua tentativa: "))
       
       if palpite < numero_aleatorio:
           print("Muito baixo. Tente um número maior.")
       elif palpite > numero_aleatorio:
           print("Muito alto. Tente um número menor.")
       else:
           print(f"Parabéns! Você acertou o número{numero_aleatorio} em "f"{tentativa + 1} tentativas! ")
           return
       
       print(f"Suas {max_tentativas} tentativas acabaram."
       f"O número correto era {numero_aleatorio}.")
       # Além da indentificação correta, é necessario 2 espaços entre as funções.
       # Mesmo após esse comentario. E não pode ter espaços em branco após
       # o fim da linha.
       # Parecia ter um espaço entre o hash # e o começo da linha do comentário.
       
       if __name__ == "__main__":
            jogo_advinhacao()
            # Precisa ter uma linha em branco após o fim do arquivo
            # mas sem espaços em branco
            
            
           