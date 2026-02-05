create database student;

create table student.academics(
    student_id int,
    firstname varchar(255),
    remark varchar(255) default 'Can do better',
    marks int,
    check ( marks > 35 )            # only accept the greater than 35 marks
);

alter table student.academics add primary key academics(student_id);

create table student.sports(
    sport_id int,
    sport_name varchar(255),
    student_id int,
    primary key sports(sport_id),
    foreign key sports(student_id) references student.academics(student_id),
    constraint abc check ( sport_id != 0 )
);

insert into student.academics(student_id, firstname, marks)
values (2, 'B', 40);

select * from student.academics;

alter table student.academics
alter column marks set default 36;

insert into student.academics(student_id, firstname)
values(3, 'C');

alter table student.academics
alter column marks drop default;

insert into student.academics
values (4, 'D', 'Good', 33);

insert into student.academics
values (4, 'D', 'Good', 36);

insert into student.sports
values (0, 'Kabbadi', 3);

insert into student.sports
values (1, 'Kabbadi', 3);

alter table student.academics
add check ( student_id < 100 );

insert into student.academics
values (101, 'C', 'Good', 6);  # first(academics_chk_1) check will be violated, then the query will terminate executing and not check for the marks>35 constrains.

insert into student.academics
values (5, 'G', 'Good', 60);

insert into student.sports
values (2, 'Cricket', 5);

drop database student;