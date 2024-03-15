#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:44:02 2024

@author: tandyllc
"""

class Course:
    def __init__(self, code, name, num_credits, time):
        self.code = code
        self.name = name
        self.num_credits = num_credits
        self.time = time
        self.students_enrolled = []
        self.prereqs = []
        
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.course_taken = []