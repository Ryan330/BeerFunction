def song_line(numbottles):
    return "%d bottles of beer on the wall, %d bottles of beer. Take one down, pass it around, %d bottles of beer on the wall!" % (numbottles, numbottles, numbottles - 1)

totalofbottles = 99
for num in range(totalofbottles + 1, 0, -1):
    print(song_line(num))