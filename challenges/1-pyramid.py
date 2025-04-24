height = int(input("\nPyramid height: ")) * 2
print("".join([f"\n{'*'+'*'*i:^{height}}" for i in range(0, height, 2)]) + "\n")
