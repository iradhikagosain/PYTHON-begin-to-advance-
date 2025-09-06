#else /finally
try:
    a=34/0
except Exception as e:
    print("error occurred",e)
#it will get executed when there will be no error in try except block
else:
    print("its correct")

finally:
    print("it get always executed")
    


#custom exceptions
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older!"):
        self.message = message
        super().__init__(self.message)

def verify_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise your custom exception
    return "Welcome!"

try:
    print(verify_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")