CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
);
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES users,
    content TEXT,
    category, TEXT
    created_at TIMESTAMP
);