CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    created_at TIMESTAMP
);
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    title TEXT,
    content TEXT,
    created_at TIMESTAMP
);
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    alias TEXT
);
CREATE TABLE post_categories (
    post_id SERIAL PRIMARY KEY REFERENCES posts ON DELETE CASCADE,
    category_id SERIAL REFERENCES categories
);
CREATE TABLE permission_levels (
    user_type SERIAL PRIMARY KEY,
    alias TEXT
);
CREATE TABLE user_roles (
    user_id SERIAL PRIMARY KEY REFERENCES users ON DELETE CASCADE,
    user_type INTEGER REFERENCES permission_levels
);

INSERT INTO permission_levels (user_type, alias) VALUES(100, 'user');
INSERT INTO permission_levels (user_type, alias) VALUES(200, 'moderator');
INSERT INTO permission_levels (user_type, alias) VALUES(300, 'admin');
INSERT INTO categories (alias) VALUES('3D');
INSERT INTO categories (alias) VALUES('Woodworking');
INSERT INTO categories (alias) VALUES('Electronics');