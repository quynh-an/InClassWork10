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

class ElectricalEngineering(Student):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.required_courses = ["EECE2140", "PHYS1151"]


class Physics(Student):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.required_courses = ["PHYS1151", "ENCP3000"]


class ElectricalEngineering_and_Physics(ElectricalEngineering, Physics):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.required_courses = list(set(ElectricalEngineering.required_courses + Physics.required_courses))
        
# =============================
rachel = ElectricalEngineering_and_Physics("Rachel Smith", 10001)
print (rachel.required_courses)
