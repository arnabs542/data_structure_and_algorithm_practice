import heapq

def kth_most_frequent_word(arr, k):
    heap = []
    frequency = dict()
    for word in arr:
        if word in frequency:
            frequency[word] -= 1
        else:
            frequency[word] = -1

    for word,count in frequency.items():
        if len(heap) > 0 and heap[0][0]==count and word > heap[0][1]:
            top = heapq.heappop(heap)
            heapq.heappush(heap, (count,word))
            heapq.heappush(heap, top)
        else:
            heapq.heappush(heap, (count,word))

    while k > 0:
        heapq.heappop(heap)
        k-=1
    return heapq.heappop(heap)

print(kth_most_frequent_word(['hello', 'i', 'love', 'pathrise', 'i', 'love', 'coding'], 2))
