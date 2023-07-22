import subprocess
import os

script_path = r'C:\Users\anush\Projects\memo_converter\extractmemos.py'
memos_dir = r'C:\Users\anush\Downloads\Mums_drive\memos'

file_no = 1
for i in os.listdir(memos_dir):
    memo_path = os.path.join(memos_dir, i)
    name = 'recipe_' + str(file_no) + '.txt'
    doc_path = os.path.join(r'C:\Users\anush\Downloads\Mums_drive\memo_docs', name)
    with open(doc_path, "w") as output:
        subprocess.call(["python", script_path, memo_path], stdout=output)
    file_no += 1
print("Done!")