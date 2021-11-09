bank_words=[]




def meno():
    print("wellcom please select from menu::")
    print('1:english to persian')
    print('2:persian to English')
    print('3:add new word')
    print('4:exit')




def laod_data():
    print("loading...")
    with open("words_bank.txt","r") as file:
        info_dic=file.read()
        words=info_dic.split("\n")

        for i in range(0,len(words),2):
            dic={"english":words[i],"persian":words[i+1]}
            bank_words.append(dic)
    print("ok Continue!")


def en2per():
    output=""
    sentence=input("please enter your text :: ")
    wor_sen=sentence.split(" ")
    
    for word in wor_sen:
        for bword in bank_words:
            if bword["english"]==word:
                output += bword["persian"] + " "
                break
        else:
            output += word + " "

    print(output)




def per2en():
    output=""
    sentence=input("please enter your text:: ")
    wor_sen=sentence.split(" ")
    
    for word in wor_sen:
        for bword in bank_words:
            if bword["persian"]==word:
                output += bword["english"] + " "
                break
        else:
            output += word + " "

    print(output)




def new_word():
    english=input("please enter english  word::")
    persian=input("please enter persian  word::")
    new_word={"english":english, "persian":persian}
    bank_words.append(new_word)
    print("Ok")



def Exit():
    with open("words_bank.txt","w") as file:
        for word in bank_words:
            file.write(word["english"])
            file.write("\n")
            file.write(word["persian"])
            file.write("\n")




    
    print("have a good time by!")
    exit()




laod_data()
while True:
    meno()
    choice=int(input("please enter your choice::"))
    if choice==1:
        en2per()
    elif choice==2:
        per2en()
    elif choice==3:
        new_word()
    elif choice==4:
        Exit()