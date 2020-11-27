array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        # 왼쪽에서부터 pivot보다 크면 break
        while left<=end and array[left]<=array[pivot]:
            left+=1
        # 오른쪽에서부터 pivot보다 작으면 break
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right:# 엇갈렸다면 작은 데이터와 pivot 교환
            # while문 탈출 직전
            array[right], array[pivot] = array[pivot], array[right]
        else:# 엇갈리지 않았다면 작은 데이터와 큰 데이터 교환
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)