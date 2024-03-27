from userpersona_using_openai import UserPersonaIdentifier
import openai

# Example usage:
openai.api_key = ""
conversation_analyzer = UserPersonaIdentifier(openai)
User_Msgs = ['i love skating', "i won the women's skating championship last year. my parents do not know that i am . . . homosexual.", 'i am married', "i watch kids for a living"]#, "i hate blue shirts",  'my parents do not know that i am . . . homosexual .']
result = conversation_analyzer.analyze_conversation(User_Msgs)
print(result)