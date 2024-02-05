Project Name: Finding Free alternatives Models to Open AI for Legal Tasks
Objective: The primary goal of this task is to investigate alternative free of cost models to OpenAI, such as Bard or any relevant open-source models, to showcase similar functionality to OpenAI without incurring costs.
Features to Implement:
1.	Researchbook Name Generation:
o	Description: Develop a mechanism to generate research book names based on legal queries. Use the model you found to achieve the desired responses. 
o	Examples 
▫	Query: "Siblings Murder"  
•	Research Book Name: " Analyzing Murder Cases: Relevant Judgments and Legal Insights "
▫	Query: " Cheque Bounce "  
•	Research Book Name: " Cheque Bounce Chronicles: Legal Perspectives and Summaries "


2.	Generating Enhanced Facts:
o	Description: Develop a mechanism to generate enhanced legal facts from the given facts. This involves transforming standard facts into more detailed and context-rich information. Use the model you found to achieve the desired responses.
o	Examples:
▫	Fact: "Loan pending with the bank."
•	Enhanced Fact: "A loan is pending with a bank."
▫	Fact: "Physical or mental torture."
•	Enhanced Fact: "The victim suffered from torture, whether physical or mental."
 
Approach:
My first approach was to research about available open-source and free large language models. I took help of chatgpt, bard and google search to search about it and selected few good models from those recommendations.
Secondly, I searched for from where I can obtain the model, how to implement the model for every of those model.
Then, I ran those code on my local machine and checked the output, compared with the desired output. After that, I tried to get better result by providing better prompt and tuning other parameters.

Models Used:
1.	Bard
2.	Bart-base
3.	T5-base
4.	Gpt2
5.	Lamda
6.	LaMini-Flan-T5-783M
7.	Lamini-GPT-774M
8.	LaMini-Cerebras-590M

Most of the models are taken from hugging face.

Platform used:
Google colab, vs code

Result:
1.	The best performance is gotten from the model LaMini-Flan-T5-783M. the model performed quite well at text enhancement. Although the accuracy can be better. At book recommendation also, it performed decent, although sometimes it generates random book name.
2.	Some other decent performances are: Lamini-GPT-774M, LaMini-Cerebras-590M, T5-base
3.	The other models didn’t perform good. 
4.	Bard doesn't response with proper answers, when it thinks it is legal/crime/sensitive/ethical issue. As our work is related to law, bard is performing very bad as it is not providing any data or responses related to that.
5.	Bart model was just returning the given fact without any changing.
6.	T5 model is returning same sentences, adding sometimes a few words to complete the sentence, not adding any legal context.
7.	Gpt-2 was generating some gibberish sentences with the words of the sentences, similar with book name answering.
8.	couldn't implement lamda model, LaMini-Neo-1.3B and some other models.

Roadblocks/ Drawbacks:
•	As these models are pretrained for general purpose, they are not good at legal specific tasks.
•	We can not prompt engineer properly for most of the models.

Improvement areas:
If we could train those pre-trained models with proper datasets according to our need, we may get better performances.
