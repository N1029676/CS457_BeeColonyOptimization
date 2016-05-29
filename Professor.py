class Professor:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return self.name

    def get_rating(self):
        return self.rating

montgomery = Professor("Montgomery", 7)
andonie = Professor("Andonie", 7)
kovalerchuk = Professor("Kovalerchuk", 7)
davendra = Professor("Davendra", 7)
vajda = Professor("Vajda", 7)
harper = Professor("Harper", 7)
guerinoni = Professor("Guerinoni", 7)
abdulwahid = Professor("Abdul-Wahid", 7)
harrison = Professor("Harrison", 7)
lulofs = Professor("Lulofs", 7)
salter = Professor("Salter", 7)
schwing = Professor("Schwing", 7)
popescu = Professor("Popescu", 7)
unknown = Professor("Unknown", 5)
