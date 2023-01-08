# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1_lc = name1.lower()
name2_lc = name2.lower()
# True count
t_count_n1 = name1_lc.count("t")
t_count_n2 = name2_lc.count("t")
t = t_count_n1 + t_count_n2

r_count_n1 = name1_lc.count("r")
r_count_n2 = name2_lc.count("r")
r = r_count_n1 + r_count_n2

u_count_n1 = name1_lc.count("u")
u_count_n2 = name2_lc.count("u")
u = u_count_n1 + u_count_n2

e_count_n1 = name1_lc.count("e")
e_count_n2 = name2_lc.count("e")
e = e_count_n1 + e_count_n2

l_count_n1 = name1_lc.count("l")
l_count_n2 = name2_lc.count("l")
l = l_count_n1 + l_count_n2

o_count_n1 = name1_lc.count("o")
o_count_n2 = name2_lc.count("o")
o = o_count_n1 + o_count_n2

v_count_n1 = name1_lc.count("v")
v_count_n2 = name2_lc.count("v")
v = v_count_n1 + v_count_n2

# column 1
c1 = str(t + r + u + e)
c2 = str(l + o + v + e)
score = int(c1 + c2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
