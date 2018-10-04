

#Query # 1a. Display the first and last names of all actors from the table `actor`.


use sakila;

select 

act.first_name
,act.last_name

from actor act ;


# 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`.


select 

concat(UPPER(act.first_name)," ",UPPER(act.last_name)) 'Actor Name'

from actor act ;


## 2a. You need to find the ID number, first name, and last name of an actor, 
#of whom you know only the first name, "Joe." What is one query would you use to 
#obtain this information?

select
act.actor_id
,act.first_name
,act.last_name


from actor act

where act.first_name like 'Joe';


## 2b. Find all actors whose last name contain the letters `GEN`:

select * from actor
where last_name like '%GEN%';

# 2c. Find all actors whose last names contain the letters `LI`. 
#This time, order the rows by last name and first name, in that order:

select * from actor

where last_name like '%LI%' 

ORDER BY last_name, first_name;


### 2d. Using `IN`, display the `country_id` and `country` columns of the following 
#countries: Afghanistan, Bangladesh, and China:

select 

c.country_id
,c.country
from country c
where c.country in ('Afghanistan', 'Bangladesh','China');

## 3a. You want to keep a description of each actor. 
#You don't think you will be performing queries on a description, 
#so create a column in the table `actor` named `description` 
#and use the data type `BLOB` (Make sure to research the type `BLOB`, 
#as the difference between it and `VARCHAR` are significant).
USE SAKILA;

ALTER TABLE actor ADD COLUMN DESCRIPTION BLOB AFTER last_update;


## 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the `description` column.

ALTER TABLE actor drop column description;
# 4a. List the last names of actors, as well as how many actors have that last name.

select 
last_name
,count(actor_id) 'Counts'

from actor

group by last_name
order by last_name asc;

# 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors.
select 
last_name
,count(actor_id) 'Counts'

from actor

group by last_name
having count(actor_id) >= 2;
# 4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`. 
#Write a query to fix the record.
set sql_safe_updates = 0;


UPDATE ACTOR 
SET FIRST_NAME = 'HARPO'
WHERE FIRST_NAME = 'GROUCHO';
# 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. 
#It turns out that `GROUCHO` was the correct name after all! 
#In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.
use Sakila;
UPDATE ACTOR 
SET FIRST_NAME = 'GROUCHO'
WHERE FIRST_NAME = 'HARPO';


# 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
show create table sakila.address;
# 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. 
#Use the tables `staff` and `address`:
select
s.first_name
,s.last_name
,a.address
from

staff s
left join address a on s.address_id = a.address_id;

#Only two staff members? Checking accuracy. 
#select * from address;
#select * from staff;
#select * from payment;
# 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. 
#Use tables `staff` and `payment`.
select 
SUM(P.AMOUNT) 'TOTALRUNGUP'
,S.FIRST_NAME
froM

staff s

JOIN PAYMENT P ON S.STAFF_ID = P.STAFF_ID
where 
month(p.payment_date) = 8 and year(p.payment_date) = 2005
GROUP BY S.FIRST_NAME;
# 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
select 
f.title 'FilmTitle'
,count(fa.actor_id) 'ActorCounts'
from film_actor fa
inner join film f on  fa.film_id = f.film_id
group by f.title;
# 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
select
f.title
,count(inv.inventory_id)'InvCounts'
from 
inventory inv
join film f on inv.film_id = f.film_id
where f.title like 'Hunchback Impossible'
group by f.title;

# 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. 
#List the customers alphabetically by last name:

select 
sum(p.amount) 'TotalPayment'
,concat(c.last_name,', ',c.first_name) 'Name'
from
payment p 
join customer c on p.customer_id = c.customer_id 
group by concat(c.last_name,', ',c.first_name)
order by c.last_name asc;

 

# 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
#films starting with the letters `K` and `Q` have also soared in popularity. 
#Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.

select
f.title 'FilmTitle'
,f.language_id 'LanguageID'
,l.name 'LanguageType'
from
film f 
join 
#using a subquery to pull all languages with id = 1; we could also just do this in the join or where clause without
#a subquery 
(select 

language_id
,language.name

from language where language_id = 1 )l on f.language_id = l.language_id 
where
(case when f.title like 'Q%' or f.title like 'K%' then 1 else 0 end) = 1;




# 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
select 
concat(a.first_name,', ',a.last_name) 'Name'
,f.title
from 
actor a
join film_actor fa on a.actor_id = fa.actor_id
join
(select 
film_id
,title
from film  where title like 'Alone Trip')f on f.film_id = fa.film_id;
# 7c. You want to run an email marketing campaign in Canada, for which you will need the names and 
#email addresses of all Canadian customers. Use joins to retrieve this information.
select 
c.first_name
,c.last_name
,c.email
,ctry.country
from customer c 
join address a on c.address_id = a.address_id
join city cty on cty.city_id = a.city_id 
join country ctry on ctry.country_id = cty.country_id
where ctry.country like 'Canada';





# 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
#Identify all movies categorized as _family_ films.
select
f.title 'FilmTitle'
,ct.name 'FilmCategory'
from film f
join film_category fc on fc.film_id = f.film_id
join category ct on ct.category_id = fc.category_id
where ct.name like'family' ;

# 7e. Display the most frequently rented movies in descending order.
select

count(r.rental_id) 'Rentals'
,f.title

from customer c 

join rental r on  c.customer_id = r.customer_id 
join inventory inv on  r.inventory_id = inv.inventory_id
join film f on inv.film_id = f.film_id

group by f.title
order by count(r.rental_id) desc;
# 7f. Write a query to display how much business, in dollars, each store brought in.
select
sum(p.amount) 'TotalSales'
,s.store_id
from

store s 

##left join inventory inv on s.store_id = inv.stored_id
left join customer c on s.store_id = c.store_id
left join payment p on c.customer_id = p.customer_id
group by s.store_id;
#selecting distinct stores to make sure we are only supposed to be aggregating for two stores (seems low)
select distinct store_id from store;

# 7g. Write a query to display for each store its store ID, city, and country.
select
s.store_id
,c.city
,con.country
from store s
left join address ad on s.address_id = ad.address_id
left join city c on ad.city_id = c.city_id
left join country con on c.country_id = con.country_id;

# 7h. List the top five genres in gross revenue in descending order. 
#(##Hint##: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select

sum(p.amount) 'Gross Revenue'
,c.name 'Genre'

from rental r 
join payment p on r.rental_id = p.rental_id
join inventory inv on  r.inventory_id = inv.inventory_id
join film_category fc on inv.film_id = fc.film_id
join category c on fc.category_id = c.category_id
group by c.name
order by sum(p.amount) desc
limit 5;


# 8a. In your new role as an executive, you would like to have an easy way of viewing the 
#Top five genres by gross revenue. Use the solution from the problem above to create a view. 
#If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW TOP_5_GENRE AS 
select

sum(p.amount) 'Gross Revenue'
,c.name 'Genre'

from rental r 
join payment p on r.rental_id = p.rental_id
join inventory inv on  r.inventory_id = inv.inventory_id
join film_category fc on inv.film_id = fc.film_id
join category c on fc.category_id = c.category_id
group by c.name
order by sum(p.amount) desc
limit 5;
# 8b. How would you display the view that you created in 8a?
SELECT * FROM TOP_5_GENRE;
# 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
DROP VIEW TOP_5_GENRE;