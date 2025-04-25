print((lambda h: "".join([f"\n{'*'+'*'*i:^{abs(h)}}" for i in range(*(0, h, 2) if h > -1 else (abs(h+2), -1, -2))]) + "\n")(int(input("\nPyramid height: ")) * 2))

# Everything in a fucking one line of fucking python fucking code. And it works for fucking reversed pyramids as well.

# Code Repo: https://github.com/GTazz/Python-challenges/blob/main/challenges/1-pyramid.py
