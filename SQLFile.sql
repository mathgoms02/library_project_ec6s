CREATE TABLE livros_disponiveis(
	idLivro int primary key auto_increment,
    titulo varchar(500),
    autor varchar(500),
    ano int,
    genero varchar(100),
    preco float
);

create table carrinho(
	idLivro int primary key auto_increment,
    idCarrinho_Usuario int,
    titulo varchar(500),
    autor varchar(500),
    ano int,
    genero varchar(100),
    unidades int,
    preco float,
    foreign key(idCarrinho_Usuario) references usuarios(idUsuario)
);

alter table carrinho
add foreign key(idLivro) references livros_disponiveis(idLivro);

alter table carrinho
add foreign key(idLivro_loja) references livros_disponiveis(idLivro);

CREATE TABLE usuarios(
	idUsuario int primary key auto_increment,
    cpfCliente bigint unique,
    nomeUsuario varchar(200),
	senhaUsuario varchar(200)
);

CREATE TABLE livros_usuarios(
	fk_idLivro int,
    fk_idUsuario int,
    foreign key(fk_idLivro) references livros_disponiveis(idLivro),
    foreign key(fk_idUsuario) references usuarios(idUsuario)
);

DROP TABLE livros_usuarios;

ALTER TABLE livros_usuarios
MODIFY fk_idLivro INT, -- Altera o tipo de dado se necessário
ADD CONSTRAINT fk_livro_loja
FOREIGN KEY (fk_idLivro)
REFERENCES carrinho(idLivro_loja);

ALTER TABLE livros_usuarios
MODIFY fk_idLivro INT,
ADD CONSTRAINT fk_livro_loja
FOREIGN KEY (fk_idLivro)
REFERENCES carrinho(idLivro_loja);

drop table livros_usuarios;

insert into carrinho(titulo, autor, ano, genero, unidades, preco)
values("Fahrenheit 451", "Ray Bradbury", 1953, "Ficção", 3, unidades*53.99);

insert into livros_disponiveis(titulo, autor, ano, genero, preco)
values("Fahrenheit 451", "Ray Bradbury", 1953, "Ficção", 53.99);

insert into livros_disponiveis(titulo, autor, ano, genero, preco)
values("Dentro da Baleia e outros ensaios", "George Orwell", 1984, "Drama", 25.99);

-- Utilizando os comandos WHERE, LIKE, COUNT, AVG, SUM, BETWEEN, AND, OR, NOT, ORDER BY, Group by e JOINs

-- Selecionar todos os livros com o título contendo a palavra "romance"
SELECT * FROM livros_disponiveis WHERE titulo LIKE '%romance%';

-- Contar o número de livros com o gênero "ficção científica"
SELECT COUNT(*) FROM livros_disponiveis WHERE genero = 'ficção científica';

-- Calcular a média dos preços dos livros
SELECT AVG(preco) FROM livros_disponiveis;

-- Calcular a soma dos preços dos livros publicados entre 2010 e 2020
SELECT SUM(preco) FROM livros_disponiveis WHERE ano BETWEEN 2010 AND 2020;

-- Selecionar todos os livros disponíveis do autor "Stephen King" e com preço acima de 50
SELECT * FROM livros_disponiveis WHERE autor = 'Stephen King' AND preco > 50;

-- Selecionar todos os livros disponíveis do autor "Agatha Christie" ou com preço abaixo de 30
SELECT * FROM livros_disponiveis WHERE autor = 'Agatha Christie' OR preco < 30;

-- Selecionar todos os livros disponíveis que não sejam do gênero "fantasia"
SELECT * FROM livros_disponiveis WHERE genero <> 'fantasia';

-- Selecionar todos os livros disponíveis ordenados por título em ordem alfabética crescente
SELECT * FROM livros_disponiveis ORDER BY titulo ASC;

-- Selecionar o número de livros disponíveis agrupados por gênero
SELECT genero, COUNT(*) FROM livros_disponiveis GROUP BY genero;

-- Selecionar os livros disponíveis e seus respectivos autores, juntamente com o nome do usuário que possui o livro
SELECT ld.titulo, ld.autor, u.nomeUsuario
FROM livros_disponiveis ld
JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario;

SELECT ld.titulo, ld.autor, u.nomeUsuario
FROM livros_disponiveis ld
JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario
WHERE u.nomeUsuario = 'junin';

SELECT ld.titulo, ld.autor, ld.preco, u.nomeUsuario
FROM livros_disponiveis ld
JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario
WHERE ld.preco IS NOT NULL 
  AND u.nomeUsuario = 'junin'; 

-- SOMA
SELECT
    SUM(preco) AS total
FROM
    livros_disponiveis ld
JOIN
    livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
JOIN
    usuarios u ON lu.fk_idUsuario = u.idUsuario
WHERE
    preco IS NOT NULL
    AND u.nomeUsuario = 'junin';


-- MÉDIA
SELECT
    AVG(preco) AS media
FROM
    livros_disponiveis ld
JOIN
    livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
JOIN
    usuarios u ON lu.fk_idUsuario = u.idUsuario
WHERE
    preco IS NOT NULL
    AND u.nomeUsuario = 'junin';

-- MODA
SELECT
    (
        SELECT preco
        FROM livros_disponiveis ld
        JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
        JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario
        WHERE preco IS NOT NULL AND u.nomeUsuario = 'junin'
        GROUP BY preco
        ORDER BY COUNT(*) DESC, preco
        LIMIT 1
    ) AS moda;

-- MEDIANA
SELECT AVG(preco) AS mediana
FROM (
    SELECT preco
    FROM (
        SELECT preco,
               ROW_NUMBER() OVER (ORDER BY preco) AS row_num,
               COUNT(*) OVER () AS total_rows
        FROM livros_disponiveis ld
        JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
        JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario
        WHERE preco IS NOT NULL AND u.nomeUsuario = 'junin'
    ) AS ranked
    WHERE row_num BETWEEN total_rows / 2 AND total_rows / 2 + 1
) AS subquery;

-- DESVIO PADRAO
SELECT
    STDDEV(preco) AS desvio_padrao
FROM
    livros_disponiveis ld
JOIN
    livros_usuarios lu ON ld.idLivro = lu.fk_idLivro
JOIN
    usuarios u ON lu.fk_idUsuario = u.idUsuario
WHERE
    preco IS NOT NULL
    AND u.nomeUsuario = 'junin';



