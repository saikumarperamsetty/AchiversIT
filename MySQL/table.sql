-- How to create Table in MySQL?
CREATE TABLE Student(
    StudentID INT Primary Key,
    StudentName Varchar(50),
    DateOfBirth DATE
);
CREATE TABLE Course(
    CourseID INT Primary Key,
    CourseName Varchar(50),
    Credits INT
);
CREATE TABLE Enrolment(
    EnrolmentID INT Primary Key,
    StudentID INT,
    CourseID INT,
    EnrolmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES  Course(CourseID)
);