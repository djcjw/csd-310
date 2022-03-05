-- drop test user if exists
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create new whatabook table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);
/*
    insert store record
*/
INSERT INTO store(locale)
    VALUES('1245 4th Street, Santa Rosa, CA 95404');

/*
    insert 9 book records
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Life of ChrisW', 'Chris Ward', 'The self written bio of the Man, the Myth and the Legend!');

INSERT INTO book(book_name, author, details)
    VALUES('Goodnight Moon', 'Margaret Wise Brown', 'An amazing childrens book!');

INSERT INTO book(book_name, author, details)
VALUES ('NoSQL Distilled', 'Pramod J Sadalage', 'Required college textbook');

INSERT INTO book(book_name, author, details)
    VALUES('The Best Pet of All', 'David LaRochelle', 'A really funny kids book');
 
INSERT INTO book(book_name, author, details)
    VALUES('The Liberation Trilogy', 'Rick Atkinson', 'One of the best trilogies that covers almost all the aspects of the second world war in Europe');

INSERT INTO book(book_name, author, details)
    VALUES('Spymasters Prism: The Fight against Russian Aggression', 'Jack Devine', 'Jack Devine details the unending struggle with Russia and its intelligence agencies as it works against our national security');

INSERT INTO book(book_name, author)
    VALUES('Enterprise Cloud Security and Governance', 'Zeal Vora');

INSERT INTO book(book_name, author)
    VALUES('Mastering AWS Security', 'Albert Anthony');

INSERT INTO book(book_name, author)
    VALUES('Practical Cloud Security. A Guide for Secure Design and Deployment', 'Chris Dotson');

/*
    insert 3 users
*/
INSERT INTO user(first_name, last_name)
    VALUES('Deb', 'Lynne');

INSERT INTO user(first_name, last_name)
    VALUES('Avid', 'Redder');

INSERT INTO user(first_name, last_name)
    VALUES('Bear', 'Bauman');

/*
    insert wishlist records
*/
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Deb'),
        (SELECT book_id FROM book WHERE book_name = 'The Best Pet of All')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Avid'),
        (SELECT book_id FROM book WHERE book_name = 'The Liberation Trilogy')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bear'),
        (SELECT book_id FROM book WHERE book_name = 'Spymasters Prism: The Fight against Russian Aggression')
    );
