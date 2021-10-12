EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
3# LINE BREAK
4 def bake_time_remaining(elapsed_bake_time):
"""
Return remaining baking time. 
This function takes a number representing the time already spent baking and calculates the total remaining minutes while baking the lasagna.
BAKE_TIME_REMAINING = EXPECTED_BAKE_TIME - elapsed_bake_time
return BAKE_TIME_REMAINING
# LINE BREAK
def preparation_time_in_minutes(number_of_layers):
"""
return total preparation time

This function takes a number representing the number of layers and calculates the time required for preparation of layers of the lasagna.
"""

PREP_TIME_REQD = number_of_layers * PREPARATION_TIME
  return PREP_TIME_REQD
  
# LINE BREAK

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
"""
Return elapsed cooking time

This function takes two numbers representing the number of layers & the time already spent 
baking and calculates the total elapsed minutes spent cooking the lasagna.
"""
PREP_TIME_REQD = number_of_layers * PREPARATION_TIME
TOTAL_ELAPSED_TIME - PREP_TIME_REQD * elapsed_bake_time
return TOTAL_ELAPSED_TIME


