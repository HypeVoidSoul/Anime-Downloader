info_btn = "More Information"
kaizoku_btn = "Kaizoku ☠️"
kayo_btn = "Kayo 🏴‍☠️"
prequel_btn = "⬅️ Prequel"
sequel_btn = "Sequel ➡️"
close_btn = "Close ❌"
airing_query = """
query ($id: Int,$search: String) { 
Media (id: $id, type: ANIME,search: $search) {
id
episodes
title {
romaji
english
native}
nextAiringEpisode {
airingAt
timeUntilAiring
episode}}}
"""
fav_query = """
query ($id: Int) {
Media (id: $id, type: ANIME) {
id
title{
romaji
english
native
}}}
"""
anime_query = """
query ($id: Int,$search: String) {
Media (id: $id, type: ANIME,search: $search) {
id
title{
romaji
english
native
}
description (asHtml: false)
startDate{
year
}
episodes
season
type
format
status
duration
siteUrl
studios{
nodes{
name
}}
trailer{
id
site
thumbnail
}
averageScore
genres
bannerImage
}}
"""
character_query = """
query ($query: String){
Character (search: $query){
id
name{
first
last
full
}
siteUrl
image{
large
}
description
}}
"""
manga_query = """
query ($id: Int,$search: String) { 
Media (id: $id, type: MANGA,search: $search) { 
id
title {
romaji
english
native
}
description (asHtml: false)
startDate{
year
}
type
format
status
siteUrl
averageScore
genres
bannerImage
}}
"""
url = "https://graphql.anilist.co"
HELPABLE = {}
HELP_STRINGS = """—⚡️••÷[  Aռɨʍɛ-աɛɛɮɛʀ  ]÷••⚡️—

火• /anime <anime>
 returns information about the anime.
 
火• /manga <manga>
 returns information about the manga.
 
火• /upcoming 
 returns a list of new anime in the upcoming seasons.
 
火• /kaizoku <anime>
 search an anime on animekaizoku.com
 
火• /kayo <anime>
 search an anime on animekayo.com


—⚡️••÷[  Aռɨʍɛ-աɛɛɮɛʀ  ]÷••⚡️—"""
HELPABLE = {}
PM_START_TEXT = """—⚡️••÷[  Aռɨʍɛ-աɛɛɮɛʀ  ]÷••⚡️—

I am Anime Searcher and Downloader by @HypeVoidLab

I AM IN MY EARLY BETA STAGE SO DO KNOW MINOR BUGS ARE PRESENT.

—⚡️••÷[  Aռɨʍɛ-աɛɛɮɛʀ  ]÷••⚡️—"""
IMPORTED = {}
HELPABLE = {}
ASTRAKOBOT_IMG = "https://telegra.ph/file/327ae4aca7dee0d5dd67c.jpg"
UT = __help__ = """—⚡️••÷[  Aռɨʍɛ-աɛɛɮɛʀ  ]÷••⚡️—

Get information about anime, manga.

*Available commands:*

火• /anime <anime>
 returns information about the anime.
 
火• /manga <manga>
 returns information about the manga.
 
火• /upcoming 
 returns a list of new anime in the upcoming seasons.
 
火• /kaizoku <anime>
 search an anime on animekaizoku.com
 
火• /kayo <anime>
 search an anime on animekayo.com

—⚡️••÷[  Aռɨʍɛ-աɛɛɮɛʀ  ]÷••⚡️—"""