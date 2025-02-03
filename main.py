# Lucas Brinks
# 2/3/25
# Dict MC

artists = {'Shinedown':'Thick as Thieves','Blacklite District':'Preach to the Choir','Gemini Syndrome':'Stardust','Crush 40':'I Am... All Of Me','Three Days Grace':'I Am Machine','Avenged Sevenfold':'So Far Away','Bring Me The Horizon':'Obet(with YUNGBLUD)','Blue Swede,  Björn Skifs':'Hooked On A Feeling'}

print(artists)

artists.update({'Shinedown':'What A Shame'})

print(artists)

for key, value in artists.items():
    print(key)
    print(value)
    print(key, value)