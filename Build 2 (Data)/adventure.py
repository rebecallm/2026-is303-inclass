hook = "You are walking through the woods in the queen's "\
"precious cargo. You hear a loud thump in the trail in front of you. "\
"What do you do? "\
"A. Run and hide "\
"B. Turn around courageously "\
"C. Run towards the noise "\

decision_a = "You hide behind a tree and fall into a reality warping hole. You land on Tatoonine."\
"What do you do? D. Get on the pod racer E. Call for help F. cry. "

decision_b = "You face a giant rat. It is hungry. What do you do? "\
"G. Fight the rat H. Rund and hide I. Befriend the rat. "\

decision_c = "You find a kin old man who tripped. He offers you a wish. What do you do?"\
"J. Rund and hide K. Ask about the conditions of the wish L. You wish for BYU Chocolate milk. "

decision_d = "You are challenged to a race. What do you do? M. Win the race N. Lose the race. " 

decision_e = "San people come to eat you. What do you do? O. Fight them P. Runand hide. "

decision_f = "You keep crying. What do you do? Q. Keep crying R. Stop Crying. "

decision_g = "You die from the rat. "

decision_h = decision_a

decision_i = "the rat is now your bestie. You win. "

decision_j = decision_a

decision_k = "the old man gets anrgy. You die. "

decision_l = "You get the chocolate milk. You win. "

decision_m = " You win. "

decision_n = "You die. "

decision_o = decision_n

decision_p = decision_a

decision_q = decision_n

decision_r = decision_m

decision = input(hook) #Collect decision from user

decision = decision.upper()
decision2 = ""
   #Write what happens when you choose...
if decision == "A": 
     decision2 = input(decision_a)
elif decision == "B":
     decision2 = input(decision_b)
elif decision =="C":
     decision2 = input(decision_c) 
else: 
     print ("You are dead. ")

decision2 = decision2.upper()
if decision == "A" or decision == "B" or decision =="C":
     decision2 = decision2.upper()
     if decision2 == "D":
          decision3 = input(decision_d)
     elif decision2 == "E":
          decision3 = input(decision_e)
     elif decision2 == "F":
          decision3 = input(decision_f)
     elif decision2 == "G":
          decision3 = input(decision_g)
     elif decision2 == "H":
          decision3 = input(decision_h)
     elif decision2 == "I":
          decision3 = input(decision_i)
     elif decision2 == "J":
          decision3 = input(decision_j)
     elif decision2 == "K":
          decision3 = input(decision_k)
     elif decision2 == "L": 
          decision3 = input(decision_l)
     else: 
            print ("You are dead. ")
