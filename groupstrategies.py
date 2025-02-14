# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING

import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","steal"),("steal","steal"),("split","steal"),("split","steal"),("steal","split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","steal"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy: Always steals the first 2 rounds and then copies one of the random last 3 moves from the opponent
# 
def USC3(history):
    if len(history) < 2:
        return "steal"
    else:
        lastOppMoves = history[-3:]
        return random.choice(lastOppMoves)[1]

        