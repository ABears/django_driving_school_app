from rolepermissions.roles import AbstractUserRole

class Administrator(AbstractUserRole):
    available_permissions = {
        'create_secretary_account': True,
        'read_secretary_account': True,
        'edit_secretary_account': True,
        'delete_secretary_account': True,
        'create_student_account': True,
        'read_student_account': True,
        'edit_student_account': True,
        'delete_student_account': True,
        'create_instructor_account': True,
        'read_instructor_account': True,
        'edit_instructor_account': True,
        'delete_instructor_account': True,
        'read_student_profil': True,
        'create_course_hour': True,
        'create_all_appointement': True,
        'read_all_appointement': True,
        'edit_all_appointement': True,
        'delete_all_appointement': True,
        'read_driving_school_planning': True
    }

class Secretary(AbstractUserRole):
    available_permissions = {
        'create_student_account': True,
        'read_student_account': True,
        'edit_student_account': True,
        'delete_student_account': True,
        'create_instructor_account': True,
        'read_instructor_account': True,
        'edit_instructor_account': True,
        'delete_instructor_account': True,
        'read_student_profil': True,
        'create_course_hour': True,
        'create_all_appointement': True,
        'read_all_appointement': True,
        'edit_all_appointement': True,
        'delete_all_appointement': True,
        'read_driving_school_planning': True
    }
    
class Instructor(AbstractUserRole):
    available_permissions = {
        'create_appointement': True,
        'read_appointement': True,
        'edit_appointement': True,
        'delete_appointement': True,
        'read_own_student_profil': True
    }

class Student(AbstractUserRole):
    available_permissions = {
        'read_appointement': True,
        'create_appointement': True
    }