# Create a tuple of strings because we don't want people to mutate our list. Our list will be outside of teh function so that we can add strings to it. It'll be a tuple so that no one mutates it on accident.

x = ['cat']
y = x
x.append('dog')
""" Print Output:
    x = "cat", "dog"
    y = "cat", "dog"
"""

t = 'cat'
g = t
t += 'dog' # t = "catdog"

print(x, y) # ['cat','dog'] ['cat','dog']

kousei_playlist = ['光るなら', '七色シンフォニー', 'キラメキ', 'Orange']
kaori_playlist = kousei_playlist[1:4] # ['七色シンフォニー', 'キラメキ', 'Orange']
kousei_playlist.append('春の香り') # ['光るなら', '七色シンフォニー', 'キラメキ', 'Orange', '春の香り']

print(kaori_playlist)
print(kousei_playlist)
