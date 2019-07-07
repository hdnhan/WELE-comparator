#There was an error "Non-ASCII character '\xe2' in file" in the Standardize_File
with open("Standardize_File_Docx.py") as fp:
    for i, line in enumerate(fp):
        if "\x92" in line:
            print i, repr(line)
