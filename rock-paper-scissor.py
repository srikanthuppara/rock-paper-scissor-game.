import tkinter as tk
import random
root=tk.Tk()
root.title("ROCK-PAPER-SCISSORS")
root.geometry("500x500")
root.resizable(False,False)
title=tk.Label(root,text="rock - paper - scissors",font=("arial",20,"bold"))
title.pack(padx=20)

your_score=0
comp_score=0

score_label=tk.Label(root,
                     text="your score:0 \n"
                     "comp score: 0",
                     font=("arial",14))
score_label.pack()




play_label=tk.Label(root,text="your choice:",
                            font=("arial",14))
play_label.pack(pady=5)
comp_label=tk.Label(root,text="computer choice:",
                            font=("arial",14))
comp_label.pack()




choose=tk.Label(root,text="choose rock/paper/scissor",
                font=("arial",16))
choose.pack(pady=20)



button_frame=tk.Frame(root)
button_frame.pack(pady=20)

rock_button=tk.Button(button_frame,text="🪨 rock",width=10,fg="brown",bg="white",command=lambda: play("rock"))
rock_button.grid(row=0,column=0)

paper_button=tk.Button(button_frame,text="📃 paper",width=10,bg="white",command=lambda: play("paper"))
paper_button.grid(row=0,column=1)

scissor_button=tk.Button(button_frame,text="✂️ scissor",width=10,fg="blue",bg="white",command=lambda: play("scissor"))
scissor_button.grid(row=0,column=2)

def play(user_choice):
    global your_score,comp_score
    comp_choice=random.choice(['rock','paper','scissor'])
    print("you:",user_choice)
    print("computer:",comp_choice)
    if (user_choice == comp_choice):
        choose.config(text="its a tie")
    elif ((user_choice=='paper' and comp_choice=='rock') or (user_choice=='scissor' and comp_choice=='paper') or(user_choice=='rock' and comp_choice=='scissor')):
        your_score+=1
        choose.config(text="you won")
        
    elif((user_choice=='rock' and comp_choice=='paper') or (user_choice=='paper' and comp_choice=='scissor') or(user_choice=='scissor' and comp_choice=='rock')):
        comp_score+=1
        choose.config(text="computer wins")

    play_label.config(text=f"your choice :{user_choice}")
    comp_label.config(text=f"computer choice :{comp_choice}")

    score_label.config(text=f"your score :{your_score}, computer score :{comp_score}")


def reset():
    global your_score,comp_score
    your_score=0
    comp_score=0
    score_label.config(text="your score :0\n" \
    "computer score :0")
    play_label.config(text="your choice :")
    comp_label.config(text="computer choice :")

    choose.config(text="choose rock/paper/scissor")

reset_btn=tk.Button(root,text="reset",width=15,command=reset,fg="red")
reset_btn.pack(pady=20)


root.mainloop()