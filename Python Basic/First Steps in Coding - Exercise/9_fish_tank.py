length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height
volume_leters = volume / 1000
volume_leters = volume_leters -  volume_leters * percent
print(volume_leters)