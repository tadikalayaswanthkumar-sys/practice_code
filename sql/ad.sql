create table if not exists users(
    id int primary key,
    name varchar(30) not null,
    email varchar(30) unique not null,
    role varchar(10) not null default 'guest',
    age int check(age >=18),
    created_at timestamp default current_timestamp
);

-- Insert sample data
insert or ignore into users (id, name, email, age) values
(1, 'Alice', 'alice@example.com', 22),
(2, 'Bob', 'bob@example.com', 25);

