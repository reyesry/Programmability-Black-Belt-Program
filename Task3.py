
#Ryan Menard Reyes
#Task 1
#Blackbelt Apprentice Level 1

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

def find_even(number = []):
    myset = []
    for seq in number:
        for key, value in seq.items():
            x = value.split(",")
			
            i = 0
            y = len(x) - 1
            while i < y:
                z = int(x[i])
                if(z%2) == 0:
                    myset.append(z); 
                i = i + 1 
    
    print("The even numbers are : " , str(myset).strip("[]"))
    
    
find_even(numbers)
