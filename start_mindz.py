''' A simple starter Api '''

import random
import requests
from flask import Flask, jsonify,request
app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(debug=True)
