#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:44:02 2024

@author: tandyllc
"""

class Student():
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.course_taken = []
        self.major = major
        self.enrolled_courses = []
        
    def enroll(self, course):
        if course.add_student(self):
            self.enrolled_courses.append(course.code)
            print(f"{self.name} successfully enrolled in {course.name}")
        else:
            print(f"Failed to enroll{self.name} in {course.name}: Course full.")
            
    def add_classes_taken(self, course):
       self.finished_courses.append(course)
       print(f"{self.name} has completed {course.code}.")
       
    def get_enrolled_courses(self):
        return self.enrolled_courses
    
    
class DualMajorStudent(Student):
    def __init__(self, name, student_id, major1, major2):
        super().__init__(name, student_id, major1)
        self.major2 = major2
        
    def enroll(self, course):
        if course.major_requirement == self.major or course.major_requirement == self.major2:
            if course.add_student(self):
                self.enrolled_courses.append(course.code)
                print(f"{self.name} successfully enrolled in {course.name}")
            else:
                print(f"Failed to enroll {self.name} in {course.name}: Course full.")
        else:
            print(f"Failed to enroll {self.name} in {course.name}: Course major requirement not met.")
        
class Course:
    def __init__(self, code, name, major_requirement, num_credits, day, time, max_students):
        self.code = code
        self.name = name
        self.major_requirement = major_requirement
        self.num_credits = num_credits
        self.time = time
        self.max_students = max_students
        self.enrolled_students = []
        self.prereqs = []
        
    def add_student(self, student):
        if len(self.enrolled_students) < self.max_students:
            print(f"Enrolling {student.name} in {self.name}")
            for course_code in self.prereqs:
                print(f"Checking if {student.name} finished {course_code}")
                for finished_course in student.finished_courses:
                    if finished_course.code == course_code:
                        self.enrolled_students.append(student.name)
                        print(f"{student.name} meets the prerequisites for {self.name}.")
            if self.prereqs == []:
                self.enrolled_students.append(student.name)
            return True
        else:
            return False
    
    def is_full(self):
        return len(self.enrolled_students) >= self.max_students
    
    def add_prerequisites(self, prereq_course_code):
        self.prereqs.append(prereq_course_code.code)
        
    def get_prerequisites(self):
        return self.prereqs
    
    def get_enrolled_students(self):
        return self.enrolled_students

# ==============================================================
def main():
    EECE2140 = Course("EECE2140", "Computing Fundamentals for Engineers", "Electrical Engineering", 4, "Wednesday", "11:45", 35)
    PHYS1151 = Course("PHYS1151", "Physics 1 for Engineers", "Physics", 4, "Monday", "11:45", 40) 
    jane = Student("Jane Doe", 10001, "Electrical Engineering")
    jane.enroll(EECE2140)
    print(jane.get_enrolled_courses())
    rachel = DualMajorStudent("Rachel Smith", 10002, "Electrical Engineering", "Physics")
    rachel.enroll(PHYS1151)
    rachel.enroll(EECE2140)
    print(PHYS1151.get_enrolled_students())
    print(rachel.get_enrolled_courses())
    print(EECE2140.get_enrolled_students())

    
    
    
main()