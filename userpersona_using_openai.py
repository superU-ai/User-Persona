import json
import openai

class UserPersonaIdentifier:
    # Initializing OpenAI credentials
    def __init__(self, openai):
        openai = openai

    # Generating prompt from the input list
    def prompt_gen(self, inp_statement):
        prompt = f'''
            Here is a statement made by a user: {inp_statement}
            '''+'''
            I want you to deduce the following from the statement and give me a JSON:
            {age: (Give me ONLY the number if the information is given or can be derived),
            gender: {gender: (Give ONLY male or female if the information is given or can be derived), confidence_score: (On a scale of 1 to 5, tell me how confident you are in deciding the gender with 1 being least confident and 5 being most confident. GIVE ME ONLY THE NUMBER)}
            city: (Give me ONLY the city name if the information is given or can be derived),
            profession: (Give ONLY profession name if the information is given or can be derived),
            relationship status: (Give ONLY Single or Not Single if the information is given or can be derived),
            interests: (Read the statement properly and give the hobbies/interests if the information is given or can be derived)}.

            Ignore all other information, ONLY RETURN JSON IN THE FORMAT MENTIONED.'''
        return prompt

    # Function call to OpenAI's API
    def gpt_func(self, list_to_send):
        messages_L1 = [{"role": "system", "content":"You are a smart and helpful assistant.You make quick and smart decisions"}]
        message_a = {"role":"user","content":self.prompt_gen(list_to_send)}
        messages_L1.append(message_a)

        response = openai.chat.completions.create(
                temperature = 0.9,
                model="data-copilot-turbo-16k",
                messages=messages_L1)
        response_message = response.choices[0].message.content
        return response_message

    # Converting the output string from OpenAI's response to JSON
    def analyze_conversation(self, list_to_send):
        response_jsons = []
        for i in list_to_send:
            response_openai = self.gpt_func(i)
            start_index = response_openai.find('{')
            end_index = response_openai.rfind('}') + 1
            response_openai_str = response_openai[start_index:end_index]
            try:
                response_to_return = json.loads(response_openai_str)
                response_jsons.append(response_to_return)
            except:
                response_to_return=""
        json_to_return = self.get_updated_json(response_jsons)
        keys_to_ensure = ['age', 'gender', 'city', 'profession', 'relationship status', 'interests']
        for key in keys_to_ensure:
            if key not in json_to_return:
                if key == 'gender':
                    json_to_return[key] = {'gender': None, 'confidence_score': None}
                elif key == 'interests':
                    json_to_return[key] = []
                else:
                    json_to_return[key] = None

        return json_to_return
    
    # Checking the values of all JSONs generated
    def update_values(self, updated_values, data):
        for key, value in data.items():
            if isinstance(value, dict):
                if key not in updated_values:
                    updated_values[key] = {}
                self.update_values(updated_values[key], value)
            elif value not in ['', None, float('nan'),[]]:
                if key not in updated_values or updated_values[key] != value:
                    updated_values[key] = value

    # Function to select the final values of all JSONs to return
    def get_updated_json(self, response_jsons):
        updated_values = {}
        for json_obj in response_jsons:
            self.update_values(updated_values, json_obj)
        return updated_values
