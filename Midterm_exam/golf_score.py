'''
Þetta forrit verður einfaldlega röð if setninga.
'''

par_for_hole = int(input("Par for hole: "))
score_on_hole = int(input("Score on hole: "))

if(score_on_hole == par_for_hole ):
    print("Par")
elif(score_on_hole == par_for_hole + 1):
    print("Bogey")
elif(score_on_hole == par_for_hole + 2):
    print("Double bogey")
elif(score_on_hole >= par_for_hole + 3):
    print("Bad score")
elif(score_on_hole == par_for_hole - 1):
    print("Birdie")
elif(score_on_hole == par_for_hole - 2):
    print("Eagle")
else:
    print("Unbelievable!")