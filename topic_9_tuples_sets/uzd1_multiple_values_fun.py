# Min, Avg, Max
def get_min_avg_max(sequence):
    if not sequence:
        raise ValueError("Sequence kaut kam vajadzētu būt")
        
    min_val = min(sequence)
    max_val = max(sequence)
    avg_val = sum(sequence) / len(sequence)
    
    return min_val, avg_val, max_val
 
print(get_min_avg_max([0, 10, 1, 9])) 