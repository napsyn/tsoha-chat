CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    title TEXT,
    content TEXT,
    created_at TIMESTAMP
);
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    alias TEXT
);
CREATE TABLE post_categories (
    post_id SERIAL PRIMARY KEY REFERENCES posts,
    category_id SERIAL REFERENCES categories
);
CREATE TABLE permission_levels (
    id SERIAL PRIMARY KEY,
    alias TEXT,
    user_type INTEGER
);
CREATE TABLE users_roles (
    id SERIAL PRIMARY KEY REFERENCES users,
    user_type INTEGER REFERENCES permission_levels
);