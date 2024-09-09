create table if not exists users (
 id INT PRIMARY KEY,
  fullname VARCHAR(100) not null,
  email VARCHAR(100) unique not null
);

create table if not exists status (
 id INT PRIMARY KEY,
  name VARCHAR(50) unique not null
);

create table if not exists tasks (
id INT PRIMARY KEY,
  title VARCHAR(100) not null,
  description TEXT,
  status_id INTEGER REFERENCES status(id),
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
)