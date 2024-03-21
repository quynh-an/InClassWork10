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
        self.courses_taken = []
        self.enrolled_courses = []
        self.credit_count = 0
        self.credit_limit = 16
        self.schedule = []
        
    def enroll(self, course):
        scheduling_conflict = 0
        if course.code not in self.enrolled_courses:
            if self.credit_count < self.credit_limit:
                for i in self.schedule:
                    if i[0] == course.day and i[1] == course.time:
                        scheduling_conflict = 1
                    else:
                        scheduling_conflict = 0
                if scheduling_conflict == 0:
                    success_course_add = course.add_student(self)
                    if success_course_add == 3:
                        self.enrolled_courses.append(course.code)
                        if course.code in self.elective_courses:
                            print(f"{self.name} successfully enrolled in the elective {course.name}")
                            print(" ")
                        else:
                            print(f"{self.name} successfully enrolled in {course.name}")
                            print(" ")
                        self.credit_count = self.credit_count + course.num_credits
                    elif success_course_add == 2:
                        print(f"Failed to enroll {self.name} in {course.name}: Prerequisite Courses Not Met.")
                        print(" ")
                    else:
                        print(f"Failed to enroll {self.name} in {course.name}: Course full.")
                        print(" ")
                else:
                    print(f"Trying to enroll {self.name} into {course.code}...")
                    print(f"Cannot register for {course.code} due to a scheduling conflict for {course.day} at {course.time}")
                    print(" ")
            else:
                print(f"{self.name} has reached the credit limit and cannot register for anymore courses.")  
                print(" ")
        else:
            print(f"{self.name} is already in the course {course.name}.")
            print(" ")
            
    def add_classes_taken(self, course):
       self.finished_courses.append(course)
       print(f"{self.name} has completed {course.code}.")
       
    def get_enrolled_courses(self):
        return self.enrolled_courses
    
    def check_requirements(self):
        remaining_courses = self.required_courses
        for course in self.enrolled_courses:
            if course in remaining_courses:
                remaining_courses.remove(course)
        for course in self.courses_taken:
            if course in remaining_courses:
                remaining_courses.remove(course)
        return remaining_courses

class ElectricalEngineering(Student):
    required_courses = ["EECE2140", "PHYS1151", "ENGW1101", "EECE2150"]
    elective_courses = ["EECE2540", "EECE3410", "BIOL1107"]
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

class Physics(Student):
    required_courses = ["PHYS1155", "PHYS1151", "ENGW1101", "PHYS2303"]
    elective_courses = ["PHYS4623", "PHYS4115", "BIOL1107"]
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        
class Biology(Student):
    required_courses = ["BIOL1107", "BIOL2299", "ENGW1101", "BIOL2301"]
    elective_courses = ["EEMB2302", "PHYS4115", "IE2140"]
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        
class Ecology(Biology, Student):
    required_courses = list(set(Biology.required_courses + ["EEMB2290", "EEMB3455", "EEMB3460", "EEMB5130"]))
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

class Genetics(Biology, Student):
    required_courses = list(set(Biology.required_courses + ["BIOL3419.", "BIOL5583" , "BIOL5591"]))
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

# MuMultiple Inheritance
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
        full = 1
        no_prereq = 2
        all_set = 3
        if len(self.enrolled_students) < self.max_students:
            print(f"Enrolling {student.name} in {self.name}...")
            print(" ")
            if self.prereqs == []:
                self.enrolled_students.append(student.name)
                class_time = (self.day, self.time)
                student.schedule.append(class_time)
                return all_set
            else:
                for course_code in self.prereqs:
                    print(f"Checking if {student.name} finished {course_code}...")
                    print(" ")
                    if student.courses_taken == []:
                        print(f"{student.name} does not fulfill prerequisites for the {self.code}.")
                        print(" ")
                        return no_prereq
                    else:
                        for finished_course in student.courses_taken:
                            if finished_course.code == course_code:
                                self.enrolled_students.append(student.name)
                                print(f"{student.name} meets the prerequisites for {self.name}.")
                                print(" ")
                                class_time = (self.day, self.time)
                                student.schedule.append(class_time)
                                return all_set
                            else:
                                print(f"{student.name} does not fulfill prerequisites for the {self.code}.")
                                print(" ")
                                return no_prereq
        else:
            return full
        
    
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
frank = Biology("Frank Johnson", 10003)
ryan = Physics("Ryan Vu", 10004)
BIOL1107 = Course("BIOL1107", "Foundations of Biology", 4, "Monday", "8:00", 60)
PHYS1151 = Course("PHYS1151", "Physics 1 for Engineers", 4, "Monday", "11:45", 40) 
ENGW1101 = Course("ENGW1101", "First Year Writing", 4, "Monday", "11:45", 30)
PHYS1155 = Course("PHYS1155", "Physics 2 for Engineers", 4, "Tuesday", "9:50", 35)
PHYS1155.add_prerequisites(PHYS1151)
PHYS2303 = Course("PHYS2303", "Modern Physics", 4, "Wednesday", "2:50", 25)
PHYS2303.add_prerequisites(PHYS1155)
PHYS4623 = Course("PHYS4623", "Medical Physics", 4, "Wednesday", "11:45", 15)
EECE2140 = Course("EECE2140", "Computing Fundamentals for Engineers", 4, "Wednesday", "11:45", 35)
MATH1341 = Course("MATH1341", "Calculus 1 for Engineers", 4, "Friday", "11:45", 30)

# =============================
def main():
    # Task 1: Enroll in course for single major
    jane.enroll(EECE2140)
    
    # Task 2: Enroll in course for double major
    print("The requirements for Electrical Engineering are:")
    print(ElectricalEngineering.required_courses)
    print(" ")
    print("The requirements for Physics are:")
    print(Physics.required_courses)
    print(" ")
    print("As a dual major, these are the classes that Rachel is required to take:")
    print(rachel.required_courses)
    print(" ")
    rachel.enroll(PHYS1151)
    print(" ")
    print("Rachel is currently enrolled in:")
    print(rachel.enrolled_courses)
    print(" ")
    print("Rachel has these remaining requirements:")
    print(rachel.check_requirements())
    print(" ")
    
    # Task 3: Elective
    jane.enroll(BIOL1107)
    
    # Task 4: Time Conflict
    jane.enroll(PHYS1151)
    
    # Task 5: Prerequisite Check
    jane.enroll(PHYS2303)
    
    # Task 6: Credit Hour Limit
    jane.enroll(ENGW1101)
    jane.enroll(MATH1341)
    print("Jane now has this many credits:", jane.credit_count)
    print(" ")
    
    # Task 7 Elective vs Requirement
    frank.enroll(BIOL1107)
    print("Frank still has these to do:")
    print(frank.check_requirements())
    print(" ")
    ryan.enroll(BIOL1107)
    print("Ryan still has these classes to take for his major:")
    print(ryan.check_requirements())
    print(" ")
    
    # Hierarchical Inheritance
    madison = Ecology("Madison Harris", 10005)
    print("These are Madison's required courses:")
    print(madison.required_courses)
    print(" ")
    rebecca = Genetics("Rebecca Turner", 10006)
    print("These are Rebecca's required courses:")
    print(rebecca.required_courses)

main()