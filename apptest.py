from app import view_all_files

try:
    
    all_files = view_all_files()
    print(all_files)
except Exception as e:
    r"error : {e}"