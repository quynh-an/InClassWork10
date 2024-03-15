#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:44:02 2024

@author: tandyllc
"""

class Course:
    def __init__(self, code, name, num_credits, time, max_students):
        self.code = code
        self.name = name
        self.num_credits = num_credits
        self.time = time
        self.max_students = max_students
        self.students_enrolled = []
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
        
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.course_taken = []
        
