SELECT *
FROM public.tasks
where user_id = 1;

select *
from tasks t 
where status_id = (select id from status s where name = 'new')

update tasks set status_id  = (select id from status s where name = 'in progress')
where id = 10

select * from users t 
where id not in (select distinct user_id from tasks)

insert into tasks (title,description,status_id,user_id)
values('Task ntitle', 'task desc', 1,1)

delete from public.tasks where id = 10

select * from users where email like '%go%'

update users set fullname  = 'John Smith'
where id =9

select status_id , count(*)
from tasks t 
group by status_id 

select t.*
from tasks t
join users u on t.user_id =u.id 
where u.email like '%example.com'

select *
from tasks 
where description is null 

select t.*
from tasks t 
inner join users u on t.user_id = u.id 
inner join status s on t.status_id  = s.id 
where s."name" ='in progress'

select u.fullname, count(*)
from users u 
left join tasks t on u.id=t.user_id
group by u.fullname 

delete from users where id =10

