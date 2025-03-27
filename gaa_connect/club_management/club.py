import uuid


class Club:
    def __init__(self, name, address, county, province, email, password, football=False, hurling=False):
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.county = county
        self.province = province
        self.email = email
        self.password = password  # In a real-world app, hash this password
        self.football = football
        self.hurling = hurling

    def __str__(self):
        sports = []
        if self.football:
            sports.append("Gaelic Football")
        if self.hurling:
            sports.append("Hurling")
        sports_played = " & ".join(sports) if sports else "None"

        return (f"Club ID: {self.id}\n"
                f"Club: {self.name}\n"
                f"Address: {self.address}\n"
                f"County: {self.county}\n"
                f"Province: {self.province}\n"
                f"Email: {self.email}\n"
                f"Sports Played: {sports_played}")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "county": self.county,
            "province": self.province,
            "email": self.email,
            "password": self.password,  # This should be hashed before storing in a real app
            "football": self.football,
            "hurling": self.hurling,
        }