# Desenvolve40+ / Magalu

## Formação com foco na linguagem Python (4 módulos - 108 horas/aula - Let´s Code)

- Lógica de Programação
- POO
- Estrutura de Dados
- Banco de Dados

Cada um dos módulos foi encerrado com um projeto com foco nas habilidades desenvolvidas:

# Projeto 01 - black_friday 

A partir do acesso a uma arquivo dado (dados.json) com uma lista de dicionários, onde cada dicionário representa um produto com: 
ID (identificador único), o preço e a categoria do produto. 

Funções implementadas: 

- listar todas as categorias, 
- listar todos os produtos de uma categoria, 
- identificar o produto mais barato e o mais caro de uma categoria e 
- o top 10 de produtos mais baratos e mais caros de toda a base de dados.

# Projeto 02 - loja_bike

Sistema de Empréstimo de Bicicletas a partir de duas classes principais (Cliente, Loja).

Cliente pode: <br>

- Ver as bicicletas disponíveis na Loja; <br> 
- Alugar bicicletas por hora (R$5/hora);<br> 
- Alugar bicicletas por dia (R$25/dia); <br>
- Alugar bicicletas por semana (R$100/semana); <br> 
- Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquertipo) com 30% de desconto no valor total.<br>

Loja pode: <br>

- Calcular a conta quando o cliente decidir devolver a bicicleta; <br>
- Mostrar o estoque de bicicletas; <br>
- Receber pedidos de aluguéis por hora, diários ou semanais validando apossibilidade com o estoque e modo de aluguel existente. <br>
- Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana); <br>
- O cliente pode decidir livremente quantas bicicletas quer alugar; <br>
- Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.

# Projeto 03 - busca_rios

Dada uma lista bi-dimensional com altura e largura não necessáriamente iguais contendo apenas 0's e 1's. 
Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. Rios são compostos por 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). 
O número de 1's adjacentes representa o tamanho do rio.

O rio pode fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados um rio só.

Criado um algoritmo que recebe esta lista bi-dimensional e retorna uma lista com os tamanhos dos rios dentro dessa estrutura, os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.

# Projeto 04 - escola

Dados modelo entidade relacinal e um modelo relacional a partir do DER: 

1.	Implementar um script SQL chamado ‘escola.sql’ com os comandos de criação do banco de dados escola.

  - Criar um banco de dados vazio chamado escola.<br>
  - Criar todas as tabelas que fazem parte do banco, a partir do modelo relacional.<br>
  - Definir as restrições de integridade referencial (chaves estrangeiras) nas tabelas necessárias.<br>
  - Definir as chaves primárias das tabelas.<br>
  - Definir as restrições de domínio de atributo.<br>
  - Conter comandos de inserção de dados em todas as tabelas. <br>
  
  Os dados inseridos serão utilizados na etapa 2 do projeto.

2.	Implementar um script SQL chamado ‘consultas_escola.sql’ com os comandos que respondam às seguintes consultas:

  - Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola.<br>
  - Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola.<br>
  - Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados.<br>
  - Produza um relatório com os dados dos professores e as disciplinas que ministram.<br>
  - Produza um relatório com os nomes das disciplinas e seus pré-requisitos.<br>
  - Produza um relatório com a média de idade dos alunos matriculados em cada curso.
  - Produza um relatório com os cursos oferecidos por cada departamento.<br>

Considere que:

1.	O SGBD adotado para o projeto deve ser o MySQL.<br>
2.	Os scripts devem ser implementados de modo que sua execução seja direta e aconteça sem erros em qualquer ambiente MySQL.<br>
3.	O domínio dos atributos (tipo de dados, formato, etc.) fica a critério do aluno.<br>
4.	O aluno tem liberdade de criar novos atributos ou relações que julgar necessário para enriquecimento do modelo.<br>
