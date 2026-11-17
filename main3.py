from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict
class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float
    married: bool 
    allergies:List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age>60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def updated_insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print('Updated')

patient_info = {'name': 'Nitish', 'email': 'abc@hdfc.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 30, 'weight': 75.2, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '9477436634', 'emergency': '7464656566'}}
patient1 = Patient(**patient_info)

updated_insert_patient_data(patient1)