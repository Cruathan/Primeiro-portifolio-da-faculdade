#Digite abaixo sua altura e peso
num1 = float(input ('Digite seu peso aqui: '))
num2 = float(input ('Digite sua altura aqui: '))

imc = float(format(num1 / (num2 * num2))[:4]) #Calcula o valor do peso dividido pela altura vezes altura
if imc <= 18.5: #Se o IMC for menor ou igual a 18.5
  print('Seu índice de massa corporal é', imc, 'classificado como magreza!')
elif imc <= 24.9: #Se o IMC for menor ou igual a 24.9
  print('Seu índice de massa corporal é', imc, 'classificado como normal!')
elif imc <= 29.9: #Se o IMC for menor ou igual a 29.9
  print('Seu índice de massa corporal é', imc, 'classificado como sobrepeso')
elif imc <= 34.9: #Se o IMC for menor ou igual a 34.9
  print('Seu índice de massa corporal é', imc, 'classificado como obesidade de 1° grau')
elif imc <= 39.9: #Se o IMC for menor ou igual a 39.9
  print('Seu índice de massa corporal é', imc, 'classificado como obesidade de 2° grau')
elif imc >= 40.0: #Se o IMC for maior ou igual a 40.0
  print('Seu índice de massa corporal é', imc, 'classificado como obesidade de 3° grau')