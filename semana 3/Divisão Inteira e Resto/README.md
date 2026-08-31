<img width="2548" height="6289" alt="Divisão Inteira e Resto" src="https://github.com/user-attachments/assets/6637e9ea-d765-4226-a628-845b2c6a245c" />

Divisão Inteira e Resto — Little Man Computer (LMC)


O programa calcula a divisão inteira e o resto de dois números digitados pelo usuário. Como o LMC tradicional não possui uma instrução de divisão, o cálculo é realizado por meio de subtrações repetidas.

O primeiro número é o dividendo e o segundo é o divisor. A cada repetição, o divisor é subtraído do dividendo e o quociente aumenta em 1.

 Exemplo

Se o usuário digitar:

17
5

O programa realiza:

17 - 5 = 12
12 - 5 = 7
7 - 5 = 2

Como não é mais possível subtrair 5 de 2:

Quociente = 3
Resto = 2
Fluxograma

O fluxograma representa visualmente o funcionamento do programa: entrada do dividendo → entrada do divisor → iniciar o quociente em 0 → subtrair o divisor do dividendo → verificar se o resultado continua maior ou igual a 0 → repetir a subtração e aumentar o quociente → quando não for possível continuar, o valor restante será o resto → exibir quociente e resto → fim.
| Execução | Dividendo | Divisor | Quociente | Resto |
| -------- | --------: | ------: | --------: | ----: |
| 1        |        17 |       5 |     **3** | **2** |
| 2        |        20 |       4 |     **5** | **0** |
| 3        |        29 |       6 |     **4** | **5** |
