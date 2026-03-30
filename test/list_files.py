from pathlib import Path # for interecting with file system
current_dir = Path.cwd() # get current working directory

current_file = Path(__file__).name # get current file

for file in current_dir.iterdir(): # iterate through files in current directory
    if file.is_file(): # check if it's a file
        print(file.name) # print the name of the file 
        if file.name == current_file: # check if it's the current file
            continue
        print(file.name) # print the name of the file if it's not the current file

        content = file.read_text(encoding='utf-8') # read the content of the file
        print(content) # print the content of the file 