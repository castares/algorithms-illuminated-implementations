
def merge(array_a, array_b, input_array):
    i = 0 # index array_a
    j = 0 # index array_b
    while i + j < len(input_array):
        if j == len(array_b) or (i < len(array_a) and array_a[i] < array_b[j]):
            input_array[i+j] = array_a[i]
            i+=1
        else:
            input_array[i+j] = array_b[j]
            j+=1
        print(f"output_array: {input_array}")

    return input_array

def merge_sort(input_array):
    """
    Max Running Time: 6n*log2n+6n

    """
    print(f"input_array: {input_array}")
    input_length = len(input_array)
    if input_length <= 2:
        return sorted(input_array)
    split = input_length // 2
    array_a = merge_sort(input_array[:split])
    array_b = merge_sort(input_array[split:])
    return merge(array_a, array_b, input_array)

if __name__ == "__main__":
    merge_sort([2,3,1,5,7,2,4])
