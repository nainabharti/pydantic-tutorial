from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict
class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int        
    height: float   #mtrs
    weight: float   #kgs
    married: bool 
    allergies:List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def updated_insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print('BMI: ', patient.calculate_bmi)
    print('Updated')

patient_info = {'name': 'Nitish', 'email': 'abc@hdfc.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 30, 'height': 1.72, 'weight': 75.2, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '9477436634', 'emergency': '7464656566'}}
patient1 = Patient(**patient_info)

updated_insert_patient_data(patient1)