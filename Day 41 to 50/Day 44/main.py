import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# spotify


oauth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=oauth)

ultimate_list = []
song_ids = []

# format 2022-month-day
def get_date():
    var = str(input("Enter Date. {format: YYYY }"))
    if len(var) < 10 or len(var) > 10:
        exit("Date should be in this format {format: YYYY } ")
    else:
        return var


# date = get_date()
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/2022-06-08/")
soup = BeautifulSoup(response.text, "html.parser")

a = soup.select(selector="div", class_='o-chart-results-list-row-container')

for div in a:
    new_soup = BeautifulSoup(str(div), "html.parser")
    list1 = new_soup.select(selector="li", class_='lrv-u-width-100p')
    if not list1:
        None
        # print("nope")
    else:
        for ul in list1:
            new_new_soup = BeautifulSoup(str(ul), "html.parser")
            song = new_new_soup.select(selector="h3", id="title-of-a-story",
                                       class_="c-title  a-no-trucate a-font-primary-bold-s "
                                              "u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 "
                                              "u-line-height-125 u-line-height-normal@mobile-max "
                                              "a-truncate-ellipsis u-max-width-245 "
                                              "u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
            if not song:
                None
            else:
                final = BeautifulSoup(str(song[0]), "html.parser")
                ultimate_list.append(final.getText().strip("\n\n\t\n\t\n\t\t\n\t\t\t\t\t").strip("\t\t\n\t\n"))

for song in ultimate_list:
    s_result = sp.search(q=song, type="track", limit=1)
    song_ids.append(s_result['tracks']['items'][0]['album']['id'])
    # print(song_ids[-1])
    # sp.user_playlist_create(name=date, user=username)
sp.playlist_add_items(username, "2tjTrGcX2sa2LHGocgd7HS", song_ids)


# TODO: Need a better way to complie spotify list. billboard site is broken.