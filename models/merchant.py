class Merchant:

    def __init__(self, merchant_name, ethics, morals, email, id = None):
        self.merchant_name = merchant_name
        self.ethics = ethics
        self.morals = morals
        self.email = email
        self.id = id

        
    def get_advice(self, ethics, morals):
        advice_dict = {
    "Chaotic Evil": "This merchant cannot be trusted. Don't be afraid to call security and have them escorted from the premises.",
    "Chaotic Good": "This merchant has a heart of gold!",
    "Chaotic Neutral": "This merchant may offer some good trades, but a firm negotation strategy is recomended.",
    "Neutral Evil": "This merchant has a mysterious and shady track record. Remember the 7 steps covered in the sales negotiation training.",
    "Neutral Good": "This merchant is a nice.",
    "Neutral Neutral": "This merchant is incredibly reliable. Great for bulk-buying and wholesale deals.",
    "Lawful Evil": "This merchant is a slipery customer but their lack of moral compass alows them to get their hands on some valuable merchandise. This makes trading with them worthwhile, but be careful when it comes to signing any contracts.",
    "Lawful Good": "Play it by the book. They will leave at the first sign of funny business.",
    "Lawful Neutral": "This merchant does not have much of a sense of humour but if the correct paperwork is filled out then they'll be easy to work with."
}
        if (ethics + " " + morals) in advice_dict:
            return advice_dict[ethics + " " + morals]
        else:
            return "Good luck!"