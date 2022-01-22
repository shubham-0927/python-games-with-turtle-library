a= int(input('''
1. ice_ball game
2. snake game
3. ping-pong ball
3. exit()
enter your choice: '''))

if a == 1:
    from files import ice_ball
    exec(open('ice_ball.py').read())
elif a == 2:
    from files import Snake_game
    exec(open('Snake_game.py').read())
elif a == 3:
    from files import ping_pong
    exec(open('ping_pong.py').read())

else :
    exit()

print("THANK YOU")
