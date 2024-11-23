from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import INTENT, ENTITIES
from rasa.nlu.model import Interpreter

# Load the Rasa interpreter (trained model directory)
interpreter = Interpreter.load("path/to/your/trained/model")  # Replace with your Rasa model path

def parse_user_input(input_text):
    """
    Parses the user input using Rasa NLU to extract intents and entities.

    Args:
        input_text (str): The raw user input text.

    Returns:
        dict: A dictionary containing the detected intent and extracted entities.
    """
    # Use the Rasa interpreter to parse the input text
    result = interpreter.parse(input_text)
    
    # Extract intent and entities
    intent = result.get(INTENT, {}).get("name", "unknown")
    entities = {
        entity["entity"]: entity["value"]
        for entity in result.get(ENTITIES, [])
    }
    
    return {"intent": intent, "entities": entities}
