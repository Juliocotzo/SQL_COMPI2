
def find_ARR(line,arr):
    i=0
    while i < len(arr):
        if arr[i] == line:
            return False
        i+=1
    return True

SELECT1 = [[1,2,3,4],[5,6,7,8],[1,3,5,7]]
SELECT2 = [[1,2,3,4],[2,4,6,8],[1,3,5,7]]

arr_INTERSECT = []
i=0
while i<len(SELECT1):
    j=0
    while j<len(SELECT2):
        if SELECT1[i] == SELECT2[j]:
            arr_INTERSECT.append(SELECT1[i])

        j+=1
    i+=1
arr_EXCEPT = []
arrE = 0
while arrE < len(SELECT1):
    val = find_ARR(SELECT1[arrE],arr_INTERSECT)
    if val:
        arr_EXCEPT.append(SELECT1[arrE])
    arrE+=1

print(arr_EXCEPT)


