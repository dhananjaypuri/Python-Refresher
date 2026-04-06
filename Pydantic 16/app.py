from pydantic import BaseModel , Field , field_validator , model_validator
from typing import List , Annotated , Optional , Set

class Address(BaseModel):
    pin: str
    city: str = None
    country: str

class User(BaseModel):
    id : int
    name: str
    skills: List[str] = Field(default=["AI"])
    username: str
    password: str
    age: int
    gaurdian: str = None
    address: Address

    @field_validator("password")
    def check_pass(cls, v):
        print(v.isalnum());
        if len(v) < 8:
            raise ValueError("Password should not be less than 8 characters. ");
        elif (len(v) > 8) and (v.isdigit() or v.isalpha()):
            raise ValueError("Password is not alphanumeric ");
        elif (len(v) > 8) and (not v.isalnum()):
            raise ValueError("Password is not alphanumeric ");
        return v
    
    @field_validator("skills")
    def check_unique_skills(cls, v):
        new = set();
        for sk in v:
            new.add(sk);
        v = list(new)
        return v;

    @field_validator("address")
    def check_address(cls, v):
        
        if v.city == None:
            v.city = "New Delhi";
        if v.country.lower() == "india":
            if len(v.pin)<6:
                raise ValueError("Pincode lenght should not be less than 6 digits as country is india .");

        return v;

    @model_validator(mode="after")
    def check_gaurdian(self):
        if self.age < 18 and (self.gaurdian == None or self.gaurdian == ""):
            raise ValueError("Gaurdian name is required");
        return self;

user = User(id="1", name="Ajay", username= "ajay.aj",age= 17, skills=["AI", "ML", "AI"], password="1212345w5666", address = Address( country="India", pin="110018"));

print(type(user.id));
print(user.id);
print(user.name);
print(user.skills);
print(user.password.isalnum());
print(user.address);

print(user.model_dump());
