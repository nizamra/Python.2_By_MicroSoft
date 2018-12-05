#use comparison operators while iterating lists
# [ ] review and run example of sorting into strings to display
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
longer_names = ""
shorter_names = ""

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += "\n" + bone_name
    else:
        longer_names += "\n" + bone_name

print(shorter_names)
print(longer_names)

# [ ] review and run example of sorting into lists
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
longer_names = []
shorter_names = []

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names.append(bone_name)
    else:
        longer_names.append(bone_name)

print(shorter_names)
print(longer_names)