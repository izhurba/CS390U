ofil = open("out_file.txt","w")
with open('input_file.txt','r') as d_in:
    for line in d_in:
        line2 = line.replace('o','X')
        ofil.write(line2)
        words = line2.split()
        for word in words:
            print(">>", word)
        print("\n*******************\n")
ofil.close()