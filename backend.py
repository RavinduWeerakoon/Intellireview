import openai 
import os
openai.api_key = os.environ.get("API_KEY").strip()




def call_openai(prompt, max_tokens=2300):


    
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0.8,
            presence_penalty=1,
            # stop=["<h"]
        )

    return response.get("choices")[0]['text']


def get_details(text):
    prompt = """As an attentive reader, meticulously extract the employee's name, organization, manager, and evaluator from the performance review document. 
    You will find the employee's name displayed prominently at the top, preceding the year. Present this vital information as concise bullet points, separated by line breaks:
Please format it nicely with line breaks to make it more readable. Add <br> html tags to make it more readable.
<ul>
<li>Employee Name:</li>
<li>Organization:</li>
<li>Manager:</li>
<li>Evaluator:</li>

"""
    response = call_openai(f"{text}\n\n{prompt}")
    print(response)
    return response 



def recommend_courses(text, details =""):
    prompt ="""Analyze the employee's performance review to identify strengths and growth areas. Recommend relevant courses from Udemy or LinkedIn Learning to help them maximize potential and address development needs. List the course recommendations concisely:
Please format it nicely with line breaks to make it more readable. And seperate each oppurtunity by html line break if possible.

Course 1 (corresponding strength/growth area)
Course 2 (corresponding strength/growth area)
Course 3 (corresponding strength/growth area)


"""
    if details:
        prompt += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
    response = call_openai(f"{text}\n\n{prompt}")
    return_response = ''
  
    temp_list = response.split('•')
    for item in temp_list:
        if item != '':
            return_response += f"* {item}"

    
    return return_response

def industry_trends(text, details=''):

    prompt = """Analyze the employee's performance review to identify growth-oriented topics for 1:1 meetings with their manager. Focus on areas benefiting from guidance, feedback, and support. Present prioritized discussion topics in a clear and organized format:

Topic 1 (related to growth objectives)
Topic 2 (related to growth objectives)
Topic 3 (related to growth objectives)
Topic 4 (related to growth objectives)
Topic 5 (related to growth objectives)
Please format it nicely with line breaks to make it more readable
"""
    if details:
        prompt += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"

    response = call_openai(f"{text}\n\n{prompt}")

    return response




def highlight_action_items(text, details =''):
    prompt = """Analyze the employee's performance review to identify areas where they can contribute to the team's goals. Suggest targeted measures to create a high-performance environment, and recommend prioritized action items for the next year based on their performance review:
Please format it nicely with line breaks to make it more readable
<ul>
<li>Action item 1 (related to strengths/growth areas)</li>
<li>Action item 2 (related to strengths/growth areas)</li>
<li>Action item 3 (related to strengths/growth areasM/li>

"""

    if details:
        prompt += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
    response = call_openai(f"{text}\n\n{prompt}")

    return response

    
def SMART(text):
    prompt = """Analyze the employee's performance review to set SMART goals for the next year. Provide an action plan with the following elements:

Milestones: Break goals into manageable milestones.
Resources: Identify relevant resources for skill development.
Time management: Offer strategies for effective time allocation.
Accountability: Suggest methods for progress tracking.
Potential obstacles: Anticipate challenges and provide strategies to overcome them.
Support network: Encourage building a network of colleagues, mentors, and peers.
A structured action plan helps the employee achieve their goals and advance in their career.
Please format it nicely with line breaks to make it more readable
"""

    response = call_openai(f"{text}\n\n{prompt}")
    return_response = ''
    temp_list = response.split('•')
    if len(temp_list) > 2:
        for item in temp_list:
            if item != '':
                return_response += f"* {item}"
        return return_response


    return response 

def soft_skills(text, details=''):

    prompt = """Based on the employee's performance review, provide personalized tips for soft skill development and topics for professional growth. List these recommendations in a prioritized order:

Tip 1 (related to strengths/growth areas)
Tip 2 (related to strengths/growth areas)
Tip 3 (related to strengths/growth areas)
Please format it nicely with line breaks to make it more readable
"""

    response = call_openai(f"{text}\n\n{prompt}")
    if details:
        prompt += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
    return_response = ''
    temp_list = response.split('•')
    if len(temp_list) > 2:
        for item in temp_list:
            if item != '':
                return_response += f"* {item}"
        return return_response

    return response 

def career_dev_ops(text, details=''):
    prompt = """Analyze the employee's performance review and identify career development opportunities:
Please format it nicely with line breaks to make it more readable. If no response at least write some common opportunities. And seperate each oppurtunity by html line break if possible

Opportunity 1
Opportunity 2
Opportunity 3


"""
    if details:
        prompt += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
    response = call_openai(f"{text} \n {prompt}")

    return response
