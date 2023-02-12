def group_by_owners(files):
    dic ={}
    res = {files[sub] for sub in files}
    #print(res)

    for i in res:
        keys = [k for k, v in files.items() if v == i]
        dic[i] = keys
    #print(dic)
    return dic

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))