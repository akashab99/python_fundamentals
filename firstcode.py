def sentence_maker(phrase):
    questions = ("how" "what" "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(questions):
        return "{}?".format(capitalized)
    else:
        return"{}.".format(capitalized)

results = []
while True:
    user_input = input("Say somethng: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))


print("".join(results))
