print("""
*********************************************************************************
███╗░░░███╗░█████╗░████████╗██╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗ *
████╗░████║██╔══██╗╚══██╔══╝██║░░██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝ *
██╔████╔██║███████║░░░██║░░░███████║  ██║░░██╗░███████║██╔████╔██║█████╗░░ *
██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░ *
██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗ *
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝ *
*******************************************************************************

THIS IS MADE FOR  MATH IQ LEVEL TEAST 
CREATED BY SATYABRATA MITRA
THIS IS BETA  VERSION
""")

print("# LEVEL ONE CHAPTER INTEGERS")
print("# LEVEL TWO CHAPTER FRACTIONS")
print("#LEVEL THREE CHAPTER Data Handling")
print(" # LEVEL FOUR CHAPTER  Simple Equations ")
print("# Level FIVE CHAPTER Congruence of Triangles")
print('# LEVEL SIX CHAPTER Comparing Quantities')
print("# LEVEL SEVEN CHAPTER Triangle and its Properties")
print("# LEVEL EIGHT CHAPTER Rational Numbers ")
print("# LEVEL NINE CHAPTER Algebraic Expressions")
print('# LEVEL TEN CHAPTER Perimeter and Area  ')
def chap_1 ():
    
    print('first integers')
ans = input("12 x 7 :")
if ans == '84':
    chap_1 = True
else:
     chap_1 = False
ans_2 = input("(-15) × 8 :")
if ans_2 != '-120':
    print('invalid ANS ')
else:
     print("RIGHT AS")
ans_3 = input("(-25) × (-9) :")
if ans_3 == '+225':
    print("right ans")
else:
    print('invalid ans')
ans_4 = input("125 × (-8) :")
if ans_4 == '1000':
    print("right ans")
else:
    print('invalid ans')
ans_5 = input("3 × (-8) × 5 :")
if ans_5 == '3 × -40 = -120':
    print("right ans")
else:
    print('invalid ans')
ans_6 = input(" (-2) × 36 × (-5):")
if ans_6 == '72 × -5 = +360 :':
    print('right ans')
else:
    print('invalid ans')
# END CHAP 1
    
# start FRICTIONS
def chap_2():
    
    print('friction')
    print('CHAPTER 2 FRICTIONS')

chap_2_ans_1 = input('Multiply 2.05 and 1.3 ;')
if chap_2_ans_1 == '2.665':
    chap_2 = True
    print('right ans')
else:
    chap_2 = False
    print('invalid ans')
chap_2_ans_2 = input('(3/5) + (2/7) : ')
if chap_2_ans_2 == '(31/35)':
    print('right ans')
else:
    print('invalid ans')
chap_2_ans_3 = input('(7/10) + (2/5) + (3/2) :')
if chap_2_ans_3 == '(13/5)':
    print('right ans')
else:
    print('invalid ans')
chap_2_ans_4 = input(' 7 × (3/5):')
if chap_2_ans_4 == ' (21/5)':
    print('right ans')
else:
    print('invalid ans')
chap_2_ans_6 = input('Solve:  \n (2/6) - (90/90)'
                     '(4/9) + (9/3) :'
                     '(9/3) + (8/9) :'
                     '(3/4) * (8/2)')
# END FRi
# data handling
def chap_3 ():
    print('data handling')
chap_3_ans = input('Sum of all observation = 1 + 2 + 2 + 3 + 4 + 4 + 4 + 5 + 5 + 5 + 5 + 5 + 6 + 6 + 6 + 6 + 7 + 7+ 8 + 9')
if chap_3_ans == '100':
    
    print('right ans')
    pass 

else:
    print('invalid ans')
    False

chap_3_ans_2 = input(" Find the mean of the first five whole numbers.")
if chap_3_ans_2 == '2':
    print('right ans')
    pass
else:
    print('invalid ans')
    print('solution')
    print("""The first five Whole numbers are 0, 1, 2, 3, and 4.
Mean = (Sum of first five whole numbers)/ (Total number of whole numbers)

Then,

Sum of five whole numbers = 0 + 1 + 2 + 3 +4

= 10

Total Number of whole numbers = 5

Mean = (10/5)

= 2""")
chap_3_ans_3 = input("""3. The weights (in kg.) of 15 students of a class are:

38, 42, 35, 37, 45, 50, 32, 43, 43, 40, 36, 38, 43, 38, 47

(i) Find the mode and median of this data.
(ii) Is there more than one mode?""")
mode = input("ENTER THE MODE:")
median = input("ENTER THE MEDIAN:")
if mode == '38 and 43':
    print("right ans")
else:
    print('invalid mode')
if median == "8":
    print("right ans")
else:
    print("invalid median")
# END 
# START CHAP3 
def chap_4 ():
    print("simple Equations")
chap_4_ans_1 = input("x + 3 = 0 \n x = 3:")
if chap_4_ans_1 == '6':
    chap_4 = True
    print("RIGHT ans")
else:
    chap_4 = False
    print("invalid ans")
chap_4_ans_2 = input("x + 3 = 0 \n x = 0:")
if chap_4_ans_2 == '3':
    print('right ans')
else :
    chap_4 = False
    print("invalid ans")
chap_4_ans_3 = input("x + 3 = 0 \n x = -3")
if chap_4_ans_3 == '0':
    print("right ans")
else :
    print('invalid ans')

chap_4_ans_5 = input("(m/3) = 2")
print('m = -6')
if chap_4_ans_5 == ' – 2':
    print("right ans")
else :
    print('invalid ans')
def chap_5 ():
    print(" Congruence of Triangles")
chap_5_ans_1 = input("""In the given triangles ABC and PQR, AB = 3.5 cm, BC = 7.1 cm, AC = 5 cm, PQ = 7.1 cm, QR = 5 cm and PR = 3.5 cm. Examine whether the given two triangles are congruent or not. If yes, then write the congruence relation in symbolic form.
""")
if chap_5_ans_1 == '''Given : AB = PR = 3.5 cm
BC = PQ = 7.1 cm and

AC = QR = 5 cm :''':
    print('right ans')
else:
    chap_5 = True
    chap_5 = False
    print('invalid ans')
chap_5_ans_2 = input("""""The measurements of some parts of two triangles are given below. Check whether the two triangles are congruent or not, using SAS congruence rule. Write it in symbolic form, if the triangles are congruent. For ∆ ABC, AB = 7 cm, BC = 5 cm, ∠B = 50° and for ∆ DEF, DE = 5 cm, EF = 7 cm, ∠E = 50:°""")
# chap_1 result 
marks = 0
if chap_1 == False :
    marks = 0
    print("chapter 1 failed ")
elif chap_1 == True :
    marks += 1
    print('chapter 1 pass')
# chap_2 result
if chap_2 == True :
    marks += 1
    print("chapter 2 Passed")
elif chap_2 == False:
    marks = 0
    print('chapter 2 failed')
# chapter 4
if chap_4 == True:
    marks += 1
    print("CHAPTER 3 PASSED")
elif chap_4 == False:
    marks = 0 
    print("CHAPTER 3 FAILED")
print("your score is" + marks)

# END
