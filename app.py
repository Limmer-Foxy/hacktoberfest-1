list_of_words = description.split()

feelings_list = []
encouragement_list = []
counter = 0

for each_word in list_of_words:

    if each_word == "bad":
        feelings_list.append("bad")
        encouragement_list.append("it's alright,you've already done your best")
        counter += 1
    if each_word == "good":
        feelings_list.append("good")
        encouragement_list.append("you should keep up the good work!")
        counter += 1
    if each_word == "moderate":
        feelings_list.append("moderate")
        encouragement_list.append("to have more confidence in yourself! You can do it!")
        counter += 1

if counter == 0:
    output = "Sorry I don't really understand. Please use different words?"

elif counter == 1:
    output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"

else:
    feelings = ""
    for i in range(len(feelings_list)-1):
        feelings += feelings_list[i] + ", "
        feelings += "and " + feelings_list[-1]
    
        encouragement = ""
        for j in range(len(encouragement_list)-1):
            encouragement += encouragement_list[i] + ", "
            encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

print()
print(output)
print()
