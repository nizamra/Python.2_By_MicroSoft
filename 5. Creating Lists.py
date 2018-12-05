#A simple lists contains comma separated objects enclosed in square brackets
empty_list = [ ]
sample_list = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]
# List object types are not restricted so a mix of object types can be in single list
# mixed_list = [1, 1, "one", "two", 2.0, sample_list, "Hello World"]

# define list of strings
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
# display type information
print("ft_bones: ", type(ft_bones))
# print the list
print(ft_bones)
print(ft_bones[1], "is connected to the",ft_bones[3])