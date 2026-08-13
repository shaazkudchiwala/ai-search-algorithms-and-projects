import os

new_directory = r"c:\Users\Shaaz\Desktop\AI_Practical_College\Final"
os.chdir(new_directory)

for i in range(1, 7):
    folder_name = f"AI_Prac_{i}"
    os.mkdir(folder_name)
    print(f"Created: {folder_name}")
