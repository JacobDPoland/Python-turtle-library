import turtle as turt

# turt starts at (0,0) in the center of the canvas
turt.shape("turtle")

# turt.forward(100)  # forward take in a distance parameter
# turt.left(90)      # left and right take in an angle parameter
# turt.forward(100)  

# small circle
for i in range(360):
    turt.forward(1)
    turt.left(1)


turt.mainloop()