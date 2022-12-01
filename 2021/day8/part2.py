import sys

# Used this as a reference: https://imgur.com/a/LIS2zZr

input = sys.argv[1] if len(sys.argv) > 1 else 'day8/input.txt'
with open(input, 'r') as f:
    sum = 0
    for line in f:
        # Split the input before and after the pipe
        signal, output = line.strip().split(' | ')
        signal = signal.split()
        output = output.split()

        # Init storage
        nums = {0: '', 1: '', 2: '', 3: '', 4: '',
                5: '', 6: '', 7: '', 8: '', 9: ''}
        len6 = list()
        len5 = list()

        # Set known values, store unknown for later
        for code in signal:
            length = len(code)
            codeset = set(code)
            if length == 2:
                nums[1] = codeset
            if length == 3:
                nums[7] = codeset
            if length == 4:
                nums[4] = codeset
            if length == 5:
                len5.append(codeset)
            if length == 6:
                len6.append(codeset)
            if length == 7:
                nums[8] = codeset

        # Determine 0, 6, and 9
        for code in len6:
            codeset = set(code)
            if nums[4].issubset(codeset):
                nums[9] = codeset
            elif nums[7].issubset(codeset):
                nums[0] = codeset
            else:
                nums[6] = codeset

        # Determine 3, 5, and 2
        for code in len5:
            codeset = set(code)
            if nums[7].issubset(codeset):
                nums[3] = codeset
            elif len(codeset.intersection(nums[4])) == 3:
                nums[5] = codeset
            else:
                nums[2] = codeset

        # Decode each digit in the output
        digits = ''
        for n in output:
            s = set(n)
            for i, key in enumerate(nums.values()):
                if s == key:
                    digits = digits + str(i)

        # Add it to the total
        sum += int(digits)
    print(f'Part 2: {sum}')
