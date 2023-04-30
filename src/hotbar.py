from whitakers_words.parser import Parser
from rumps import *

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

@clicked('Testing')
def tester(sender):
    sender.state = not sender.state

class DEM(rumps.App):
    def __init__(self):
        super(DEM, self).__init__(type(self).__name__, menu=['Latin To English'])
        rumps.debug_mode(False)

    @clicked('Latin To English')
    def button(self, sender):
        # sender.title = 'Off' if sender.title == 'On' else 'On'
        message = Window(message="Enter Latin Text Here", default_text="").run()
        try:
            data, definitions = getInfo(message.text.strip())
            response = formatStr(message.text.strip(), data, definitions)
            rumps.alert(title="Data on Form(s)", message=response)
        except:
            rumps.alert(title="Unkown Word or Form", message="The word that you requested was invalid or uncatalogued")

if __name__ == "__main__":
    DEM().run()
