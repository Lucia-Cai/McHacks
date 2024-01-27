import openai
# import openai as oa
client = openai.OpenAI(
	api_key='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'
)

def comp(PROMPT, MaxToken=500, outputs=3): 
	# using OpenAI's Completion module that helps execute 
	# any tasks involving text 
	response = client.chat.completions.create( 
		#messages=PROMPT,
		model="gpt-3.5-turbo-1106", 
		messages=[{"role": "user", "content": PROMPT}],
		max_tokens=MaxToken
	) 
	# creating a list to store all the outputs 
	
	output = response.choices[0].message.content 
	return output


	
m = comp("give me the first 10 digits of pi", MaxToken=50, outputs=1)
print(m)





	




