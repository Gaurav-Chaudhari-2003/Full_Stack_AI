import os

for i in range(3, 6):
    location = 'G:\\Full Stack AI\\w1_assignments\\';
    os.mkdir(f'{location}q{i}')
    open(f"{location}q{i}\\main.py", "x")

