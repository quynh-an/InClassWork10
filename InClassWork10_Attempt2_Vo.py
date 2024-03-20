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
        self.credit_count = 0
        self.credit_limit = 16
        self.schedule = []
        self.elective_courses = ["EECE2540", "EECE3410", "PHYS4623", "PHYS4115", "BIOL1115"]
        
    def enroll(self, course):
        scheduling_conflict = 0
        if course.code not in self.enrolled_courses:
            if self.credit_count <= self.credit_limit:
                for i in self.schedule:
                    if i[0] == course.day and i[1] == course.time:
                        scheduling_conflict = 1
                    else:
                        scheduling_conflict = 0
                if scheduling_conflict == 0:
                    if course.add_student(self):
                        self.enrolled_courses.append(course.code)
                        if course.code in self.elective_courses:
                            print(f"{self.name} successfully enrolled in the elective {course.name}")
                        else:
                            print(f"{self.name} successfully enrolled in {course.name}")
                        self.credit_count = self.credit_count + course.num_credits
                    else:
                        print(f"Failed to enroll{self.name} in {course.name}: Course full.")
                else:
                    print(f"Cannot register for {course.code} due to a scheduling conflict for {course.day} at {course.time}")
                        
            else:
                print(f"{self.name} has reached the credit limit and cannot register for anymore courses.")  
        else:
            print(f"{self.name} is already in the course {course.name}.")
            
    def add_classes_taken(self, course):
       self.finished_courses.append(course)
       print(f"{self.name} has completed {course.code}.")
       
    def get_enrolled_courses(self):
        return self.enrolled_courses
    
    def check_requirements(self):
        

class ElectricalEngineering(Student):
    required_courses = ["EECE2140", "PHYS1151", "ENGW1101", "EECE2150"]
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

class Physics(Student):
    required_courses = ["PHYS1155", "PHYS1151", "ENGW1101", "PHYS2303"]
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

class ElectricalEngineering_and_Physics(ElectricalEngineering, Physics):
    def __init__(self, name, student_id):
        super().__init__(name,student_id)
        self.required_courses = list(set(ElectricalEngineering.required_courses + Physics.required_courses))
        
class Course:
    def __init__(self, code, name, num_credits, day, time, max_students):
        self.code = code
        self.name = name
        self.num_credits = num_credits
        self.day = day
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
            class_time = (self.day, self.time)
            student.schedule.append(class_time)
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
jane = ElectricalEngineering("Jane Doe", 10002)
BIOL1115 = Course("BIOL1115", "General Biology 1 for Engineers", 4, "Monday", "8:00", 60)
PHYS1151 = Course("PHYS1151", "Physics 1 for Engineers", 4, "Monday", "11:45", 40) 
ENGW1101 = Course("ENGW1101", "First Year Writing", 4, "Monday", "11:45", 30)
PHYS1155 = Course("PHYS1155", "Physics 2 for Engineers", 4, "Tuesday", "9:50", 35)
PHYS1155.add_prerequisites(PHYS1151)
PHYS2303 = Course("PHYS2303", "Modern Physics", 4, "Wednesday", "2:50", 25)
PHYS2303.add_prerequisites(PHYS1155)
PHYS4623 = Course("PHYS4623", "Medical Physics", 4, "Wednesday", "11:45", 15)
EECE2140 = Course("EECE2140", "Computing Fundamentals for Engineers", 4, "Wednesday", "11:45", 35)

# =============================
def main():
    # Task 1: Enroll in course for single major
    jane.enroll(EECE2140)
    jane.enroll(ENGW1101)
    
    # Task 2: Enroll in course for double major
    rachel.enroll(PHYS1151)
    
    # Task 3: Elective
    jane.enroll(BIOL1115)
    
    # Task 3:
    jane.enroll(PHYS1151)

main()