
def clean_file(src_file,dest_file,good_text="",bad_text=""):
    # TODO
    # open src_file
    # keep only lines with good text BUT not with bad_text
    # save onto dest_file overwritting the existing file there
    print(f"Cleaned file {src_file} and saved onto {dest_file}")

def clean_file_many(src_file,dest_file,good_texts=(),bad_texts=()):
    # TODO
    # open src_file
    # keep only lines with any good text BUT NOT with ANY bad text
    # save onto dest_file overwritting the existing file there
    print(f"Cleaned file {src_file} and saved onto {dest_file}")

def clean_folder_many_texts(src_folder,dest_folder, src_postfix=".txt",dest_postfix="_cleaned.txt", good_texts=(),bad_texts=()):
    # TODO
    # open src_folder
    # keep only lines with good text BUT not with bad_text
    # check for default edge cases when good_texts and/or bad_texts are empty