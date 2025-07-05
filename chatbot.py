import smtplib
import os
from jinja2 import Template

# Mock student database
students_db = {
    "22053364": "Shivam Sodhani",
    "22053365": "John Doe",
    "2205060": "Saakshi Dewangan"
}

# Predefined responses
responses = {
    "bonafide_certificate": "Generating your bonafide certificate...",
    "fee_details": "Please check the official portal for fee details."
}

# Function to verify roll number
def verify_student(roll_number):
    return students_db.get(roll_number, None)

# Function to generate a bonafide certificate
def generate_certificate(name, roll_number):
    template = Template("""
        TO WHOMSOEVER IT MAY CONCERN
        
        This is to certify that {{ name }}, Roll No: {{ roll_number }}, is a bonafide student of our institution.
        
        Principal,
        XYZ Institute
    """)
    
    certificate_text = template.render(name=name, roll_number=roll_number)
    with open(f"bonafide_{roll_number}.txt", "w") as file:
        file.write(certificate_text)
    return f"bonafide_{roll_number}.txt"

# Function to send an email
def send_email(recipient, file_path):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    with open(file_path, "r") as file:
        certificate_content = file.read()
    
    subject = "Bonafide Certificate"
    body = f"Hello,\n\nPlease find attached your bonafide certificate.\n\n{certificate_content}\n\nBest Regards,\nCompliance Cell"
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main chatbot interaction
def chatbot():
    roll_number = input("Enter your roll number: ")
    student_name = verify_student(roll_number)
    
    if not student_name:
        print("Invalid roll number. Please try again.")
        return
    
    print(f"Welcome, {student_name}!")
    print("How can I help you today?")
    print("1. Request Bonafide Certificate\n2. Check Fee Details")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        print(responses["bonafide_certificate"])
        file_path = generate_certificate(student_name, roll_number)
        email = input("Enter your email: ")
        send_email(email, file_path)
    elif choice == "2":
        print(responses["fee_details"])
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    chatbot()
