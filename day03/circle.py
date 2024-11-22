--import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--radius', help='Enter circle radius', required=True, type=int)

args = parser.parse_args()

radius = args.radius

area = (math.pi) * (radius**2)
circumference = 2 * (math.pi) * radius

print("Circle area:", area)
print("Circle circumference:", circumference)