create database Snehlee_Student_MngApp
USE Snehlee_Student_MngApp

show tables
show columns from school_profile

drop table userRegister
create table userRegister(
USER_ID VARCHAR(100) PRIMARY KEY,
FNAME VARCHAR(300),
MIDNAME VARCHAR(300),
LNAME VARCHAR(300),
PSW VARCHAR(300),
MOBILE VARCHAR(10),
EMAIL varchar(150),
IMAGE LONGBLOB,
SECQ VARCHAR(500),
SECANS VARCHAR(500)
)


create table school_profile (
school_name varchar(600),
school_address varchar(1000),
school_logo longblob,
school_board varchar(100),
school_title varchar(1000)
)
drop Table school_profile

insert into school_profile(school_name,school_address,school_board,school_title) values(
"Amrit Memorial Higher Secondary School",
"Chaliswan Mohammadabad Gohana Mau",
"CBSE",
"Knowledge is Infinite"
)

update school_profile set school_name= 'sdfsdf' where school_board='CBSE'

select * from userRegister



create table MyStudentBasicDetails (
St_Serial_Number int Primary key Auto_Increment,
St_RegistrationId varchar(10),
St_class varchar(10),
St_Name varchar(500),
St_Gender varchar(50),
St_dob varchar(150),
St_BloodGroup varchar(50),
St_Caste varchar(60),
St_adhar varchar(20),
St_Mobile varchar(13),
St_Email varchar(500),
St_image longblob
)
select * from MyStudentBasicDetails
drop table MyStudentBasicDetails


create table MyStudentFatherDetails(
F_Serial_Number int Primary key Auto_Increment,
St_RegistrationId varchar(10),
F_firstName varchar(300),
F_midName varchar(200),
F_lastName varchar(200),
F_dob varchar(50),
F_nationality varchar(100),
F_education varchar(200),
F_occupation varchar(500),
F_annualIncome varchar(200),
F_mobile varchar(15),
F_email varchar(500),
F_officeAddrs varchar(1500),
F_image longblob
)
drop table MyStudentFatherDetails
select * from MyStudentFatherDetails








create table MyStudentMotherDetails(
M_Serial_Number int Primary key Auto_Increment,
St_RegistrationId varchar(10),
M_firstName varchar(300),
M_midName varchar(200),
M_lastName varchar(200),
M_dob varchar(50),
M_nationality varchar(100),
M_education varchar(200),
M_occupation varchar(500),
M_annualIncome varchar(200),
M_mobile varchar(15),
M_email varchar(500),
M_officeAddrs varchar(1500),
M_image longblob
)
drop table MyStudentMotherDetails
select * from MyStudentMotherDetails








create table MyStudentGuardianDetails(
G_Serial_Number int Primary key Auto_Increment,
St_RegistrationId varchar(10),
G_firstName varchar(300),
G_midName varchar(200),
G_lastName varchar(200),
G_dob varchar(50),
G_nationality varchar(100),
G_education varchar(200),
G_occupation varchar(500),
G_annualIncome varchar(200),
G_mobile varchar(15),
G_email varchar(500),
G_officeAddrs varchar(1500),
G_image longblob
)
drop table MyStudentGuardianDetails
select * from MyStudentGuardianDetails


