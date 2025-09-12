CREATE DATABASE library_db;

USE library_db;

CREATE TABLE authors (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO authors (name)
VALUES 
('J.K. Rowling'), 
('George R.R. Martin'), 
('J.R.R. Tolkien'), 
('Isaac Asimov'), 
('Agatha Christie');

CREATE TABLE genres (
  id INT AUTO_INCREMENT PRIMARY KEY,
  genre_name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO genres (genre_name)
VALUES ('Fantasy'), ('Science Fiction'), ('Mystery'), ('Thriller')

CREATE TABLE books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100),
  author_id INT,
  genre_id INT,
  FOREIGN KEY (author_id) REFERENCES authors(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id)
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'Harry Potter and the Philosopher''s Stone',
  (SELECT id FROM authors WHERE name = 'J.K. Rowling'),
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'Harry Potter and the Chamber of Secrets',
  (SELECT id FROM authors WHERE name = 'J.K. Rowling'),
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'A Game of Thrones',
  (SELECT id FROM authors WHERE name = 'George R.R. Martin'),
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'A Clash of Kings',
  (SELECT id FROM authors WHERE name = 'George R.R. Martin'),
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'The Hobbit',
  (SELECT id FROM authors WHERE name = 'J.R.R. Tolkien'),
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'The Lord of the Rings',
  (SELECT id FROM authors WHERE name = 'J.R.R. Tolkien'),
  (SELECT id FROM genres WHERE genre_name = 'Fantasy')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'Foundation',
  (SELECT id FROM authors WHERE name = 'Isaac Asimov'),
  (SELECT id FROM genres WHERE genre_name = 'Science Fiction')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'I, Robot',
  (SELECT id FROM authors WHERE name = 'Isaac Asimov'),
  (SELECT id FROM genres WHERE genre_name = 'Science Fiction')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'Murder on the Orient Express',
  (SELECT id FROM authors WHERE name = 'Agatha Christie'),
  (SELECT id FROM genres WHERE genre_name = 'Mystery')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'The Mysterious Affair at Styles',
  (SELECT id FROM authors WHERE name = 'Agatha Christie'),
  (SELECT id FROM genres WHERE genre_name = 'Mystery')
);

INSERT INTO books (title, author_id, genre_id)
VALUES (
  'The Girl with the Dragon Tattoo',
  (SELECT id FROM authors WHERE name = 'Agatha Christie'),
  (SELECT id FROM genres WHERE genre_name = 'Thriller')
);

SELECT * FROM books;