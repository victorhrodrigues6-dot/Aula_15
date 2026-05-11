temperatura_limite = 80
sistema_ativo = True

while sistema_ativo:
  
#Simulação de leitura de sensor
 
    temperatura_atual = float(input("Digite a temperatura atual do servidor (°C): "))
    
    if temperatura_atual > temperatura_limite:
        print("ALERTA: Temperatura crítica!")
        print("Resfriamento ativado.")
    else:
        print("Temperatura estável.")
    
#Encerrar o monitoramento
   
    continuar = input("Continuar monitoramento? (s/n): ")
    if continuar.lower() == 'n':
        sistema_ativo = False