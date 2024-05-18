questions=["which languare was used to create facebook?",
           "python", "JS", "php", "none"]

["which languare was used to create whatsapp?",
           "python", "JS", "php", "none"]

["which languare was used to create instagram?",
           "python", "JS", "php", "none"]

["which languare was used to create chatgpt?",
           "python", "JS", "php", "none"]

["which languare was used to create snapchat?",
           "python", "JS", "php", "none"]
["which languare was used to create snapchat?",
           "python", "JS", "php", "none"]

["which languare was used to create snapchat?",
           "python", "JS", "php", "none"]

["which languare was used to create snapchat?",
           "python", "JS", "php", "none"]

["which languare was used to create snapchat?",
           "python", "JS", "php", "none"]
["which languare was used to create snapchat?",
           "python", "JS", "php", "none"]


levels=[10000,20000,30000,50000,80000,100000, 400000, 800000,1000000,7000000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"QUESTION FOR RS{levels[i]}")

    print(f"a.{question[1]}  b.{question[2]}")
    print(f"c.{question[3]}  d.{question[4]}")

    reply=int(input("ENTER YOUR OPTION"))
    if(reply==question[-1]):
        print("correct answer,{levels[i]}")
        if(i==4):
            money=50000
        elif(i==9):
            money=1000000
        elif(i==10):
            money=70000000
    else:
        print("wrong answer")
        break


