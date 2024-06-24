

create table items(
    id serial primary key,
    name varchar(50) Not null,
    price integer not null
)


create table customers(
    id serial primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null
)

insert into items(name,price) values ('Small Desk', 100)
insert into items(name,price) values ('Large Desk', 300)
insert into items(name,price) values ('Fan', 80)


#Adding 5 customers to customers table
insert into customers (first_name, last_name), values ('Greg', 'Jones');
insert into customers (first_name, last_name), values ('Sandra', 'Jones');
insert into customers (first_name, last_name), values ('Scott', 'Scott');
insert into customers (first_name, last_name), values ('Trevor', 'Green')
insert into customers (first_name, last_name), values ('Melanie' 'Johnson');




#Fetching data from the database 

select * from items where price > 80;
select * from price where price <= 300 ;
select * from customers where last_name = 'Smith';
select * from customers where last_name = 'Jones';
select * from customers where first_name !='Scott';
