# AI Chatbot for College Helpdesk

def chatbot():
    print("🤖 College Helpdesk Chatbot")
    print("Type 'exit' to quit.\n")

    responses = {
        "admission": "Admissions are open from June to August. Visit the admission office or website for details.",
        "fees": "You can pay fees online through the student portal or at the accounts office.",
        "exam": "Exams are conducted twice a semester. Check the academic calendar for dates.",
        "library": "The library is open from 8:00 AM to 8:00 PM on weekdays.",
        "hostel": "Hostel facilities are available for both boys and girls. Contact the hostel office for admission.",
        "placement": "The placement cell organizes training and recruitment drives throughout the year.",
        "canteen": "The college canteen is open from 8:00 AM to 6:00 PM.",
        "contact": "You can contact the college at info@college.edu or call +91-1234567890."
    }

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "exit":
            print("Chatbot: Thank you! Have a great day.")
            break

        found = False

        for keyword in responses:
            if keyword in user_input:
                print("Chatbot:", responses[keyword])
                found = True
                break

        if not found:
            print("Chatbot: Sorry, I couldn't understand your query. Please contact the helpdesk.")

# Run chatbot
chatbot()
