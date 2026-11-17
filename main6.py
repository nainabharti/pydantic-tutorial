from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Nitish', 'age': 30, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=['name', 'gender'])
temp1 = patient1.model_dump_json()
temp2 = patient1.model_dump(exclude={'address': ['state']})
temp3 = patient1.model_dump(exclude_unset=True)  #object banate time jo chizein set nhi ki gyi hai wo export nhi hogi
print(temp)
print(type(temp))
print(temp1)
print(type(temp1))
print(temp2)
print(temp3)