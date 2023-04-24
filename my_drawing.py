import turtle as t


def cube(t, x, y, w, h, hand):
    t.up()
    t.goto(x, y)
    t.setheading(0)

    t.down()

    if hand == 'right':
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    elif hand == 'left':
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    else:
        print(f'手性错误: {hand}')

    t.up()


t.setup(1000, 800)
#t.done()

def turn_left_line(t,length):
   if length < 0:
      return

   t.left(90)
   t.forward(length)

   turn_left_line(t,length-5)

t.setup(1000,800)
t.down()

turn_left_line(t,240)

t.done()