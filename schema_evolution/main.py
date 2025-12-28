from pydantic import BaseModel, ValidationError

# This is our 'Contract' for the source data
class UserSchema(BaseModel):
    user_id: int
    email: str
    signup_date: str 
    # Imagine: 'is_active' is missing. 
    # If the source adds it, this schema ignores it (Head in the Sand).
    # If the source renames 'email' to 'user_email', this fails (Brick Wall).

def process_data(raw_input):
    try:
        validated_data = UserSchema(**raw_input)
        print("Schema valid. Proceeding to Lakehouse...")
    except ValidationError as e:
        # Trigger that 2 AM alarm!
        raise ValueError(f"CRITICAL: Schema mismatch detected! {e}")
    

if __name__ == "__main__":
    # Example normal payload
    incoming_data = {
        "user_id": 123,
        "email": "bob@ross.org",
        "signup_date": "2024-01-01"
    }
    process_data(incoming_data)
    
    # Example additional field (Head in the Sand)
    incoming_data = {
        "user_id": 456,
        "email": "diane@ross.org",
        "signup_date": "2025-01-01",
        "is_active": True
    }
    process_data(incoming_data)

    # Example missing/renamed field (Brick Wall)
    incoming_data = {
        "user_id": 789,
        "signup_date": "2026-01-01"
    }
    process_data(incoming_data)