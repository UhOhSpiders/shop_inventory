class Merchant:

    def __init__(self, merchant_name, ethics, morals, email, id = None):
        self.merchant_name = merchant_name
        self.ethics = ethics
        self.morals = morals
        self.email = email
        self.id = id

        
    def get_advice(self, ethics, morals):
        advice_dict = {
    "Chaotic Evil": "Chaotic evil advice",
    "Chaotic Good": "Chaotic good advice",
    "Chaotic Neutral": "Chaotic neutral advice",
    "Neutral Evil": "Neutral evil advice.",
    "Neutral Good": "Neutral good advice.",
    "Neutral Neutral": "True neutral advice.",
    "Lawful Evil": "Lawful eveil advice",
    "Lawful Good": "Lawful good advice.",
    "Lawful Neutral": "Lawful neutral advice."
}
        if (ethics + " " + morals) in advice_dict:
            return advice_dict[ethics + " " + morals]
        else:
            return "Good luck!"