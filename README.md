# CalculadoraIRPF
Um programa em python que pergunta informações de salário e renda para calcular o imposto de renda

O código solicita o número de dependentes e o salário bruto ao usuário no início do código e atribui as varáveis de dados "NumDepend" e "SalarioBruto";

Uma função é chamada para determinar a faixa da aliquota do INSS com base no salário informado, uma estrutura switch verifica qual valor o resultado lógico é True;

A variável "BaseCalculoIRPF" é calculada subtraindo-se do salário bruto a contribuição do INSS e uma dedução por dependente (R$ 189,59 por dependente);

Uma segunda função é chamada para determinar a alíquota do Imposto de Renda Pessoa Física (IRPF) com base na BaseCalculoIRPF. Novamente a estrutura switch  é utilizada para selecionar a alíquota correta, com base na faixa em que a base de cálculo se encontra. Além disso, ela retorna a alíquota e a parcela dedutível referente à faixa relacionada;

O valor do Imposto de Renda é calculado multiplicando-se a diferença entre a BaseCalculoIRPF e a faixa anterior pela alíquota do IRPF;

Para determinar o valor mensal do Imposto de Renda, por último,divide-se o valor total do imposto por 12;
