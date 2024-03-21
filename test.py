from userpersona_using_openai import UserPersonaIdentifier
import openai

# Example usage:
openai.api_key = ''
conversation_analyzer = UserPersonaIdentifier(openai)
User_Msgs = ['how are you doing today', 'what do you weld ? houses ?', 'how does that feel for you', 'i watch kids for a living\ti come from a large family .', 'i want candy .', 'my wedding is set for april 11 .\ti do not travel .', 'i handle cash .', 'i need to educate myself more .']
result = conversation_analyzer.analyze_conversation(User_Msgs)
print(result)