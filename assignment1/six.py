color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("color:", color)

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = ['Purple' if item in ['Black', 'Pink'] else item for item in color]
print("color:", color)
