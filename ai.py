from google import genai
ai =genai.Client(api_key="AIzaSyBhR_pfAzOQoXh7seRsdefYUs1PoduqZXE")
while True:
	q=input("Question: ")
	ans = ai.models.generate_content(model="gemini-2.5-flash",contents=q)
	print("ANSWER:",ans.text)