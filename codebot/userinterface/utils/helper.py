from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path

# env_path = Path(__file__).resolve().parent / 'utils' / '.env'
load_dotenv()


GET_API_KEY = os.getenv('API_KEY')

def languages():
    lan = 'markup+css+clike+javascript+c+csharp+cpp+python+ruby+sql'
    lan_lits = lan.split('+')
    lan_lits.append('html')
    lan_lits = sorted(lan_lits)
    return lan_lits

def codecorrect(code, language, api_key=GET_API_KEY):
    api = api_key
    clent = Groq(api_key=api)
    chat = clent.chat.completions.create(
        messages=[
            {"role": "user",
            "content": f"Give only code. Return only the corrected code. Debug the following {language} code: {code}. Fix any errors and return the corrected version of the code without additional explanations or comments. Dp not includes." }],
        model="gemma2-9b-it",
    )
    respons = chat.choices[0].message.content
    return respons

def codegen(code, api_key=GET_API_KEY):
    api = GET_API_KEY
    clent = Groq(api_key=api)
    chat = clent.chat.completions.create(
        messages=[
            {"role": "user",
            "content": f"{code}" }],
        model="gemma2-9b-it",
    )
    respons = chat.choices[0].message.content
    return respons
