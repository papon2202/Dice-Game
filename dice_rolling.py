from tkinter import *
import random


def diceRolling():
    main_dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    # custom = random.choices(main_dice,weights =[10,20,20,10,50,70])
    dice_label.configure(text=random.choices(main_dice,weights=[10,20,20,10,50,70]))#70% chance to be 6
    dice_label.pack()

root = Tk()
root.title("Dice Game")
root.geometry('250x300')



dice_label = Label(root,font =("jost",150, "bold"),text ="",fg ="blue")



roll_dice = Button(root,font =("jost",20, "bold"),text ="Roll Dice",command = diceRolling)
roll_dice.pack()

root.mainloop()