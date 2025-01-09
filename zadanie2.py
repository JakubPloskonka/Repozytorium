import json

class Person:
    def __init__(self, first_name, last_name, address, postal_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel

    def to_dict(self):

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "postal_code": self.postal_code,
            "pesel": self.pesel
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            postal_code=data["postal_code"],
            pesel=data["pesel"]
        )

    def save_to_json(self, file_path):
        """Saves the object to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_json(cls, file_path):
        """Loads an object from a JSON file."""
        with open(file_path, 'r') as file:
            data = json.load(file)
            return cls.from_dict(data)

# Example usage
if __name__ == "__main__":
    # Create a person object
    person = Person(
        first_name="Jan",
        last_name="Kowalski",
        address="123 Czarnowiejska",
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
