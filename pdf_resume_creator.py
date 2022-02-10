
from fpdf import FPDF
import json
# Read the JSON file
my_details = open(r'C:\Users\Owner\OneDrive\Desktop\PUP\PLD\Assignment9\resume.json')
resume_data = my_details.read()
data = json.loads(resume_data)
# For importing basic information part
basic_information_data = data['Basic Information']
name = basic_information_data['Name']
birthday = basic_information_data['Birthday']
age = basic_information_data['Age']
gender = basic_information_data['Gender']
address = basic_information_data['Address']
email = basic_information_data['Email']
phone_number = basic_information_data['Phone Number']
# For importing obejctives part
objectives_data = data['Objectives']
career = objectives_data['Career Objectives']
# For importing education background part
educ_background = data['Educational Background']
elem = educ_background['Elementary']
junior = educ_background['Junior High School']
senior = educ_background['Senior High School']
college = educ_background['College']
# For importing experience part
experience_data = data['Experience']
college_experience = experience_data['College']
professional_experience = experience_data['Professional']
# Make the program a pdf
pdf = FPDF('P', 'mm', 'Letter')
# For adding page and setting the font, fontstyle, font size and creating a cell
pdf.add_page()
pdf.set_font('helvetica', 'B', 16 )
pdf.cell(200, 15, txt= "RESUME", ln= True, align= 'C', border= True)
# For creating the basic info in pdf
pdf.set_font('helvetica', 'B', 12 )
pdf.cell(200, 10, txt= "Basic Information", ln= True, align= 'C', border= True)
for basic_information in data['Basic Information']:
    if basic_information in 'Name':
        text = name
    if basic_information in 'Birthday':
        text = birthday
    if basic_information in 'Age':
        text = age
    if basic_information in 'Gender':
        text = gender
    if basic_information in 'Address':
        text = address
    if basic_information in 'Email':
        text = email
    if basic_information in 'Phone Number':
        text = phone_number
    pdf.set_font('helvetica', 'B', 10 )
    pdf.cell(45, 8, txt= f'{basic_information}:', ln= 0, align= 'L', border= True)
    pdf.set_font('helvetica', '', 10 )
    pdf.cell(155, 8, txt= f'{text}', ln= True, align= 'L', border= True)

# For creating the objectives in pdf
pdf.set_font('helvetica', 'B', 12 )
pdf.cell(200, 10, txt= "Objectives", ln= True, align= 'C', border= True)

for career_objectives in data['Objectives']:
    if career_objectives in 'Career Objectives':
        text = career
    pdf.set_font('helvetica', 'B', 10 )
    pdf.cell(200, 8, txt= f'{career_objectives}:', ln= True, align= 'J', border= True)
    pdf.set_font('helvetica', '', 10 )
    pdf.multi_cell(200, 8, txt= f'{text}', ln= True, align= 'J', border= True)

# For creating the education background in pdf
pdf.set_font('helvetica', 'B', 12 )
pdf.cell(200, 10, txt= "Educational Background", ln= True, align= 'C', border= True)

for educ_background in data['Educational Background']:
    if educ_background in 'Elementary':
        text = elem
    if educ_background in 'Junior High School':
        text = junior
    if educ_background in 'Senior High School':
        text = senior
    if educ_background in 'College':
        text = college
    pdf.set_font('helvetica', 'B', 10 )
    pdf.cell(45, 8, txt= f'{educ_background}:', ln= 0, align= 'L', border= True)
    pdf.set_font('helvetica', '', 10 )
    pdf.cell(155, 8, txt= f'{text}', ln= True, align= 'L', border= True)

# For creating the experience in pdf
pdf.set_font('helvetica', 'B', 12 )
pdf.cell(200, 10, txt= "Experience", ln= True, align= 'C', border= True)
for experience_data in data['Experience']:
    if experience_data in 'College':
        text = college_experience
    if experience_data in 'Professional':
        text = professional_experience
    pdf.set_font('helvetica', 'B', 10 )
    pdf.cell(45, 8, txt= f'{experience_data}:', ln= 0, align= 'L', border= True)
    pdf.set_font('helvetica', '', 10 )
    pdf.cell(155, 8, txt= f'{text}', ln= True, align= 'L', border= True)

pdf.cell(200, 65, ln= True, align= 'J', border= True)

# Making it a pdf file
pdf.output('PORRAS_MICA.pdf')