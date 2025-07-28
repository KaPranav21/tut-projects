def celciusToFK(cel):
    far = cel * (9/5) + 32
    kel = cel + 273.15 
    print("F: ", float(far)," C: ", float(cel), " K: ", float(kel))
    # (far, cel, kel)

def faranToCK(far):
    cel = (far - 32) * (5/9)
    kel = cel + 273.15
    print("F: ", float(far)," C: ", float(cel), " K: ", float(kel))
    # return (far, cel, kel)

def kelvinToFC(kel):
    cel = kel - 273.15
    far = cel * (9/5) + 32 
    print("F: ", float(far)," C: ", float(cel), " K: ", float(kel))
    # return (far, cel, kel)

if __name__ == "__main__":
    degree = int(input("convert what number?: "))
    op = ''
    while op not in ['f', 'c', 'k']:
        op = input("Select unit: (f, c, k)")
        if op not in ['f', 'c', 'k']:
            print('not a valid unit')

    if op == 'f':
        faranToCK(degree)
    elif op == 'c':
        celciusToFK(degree)
    elif op == 'k':
        kelvinToFC(degree)
