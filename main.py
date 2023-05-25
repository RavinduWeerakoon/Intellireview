
from fileinput import filename
from flask import *
app = Flask(__name__)

from backend import get_details, career_dev_ops, recommend_courses, highlight_action_items
from PyPDF2 import PdfReader

def get_pdf_text(filename='uploaded_pdf', start=0, finish=1):
   reader = PdfReader('uploaded.pdf')
   pages = len(reader.pages)
   text = ""
   while(start<finish):
      
      text += reader.pages[start].extract_text()
      start +=1
   return text



@app.route('/')
def get():
   return render_template('index.html')

@app.route('/tabs')
def get_tabs():
   return render_template('tabs.html')
	
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':

      goals = request.form.get('goals')
      obstacles = request.form.get('obstacles')
      skills = request.form.get('skill')
      f = request.files['file']
      f.save("uploaded.pdf")

      details = f"Use this data grab more understanding about the user User's Goals: {goals} \n What the user thinks as Obstacles: {obstacles} \n USer's Skills: {skills}"
      return render_template('tabs.html', details=details)
		
@app.route('/details')
def details():

   details = get_details(get_pdf_text())

   return details



@app.route('/tab2', methods=['POST'])
def dev_ops():

   user_details = request.form.get("details")
   
   details = career_dev_ops(get_pdf_text(start=1, finish=3), details=user_details)

   print(details)
   

   return details

@app.route('/tab3', methods=['POST'])
def rec_courses():
   user_details = request.form.get("details")
   details = recommend_courses(get_pdf_text(start=1, finish=3), details=user_details)

   return details

@app.route('/tab4', methods=['POST'])
def action_items():
   user_details = request.form.get("details")
   details = highlight_action_items(get_pdf_text(start=1, finish=3), details=user_details)

   return details

@app.route('/tab5', methods=['POST'])
def optimizer():
   user_details = request.form.get("details")
   details = highlight_action_items(get_pdf_text(start=1, finish=3), details=user_details)

   return details



if __name__ == '__main__':
   app.run(debug = True)