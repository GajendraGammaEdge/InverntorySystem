import google.generativeai as genai

genai.configure(api_key="AIzaSyB3xfoT6L9UBCdjpV3wtPfGBkjH0teHR_c")
# model = genai.GenerativeModel('gemini-1.5-flash')
model1 = genai.get_model('gemini-1.5-flash')
# model = genai.GenerativeModel('gemini-1.5-flash')

def getting_output_openai(te):
       response = model1.generate_content(te)
       return response.text

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break
    t = getting_output_openai(prompt)
    print("Gemini:", t)
