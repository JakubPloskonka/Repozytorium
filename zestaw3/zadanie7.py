from dataclasses import dataclass, asdict
import json

@dataclass
class Person:
    first_name: str
    last_name: str
    address: str
    postal_code: str
    pesel: str

    def save_to_json(self, file_path):
        """Saves the object to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump(asdict(self), file, indent=4)

    @classmethod
    def load_from_json(cls, file_path):
        """Loads an object from a JSON file."""
        with open(file_path, 'r') as file:
            data = json.load(file)
            return cls(**data)

# Example usage
if __name__ == "__main__":
    # Create a person object
    person = Person(
        first_name="John",
        last_name="Doe",
        address="123 Main Street",
        postal_code="00-123",
        pesel="12345678901"
    )

    # Save the object to a JSON file
    json_file = "person.json"
    person.save_to_json(json_file)

    print(f"Data saved to {json_file}")

    # Load the object from the JSON file
    loaded_person = Person.load_from_json(json_file)
    print("Data loaded from JSON:")
    print(f"First Name: {loaded_person.first_name}")
    print(f"Last Name: {loaded_person.last_name}")
    print(f"Address: {loaded_person.address}")
    print(f"Postal Code: {loaded_person.postal_code}")
    print(f"PESEL: {loaded_person.pesel}")
