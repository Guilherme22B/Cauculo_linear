import os
import time

def cls():
  time.sleep(2)
  os.system('cls')




class layout():
  #classe para organizar layout
  #essa classe vai servir unicamente para questoes graficas dentro do sistema
  @staticmethod
  def bem_vindo():
    print("--------------------------")
    print("    Seja bem vindo!!!   ")
    print("--------------------------")

    cls()

  @staticmethod
  def menu():
    print("==========================================")
    print("||           CALCULO LINEAR             ||")
    print("==========================================")
    print("||                                      ||")
    print("||   [1] Iniciar Sistema                ||")
    print("||   [2] Consultar Logs                 ||")
    print("||   [3] Informações do Sistema         ||")
    print("||   [4] Sair                           ||")
    print("||                                      ||")
    print("==========================================")

  @staticmethod
  def info_sistema():


    
    print("----------------------------------------------------------")
    print("-  Esse é um programa para resolução de sistemas lineares -")
    print("----------------------------------------------------------")
    cls()

    print("--------------------------------------------")
    print("- levando em conta uma matriz de até 10x10 -")
    print("--------------------------------------------")
    cls()


    print("==========================================")
    print("||                                       ||")
    print("||     Linguagem ultilizada: python      ||")
    print("||                                       ||")
    print("==========================================")
    cls()
