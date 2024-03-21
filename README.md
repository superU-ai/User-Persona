# User Persona Identification

## Overview
This tool is designed to identify the persona of a user based on their conversations or statements. By analyzing the text, it extracts and identifies key aspects of a user's persona, such as age, gender, profession, hobbies, relationship status, and city.

## Installation

### Step 1: Clone the Repository
First, clone the repository to your local machine using the following command:

```
git clone <repository-url>
```
Replace `<repository-url>` with the actual URL of the repository.

### Step 2: Install Dependencies
Navigate into the cloned repository directory and install the required Python package (`openai`):

```
pip install openai
```

## Setting Up Your OpenAI API Key
To use this tool, you will need an API key from OpenAI. Once you have your API key, you can set it in your code like this:

```python
# test.py
openai.api_key = 'YOUR_API_KEY_HERE'
```

## Usage
Here's a simple example to get you started with the User Persona Identifier:

1. Import the necessary modules and set your OpenAI API key:

```python
# test.py

from userpersona_using_openai import UserPersonaIdentifier
import openai
openai.api_key = 'YOUR_API_KEY_HERE'
```

2. Create an instance of `UserPersonaIdentifier` and pass in the `openai` module:

```python
conversation_analyzer = UserPersonaIdentifier(openai)
```

3. Define a list of statements or conversation snippets from the user:

```python
User_Msgs = [
    'how are you doing today',
    'what do you weld ? houses ?',
    'how does that feel for you',
    'i watch kids for a living	i come from a large family .',
    'i want candy .',
    'my wedding is set for april 11 .	i do not travel .',
    'i handle cash .',
    'i need to educate myself more .'
]
```

4. Analyze the conversation and print the results:

```python
result = conversation_analyzer.analyze_conversation(User_Msgs)
print(result)
```

This will output the identified persona attributes based on the provided conversation snippets.

## Note
The accuracy of the persona identification depends on the quality and quantity of the conversation data provided. Ensure that the conversations are representative of the user's typical communication style for the best results.
