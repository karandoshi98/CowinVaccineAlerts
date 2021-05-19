import json

def update_user_details_file(user):
    # #write to file
    # cur = open("user_details_18.json", "r+")
    # json.dump(user,cur)
    # cur.close()

    data = {}
    cur = open("user_details_18.json", "r")
    data = json.loads(cur.read())
    print('Before' + str(data))

    new_pincode =  list(user.keys())[0]
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
    print('After' + str(data))

    cur1.close()


    # usr_details = dict()
    # print(type(usr_details))
    # user_det = dict(cur.read())
    # print()
    # print(type(user_det))
    # l = list(user.keys())
    # print(l[0])
    # if user_det[l[0]] != "":
    #     print(user_det[l[0]])
    #
    # # user_det.update(user)
    # # print(user_det)
    # # cur.write(str(user))

user = {'421201': ['monil0206@gmail.com','karandoshi98@gmail.com']}

update_user_details_file(user)
