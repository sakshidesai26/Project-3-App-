CREATE DATABASE project3;
USE project3;
CREATE TABLE Courses ( CID int auto_increment primary key, CourseName varchar(100) not null, Content text, Duration int);
INSERT INTO Courses (CourseName, Content, Duration) VALUES
('Introduction to Computer Science', 'An introductory course on computer science and programming.', 10),
('Advanced Mathematics', 'A comprehensive course on advanced mathematical concepts and techniques.', 15),
('Creative Writing', 'A course designed to enhance creative writing skills.', 8),
('Physics Basics', 'Fundamental concepts of physics.', 12),
('History of Art', 'An overview of art history.', 10);
CREATE TABLE Instructors (InstructorID int auto_increment primary key, Iname varchar(100) not null, email varchar(100) not null unique);
INSERT INTO Instructors (Iname, email) VALUES
('John Smith', 'john.smith@example.com'),
('Alice Johnson', 'alice.johnson@example.com'),
('Robert Brown', 'robert.brown@example.com'),
('Emily Davis', 'emily.davis@example.com'),
('Michael Wilson', 'michael.wilson@example.com');
CREATE TABLE Students (SID int auto_increment primary key, StudentName varchar(100) not null, email varchar(100) not null unique);
INSERT INTO Students (StudentName, email) VALUES
('Emma Thompson', 'emma.thompson@example.com'),
('Liam Harris', 'liam.harris@example.com'),
('Olivia Martinez', 'olivia.martinez@example.com'),
('Noah Clark', 'noah.clark@example.com'),
('Ava Lewis', 'ava.lewis@example.com');
CREATE TABLE Enrollments (EID int auto_increment primary key, SID int, CID int, EDate date, foreign key (SID) references Students(SID),foreign key (CID) references Courses(CID));
INSERT INTO Enrollments (SID, CID, EDate) VALUES
(1, 1, '2024-01-10'),
(2, 2, '2024-01-11'),
(3, 3, '2024-01-12'),
(4, 4, '2024-01-13'),
(5, 5, '2024-01-14');
CREATE TABLE Assessments (AID int auto_increment primary key, CID int, AName varchar(100) not null, DueDate date, foreign key (CID) references Courses(CID));
INSERT INTO Assessments (CID, AName, DueDate) VALUES
(1, 'Midterm Exam', '2024-03-01'),
(2, 'Final Project', '2024-03-15'),
(3, 'Essay', '2024-02-20'),
(4, 'Lab Report', '2024-03-05'),
(5, 'Presentation', '2024-02-25');
CREATE TABLE Grades (GID int auto_increment primary key, AID int, SID int, Grade decimal(5,2), foreign key (AID) references Assessments(AID), foreign key (SID) references Students(SID));
INSERT INTO Grades (AID, SID, Grade) VALUES
(1, 1, 85.50),
(2, 2, 90.00),
(3, 3, 88.75),
(4, 4, 92.00),
(5, 5, 87.25);
CREATE TABLE Courses_Archive (CID int auto_increment primary key, CourseName varchar(255) not null, Content text, Duration varchar(50));
CREATE TABLE Instructors_Archive (InstructorID int auto_increment primary key, Iname VARCHAR(255), email VARCHAR(255));
CREATE TABLE Students_Archive (SID INT PRIMARY KEY, SName VARCHAR(255), email VARCHAR(255));
CREATE TABLE Assessments_Archive (AID INT PRIMARY KEY, CID INT, AssessmentName VARCHAR(255), DueDate DATE);
CREATE TABLE Grades_Archive (GradeID INT PRIMARY KEY, AID INT, SID INT, Grade VARCHAR(10));
SELECT * FROM Courses;
SELECT * FROM Instructors;
SELECT * FROM Students;
SELECT * FROM Enrollments;
SELECT * FROM Instructors_Archive;