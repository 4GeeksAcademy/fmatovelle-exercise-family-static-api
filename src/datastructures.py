
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] =self._generateId()
        self._members.append(member)
        return(member)
    
    def delete_member(self, id):
        self._members = [member for member in self._members if member[id] != id ]
        return {"done", True}
    
    def get_member(self, id):
        member = next((member for member in self._members if member["id"] == id), None)
        return member
    def get_all_members(self):
        return self._members