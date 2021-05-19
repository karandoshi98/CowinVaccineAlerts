from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST'])
def add_mail_recepient():
    if (request.method == 'POST'):
        age = str(request.form['age'])
        pincode = str(request.form['pincode'])
        mail = str(request.form['mail_id'])
        print(pincode,age,mail)
        if pincode.isnumeric():
            result = f'Vaccine alert setup successfully for {mail}\nPincode - {pincode}\nAge - {age}'
            user = {pincode: mail}
            if age == '18':
                updated_details = update_user_details_file_18(user)
            else:
                updated_details = update_user_details_file_45(user)
            print(updated_details)
        else:
            result = f'Vaccine alert setup unsuccessful. Make sure pincode is numeric'


    return render_template('results.html', result=result)


def update_user_details_file_18(user):
    # #write to file
    # cur = open("user_details_18.json", "r+")
    # json.dump(user,cur)
    # cur.close()

    data = {}
    cur = open("user_details_18.json", "r")
    try:
        data = json.loads(cur.read())
    except Exception as e:
        print(e)
        data = {}
    print('Before' + str(data))

    new_pincode = list(user.keys())[0]
    if new_pincode in list(data.keys()) :
        og = data[new_pincode]
        new = user[new_pincode]
        if new[0] not in og:
            og.extend(new)
        print("updating existing list ....")
    else:
        print("added new key:value pair")
        data.update(user)

    cur.close()
    cur1 = open("user_details_18.json", "w+")
    json.dump(data, cur1)
    print("Age 18 file")

    print('After' + str(data))
    cur1.close()
    return data

def update_user_details_file_45(user):
    # #write to file
    # cur = open("user_details_18.json", "r+")
    # json.dump(user,cur)
    # cur.close()

    data = {}
    cur = open("user_details_45.json", "r")
    try:
        data = json.loads(cur.read())
    except Exception as e:
        print(e)
        data = {}
    print('Before' + str(data))

    new_pincode = list(user.keys())[0]
    if new_pincode in list(data.keys()) :
        og = data[new_pincode]
        new = user[new_pincode]
        if new[0] not in og:
            og.extend(new)
        print("updating existing list ....")
    else:
        print("added new key:value pair")
        data.update(user)

    cur.close()
    cur1 = open("user_details_45.json", "w+")
    json.dump(data, cur1)
    print("Age 45 file")
    print('After' + str(data))
    cur1.close()
    return data


if __name__ == '__main__':
    print('app is working')
    app.run()
