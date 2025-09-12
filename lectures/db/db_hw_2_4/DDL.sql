USE libraries;

UPDATE books
SET price = 12.99
where isbn = '9780743273565';

UPDATE books
SET genre = 'Science Fiction'
where isbn = '9780451524935';

UPDATE books
SET publisher = 'Charles Scribner''s Sons'
where isbn = '9780743273565';

SELECT * FROM books
