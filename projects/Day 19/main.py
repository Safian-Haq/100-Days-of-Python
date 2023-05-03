from turtle import Screen, Turtle
from random import randint

turtle_colors = ['purple', 'blue', 'green', 'yellow',
                 'orange', 'red']

if __name__ == '__main__':

    is_turtle_selected = False
    while not is_turtle_selected:
        # Ask user to select a turtle color
        print(f'Available turtle colors \n{turtle_colors}\n')
        player_choice = input('Please enter a turtle color: ').lower()

        if player_choice in turtle_colors:
            break
        else:
            print('\n--------------\nPlease select a valid color.\n')

    # Initialize turtles
    turtles = []
    screen = Screen()
    width = screen.canvwidth
    height = screen.canvheight

    for i in range(len(turtle_colors)):
        temp_turtle = Turtle(visible=False)
        temp_turtle.penup()
        temp_turtle.color(turtle_colors[i])
        temp_turtle.shape('turtle')
        temp_turtle.setpos(-width + 30,(len(turtle_colors) * 30)/2 - (30 * i) )
        temp_turtle.showturtle()
        turtles.append(temp_turtle)


    # Make each turtle move randomly
    isRace = True
    win_turtle = None
    while isRace:

        for turtle in turtles:
            turtle.forward(randint(0, 25))

    # Check if any turtle has won
        for turtle in turtles:
            if turtle.xcor() > width - 50:
                isRace = False
                win_turtle = turtle.color()[0]

    # Display result to user
    print(f'The winning turtle is : {win_turtle}. | ', end='')
    if win_turtle == player_choice:
        print('You won!!')
    else:
        print('You lost!!')

    screen.exitonclick()
