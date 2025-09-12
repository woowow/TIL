USE library_db;

SELECT 
    b.title AS book_title,
    a.name AS author_name,
    g.genre_name AS genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id;


CREATE INDEX authors_name_idx ON authors (name);

CREATE INDEX genres_name_idx ON genres(genre_name);

SELECT 
    b.title AS book_title,
    a.name AS author_name,
    g.genre_name AS genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id
WHERE a.name = 'J.K. Rowling'
  AND g.genre_name = 'Fantasy';