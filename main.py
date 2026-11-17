from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give the name of the Patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False, description='Is the Patient married or not')]
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

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

patient_info = {'name': 'Nitish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1234', 'age': 30, 'weight': 75.2, 'contact_details': {'phone': '9477436634'}}
patient1 = Patient(**patient_info)

updated_insert_patient_data(patient1)