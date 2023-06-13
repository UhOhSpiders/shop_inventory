ethics = 'Neutral'
morals = 'Neutral'

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
def get_advice(ethics, morals):
    return advice_dict[ethics + " " + morals]

print(get_advice(ethics, morals))
# if ethics == 'Chaotic':
#     ethics_advice = "chaotic advice "
# if ethics == 'Neutral':
#     ethics_advice = "neutral advice "
# if ethics == "Lawful":
#     ethics_advice = "lawful advice "
# if morals == 'Evil':
#     morals_advice = "evil advice"
# if morals == "Good":
#     morals_advice = "good advice"
# if morals == "Neutral":
#     morals_advice = "neutral advice"
# print(ethics_advice + morals_advice)

if ethics == 'Chaotic':
    if morals == 'Evil':
        advice = "chaotic evil advice"
    if morals == "Good":
        advice = "chaotic good advice"
    if morals == "Neutral":
        advice = "chaotic neutral advice"
if ethics == 'Neutral':
    if morals == 'Evil':
        advice = "neutral evil advice"
    if morals == "Good":
        advice = "neutral good advice"
    if morals == "Neutral":
        advice = "true neutral"
if ethics == "Lawful":
    if morals == 'Evil':
        advice = "lawful evil advice"
    if morals == "Good":
        advice = "lawful good advice"
    if morals == "Neutral":
        advice = "lawful neutral advice"
print(advice)

