CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
    utype INTEGER REFERENCES user_roles
);
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    content TEXT,
    category INTEGER REFERENCES categories
    created_at TIMESTAMP
);
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    desc TEXT
);
CREATE TABLE user_roles (
    id SERIAL PRIMARY KEY,
    desc TEXT,
    utype INTEGER
);