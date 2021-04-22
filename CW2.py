import os
from typing import List, Any


class Patient:
    firstName = 'Adham'
    lastName = 'Ramoun'
    patientID = 0
    appintmentslot = 0
    appointmentDay = 'Sunday'

    def __init__(self):
        self.patientID = 0

    def patientID_setter(self, id):
        self.patientID = id

    def firstName_setter(self, name):
        self.firstName = name

    def lastName_setter(self, name):
        self.lastName = name
        
    def appointmentDay_setter(self, day):
        self.appointmentDay = day

    def appintmentslot_setter(self, slot):
        self.appintmentslot = slot

    def firstName_getter(self):
        return self.firstName

    def lastName_getter(self):
        return self.lastName

    def appointmentDay_getter(self):
        return self.appointmentDay

    def appintmentslot_getter(self, number):
        return self.appintmentslot

    def patientID_getter(self):
        return self.patientID

    def display_patient_data(self):
        print(f'ID: {self.patientID}  Patient Name: {self.firstName} {self.lastName} Appintment day: {self.appointmentDay} at {self.appintmentslot}')


class doctor:
    firstName = 'First'
    lastName = 'Last'
    doctorID = 1
    NoOfPatients = 0
    NoOfDoctors = 0
    listOfPatients = []

    def __init__(self):
        self.doctorID = 0

    def firstName_setter(self,name):
        self.firstName = name

    def lastName_setter(self,name):
        self.lastName = name

    def NoOfPatients_setter(self, number):
        self.NoOfPatients = number

    def NoOfDoctors_setter(self, number):
        self.NoOfDoctors = number

    def doctorID_setter(self, id):
        self.doctorID = id

    def listOfPatients_setter(self, _list):
        self.listOfPatients = _list.copy()

    def firstName_getter(self):
        return self.firstName

    def lastName_getter(self):
        return self.lastName

    def doctorID_getter(self):
        return self.doctorID

    def NoOfPatients_getter(self):
        return self.NoOfPatients

    def NoOfDoctors_getter(self):
        return self.NoOfDoctors
        
    def Count_Week(self, number):
        print("There are total of ", NoOfPatients, " Appointment for the week")

    def returnPatient(self, _list, index):
        i = 0
        for Patient in _list:
            if index == i:
                return Patient
            i = i + 1

    def sortOnhour(self):
        _list = []
        _list = self.listOfPatients.copy()
        for i in range(len(_list)):
            min_idx = i
            for j in range(i + 1, len(_list)):
                min = self.returnPatient(_list, min_idx)
                a_min = self.returnPatient(_list, j)
                if min.appintmentslot > a_min.appintmentslot:
                    min_idx = j
            _list[i], _list[min_idx] = _list[min_idx], _list[i]

        return _list

    def sortOnName(self, name):
        arr = []
        arr = self.returnPatient.copy()
        n = self.NoOfPatients
        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                min = self.returnPatient(arr, min_index)
                a_min = self.returnPatient(arr, j)
                if name == 1:
                    if min.firstName > a_min.firstName:
                        min_index = j
                elif name == 2:
                    if min.lastName > a_min.lastName:
                        min_index = j


            if min_index != i:
                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index] = temp

        return arr

def main_menu():
    print('1. Sort the Patients Data'
          '2. Display appointments for Specefic day'
          '3. Calculate the number of appointments for the week'
          '4. Search for a patient'
          '5. Search for a doctor'
          '6. Search for an appointment'
          '7. Exit')

def sort_menu():
    print("1. Sort by appointment hour")
    print("2. Sort by first name ")
    print("3. Sort by last name ")

def patient_search_menu():
    print("1. Search for patient by ID")
    print("2. Search for patient by first name ")
    print("3. Search for patient by last name ")

def doctor_search_menu():
    print("1. Search for doctor by ID")
    print("2. Search for doctor by first name ")
    print("3. Search for doctor by last name ")

def appointment_search_menu():
    print("1. Search for appointment by appointment hour")
    print("2. Search for appointment by day")

def populate_doctor():
    doctors = []
    for i in range(NoOfDoctors):
        firstName = str(input("First Name of the Doctor: "))
        lastName = str(input("Last Name of the Doctor: "))
        doctor_id = str(input("Enter Doctor's ID: "))
        patients_number = int(input("Enter number of Patients : "))
        doc_patients = []

        doctor = doctors()
        doctor.doctorID_setter(doctorID)
        doctor.firstName_setter(firstName)
        doctor.lastName_setter(lastName)
        doctor.NoOfPatients_setter(patients_number)
        doctor.append(doctors)
    return doctor


def populate_patients(doctor, NoOfDoctors):
    patients = []
    branch_patients = []
    for i in range(NoOfDoctors):
        Patient.append(branch_patients)
        Patient[i].clear()

    for i in range(doctor[0].NoOfPatients_getter()):
        firstname = input("First name: ")
        lastname = input("Last name: ")
        patientID = str(input("Patient ID: "))
        appointment_slot = int(input("Appointment Hour: "))
        apoointment_day = input("Appointment day: ")

        Patient = patients()
        Patient.firstName_setter(firstname)
        Patient.lastName_setter(lastname)
        Patient.patientID_setter(patientID)
        Patient.appointmentDay_setter(apoointment_day)
        Patient.appointmentslot_setter(appointment_slot)
        patient[index].append(patients)

    for i in range(number_of_module):
        Doctor[i].listOfPatients_setter(patients[i])     #maybe an error

    return Doctor


if __name__ == '__main__':

    NoOfDoctors = int(input("Enter Number of Doctors: "))
    doctor = populate_doctor()
    NoOfPatients = int(input('Number of Patients for this doctor: '))
    for number in range(NoOfDoctors):
        doctor[number].NoOfPatients_setter(NoOfPatients)

    doctor = populate_patients(doctor, NoOfDoctors)

    _flag = True
    while _flag:
        flag = True
        for doc in range(NoOfDoctors):
            print(f'{doc + 1}: ID: {doctor[doc].doctorID_getter()} First Name: {doctor[doc].firstName_getter()} Last Name: {doctor[doc].lastName_getter()} ')

        print(f'{NoOfDoctors + 1 }: Close Program')
        doc_no = int(input('Choose The Doctor: '))

        if doc_no > 0 and doc_no <= NoOfDoctors:
            while flag:
                main_menu()
                option = int(input('Choose the option from above: '))
                if option == 2:
                    while True:
                        d = input("Enter the day to print data for: ")
                        for doc in range(NoOfPatients):
                            if patient[appointment_Day] == d:
                                print(f'{doc + 1}: ID: {doctor[doc].doctorID_getter()} First Name: {doctor[doc].firstName_getter()} Last Name: {doctor[doc].lastName_getter()} ')

                elif option == 7:
                    flag = False

        elif doc_no == NoOfDoctors + 1:
            _flag = False

os.system('cls')