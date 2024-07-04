#printing a pyramid 
#where each row have the same color
#And the have column different colors 


def full_pyramid(n):
    #  the counter factor
        for i in range(1, n + 1):
            # Print leading spaces
            for j in range(n- i):
                print(" ", end="")
                
            # Print same colors for the current row
            color = ["R","B"] 
            #where "R" = "Red"
            #where "B" = "Blue"
            for k in range(1, i):
                if i%2 == 0:
                    print(" " + color[0], end="")
                else:
                    print(" " + color[1], end="")
            print()
   
full_pyramid(20)
#Beatiful Code