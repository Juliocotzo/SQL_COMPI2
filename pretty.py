from prettytable import PrettyTable

def toPretty(arr):
    x = PrettyTable()
    x.field_names = arr[0]
    if len(arr) > 1:
        i = 1
        while i < len(arr):
            x.add_row(arr[i])
            i+=1 
    
    return str(x)

print(toPretty(arregloTabla))