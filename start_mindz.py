''' A simple starter Api '''

import random
import requests
from flask import Flask, jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# alphabet - a-z

alpha = ['a','b','c', 'd', 'e', 'f']
# num 1-9
num = ['1','2','4','6']
# all
charp = ['$','%', '$', '#', '%']

@app.route('/mypwd', methods=['Get'])
def get_passwd():
    '''get the passwd for user'''
    count_char = 5
    # count_char = count_char
    print( "you want password of size",count_char,"we will share shortly" )
    userpwd_count = 0
    userpassword = []
    whileloop =0
    while userpwd_count < count_char:
        whileloop +=  1
        # print(whileloop, "is the while loop count")
        userpassword.append( random.choice(alpha))
        userpassword.append(random.choice(alpha))
        userpwd_count = userpwd_count+2
        userpassword.append(random.choice(num))
        userpwd_count= userpwd_count+1
        userpassword.append(random.choice(charp))
        userpassword.append(random.choice(charp))
        userpwd_count= userpwd_count+2
        # print(userpwdCount)
    generatedpassword = ""
    for i in userpassword:
        generatedpassword = generatedpassword+i
    return jsonify({"gpwd": generatedpassword})
    # Return the response from the /guess API

# user input : Ask user to enter the size of password they want to be generated min num 5 chatracter . 
# then generate a random password that coinsists of 2 alphabets 2 signs and 1 number 
@app.route('/mygame', methods=['POST'])
def start_games():
    ''' Simple starter api '''
    data = request.get_json()
    count_char = data.get("count_char")
    # count_char = count_char
    print( "you want password of size",count_char,"we will share shortly" )
    userpwd_count = 0
    userpassword = []
    whileloop =0
    while userpwd_count < count_char:
        whileloop +=  1
        # print(whileloop, "is the while loop count")
        userpassword.append( random.choice(alpha))
        userpassword.append(random.choice(alpha))
        userpwd_count = userpwd_count+2
        userpassword.append(random.choice(num))
        userpwd_count= userpwd_count+1
        userpassword.append(random.choice(charp))
        userpassword.append(random.choice(charp))
        userpwd_count= userpwd_count+2
        # print(userpwdCount)
    generatedpassword = ""
    for i in userpassword:
        generatedpassword = generatedpassword+i
    return jsonify({"gpwd": generatedpassword})
    # print(generatedpassword)

@app.route('/gamerock', methods=["Post"])
def play_game():
    ''' Play Rock paper scisors with User choice'''
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    sign_choice = [ROCK, PAPER, SCISSORS]
    data = request.get_json()
    user_choice= data.get("userChoice").lower()
    if user_choice not in sign_choice :
        return jsonify({"message":"Invalid User Choice" ,"game_code": -1, "status_code": 200})

    buddy_comp_choice = random.choice(sign_choice)
    if user_choice == buddy_comp_choice:
        return jsonify({"message": "Its Draw", "game_code": 0,"status_code": 200,"comp_choice":""})
    elif\
    (user_choice == ROCK and buddy_comp_choice == SCISSORS) or \
    (user_choice == PAPER and buddy_comp_choice == ROCK) or \
    (user_choice == SCISSORS and buddy_comp_choice == PAPER):
        return jsonify({"message": "You Win", "game_code": 1, "status_code": 200,\
                         "comp_choice":buddy_comp_choice })
    else:
        return jsonify({"message": "Computer Won", "game_code": 2, \
                        "status_code": 200, "comp_choice":buddy_comp_choice}) 



if __name__ == '__main__':
    app.run(debug=True)
