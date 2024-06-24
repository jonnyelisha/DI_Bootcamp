
-- This creates the SQL table for students with the first name and the last name */

-- This creates the SQL table for students with the first name and the last name */

create table students(
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    birth_date date not null
)
 
--The names of the students---
insert into students(
    first_name, last_name, birth_date) values 
('Marc','Benichou','1998/11/02')
('Yoan','Cohen','2010/12/03')
('Lea','Benichou,'1987/27/07/')
('Amelia','Dux','1996/07/04/')
('David','Grez','2003/14/06')
('Omer','Simpson','1980/10/03')


/* Recieves the entire list of first_names and last_names */
select * from first_name
select * from last_name

-- Below is straightforward
select first_name, last_name  from students where id=2;
select first_name, last_name  from students where last_name = 'Benichou' and first_name = 'Marc';
select first_name, last_name  from students where last_name = 'Benichou' OR first_names are 'Marc';

--Fetch the students whose first_names contain the letter a.
select first_name, last_name  from students where first_name LIKE '%a%';

--Fetch the students whose first_names start with the letter a.
select first_name, last_name  from students where first_name LIKE 'a%';

--Fetch the students whose first_names end with the letter a.
select first_name, last_name  from students where first_name LIKE '%a';

--Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select first_name, last_name  from students where first_name LIKE '%a_';

--Gets the Ids between 1 and 3-- 
select first_name, last_name  from students where id IN (1, 3);

