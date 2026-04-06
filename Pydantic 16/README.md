# Pydantic Data Validation Example

This project demonstrates advanced data validation using **Pydantic**, a popular Python library for data parsing and validation using Python type annotations.

## Overview

The example showcases a `User` model with nested `Address` model, implementing various validation techniques to ensure data integrity.

## Key Components

### Models

#### Address Model
```python
class Address(BaseModel):
    pin: str
    city: str = None
    country: str
```
A nested model representing a user's address with:
- `pin`: Postal code (required)
- `city`: City name (optional, defaults to None)
- `country`: Country name (required)

#### User Model
```python
class User(BaseModel):
    id: int
    name: str
    skills: List[str] = Field(default=["AI"])
    username: str
    password: str
    age: int
    guardian: str = None
    address: Address
```
A comprehensive user model with:
- `id`: User identifier (integer)
- `name`: User's full name
- `skills`: List of skills (defaults to ["AI"])
- `username`: Login username
- `password`: Encrypted password (validated)
- `age`: User's age
- `guardian`: Required for users under 18
- `address`: Nested Address object

## Validators

### 1. Password Validator (`@field_validator`)
Validates password strength:
- Minimum length: 8 characters
- Must be alphanumeric
- Raises `ValueError` if validation fails

### 2. Skills Validator (`@field_validator`)
- Removes duplicate skills by converting to a set and back to a list
- Ensures unique skills in the list

### 3. Address Validator (`@field_validator`)
- Defaults city to "New Delhi" if not provided
- For Indian addresses (country="India"):
  - Enforces minimum pincode length of 6 digits

### 4. Guardian Validator (`@model_validator`)
- Operates on the entire model after individual field validation
- Requires a guardian name for users under 18 years old
- Raises `ValueError` if validation fails

## Usage Example

```python
user = User(
    id="1", 
    name="Ajay", 
    username="ajay.aj",
    age=17, 
    skills=["AI", "ML", "AI"],  # Duplicates will be removed
    password="1212345w5666", 
    address=Address(country="India", pin="110018")
)

# Access validated data
print(user.id)           # Output: 1
print(user.name)         # Output: Ajay
print(user.skills)       # Output: ['AI', 'ML'] (duplicates removed)
print(user.address)      # Output: Complete address object
print(user.model_dump()) # Output: Dictionary representation of the model
```

## Key Features Demonstrated

- **Type Hints**: Strong typing with Python annotations
- **Nested Models**: Address nested within User
- **Field Validators**: Validate individual fields
- **Model Validators**: Validate across multiple fields
- **Default Values**: Using `Field()` for complex defaults
- **Type Coercion**: Automatic type conversion (e.g., string "1" to int 1)
- **Error Handling**: Comprehensive validation error messages

## Running the Code

```bash
python app.py
```

This will create a User instance and print validation results along with the model's dictionary representation.

## Notes

- The example uses Pydantic v2 syntax with `@field_validator` and `@model_validator`
- Type hints include `List`, `Optional`, `Set`, and `Annotated` from `typing` module
- The `mode="after"` in `@model_validator` ensures it runs after all field validators
