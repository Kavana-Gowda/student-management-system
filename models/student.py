class Student:
    def __init__(self, name, age, gender, parent_name,
                 address, mobile, school_details, year):
        self.name = name
        self.age = age
        self.gender = gender
        self.parent_name = parent_name
        self.address = address
        self.mobile = mobile
        self.school_details = school_details
        self.year = year

    def to_tuple(self):
        return (
            self.name,
            self.age,
            self.gender,
            self.parent_name,
            self.address,
            self.mobile,
            self.school_details,
            self.year
        )