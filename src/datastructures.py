
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]},

            {"id": 2,
             "first_name": "Jane",
             "last_name": last_name,
             "age": 35,
             "lucky_numbers": [10, 14, 3]},

            {"id": 7,
             "first_name": "Tommy",
             "last_name": last_name,
             "age": 5,
             "lucky_numbers": [1]}]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if ("first_name", "age", "lucky_numbers" in member):
            self._members.append(member)
            return "added"
        else:
            return "fail"

    def delete_member(self, id):
        for idx, member in enumerate(self._members):
            if id == member["id"]:
                self._members.pop(idx)
                return {"done": True}
        return "not found"

    def get_member(self, id):
        for member in self._members:
            if id == member["id"]:
                return member
        return "not found"

    def get_all_members(self):
        return self._members
