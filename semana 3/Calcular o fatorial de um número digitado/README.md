<img width="2531" height="7161" alt="Calcular o fatorial de um número digitado" src="https://github.com/user-attachments/assets/319419e4-0980-4e16-bec4-01b0723fe563" />


Fatorial de um Número — Little Man Computer (LMC)


O programa calcula o fatorial de um número digitado pelo usuário. O fatorial é obtido multiplicando o número por todos os valores inteiros menores que ele até chegar a 1.

Como o LMC tradicional não possui uma instrução de multiplicação, o programa realiza a multiplicação por meio de somas repetidas.

 Exemplo

Se o usuário digitar:

4

O cálculo será:

4 × 3 × 2 × 1 = 24

Resultado:

24
 Fluxograma

O fluxograma representa visualmente o funcionamento do programa: entrada do número → inicialização do resultado → verificar o valor de n → preparar a multiplicação → realizar a multiplicação por somas repetidas → atualizar os valores → repetir até chegar a 1 → exibir o resultado → fim.

| Execução | Entrada | Cálculo           | Resultado |
| -------- | ------: | ----------------- | --------: |
| 1        |       4 | 4 × 3 × 2 × 1     |    **24** |
| 2        |       5 | 5 × 4 × 3 × 2 × 1 |   **120** |
| 3        |       3 | 3 × 2 × 1         |     **6** |
