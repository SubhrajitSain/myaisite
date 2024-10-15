import google.generativeai as genai
from flask import *

genai.configure(api_key="AIzaSyAW5sMrTKYwyystY2A9kbyZQ9PlwjI02C0")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 10000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are a bot who is assigned the role of a AI webpage creator. YOU MUST FOLLOW THE PROMPTS EXACTLY. FOR EXAMPLE, IF YOU ARE ASKED TO GIVE A COLOR FOR CSS IN TEXT, YOU MUST, FOR EXAMPLE SAY 'darkred'. OR FOR HEXADECIMAL COLORS, FOR EXAMPLE, '#660000'. NOTHING ELSE SHOULD BE SAID BY YOU IF NOT ASKED TO SAY IT FOR CONTENT. YOU AMY ALSO BE ASKED FOR HEADINGS, PASSAGES, TEXTS, DATA, ETC, BUT IF YOU ARE ASKED FOR SOMETHING, YOU MUST ONLY SPECIFY THE ASKED STUFF AND NOTHING ELSE."
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

app = Flask(__name__)

@app.route('/')
def index():
    response1 = chat_session.send_message("Please specify a nice blue color. [AS HEXADECIMAL COLOR CODE FOR CSS]")
    response2 = chat_session.send_message("Please specify a dark blue color. [AS HEXADECIMAL COLOR CODE FOR CSS]")
    return render_template('index.html', header_footer_color=response1, body_color=response2)
