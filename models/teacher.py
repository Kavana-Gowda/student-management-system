class Teacher:
    def __init__(self, name, gender, address, mobile, joining_date):
        self.name = name
        self.gender = gender
        self.address = address
        self.mobile = mobile
        self.joining_date = joining_date

    def to_tuple(self):
        return (
            self.name,
            self.gender,
            self.address,
            self.mobile,
            self.joining_date
        )