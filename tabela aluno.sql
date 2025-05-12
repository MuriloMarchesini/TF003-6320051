CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL
);

INSERT INTO alunos (nome, idade) VALUES
('Ana', 20),
('Bruno', 22),
('Carlos', 19),
('Diana', 21),
('Eduardo', 23),
('Fernanda', 20),
('Gustavo', 22),
('Helena', 19),
('Igor', 21),
('Juliana', 23);
