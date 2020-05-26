# Return the words of the initial song in a dubsteb remix.
#  Separate the words with a space.


def song_decoder(song):
    list_of_words = song.split("WUB")
    while "" in list_of_words:
        list_of_words.remove("")
    print(list_of_words)
    return " ".join(list_of_words)


print(song_decoder("HWUBNWUBWUBPWUBWUB"))
