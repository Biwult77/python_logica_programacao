-- CREATE DATABASE escola_2

USE escola_2;
/*
CREATE TABLE aluno (
CPF CHAR(11) PRIMARY KEY NOT NULL,
Nome VARCHAR(20) NOT NULL,
Endereço VARCHAR(50) NOT NULL,
Telefone CHAR(11) NOT NULL,
Data_Nasc DATE NOT NULL
);
*/

/*
INSERT INTO aluno (CPF, nome, Endereço, Telefone, Data_Nasc) VALUES ('01010101010', 'ANA', 'Rua letscode, 123', '11987654321', '1980-05-23');
INSERT INTO aluno (CPF, nome, Endereço, Telefone, Data_Nasc) VALUES ('11111111111', 'MATHEUS','Rua letscode, 456', '11952360873', '1977-09-15');
INSERT INTO aluno (CPF, nome, Endereço, Telefone, Data_Nasc) VALUES ('22222222222', 'FERNANDO', 'Rua letscode, 789','11945456362', '1978-12-25');
INSERT INTO aluno (CPF, nome, Endereço, Telefone, Data_Nasc) VALUES ('12121212121', 'WALNEY', 'Rua letscode, 1122', '91978648253', '1963-01-08');
INSERT INTO aluno (CPF, nome, Endereço, Telefone, Data_Nasc) VALUES ('21212121212', 'ANGELITA', 'Rua letscode, 1', '21212121212', '1971-07-04');
INSERT INTO aluno (CPF, nome, Endereço, Telefone, Data_Nasc) VALUES ('33333333333', 'FABIO', 'Rua letscode, 45', '33333333333', '1969-11-11');
*/
-- UPDATE aluno SET Nome = 'SANDRA' WHERE CPF = '11111111111';
/*
CREATE TABLE departamento (
Código BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
Nome VARCHAR(20) NOT NULL
);

INSERT INTO departamento (Nome) VALUES ('Bacharelado');
INSERT INTO departamento (Nome) VALUES ('Tecnólogo');
*/

/*
CREATE TABLE professor (
Matrícula BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
Nome VARCHAR(20) NOT NULL,
Endereço VARCHAR(50) NOT NULL,
Telefone CHAR(11) NOT NULL,
Data_Nasc DATE NOT NULL,
Código_Depto BIGINT NOT NULL,
Data_Contratação DATE NOT NULL,
FOREIGN KEY (Código_Depto) REFERENCES departamento (Código)
);

INSERT INTO professor (Nome, Endereço, Telefone, Data_Nasc, Código_Depto, Data_Contratação) VALUES ('Matheus', 'Rua Magalu, 26', '11978451263', '1995-06-30', '0001', '2021-01-31');
INSERT INTO professor (Nome, Endereço, Telefone, Data_Nasc, Código_Depto, Data_Contratação) VALUES ('Rafael', 'Rua Magalu, 84', '11935468726', '1989-11-05', '0001', '2020-07-14');
INSERT INTO professor (Nome, Endereço, Telefone, Data_Nasc, Código_Depto, Data_Contratação) VALUES ('Paulo', 'Rua Magalu, 346', '11995478131', '2000-09-03', '0002', '2021-06-02');
INSERT INTO professor (Nome, Endereço, Telefone, Data_Nasc, Código_Depto, Data_Contratação) VALUES ('Brian', 'Rua Magalu, 91', '11995550873', '2001-04-22', '0002', '2020-11-01');
*/

-- DROP TABLE professor;

/*
CREATE TABLE curso (
Código BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
Nome VARCHAR(50) NOT NULL,
Descrição VARCHAR(50) NOT NULL,
Código_Depto BIGINT NOT NULL,
FOREIGN KEY (Código_Depto) REFERENCES departamento (Código)
);

INSERT INTO curso (Nome, Descrição, Código_Depto) VALUES ('Sistemas de Informação', 'Software Engineering & Devops', 1);
INSERT INTO curso (Nome, Descrição, Código_Depto) VALUES ('Engenharia Mecatrônica', 'Robotics Systemss & Machine Learning', 1);
INSERT INTO curso (Nome, Descrição, Código_Depto) VALUES ('Gestão da Tecnologia da Informação', 'Digital Management Enterprise', 2);
INSERT INTO curso (Nome, Descrição, Código_Depto) VALUES ('Análise e Desenvolvimento de Sistemas', 'Full Stack, Apps & Artificial Intelligence', 2);
INSERT INTO curso (Nome, Descrição, Código_Depto) VALUES ('Banco de Dados', 'Data Science, Big Data & BI', 2);
*/

/*
CREATE TABLE matrícula (
Código_Curso BIGINT NOT NULL,
CPF_Aluno CHAR(11) NOT NULL,
Data_Matrícula DATE NOT NULL,
FOREIGN KEY (Código_Curso) REFERENCES curso (Código),
FOREIGN KEY (CPF_Aluno) REFERENCES aluno (CPF)
);

INSERT INTO matrícula (Código_Curso, CPF_Aluno, Data_Matrícula) VALUES (1, '33333333333', '2022-01-08');
INSERT INTO matrícula (Código_Curso, CPF_Aluno, Data_Matrícula) VALUES (1, '11111111111', '2022-01-10');
INSERT INTO matrícula (Código_Curso, CPF_Aluno, Data_Matrícula) VALUES (1, '01010101010', '2022-01-07');
INSERT INTO matrícula (Código_Curso, CPF_Aluno, Data_Matrícula) VALUES (2, '12121212121', '2022-01-12');
INSERT INTO matrícula (Código_Curso, CPF_Aluno, Data_Matrícula) VALUES (2, '22222222222', '2022-01-11');
INSERT INTO matrícula (Código_Curso, CPF_Aluno, Data_Matrícula) VALUES (2, '21212121212', '2022-01-13');
*/

