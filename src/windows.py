from whitakers_words.parser import Parser

def getInfo(word):
    parser = Parser()
    word = parser.parse(word)
    definitions = word.forms[0].analyses[list(word.forms[0].analyses.keys())[0]].lexeme.senses
    inflections = word.forms[0].analyses[list(word.forms[0].analyses.keys())[0]].inflections
    data = []
    for inf in inflections:
        info = {}
        info["wordType"] = inf.wordType.value
        features = {}
        for feature in inf.features.keys():
            features[feature] = inf.features[feature].value
        info["features"] = features
        data.append(info)

    return data, definitions

def formatStr(word, data, definitions):
    final_str = f"Definitions For {word.capitalize()}: {', '.join(definitions)}\n\n"
    for form in data:
        form_str = ""
        form_str += f"Word Type: {form['wordType']}\n"
        for feature in form["features"].keys():
            form_str += f"{feature}: {form['features'][feature]}\n"
        final_str += form_str + "\n"

    return final_str

if __name__ == "__main__":
    while True:
        try:
            word = input("Enter your word disregarding long marks: ")
            data, definitions = getInfo(word.strip())
            response = formatStr(word.strip(), data, definitions)
            print(f"\nData on Form(s)\n\n{response}")
        except:
            print("\nUnkown Word or Form\n\nThe word that you requested was invalid or uncatalogued\n\n")