import statistics

green = 0

yellow= 0

brown= 0

pink= 0

cream= 0

orange = 0

white= 0

red= 0

blue = 0

mon= ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW," "ORANGE", "CREAM", "ORANGE", "RED", "WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"]

tues= ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]

wed= ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]

thurs= ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE, WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]

fri= ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE, RED, RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]

#Monday analysis

for item in mon:

   if (item == "GREEN"):

      green += 1

   elif (item == "BROWN"):

       brown += 1

   elif(item == "CREAM"):

       cream += 1

   elif(item == "ORANGE"):

       orange += 1

   elif (item == "PINK"):

       pink += 1

   elif (item == "YELLOW"):

       yellow += 1

   elif(item == "WHITE"):

       white += 1

   elif(item == "RED"):

       red += 1

   elif (item == "BLUE"):

       blue += 1

       

#Tuesday

for item in tues:

   if (item == "GREEN"):

      green += 1

   elif (item == "BROWN"):

       brown += 1

   elif(item == "CREAM"):

       cream += 1

   elif(item == "ORANGE"):

       orange += 1

   elif (item == "PINK"):

       pink += 1

   elif (item == "YELLOW"):

       yellow += 1

   elif(item == "WHITE"):

       white += 1

   elif(item == "RED"):

       red += 1

   elif (item == "BLUE"):

       blue += 1

       

#Wednesday

for item in wed:

   if (item == "GREEN"):

      green += 1

   elif (item == "BROWN"):

       brown += 1

   elif(item == "CREAM"):

       cream += 1

   elif(item == "ORANGE"):

       orange += 1

   elif (item == "PINK"):

       pink += 1

   elif (item == "YELLOW"):

       yellow += 1

   elif(item == "WHITE"):

       white += 1

   elif(item == "RED"):

       red += 1

   elif (item == "BLUE"):

       blue += 1

       

#Thursday

for item in thurs:

   if (item == "GREEN"):

      green += 1

   elif (item == "BROWN"):

       brown += 1

   elif(item == "CREAM"):

       cream += 1

   elif(item == "ORANGE"):

       orange += 1

   elif (item == "PINK"):

       pink += 1

   elif (item == "YELLOW"):

       yellow += 1

   elif(item == "WHITE"):

       white += 1

   elif(item == "RED"):

       red += 1

   elif (item == "BLUE"):

       blue += 1

       

#Friday

for item in fri:

   if (item == "GREEN"):

      green += 1

   elif (item == "BROWN"):

       brown += 1

   elif(item == "CREAM"):

       cream += 1

   elif(item == "ORANGE"):

       orange += 1

   elif (item == "PINK"):

       pink += 1

   elif (item == "YELLOW"):

       yellow += 1

   elif(item == "WHITE"):

       white += 1

   elif(item == "RED"):

       red += 1

   elif (item == "BLUE"):

       blue += 1

print(f"Green: {green}\nBrown: {brown}\nCream: {cream}\nOrange: {orange}\nPink: {pink}\nYellow: {yellow}\nWhite: {white}\nRed: {red}\nBlue: {blue}")

grp= [green, brown, cream, orange, pink, yellow, white, red, blue]

print("Mean: ", round(statistics.mean(grp), 3))

print("Most worn: ", max(grp))

print("Median: ", statistics.median(grp))

print("Variance: ", round(statistics.variance(grp), 3))

pRed= red/(green+brown+cream+orange+pink+yellow+white+red+blue)

print("Probability: ", round(pRed, 3))
