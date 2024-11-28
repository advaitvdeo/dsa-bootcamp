def subsets(string, ds, index):
    if index == len(string):
        print(ds)
        return

    subsets(string, ds + string[index], index+1)
    subsets(string, ds, index+1)


string = "abc"
subsets(string, "", 0)