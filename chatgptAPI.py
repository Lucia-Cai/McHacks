import openai
from pdf import extract_text_from_pdf

client = openai.OpenAI(
	api_key='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'
)

def comp(PROMPT, MaxToken=500, outputs=3): 
	response = client.chat.completions.create( 
		#messages=PROMPT,
		model="gpt-3.5-turbo-1106", 
		messages=[{"role": "user", "content": PROMPT}],
		max_tokens=MaxToken,
	) 
	
	output = response.choices[0].message.content
	return output


def text_to_dict(text):
	qa = {}
	flashcard_lst = m.strip().split('\n\n')
	for i in range(len(flashcard_lst)):
		qa_lst = flashcard_lst[i].split('\n')
		q = qa_lst[0].replace(f'Question {i+1}: ', '')
		a = qa_lst[1].replace(f'Answer {i+1}: ', '')
		qa[q] = a
	return(qa)





input_text = extract_text_from_pdf('test.pdf')
prompt = '''Make 5 flashcard questions with the corresponding answers with the following text in the format
Question 1:
Answer 1: 
The text: ''' + input_text



# m = comp(prompt, MaxToken=500, outputs=1)
# print(m)


m = '''Question 1: What is the mycelium?
Answer 1: The mycelium is a network of thread-like structures hidden beneath the substrate, such as soil or wood, and is the true essence of the fungus.

Question 2: How do mushrooms reproduce?
Answer 2: Mushrooms reproduce through the production and dispersal of spores, which are released from the gills or pores under the mushroom cap.

Question 3: What is mycorrhizae?
Answer 3: Mycorrhizae is the symbiotic relationship between mushrooms and plants, in which the fungus aids the plant in nutrient absorption and the plant provides carbohydrates to the fungus.

Question 4: What is the ecological importance of mushrooms as decomposers?
Answer 4: Mushrooms break down complex organic compounds in dead plant and animal material, releasing essential nutrients back into the environment and contributing to nutrient cycling in ecosystems.

Question 5: What are some potential medicinal properties of mushrooms?
Answer 5: Some mushrooms, such as reishi and shiitake, are known for their potential immune-boosting, antiviral, and cholesterol-lowering properties, highlighting their potential applications in human health and well-being.'''


if __name__ == "__main__":
	a = text_to_dict(m)
	print(a)
	# returns a dict 
	# {'What is the mycelium?': 'The mycelium is a network of thread-like structures hidden beneath the substrate, such as soil or wood, and is the true essence of the fungus.', 
	# 'How do mushrooms reproduce?': 'Mushrooms reproduce through the production and dispersal of spores, which are released from the gills or pores under the mushroom cap.', 
	# 'What is mycorrhizae?': 'Mycorrhizae is the symbiotic relationship between mushrooms and plants, in which the fungus aids the plant in nutrient absorption and the plant provides carbohydrates to the fungus.', 
	# 'What is the ecological importance of mushrooms as decomposers?': 'Mushrooms break down complex organic compounds in dead plant and animal material, releasing essential nutrients back into the environment and contributing to nutrient cycling in ecosystems.', 
	# 'What are some potential medicinal properties of mushrooms?': 'Some mushrooms, such as reishi and shiitake, are known for their potential immune-boosting, antiviral, and cholesterol-lowering properties, highlighting their potential applications in human health and well-being.'}




	




