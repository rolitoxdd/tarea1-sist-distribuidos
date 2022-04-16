
CREATE TABLE products( -- tabla productos
    id SERIAL PRIMARY KEY,
    name_product CHAR(30) NOT NULL,
    price FLOAT NOT NULL
);


insert into products (name_product,price) values ('Papa', 30.2);
insert into products (name_product,price) values ('Manzana', 10.5);
insert into products (name_product,price) values ('Lechuga', 20.0);
insert into products (name_product,price) values ('Zapallo', 40.2);
insert into products (name_product,price) values ('Calabaza', 100.7);
insert into products (name_product,price) values ('Dragon', 66.4);
insert into products (name_product,price) values ('Melon', 25.1);
insert into products (name_product,price) values ('Watermelon', 78.3);
insert into products (name_product,price) values ('Apple', 105.5);
insert into products (name_product,price) values ('Pera', 55.5);
insert into products (name_product,price) values ('Platano', 99.9);