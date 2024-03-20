#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:06:19 2024

@author: tandyllc
"""

class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.course_taken = []
        self.enrolled_courses = []
        credit_limit = 16
        
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

class Major(Student):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        elective_courses = ["EECE2540", "EECE3410", "PHYS4623", "PHYS4115"]
        pass

class ElectricalEngineering(Major):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.required_courses = ["EECE2140", "PHYS1151"]

class Physics(Major):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.required_courses = ["PHYS1151", "PHYS2303"]

class ElectricalEngineering_and_Physics(ElectricalEngineering, Physics):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        EE = ElectricalEngineering(name, student_id)
        physics_major = Physics(name, student_id)
        self.required_courses = list(set(EE.required_courses + physics_major.required_courses))
        
class Course:
    def __init__(self, code, name, num_credits, day, time, max_students):
        self.code = code
        self.name = name
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



# =============================
rachel = ElectricalEngineering_and_Physics("Rachel Smith", 10001)
PHYS4623 = Course("PHYS4623", "Medical Physics", 4, "Wednesday", "11:45", 25)
print (rachel.required_courses)
