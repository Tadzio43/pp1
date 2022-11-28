def letter_count(str):
    count = 0
    for i in str:
        if i == "e":
            count = count + 1
    return count
    
print(letter_count("jem wiele melonów"))