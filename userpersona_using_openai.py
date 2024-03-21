import json
import openai

class UserPersonaIdentifier:
    # Initializing OpenAI credentials
    def __init__(self, openai):
        openai = openai

    # Generating prompt from the input list
    def prompt_gen(self, list_to_send):
        prompt = f'''I am giving you a list, which contain statements made by a person. Here are the statements made {list_to_send}.
          I want you to deduce the following from the conversation return the following in JSON format and if something is missing then return Nan in that field:'''+'''
          {age: (Give me ONLY the number if the information is given or can be derived, else give "Nan"),
          gender: (Give ONLY male or female if the information is given or can be derived, else give "Nan"),
          city: (Give ONLY city name if the information is given or can be derived, else give "Nan"),
          profession: (Give ONLY profession name if the information is given or can be derived, else give "Nan"),
          relationship status: (Give ONLY Relationship or single if the information is given or can be derived, else give "Nan"),
          interests: (Give an array of interests if the information is given or can be derived, else give "Nan"),
          name: (Give the name of the user if the information is given or can be derived, else give "Nan"),
          email: (Give the email of the user if the information is given or can be derived, else give "Nan"),
          phone number: (Give the phone number of the user if the information is given or can be derived, else give "Nan")}.
          Ignore all other information, ONLY RETURN JSON.'''
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

    # Converting the output string from OpenAI's response to  JSON
    def analyze_conversation(self, list_to_send):
        response_openai = self.gpt_func(list_to_send)
        start_index = response_openai.find('{')
        end_index = response_openai.rfind('}') + 1
        response_openai_str = response_openai[start_index:end_index]
        try:
            # print(response_openai_str)
            response_to_return = json.loads(response_openai_str)
            return response_to_return
        except:
            return "Error decoding JSON"
