questions = [
    ["Who is Narendra Modi?", "Wrestler", "Actor", "Prime Minister", "Shopkeeper",3],
    ["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai",2],
    ["Which is the largest planet?", "Earth", "Mars", "Jupiter", "Venus",3],
    ["Which keyword is used to create a function in Python?", "func", "define", "def", "lambda",3],
    ["Which data type is used to store text in Python?", "int", "str", "float", "bool",2],
    ["Which animal is known as the King of the Jungle?", "Elephant", "Tiger", "Lion", "Leopard",3],
    ["Which festival is known as the festival of lights?", "Diwali", "Holi", "Eid", "Christmas",1],
    ["Which gas do humans need to breathe?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen",1],
    ["What is 2 + 2 * 2?", "6", "8", "4", "2",2],
    ["Which device is used to type on a computer?", "Mouse", "Keyboard", "Monitor", "Speaker",2]
]

reward=100
for ques in questions:
    print(ques[0])
    print(f"a. {ques[1]}")
    print(f"b. {ques[2]}")
    print(f"c. {ques[3]}")
    print(f"d. {ques[4]}")
    ans=int(input("enter your annwer 1. for a  2. for b  3. for c 4. for d:"))
    if(ans==ques[5]):
        print(f"You got the correct answer!")
        reward+=100
    else:
        print(f"wrong answer ,correct answer is :{ques[5]}")
        break

print(f"YOUR REWARD:{reward}")




