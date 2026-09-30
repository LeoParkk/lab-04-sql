DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id  INT,
    name     VARCHAR(50),
    location     VARCHAR(50),
    PRIMARY KEY (user_id)
);

CREATE TABLE posts (
    post_id  INT PRIMARY KEY,
    user_id  INT,
    title    VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
); 

INSERT INTO users (user_id,name,location) VALUES (1,'Leo','Centreville');
INSERT INTO users (user_id, name, location) VALUES (2,'Bob','LA');
INSERT INTO users (user_id, name, location) VALUES (3,'BOBBY','LA');
INSERT INTO users (user_id, name, location) VALUES (4,'Bobby Jr','LA');
INSERT INTO users (user_id, name, location) VALUES (5, 'pc', 'charlottesville');
INSERT INTO users (user_id, name, location) VALUES (6,'jon','chicago');
INSERT INTO users (user_id, name, location) VALUES (7, 'david','centreville');
INSERT INTO users (user_id, name, location) VALUES (8,'dog','pet store');
INSERT INTO users (user_id, name, location) VALUES (9,'fish','pet store');
INSERT INTO users (user_id, name, location) VALUES (10, 'cow','farm');

INSERT INTO posts (post_id, user_id, title) VALUES (1, 1, 'First!');
INSERT INTO posts (post_id, user_id, title) VALUES (2, 2, 'yoohoo');
INSERT INTO posts (post_id, user_id, title) VALUES (3, 3, 'hi');
INSERT INTO posts (post_id, user_id, title) VALUES (4, 4, 'bye');
INSERT INTO posts (post_id, user_id, title) VALUES (5, 5, 'hello');
INSERT INTO posts (post_id, user_id, title) VALUES (6, 7, 'good morning');
INSERT INTO posts (post_id, user_id, title) VALUES (7, 6, 'good afternoon');
INSERT INTO posts (post_id, user_id, title) VALUES (8, 8, 'good night');
INSERT INTO posts (post_id, user_id, title) VALUES (9, 9, 'good noon');
INSERT INTO posts (post_id, user_id, title) VALUES (10, 1, 'bye');

