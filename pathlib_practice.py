import os
from pathlib import Path

print(Path.cwd()) # cwd means current working directory

#for p in Path().iterdir(): # Path() defaults to cwd, so a directory's contents can be printed by using the .iterdir() method
    #print(p)

my_dir = Path("Directory_1")
my_file = Path("text_based.py")

new_file = my_dir / "new_file.txt" # if you don't want to use the slash operator, the .joinpath("str") method will do the same thing

print(my_dir.name) # calling just the object name (my_ dir or my_file in this case) will have the same result
print(my_file.name) 

print(my_dir.stem)
print(my_file.stem)

print(my_dir.suffix)
print(my_file.suffix)

print(new_file)

print(my_dir.exists())
print(my_file.exists())
print(new_file.exists())

print(my_dir.parent)
print(my_file.parent)
print(new_file.parent)
