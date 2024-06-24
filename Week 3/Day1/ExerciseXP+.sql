create table students(
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    birth_date date not null
)

insert into students(
    first_name, last_name, birth_date) values 
('Marc','Benichou','1998/11/02')
('Yoan','Cohen','2010/12/03')
('Lea','Benichou,'1987/27/07/')
('Amelia','Dux','1996/07/04/')
('David','Grez','2003/14/06')
('Omer','Simpson','1980/10/03')

select * from first_name
select * from last_name



##
select first_name, last_name  from students where id=2;
select first_name, last_name  from students where last_name = 'Benichou' and first_name = 'Marc';
select first_name, last_name  from students where last_name = 'Benichou' OR first_names are 'Marc';
select first_name, last_name  from students WHERE first_name LIKE '%a%';
select first_name, last_name  from students WHERE first_name LIKE 'a%';
select first_name, last_name  from students WHERE first_name LIKE '%a';
select first_name, last_name  from students WHERE first_name LIKE '%a_';
select first_name, last_name  from students WHERE id IN (1, 3);

