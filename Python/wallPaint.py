#Write your code below this line 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height=test_h, width=test_w, cover=coverage):
    paint_calc = round((height * width / cover),2)
    print(f'Hello you require {paint_calc} cans of paint')
    print(f'Please buy {paint_calc} cans for your wall painting')

paint_calc(height=test_h, width=test_w, cover=coverage)

