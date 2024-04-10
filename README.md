# DIO_Bank

Fomos contratados pelo <b>DIO Bank</b> para desenvolver um novo sistema.

Esse banco deseja modernizar suas operações e escolheu a linguagem Python.

Para a primeira versão, deveremos implementar apenas 3 operações: Depósito, Saque e Extrato.

<b>Depósito</b>

Deve ser possível depositar valores positivos para a conta bancária. A versão 1 do projeto trabalha apenas com 1 usuário,
dessa forma não precisaremos nos preocupar em identificar qual é o número da agência e conta bancária. Totos os depósitos
devem ser armazenados em uma variável e exibidos na operação extrato.

<b>Saque</b>

O sistema deve permitir realizar 3 saques diários com limite de 500 por saque. Caso o usuários não tenha saldo em conta,
o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques
deverão ser armazenados em uma variável e exibidos na operação de extrato.

<b>Extrato</b>

Essa operação deve listar todos os depósitos e saques realizados na conta.
No fim a listagem deve exibir o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

