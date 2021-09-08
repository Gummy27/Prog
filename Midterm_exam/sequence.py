'''
Þetta forrit mun taka inn step og length gildi. Síðan er for lykkja
skilgreind til að keyra length sinnum. Forritið prentar út x * step.
'''

sequence_length = int(input("Length of sequence: "))
sequence_step = int(input("Step size: "))

for x in range(1, sequence_length+1):
    print(x*sequence_step)