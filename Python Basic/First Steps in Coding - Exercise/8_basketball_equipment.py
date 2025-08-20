year_tax = int(input())
shoes = year_tax - year_tax * 0.4
clothes = shoes - shoes * 0.2
ball = 0.25 * clothes
accessories = 1/5 * ball
print(shoes+clothes+ball+accessories+year_tax)