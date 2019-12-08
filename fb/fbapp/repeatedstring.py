string = "eeeabdbaaddd"
i = 0
max_count = 0
while i < len(string):
    character_count = string[0:i+1].count(string[i])
    if character_count > max_count:
        max_count = character_count
        outputCharacter = string[i]
    i+=1
print(outputCharacter)
