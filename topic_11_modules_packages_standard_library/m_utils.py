import math

def sum_prod(seq_a, seq_b, debug=False):
    prod_seq_a = math.prod(seq_a)
    prod_seq_b = math.prod(seq_b)
    result = prod_seq_a + prod_seq_b
    if debug:
        print(f"{seq_a } prod_seq_a: {prod_seq_a}")
        print(f"{seq_b } prod_seq_b: {prod_seq_b}")
        print("result:", result)
    return result

# let's function that takes in unlimited number of sequences
def sum_prod_unlimited(*args, debug=False):
    result = 0
    for seq in args:
        prod_seq = math.prod(seq)
        result += prod_seq
        if debug:
            print(f"{seq } prod_seq: {prod_seq}")
            print("result:", result)
    return result

if __name__ == "__main__":
    print(sum_prod([2,3],[5,10,2], debug=True))
    print(sum_prod_unlimited(range(1,4), range(2,5), range(10,13), debug=True))