/*
CREATE TABLE disciplina (
Código BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL,
Qtde_Créditos CHAR(11) NOT NULL,
Matrícula_Prof BIGINT NOT NULL,
Nome VARCHAR(50) NOT NULL,
FOREIGN KEY (Matrícula_Prof) REFERENCES professor (Matrícula)
);

INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (20, 1, 'Laboratório e Programação');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (20, 2, 'Sensores e Circuitos Digitais');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (20, 4, 'Arquitetura e Organização de Computadores');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (20, 3, 'Nano Courses');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (20, 3, 'Resolução Diferenciada de Problemas');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (10, 3, 'Web Stands and Game Developing');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (10, 1, 'Storytelling e Inspiração Empreenderora');
INSERT INTO disciplina (Qtde_Créditos, Matrícula_Prof, Nome) VALUES (10, 4, 'Formação Social e Sustentabilidade');
*/

/*
CREATE TABLE cursa (
CPF_Aluno CHAR(11) NOT NULL,
Código_Disc BIGINT NOT NULL,
FOREIGN KEY (CPF_Aluno) REFERENCES aluno (CPF),
FOREIGN KEY (Código_Disc) REFERENCES disciplina (Código)
);

INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('11111111111', 1);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('11111111111', 2);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('11111111111', 3);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('11111111111', 4);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('12121212121', 5);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('12121212121', 6);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('12121212121', 7);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('33333333333', 7);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('33333333333', 8);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('21212121212', 5);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('21212121212', 6);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('21212121212', 7);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('22222222222', 8);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('22222222222', 3);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('01010101010', 4);
INSERT INTO cursa (CPF_Aluno, Código_Disc) VALUES ('01010101010', 1);
*/

/*
CREATE TABLE compõe (
Código_Curso BIGINT NOT NULL,
Código_Disc BIGINT NOT NULL,
FOREIGN KEY (Código_Curso) REFERENCES curso (Código),
FOREIGN KEY (Código_Disc) REFERENCES disciplina (Código)
);

INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (1, 4);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (1, 3);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (1, 2);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (1, 1);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (1, 8);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (2, 1);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (2, 2);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (2, 3);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (2, 8);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (3, 5);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (3, 6);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (3, 8);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (4, 5);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (4, 6);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (4, 7);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (4, 8);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (5, 6);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (5, 7);
INSERT INTO compõe (Código_Curso, Código_Disc) VALUES (5, 8);
*/

/*
CREATE TABLE pre_req (
Código_Disc BIGINT NOT NULL,
Código_Disc_Dependência BIGINT NOT NULL,
FOREIGN KEY (Código_Disc_Dependência) REFERENCES disciplina (Código),
FOREIGN KEY (Código_Disc) REFERENCES disciplina (Código)
);

INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (1, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (2, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (3, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (4, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (5, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (6, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (7, 8);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (2, 4);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (3, 1);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (6, 7);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (5, 7);
INSERT INTO pre_req (Código_Disc, Código_Disc_Dependência) VALUES (3, 1);
*/

-- SELECT * FROM pre_req;

-- a. Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola.
/*
SELECT a.*, c.nome Curso
FROM aluno a
INNER JOIN matrícula m
ON a.CPF = m.CPF_Aluno
INNER JOIN curso c
ON c.Código = m.Código_Curso;
*/

-- b. Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola.
/*
SELECT c.*, d.nome Disciplina
FROM curso c
INNER JOIN compõe cm
ON c.Código = cm.Código_Curso
INNER JOIN disciplina d
ON d.Código = cm.Código_Disc;
*/

-- c. Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados.
/*
SELECT a.Nome Nome, d.nome Disciplina
FROM aluno a
INNER JOIN cursa c
ON a.CPF = c.CPF_Aluno
INNER JOIN disciplina d
ON d.Código = c.Código_Disc;
*/

-- d. Produza um relatório com os dados dos professores e as disciplinas que ministram.
/*
SELECT p.*, d.nome Disciplina
FROM professor p
INNER JOIN disciplina d
ON d.Matrícula_Prof = p.Matrícula;
*/

-- e. Produza um relatório com os nomes das disciplinas e seus pré-requisitos.
/*
SELECT d.nome Disciplina, dd.nome Pré_Requisito
FROM pre_req pr
INNER JOIN disciplina d
ON d.Código = pr.Código_Disc
INNER JOIN disciplina dd
ON dd.Código = pr.Código_Disc_Dependência;
*/

-- f. Produza um relatório com a média de idade dos alunos matriculados em cada curso.
/*
SELECT c.nome Curso, FLOOR(AVG(DATEDIFF(now(), a.Data_Nasc)/365)) Média_Idade 
FROM aluno a
INNER JOIN matrícula m
ON a.CPF = m.CPF_Aluno
INNER JOIN curso c
ON c.Código = m.Código_Curso
GROUP BY 1;
*/

-- g. Produza um relatório com os cursos oferecidos por cada departamento.
/*
SELECT d.nome Departamento, c.Nome Nome_Curso
FROM curso c
INNER JOIN departamento d
ON d.Código = c.Código_Depto
*/
