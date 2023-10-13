def count_deaf_rats(town):
    # First, remove all spaces from the input string
    town = town.replace(' ', '')
    
    # Find the position of the Pied Piper ('P')
    piper_index = town.index('P')
    
    # Initialize counters for deaf rats before and after the Pied Piper
    deaf_rats_before = 0
    deaf_rats_after = 0
    
    # Iterate through the town string and count deaf rats
    for i in range(0, piper_index, 2):
        if town[i:i+2] == 'O~':
            deaf_rats_before += 1
    
    for i in range(piper_index + 1, len(town), 2):
        if town[i:i+2] == '~O':
            deaf_rats_after += 1
    
    return deaf_rats_before + deaf_rats_after