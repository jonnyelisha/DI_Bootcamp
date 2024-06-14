matrix = [
    ["7", "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

secret_message = ""

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
            secret_message += char
        elif char != " ":
            secret_message += " "

print(secret_message)
