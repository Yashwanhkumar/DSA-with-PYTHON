arr = [-1,0,1,2,-1,-4]
n = len(arr)
unique_triplets = set()

for i in range(n):
    # Use a set to store seen elements for this i
    seen = set()
    for j in range(i+1, n):
        third = -(arr[i] + arr[j])
        if third in seen:
            triplet = tuple(sorted([arr[i], arr[j], third]))
            unique_triplets.add(triplet)
        seen.add(arr[j])

# Print all unique triplets
for triplet in unique_triplets:
    print(list(triplet))
