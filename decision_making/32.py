'''question "Question : Monsoon Weather Advisory
Write a program that takes the value for rainfall amount from user.
 It gives weather advisory based on rainfall (in mm): Light rain (0-25), Moderate rain (26-75), Heavy rain (76+).

Expected Output Format:
Display rain category and appropriate advisory"'''


rainfall= float (input("enter rainfall in mm:"))
if rainfall <= 25:
    category = "light rain"
    advisory = "carry an umbrella"
elif 26<= rainfall >= 75:
    category = "moderate rain" 
    advisory = "avoid travel"
else: 
    
     category ="heavy rain"
     advisory ="stay home"