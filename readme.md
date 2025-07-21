# Add to Playlist
This is a repository containing data about <a href="https://www.bbc.co.uk/programmes/m00106lb" target="_blank">Add to Playlist</a> - a BBC Radio 4 show which selects and discusses several tracks for a "playlist" in each episode.

While it's possible to view each _individual_ episode's playlist tracks on the BBC Sounds website, it's not possible to view them all as one big list.

The primary motivation of this project was to create such a list, which is displayed further down on this page.

As well as each track's name and artist(s), included where possible is a link to Spotify (or YouTube when the former is unavailable).

An asterisk (\*) next to an episode number indicates a one-off special where the tracks do not connect to the previous/following episodes.

Also included are links to several Spotify playlists: one playlist per series, and one big playlist for the entire series as a whole.


### About

Most of the data shown in the tables below was gathered automatically by scraping each episode's BBC Sounds page, parsing the HTML, then querying Spotify's Web API to find a recording.

Due to the nature of Spotify's API, there may be slight inconsistencies between the Spotify link and the version of the track played in the show, e.g. a remixed version may appear before the original version in Spotify's search results.

Care has been taken, however, to find the exact recordings used in the show where possible (by using music identification software such as Shazam and SoundHound).

The descriptions of how the tracks relate to each other were written manually up until series 4, episode 7, when AI was used to speed up the process - first, using [Whisper](https://github.com/openai/whisper) to create transcripts of each episode, then uploading the transcripts to [Claude](https://claude.ai/new) and [DeepSeek](https://chat.deepseek.com/) for analysis. Finally, the AI output was reviewed, corrected when needed, and then added to the tables.

Although care has been taken to make this page as accurate as possible, there will probably be a few mistakes; corrections are therefore very much welcomed!


---


### Contents

1. [Overview (All Series)](#overview-all-series)
2. [Top 25 Artists](#top-25-artists)
3. [Series 1](#series-1)
4. [Series 2](#series-2)
5. [Series 3](#series-3)
6. [Series 4](#series-4)
7. [Series 5](#series-5)
8. [Series 6](#series-6)
9. [Series 7](#series-7)
10. [Series 8](#series-8)
11. [Series 9](#series-9)
12. [Series 10](#series-10)
13. [Series 11](#series-11)
14. [Series 12](#series-12)
15. [Series 13](#series-13)



## Overview (All Series)

A Spotify playlist containing every track chosen in the series so far can be found [here](https://open.spotify.com/playlist/2PgU4Fct9zICx1Hbt4X8N0) (excluding, of course, the small number of tracks that aren't available on Spotify).

<table>
 <thead>
  <tr>
   <th align="left">
    Series
   </th>
   <th align="left">
    Ep. Overall
   </th>
   <th align="left">
    Ep. in Series
   </th>
   <th align="left">
    Tracks Overall
   </th>
   <th align="left">
    Broadcast
   </th>
   <th align="left">
    Playlist Link
   </th>
   <th align="left">
    Ep. Link
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="8">
    1
   </td>
   <td>
    1
   </td>
   <td>
    1
   </td>
   <td>
    5
   </td>
   <td>
    8 October 2021
   </td>
   <td rowspan="8">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/4HLH5EHjBPOpXuLto27Cf2" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00106l9" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    2
   </td>
   <td>
    2
   </td>
   <td>
    10
   </td>
   <td>
    15 October 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0010hq8" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    3
   </td>
   <td>
    3
   </td>
   <td>
    15
   </td>
   <td>
    22 October 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0010ntz" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    4
   </td>
   <td>
    4
   </td>
   <td>
    20
   </td>
   <td>
    29 October 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0010xvk" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    5
   </td>
   <td>
    5
   </td>
   <td>
    25
   </td>
   <td>
    5 November 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00114v2" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    6
   </td>
   <td>
    6
   </td>
   <td>
    30
   </td>
   <td>
    12 November 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0011cd7" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    7
   </td>
   <td>
    7
   </td>
   <td>
    35
   </td>
   <td>
    19 November 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0011lq4" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    8
   </td>
   <td>
    8
   </td>
   <td>
    40
   </td>
   <td>
    26 November 2021
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0011tc5" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="8">
    2
   </td>
   <td>
    9
   </td>
   <td>
    1
   </td>
   <td>
    45
   </td>
   <td>
    4 February 2022
   </td>
   <td rowspan="8">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/0757rUOarwlkD2olfe7sRo" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0013zsz" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    10
   </td>
   <td>
    2
   </td>
   <td>
    50
   </td>
   <td>
    11 February 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00146jd" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    11
   </td>
   <td>
    3
   </td>
   <td>
    55
   </td>
   <td>
    18 February 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0014gvc" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    12
   </td>
   <td>
    4
   </td>
   <td>
    60
   </td>
   <td>
    25 February 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0014qdx" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    13
   </td>
   <td>
    5
   </td>
   <td>
    65
   </td>
   <td>
    4 March 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0014xy8" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    14
   </td>
   <td>
    6
   </td>
   <td>
    70
   </td>
   <td>
    11 March 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00154qh" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    15
   </td>
   <td>
    7
   </td>
   <td>
    75
   </td>
   <td>
    18 March 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0015bc3" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    16
   </td>
   <td>
    8
   </td>
   <td>
    80
   </td>
   <td>
    25 March 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0015l17" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="9">
    3
   </td>
   <td>
    17
   </td>
   <td title="This episode was a one-off special.">
    1*
   </td>
   <td>
    85
   </td>
   <td>
    3 June 2022
   </td>
   <td rowspan="9">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/29PDzvsHMt25PHW4xHW5Js" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0017tjx" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    18
   </td>
   <td>
    2
   </td>
   <td>
    90
   </td>
   <td>
    10 June 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00181mm" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    19
   </td>
   <td>
    3
   </td>
   <td>
    95
   </td>
   <td>
    17 June 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001886f" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    20
   </td>
   <td>
    4
   </td>
   <td>
    100
   </td>
   <td>
    24 June 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0018h1y" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    21
   </td>
   <td>
    5
   </td>
   <td>
    105
   </td>
   <td>
    1 July 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0018p1s" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    22
   </td>
   <td>
    6
   </td>
   <td>
    110
   </td>
   <td>
    8 July 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0018xky" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    23
   </td>
   <td>
    7
   </td>
   <td>
    115
   </td>
   <td>
    15 July 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00194cn" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    24
   </td>
   <td>
    8
   </td>
   <td>
    120
   </td>
   <td>
    22 July 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0019b63" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    25
   </td>
   <td>
    9
   </td>
   <td>
    125
   </td>
   <td>
    29 July 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0019kdt" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="9">
    4
   </td>
   <td>
    26
   </td>
   <td>
    1
   </td>
   <td>
    130
   </td>
   <td>
    7 October 2022
   </td>
   <td rowspan="9">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/4mwdzqcSij07oa1NRnPAju" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001cq8c" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    27
   </td>
   <td>
    2
   </td>
   <td>
    135
   </td>
   <td>
    14 October 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001cxsl" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    28
   </td>
   <td>
    3
   </td>
   <td>
    140
   </td>
   <td>
    21 October 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001d5rb" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    29
   </td>
   <td>
    4
   </td>
   <td>
    145
   </td>
   <td>
    28 October 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001df0h" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    30
   </td>
   <td>
    5
   </td>
   <td>
    150
   </td>
   <td>
    4 November 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001dp3f" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    31
   </td>
   <td>
    6
   </td>
   <td>
    155
   </td>
   <td>
    11 November 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001dxqc" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    32
   </td>
   <td>
    7
   </td>
   <td>
    160
   </td>
   <td>
    18 November 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001f5kc" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    33
   </td>
   <td>
    8
   </td>
   <td>
    165
   </td>
   <td>
    25 November 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001fdb7" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    34
   </td>
   <td>
    9
   </td>
   <td>
    170
   </td>
   <td>
    2 December 2022
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001fn6s" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="8">
    5
   </td>
   <td>
    35
   </td>
   <td>
    1
   </td>
   <td>
    175
   </td>
   <td>
    10 February 2023
   </td>
   <td rowspan="8">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/5qyhiiEWSnEqRBQ6wpFWCY" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001hxc5" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    36
   </td>
   <td>
    2
   </td>
   <td>
    180
   </td>
   <td>
    17 February 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001j4kn" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    37
   </td>
   <td>
    3
   </td>
   <td>
    185
   </td>
   <td>
    24 February 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001jcgj" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    38
   </td>
   <td>
    4
   </td>
   <td>
    190
   </td>
   <td>
    3 March 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001jldr" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    39
   </td>
   <td>
    5
   </td>
   <td>
    195
   </td>
   <td>
    10 March 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001jsww" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    40
   </td>
   <td>
    6
   </td>
   <td>
    200
   </td>
   <td>
    17 March 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001k17h" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    41
   </td>
   <td>
    7
   </td>
   <td>
    205
   </td>
   <td>
    24 March 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001k84y" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    42
   </td>
   <td>
    8
   </td>
   <td>
    210
   </td>
   <td>
    31 March 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001kh5v" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="9">
    6
   </td>
   <td>
    43
   </td>
   <td>
    1
   </td>
   <td>
    215
   </td>
   <td>
    9 June 2023
   </td>
   <td rowspan="9">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/0dremLIKIqv5Nd8geXlwDI" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001mm1c" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    44
   </td>
   <td>
    2
   </td>
   <td>
    220
   </td>
   <td>
    16 June 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001mtfw" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    45
   </td>
   <td>
    3
   </td>
   <td>
    225
   </td>
   <td>
    23 June 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001n238" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    46
   </td>
   <td>
    4
   </td>
   <td>
    230
   </td>
   <td>
    30 June 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001n8ym" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    47
   </td>
   <td>
    5
   </td>
   <td>
    236
   </td>
   <td>
    7 July 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001nh47" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    48
   </td>
   <td>
    6
   </td>
   <td>
    241
   </td>
   <td>
    14 July 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001npgc" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    49
   </td>
   <td>
    7
   </td>
   <td>
    246
   </td>
   <td>
    21 July 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001nw1r" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    50
   </td>
   <td>
    8
   </td>
   <td>
    251
   </td>
   <td>
    28 July 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001p22d" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    51
   </td>
   <td>
    9
   </td>
   <td>
    256
   </td>
   <td>
    4 August 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001p7rt" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="9">
    7
   </td>
   <td>
    52
   </td>
   <td>
    1
   </td>
   <td>
    261
   </td>
   <td>
    13 October 2023
   </td>
   <td rowspan="9">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/1fFOSM0O7ZHfkHq0H0TSIO" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001r7ww" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    53
   </td>
   <td>
    2
   </td>
   <td>
    266
   </td>
   <td>
    20 October 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001rh85" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    54
   </td>
   <td>
    3
   </td>
   <td>
    271
   </td>
   <td>
    27 October 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001rqzr" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    55
   </td>
   <td>
    4
   </td>
   <td>
    276
   </td>
   <td>
    3 November 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001rysb" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    56
   </td>
   <td>
    5
   </td>
   <td>
    281
   </td>
   <td>
    10 November 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001s63y" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    57
   </td>
   <td>
    6
   </td>
   <td>
    286
   </td>
   <td>
    17 November 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001sdyx" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    58
   </td>
   <td>
    7
   </td>
   <td>
    291
   </td>
   <td>
    24 November 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001smvw" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    59
   </td>
   <td>
    8
   </td>
   <td>
    296
   </td>
   <td>
    1 December 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001sv9b" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    60
   </td>
   <td>
    9
   </td>
   <td>
    301
   </td>
   <td>
    8 December 2023
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001t33x" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="8">
    8
   </td>
   <td>
    61
   </td>
   <td>
    1
   </td>
   <td>
    306
   </td>
   <td>
    9 February 2024
   </td>
   <td rowspan="8">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/0Ds5lazcAbTyJk4Znq4442" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001w1gw" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    62
   </td>
   <td>
    2
   </td>
   <td>
    311
   </td>
   <td>
    16 February 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001w8sy" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    63
   </td>
   <td>
    3
   </td>
   <td>
    316
   </td>
   <td>
    23 February 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001wjt0" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    64
   </td>
   <td>
    4
   </td>
   <td>
    321
   </td>
   <td>
    1 March 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001wrm8" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    65
   </td>
   <td>
    5
   </td>
   <td>
    326
   </td>
   <td>
    8 March 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001wy3f" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    66
   </td>
   <td>
    6
   </td>
   <td>
    331
   </td>
   <td>
    15 March 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001x5c6" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    67
   </td>
   <td>
    7
   </td>
   <td>
    336
   </td>
   <td>
    22 March 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001xfxf" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    68
   </td>
   <td>
    8
   </td>
   <td>
    341
   </td>
   <td>
    29 March 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001xng0" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="6">
    9
   </td>
   <td>
    69
   </td>
   <td>
    1
   </td>
   <td>
    346
   </td>
   <td>
    24 May 2024
   </td>
   <td rowspan="6">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/0e7JreuqtEFYMcNTTClDVC" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001zdv1" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    70
   </td>
   <td>
    2
   </td>
   <td>
    351
   </td>
   <td>
    31 May 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001zmbr" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    71
   </td>
   <td>
    3
   </td>
   <td>
    356
   </td>
   <td>
    7 June 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m001zw60" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    72
   </td>
   <td>
    4
   </td>
   <td>
    361
   </td>
   <td>
    14 June 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00202ss" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    73
   </td>
   <td>
    5
   </td>
   <td>
    366
   </td>
   <td>
    21 June 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00208pz" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    74
   </td>
   <td>
    6
   </td>
   <td>
    371
   </td>
   <td>
    28 June 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0020jfd" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="7">
    10
   </td>
   <td>
    75
   </td>
   <td>
    1
   </td>
   <td>
    376
   </td>
   <td>
    16 August 2024
   </td>
   <td rowspan="7">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/3TEi3V4NPez2gxSQPSrEON" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0021xvw" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    76
   </td>
   <td>
    2
   </td>
   <td>
    381
   </td>
   <td>
    23 August 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00224t0" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    77
   </td>
   <td>
    3
   </td>
   <td>
    386
   </td>
   <td>
    30 August 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0022cq5" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    78
   </td>
   <td>
    4
   </td>
   <td>
    391
   </td>
   <td>
    6 September 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0022l1k" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    79
   </td>
   <td>
    5
   </td>
   <td>
    396
   </td>
   <td>
    13 September 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0022skv" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    80
   </td>
   <td>
    6
   </td>
   <td>
    401
   </td>
   <td>
    20 September 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002309s" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    81
   </td>
   <td>
    7
   </td>
   <td>
    406
   </td>
   <td>
    27 September 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00237nb" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="7">
    11
   </td>
   <td>
    82
   </td>
   <td>
    1
   </td>
   <td>
    411
   </td>
   <td>
    26 November 2024
   </td>
   <td rowspan="7">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/5wqzfsRuWIWtMod5ro0MpV" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00254hv" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    83
   </td>
   <td>
    2
   </td>
   <td>
    416
   </td>
   <td>
    3 December 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0025c0p" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    84
   </td>
   <td>
    3
   </td>
   <td>
    421
   </td>
   <td>
    10 December 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0025lcp" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    85
   </td>
   <td>
    4
   </td>
   <td>
    426
   </td>
   <td>
    17 December 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0025w2d" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    86
   </td>
   <td title="This episode was a one-off special.">
    5*
   </td>
   <td>
    431
   </td>
   <td>
    25 December 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002622x" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    87
   </td>
   <td>
    6
   </td>
   <td>
    436
   </td>
   <td>
    31 December 2024
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00268xn" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    88
   </td>
   <td>
    7
   </td>
   <td>
    441
   </td>
   <td>
    7 January 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0026961" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="7">
    12
   </td>
   <td>
    89
   </td>
   <td>
    1
   </td>
   <td>
    446
   </td>
   <td>
    25 February 2025
   </td>
   <td rowspan="7">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/7b93UoWr6TY0LFfQIMYkMC" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0028388" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    90
   </td>
   <td>
    2
   </td>
   <td>
    451
   </td>
   <td>
    4 March 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00289xp" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    91
   </td>
   <td>
    3
   </td>
   <td>
    456
   </td>
   <td>
    11 March 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0028l3c" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    92
   </td>
   <td>
    4
   </td>
   <td>
    461
   </td>
   <td>
    18 March 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0028v4s" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    93
   </td>
   <td>
    5
   </td>
   <td>
    466
   </td>
   <td>
    25 March 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00290fc" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    94
   </td>
   <td>
    6
   </td>
   <td>
    471
   </td>
   <td>
    1 April 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m00297f4" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    95
   </td>
   <td>
    7
   </td>
   <td>
    476
   </td>
   <td>
    8 April 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m0029hwy" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="6">
    13
   </td>
   <td>
    96
   </td>
   <td>
    1
   </td>
   <td>
    481
   </td>
   <td>
    27 May 2025
   </td>
   <td rowspan="6">
    <span>
     <img height="16" src="images/spotify.png" width="16"/>
    </span>
    <a href="https://open.spotify.com/playlist/4A4zUOpersExaZmgbBygs1" target="_blank">
     Spotify
    </a>
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002cf4j" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    97
   </td>
   <td>
    2
   </td>
   <td>
    486
   </td>
   <td>
    3 June 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002cq5w" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    98
   </td>
   <td>
    3
   </td>
   <td>
    491
   </td>
   <td>
    10 June 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002czpv" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    99
   </td>
   <td>
    4
   </td>
   <td>
    496
   </td>
   <td>
    17 June 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002dc9t" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    100
   </td>
   <td>
    5
   </td>
   <td>
    501
   </td>
   <td>
    24 June 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002dlj1" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
  <tr>
   <td>
    101
   </td>
   <td>
    6
   </td>
   <td>
    506
   </td>
   <td>
    1 July 2025
   </td>
   <td>
    <span>
     <img height="16" src="images/bbc-sounds.png" width="16"/>
    </span>
    <a href="https://www.bbc.co.uk/programmes/m002f01w" target="_blank">
     BBC Sounds
    </a>
   </td>
  </tr>
 </tbody>
</table>



## Top 25 Artists
The following table lists the most-selected artists from the series overall.

Although a subjective topic, conductors and orchestras are excluded from this list to provide a more "accurate" ranking (otherwise artists such as Leonard Bernstein or the London Symphony Orchestra push others off the list).

<table>
 <thead>
  <tr>
   <th align="left">
    Position
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Total
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Chosen
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td rowspan="5">
    Joint 1st
   </td>
   <td rowspan="5">
    Wolfgang Amadeus Mozart
   </td>
   <td rowspan="5">
    5
   </td>
   <td>
    12 Variations in C Major on "Ah, vous dirai-je Maman", K. 265: Variation No. 3
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0013zsz" target="_blank">
     Series 2, ep. 1, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    O, wie will ich triumphieren (Die Entführung aus dem Serail)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001d5rb" target="_blank">
     Series 4, ep. 3, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Magic Flute: Der Vogelfänger bin ich ja (Birdcatcher's Song)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001p7rt" target="_blank">
     Series 6, ep. 9, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Mozart: Symphony No. 40 in G Minor, K. 550: I. Molto allegro
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001rysb" target="_blank">
     Series 7, ep. 4, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Ballet Intermezzo, K. 299c (Compl. &amp; Orch. Smith): VIII. Tambourin
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0025c0p" target="_blank">
     Series 11, ep. 2, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="5">
    Joint 1st
   </td>
   <td rowspan="5">
    Igor Stravinsky
   </td>
   <td rowspan="5">
    5
   </td>
   <td>
    L'oiseau de feu, K. 10. Suite 1919: V. Danse infernale du roi Kastchei
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0014xy8" target="_blank">
     Series 2, ep. 5, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Rite of Spring (Scenes of Pagan Russia in Two Parts): Part One - Spring Rounds (1921 Version)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001j4kn" target="_blank">
     Series 5, ep. 2, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Stravinsky: Petrushka, Pt. 1 "The Shrovetide Fair": The Charlatan's Booth - Russian Dance (1947 Version)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001rh85" target="_blank">
     Series 7, ep. 2, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Firebird Suite (1919 Version): VII. Finale
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001t33x" target="_blank">
     Series 7, ep. 9, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Rake's Progress: Act III Scene 3: Duet: In a foolish dream… (Tom, Anne)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002cq5w" target="_blank">
     Series 13, ep. 2, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="5">
    Joint 1st
   </td>
   <td rowspan="5">
    Ludwig van Beethoven
   </td>
   <td rowspan="5">
    5
   </td>
   <td>
    Symphony No. 3 in E-Flat Major, Op. 55 “Eroica”: I. Allegro con brio
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0017tjx" target="_blank">
     Series 3, ep. 1, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Symphony No. 9 in D Minor, Op. 125 "Choral": IV. Finale. Presto - Live
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001p7rt" target="_blank">
     Series 6, ep. 9, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Für Elise, Bagatelle in A Minor, WoO 59
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001smvw" target="_blank">
     Series 7, ep. 7, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    March – from A Clockwork Orange
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0022l1k" target="_blank">
     Series 10, ep. 4, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Piano Sonata No. 32 In C Minor, Op. 111: 2. Arietta (Adagio molto semplice e cantabile)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002dc9t" target="_blank">
     Series 13, ep. 4, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="4">
    Joint 4th
   </td>
   <td rowspan="4">
    Louis Armstrong
   </td>
   <td rowspan="4">
    4
   </td>
   <td>
    Heebie Jeebies
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m00114v2" target="_blank">
     Series 1, ep. 5, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    When The Saints Go Marching In
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001df0h" target="_blank">
     Series 4, ep. 4, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Basin Street Blues
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001dp3f" target="_blank">
     Series 4, ep. 5, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Summertime
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002309s" target="_blank">
     Series 10, ep. 6, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="4">
    Joint 4th
   </td>
   <td rowspan="4">
    Johann Sebastian Bach
   </td>
   <td rowspan="4">
    4
   </td>
   <td>
    Toccata and Fugue in D Minor, BWV 565
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0015bc3" target="_blank">
     Series 2, ep. 7, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Orchestral Suite No. 3 in D, BWV 1068: 2. Air
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001k17h" target="_blank">
     Series 5, ep. 6, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Well-Tempered Clavier, Book 1, BWV 846-869: Prelude and Fugue in C Major, BWV 846
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001wrm8" target="_blank">
     Series 8, ep. 4, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Concerto for Two Violins in D Minor, BWV 1043: I. Vivace
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002309s" target="_blank">
     Series 10, ep. 6, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="4">
    Joint 4th
   </td>
   <td rowspan="4">
    David Bowie
   </td>
   <td rowspan="4">
    4
   </td>
   <td>
    Starman - 2012 Remaster
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0018p1s" target="_blank">
     Series 3, ep. 5, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Lazarus
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001wrm8" target="_blank">
     Series 8, ep. 4, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Peter and the Wolf, Op. 67 (Remastered): The Duck, Dialogue with the Bird, Attack of the Cat
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001zdv1" target="_blank">
     Series 9, ep. 1, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Modern Love - 2002 Remaster
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002dc9t" target="_blank">
     Series 13, ep. 4, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="4">
    Joint 4th
   </td>
   <td rowspan="4">
    Ella Fitzgerald
   </td>
   <td rowspan="4">
    4
   </td>
   <td>
    It Don't Mean A Thing (If It Ain't Got That Swing)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001dxqc" target="_blank">
     Series 4, ep. 6, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    How High The Moon - 1st Take
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001xfxf" target="_blank">
     Series 8, ep. 7, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    My Bonnie Lies Over The Ocean
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m00224t0" target="_blank">
     Series 10, ep. 2, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Summertime
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002309s" target="_blank">
     Series 10, ep. 6, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="4">
    Joint 4th
   </td>
   <td rowspan="4">
    George Frideric Handel
   </td>
   <td rowspan="4">
    4
   </td>
   <td>
    Scherza infida
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001f5kc" target="_blank">
     Series 4, ep. 7, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Messiah, HWV 56, Part II: Aria "He was Despised and Rejected of Men" - 2021 Remastered Version
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001jsww" target="_blank">
     Series 5, ep. 5, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Zadok the Priest (Coronation Anthem No. 1, HWV 258)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001nh47" target="_blank">
     Series 6, ep. 5, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Eternal Source Of Light Divine (Ode For The Birthday Of Queen Anne), HWV 74
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0025c0p" target="_blank">
     Series 11, ep. 2, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="4">
    Joint 4th
   </td>
   <td rowspan="4">
    John Williams
   </td>
   <td rowspan="4">
    4
   </td>
   <td>
    Main Title And First Victim - From "Jaws" Soundtrack
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001s63y" target="_blank">
     Series 7, ep. 5, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Knight Bus - From "Harry Potter and the Prisoner of Azkaban"
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001zdv1" target="_blank">
     Series 9, ep. 1, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    The Imperial March (Darth Vader's Theme)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0029hwy" target="_blank">
     Series 12, ep. 7, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Star Wars Suite (arr. H. Feller): V. Throne Room - End Title
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002dlj1" target="_blank">
     Series 13, ep. 5, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Claude Debussy
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Préludes / Book 1, L. 117: VIII. La fille aux cheveux de lin
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010hq8" target="_blank">
     Series 1, ep. 2, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Clair de lune - Arr. for Theremin and Voice by Carolina Eyck
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001k84y" target="_blank">
     Series 5, ep. 7, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Pour le piano, CD 95: II. Sarabande
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0028v4s" target="_blank">
     Series 12, ep. 4, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Stevie Wonder
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Higher Ground
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010xvk" target="_blank">
     Series 1, ep. 4, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Sir Duke
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001hxc5" target="_blank">
     Series 5, ep. 1, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Fingertips, Pt. 2 - Live/1962
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001r7ww" target="_blank">
     Series 7, ep. 1, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    John Coltrane
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    After The Rain
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0013zsz" target="_blank">
     Series 2, ep. 1, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    So What (feat. John Coltrane, Cannonball Adderley &amp; Bill Evans)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001jsww" target="_blank">
     Series 5, ep. 5, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    A Love Supreme, Pt. I – Acknowledgement
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0025w2d" target="_blank">
     Series 11, ep. 4, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Lady Gaga
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Poker Face
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0017tjx" target="_blank">
     Series 3, ep. 1, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Bad Romance
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001wrm8" target="_blank">
     Series 8, ep. 4, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Abracadabra
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002cf4j" target="_blank">
     Series 13, ep. 1, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Elton John
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Don't Go Breaking My Heart
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0018p1s" target="_blank">
     Series 3, ep. 5, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Bennie And The Jets - Remastered 2014
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0022skv" target="_blank">
     Series 10, ep. 5, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Honky Cat
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m002czpv" target="_blank">
     Series 13, ep. 3, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Kate Bush
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Wuthering Heights - 2018 Remaster
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m00194cn" target="_blank">
     Series 3, ep. 7, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Snowflake - 2018 Remaster
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001k84y" target="_blank">
     Series 5, ep. 7, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Babooshka - 2018 Remaster
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001x5c6" target="_blank">
     Series 8, ep. 6, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Leonard Bernstein
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    America
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0019kdt" target="_blank">
     Series 3, ep. 9, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Overture to Candide
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001dp3f" target="_blank">
     Series 4, ep. 5, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Maria from West Side Story Suite - Instrumental
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0029hwy" target="_blank">
     Series 12, ep. 7, track 2
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Gustav Mahler
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Symphony No. 5: IV. Adagietto. Sehr langsam
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001n238" target="_blank">
     Series 6, ep. 3, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Piano Quartet in A Minor: I. Allegro
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001r7ww" target="_blank">
     Series 7, ep. 1, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Symphony No. 9 in D Major: Ia. Andante comodo
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001wrm8" target="_blank">
     Series 8, ep. 4, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="3">
    Joint 10th
   </td>
   <td rowspan="3">
    Beyoncé
   </td>
   <td rowspan="3">
    3
   </td>
   <td>
    Crazy In Love (feat. Jay-Z)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001n238" target="_blank">
     Series 6, ep. 3, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    TEXAS HOLD 'EM
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001xng0" target="_blank">
     Series 8, ep. 8, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Freedom - Homecoming Live
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001zmbr" target="_blank">
     Series 9, ep. 2, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    Antônio Carlos Jobim
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    The Girl From Ipanema
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010hq8" target="_blank">
     Series 1, ep. 2, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Meditation (Meditação)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001w1gw" target="_blank">
     Series 8, ep. 1, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    Juliette Gréco
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    Sous les ponts de Paris
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010hq8" target="_blank">
     Series 1, ep. 2, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Un petit poisson un petit oiseau
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001df0h" target="_blank">
     Series 4, ep. 4, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    Björk
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    It's Oh So Quiet
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010hq8" target="_blank">
     Series 1, ep. 2, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Venus as a Boy
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m00208pz" target="_blank">
     Series 9, ep. 5, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    The Hilliard Ensemble
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    Parce Mihi Domine
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010ntz" target="_blank">
     Series 1, ep. 3, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Ma fin est mon commencement, Rondeau 14
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001wy3f" target="_blank">
     Series 8, ep. 5, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    Nina Simone
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    Sinnerman
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010ntz" target="_blank">
     Series 1, ep. 3, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Don't Let Me Be Misunderstood
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0021xvw" target="_blank">
     Series 10, ep. 1, track 5
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    Simon Preston
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    Variations on a theme by Mozart for four harpsichords
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0010xvk" target="_blank">
     Series 1, ep. 4, track 4
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Zadok the Priest (Coronation Anthem No. 1, HWV 258)
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001nh47" target="_blank">
     Series 6, ep. 5, track 1
    </a>
   </td>
  </tr>
  <tr>
   <td rowspan="2">
    Joint 19th
   </td>
   <td rowspan="2">
    Charmian Carr
   </td>
   <td rowspan="2">
    2
   </td>
   <td>
    Edelweiss
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m0011cd7" target="_blank">
     Series 1, ep. 6, track 3
    </a>
   </td>
  </tr>
  <tr>
   <td>
    Do-Re-Mi
   </td>
   <td width="192">
    <a href="https://www.bbc.co.uk/programmes/m001dxqc" target="_blank">
     Series 4, ep. 6, track 5
    </a>
   </td>
  </tr>
 </tbody>
</table>


## Series 1

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00106l9" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Lil Nas X
    <br/>
    Billy Ray Cyrus
   </td>
   <td>
    <a href="https://open.spotify.com/track/2YpeDb67231RjR0MgVLzsG" target="_blank">
     Old Town Road - Remix
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Aaron Copland
    <br/>
    Colorado Symphony
    <br/>
    Andrew Litton
   </td>
   <td>
    <a href="https://open.spotify.com/track/77TGlE4E4OEDu2iBNuaLGA" target="_blank">
     Rodeo: No. 5, Hoe-Down
    </a>
   </td>
   <td width="128">
    Samples an existing melody.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Run–D.M.C.
    <br/>
    Aerosmith
   </td>
   <td>
    <a href="https://open.spotify.com/track/6qUEOWqOzu1rLPUPQ1ECpx" target="_blank">
     Walk This Way (feat. Aerosmith)
    </a>
   </td>
   <td width="128">
    Collaboration; cross-genre.
   </td>
   <td width="128">
    Kojo Samuel
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Dionne Warwick
   </td>
   <td>
    <a href="https://open.spotify.com/track/3xsOtNxtBW0oTI1OWKAzTm" target="_blank">
     Walk on By
    </a>
   </td>
   <td width="128">
    Titles reference walking.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Ottilie Patterson
    <br/>
    Chris Barber's Jazz Band
   </td>
   <td>
    <a href="https://open.spotify.com/track/5vWxd52nowVqjVYuE1fxYR" target="_blank">
     Let Him Go, Let Him Tarry
    </a>
   </td>
   <td width="128">
    Cross-genre.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0010hq8" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Stan Getz
    <br/>
    João Gilberto
    <br/>
    Antônio Carlos Jobim
   </td>
   <td>
    <a href="https://open.spotify.com/track/7z3l6quyFofhd78Vx94fi1" target="_blank">
     The Girl From Ipanema
    </a>
   </td>
   <td width="128">
    "Jazz take" of a traditional song.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Claude Debussy
    <br/>
    Víkingur Ólafsson
   </td>
   <td>
    <a href="https://open.spotify.com/track/3vSOD8Ng5m8eLH4EhoJcTL" target="_blank">
     Préludes / Book 1, L. 117: VIII. La fille aux cheveux de lin
    </a>
   </td>
   <td width="128">
    Relaxed, laid-back "portrait" of a girl.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Juliette Gréco
    <br/>
    Melody Gardot
   </td>
   <td>
    <a href="https://open.spotify.com/track/0GOYSnwm5SPUyfboTi8LNJ" target="_blank">
     Sous les ponts de Paris
    </a>
   </td>
   <td width="128">
    French.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Björk
   </td>
   <td>
    <a href="https://open.spotify.com/track/0OMNQyneWmmZtTQpULYJcl" target="_blank">
     It's Oh So Quiet
    </a>
   </td>
   <td width="128">
    Begins with French-sounding waltz.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    The Dave Brubeck Quartet
   </td>
   <td>
    <a href="https://open.spotify.com/track/1YQWosTIljIvxAgHWTp7KP" target="_blank">
     Take Five
    </a>
   </td>
   <td width="128">
    Popular piece of music not in a 4/4 time signature.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0010ntz" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Sachal Studios Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/640464KPzlcFMrsDolfyEb" target="_blank">
     The Pink Panther
    </a>
   </td>
   <td width="128">
    Sachal Studios Orchestra recorded previous track in an Indian classical style.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Sting
   </td>
   <td>
    <a href="https://open.spotify.com/track/4KFM3A5QF2IMcc6nHsu3Wp" target="_blank">
     Englishman In New York
    </a>
   </td>
   <td width="128">
    Famous saxophonists; cross-culture.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Jan Garbarek
    <br/>
    Cristobal de Morales
    <br/>
    The Hilliard Ensemble
   </td>
   <td>
    <a href="https://open.spotify.com/track/46tPGzCXCI2oKsemztDA9u" target="_blank">
     Parce Mihi Domine
    </a>
   </td>
   <td width="128">
    Saxophone.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Nina Simone
   </td>
   <td>
    <a href="https://open.spotify.com/track/5xRP5iyVdGglqlY4Vcjhkx" target="_blank">
     Sinnerman
    </a>
   </td>
   <td width="128">
    Lyrics reference sinning.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Hozier
    <br/>
    Mavis Staples
   </td>
   <td>
    <a href="https://open.spotify.com/track/4rcSvYi807urIIqfeX3tBo" target="_blank">
     Nina Cried Power (feat. Mavis Staples)
    </a>
   </td>
   <td width="128">
    Track's title refers to lyric in previous song.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0010xvk" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Edikanfo
   </td>
   <td>
    <a href="https://open.spotify.com/track/26dN5lHMksauvioMNwI3R9" target="_blank">
     Nka Bom
    </a>
   </td>
   <td width="128">
    Previous track references song with "distinctly African percussive energy".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Bee Gees
   </td>
   <td>
    <a href="https://open.spotify.com/track/3mRM4NM8iO7UBqrSigCQFH" target="_blank">
     Stayin' Alive - From "Saturday Night Fever" Soundtrack
    </a>
   </td>
   <td width="128">
    High-octane energy; groove; hi-hats.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Stevie Wonder
   </td>
   <td>
    <a href="https://open.spotify.com/track/0dMd4rilfd6gPbXaLpNYhu" target="_blank">
     Higher Ground
    </a>
   </td>
   <td width="128">
    Pentatonic scales; funky basslines; sense of survival.
   </td>
   <td width="128">
    Soweto Kinch
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    George Malcolm
    <br/>
    Valda Aveling
    <br/>
    Geoffrey Parsons
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Simon Preston
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/3LY17MUVlWF1rC4TBBlBxo" target="_blank">
     Variations on a theme by Mozart for four harpsichords
    </a>
   </td>
   <td width="128">
    Valda Aveling was a pupil of Violet Gordon-Woodhouse, who was influential in bringing the clavichord back into fashion (the pre-cursor to the Clavinet, which is associated with Stevie Wonder).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Luis Fonsi
    <br/>
    Daddy Yankee
    <br/>
    Justin Bieber
   </td>
   <td>
    <a href="https://open.spotify.com/track/6rPO02ozF3bM7NnOV4h6s2" target="_blank">
     Despacito - Remix
    </a>
   </td>
   <td width="128">
    Opening guitar riff sounds like a harpsichord.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00114v2" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Sophia Loren
    <br/>
    Paolo Bacilleri
   </td>
   <td>
    <a href="https://open.spotify.com/track/6TPZilI8mlXpnsMCkwV3OP" target="_blank">
     Tu Vuo Fa L' Americano
    </a>
   </td>
   <td width="128">
    Successful song both translated and in its original language.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Louis Armstrong
   </td>
   <td>
    <a href="https://open.spotify.com/track/3aUy1mENoki136roAaQpn5" target="_blank">
     Heebie Jeebies
    </a>
   </td>
   <td width="128">
    Contains unplanned moment (Paolo Bacilleri laughs in previous track; according to popular legend, Louis Armstrong dropped his lyric sheet during recording and improvised his vocals).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Sa Dingding
   </td>
   <td>
    <a href="https://open.spotify.com/track/0XkIj9XLzNi8q1vCGpNHPb" target="_blank">
     Ha Ha Lili
    </a>
   </td>
   <td width="128">
    Sings in a self-created/non-formal language.
   </td>
   <td width="128">
    Jasmin Kent Rodgman
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Giacomo Puccini
    <br/>
    Luciano Pavarotti
    <br/>
    Orchestra Del Teatro Dell'Opera Di Roma
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Orchestra del Maggio Musicale Fiorentino
     <br/>
     Zubin Mehta
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/7tNpjS22EB4K7DR6230PfJ" target="_blank">
     Turandot / Act 3: "Nessun dorma!" - Live
    </a>
   </td>
   <td width="128">
    From an opera set in China; features Chinese instruments and a recurring motif from a Chinese folk song.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Doris Day
    <br/>
    Jack Smith
   </td>
   <td>
    <a href="https://open.spotify.com/track/6piKfO63He2tQ9V2RPgJ8b" target="_blank">
     I'm Forever Blowing Bubbles
    </a>
   </td>
   <td width="128">
    Associated with football.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0011cd7" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Boswell Sisters
   </td>
   <td>
    <a href="https://open.spotify.com/track/6tQAMkPziolCQoRNwmG8tM" target="_blank">
     It Don't Mean A Thing
    </a>
   </td>
   <td width="128">
    Harmonies between voices.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Frank Ifield
   </td>
   <td>
    <a href="https://open.spotify.com/track/5E7gR6HVui3M3oWXzMDrEz" target="_blank">
     She Taught Me How to Yodel
    </a>
   </td>
   <td width="128">
    <em>
     No connection.
    </em>
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Bill Lee
    <br/>
    Charmian Carr
   </td>
   <td>
    <a href="https://open.spotify.com/track/6IepN5nR2WGxVCVNFxIgbu" target="_blank">
     Edelweiss
    </a>
   </td>
   <td width="128">
    Alps mountain range.
   </td>
   <td width="128">
    Joe Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Asha Bhosle
    <br/>
    R. D. Burman
   </td>
   <td>
    <a href="https://open.spotify.com/track/7l84ITKK71ZjjrwLkFj401" target="_blank">
     Piya Tu Ab To Aaja (From "Caravan")
    </a>
   </td>
   <td width="128">
    Playback singers.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Destiny's Child
   </td>
   <td>
    <a href="https://open.spotify.com/track/4dvQg9sD8k9y4qiEURuj8v" target="_blank">
     Lose My Breath
    </a>
   </td>
   <td width="128">
    Heavy breathing.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0011lq4" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Richard Wagner
    <br/>
    Dietrich Fischer-Dieskau
    <br/>
    Martti Talvela
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Berliner Philharmoniker
     <br/>
     Herbert von Karajan
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6LrjrlOBk1hX5O5ytKFPFo" target="_blank">
     Das Rheingold, Scene 2: Sanft schloß Schlaf dein Aug'
    </a>
   </td>
   <td width="128">
    Brass instrumentation.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Herlin Riley
    <br/>
    Wycliffe Gordon
    <br/>
    Wynton Marsalis
    <details>
     <summary>
      <em>
       +3 more
      </em>
     </summary>
     Victor Goines
     <br/>
     Eric Lewis
     <br/>
     Reginald Veal
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/16xxrEYm6SpOc8DR2GiT4Y" target="_blank">
     Trombone Joe
    </a>
   </td>
   <td width="128">
    Brass instrumentation.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Carpenters
    <br/>
    Joe Raposo
   </td>
   <td>
    <a href="https://open.spotify.com/track/4VpKPtsc1Gfh2hH3AGSR3l" target="_blank">
     Sing
    </a>
   </td>
   <td width="128">
    The name "Joe".
   </td>
   <td width="128">
    Jamie Cullum
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Francis Bebey
   </td>
   <td>
    <a href="https://open.spotify.com/track/6qBkgf34enQ1CdaXDy46yr" target="_blank">
     The Coffee Cola Song
    </a>
   </td>
   <td width="128">
    Begins with wind instrument; also uses a simple instrument in a complex way (previous track used "complex" music but was simple/accessible).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Future
   </td>
   <td>
    <a href="https://open.spotify.com/track/0VgkVdmE4gld66l8iyGjgx" target="_blank">
     Mask Off
    </a>
   </td>
   <td width="128">
    Flute.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0011tc5" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Hildegard von Bingen
    <br/>
    Emily D'Angelo
    <br/>
    Mikayel Hakhnazaryan
   </td>
   <td>
    <a href="https://open.spotify.com/track/5ybJRjlZxgDF1ZR9t6mJx2" target="_blank">
     O frondens virga (Arr. Missy Mazzoli)
    </a>
   </td>
   <td width="128">
    "Overcoming substance abuse and finding spiritual healing".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Vangelis
   </td>
   <td>
    <a href="https://open.spotify.com/track/3zmXCcrMKpGho2sTRZG1Ux" target="_blank">
     Chariots Of Fire
    </a>
   </td>
   <td width="128">
    Opens with perfect fifth; "repeating electronic pulse".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Bob James
   </td>
   <td>
    <a href="https://open.spotify.com/track/6i5U5NyCknF93w4BilFity" target="_blank">
     Take Me To The Mardi Gras
    </a>
   </td>
   <td width="128">
    Slow/gradual build-up.
   </td>
   <td width="128">
    Dele Sosimi
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    The Doors
   </td>
   <td>
    <a href="https://open.spotify.com/track/14XWXWv5FoCbFzLksawpEe" target="_blank">
     Riders on the Storm
    </a>
   </td>
   <td width="128">
    Rhodes piano.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    The Weather Girls
   </td>
   <td>
    <a href="https://open.spotify.com/track/2IvetNzSZMH5gwjInoyr18" target="_blank">
     It's Raining Men
    </a>
   </td>
   <td width="128">
    Titles reference weather/rain.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 2

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0013zsz" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Rihanna
    <br/>
    JAY-Z
   </td>
   <td>
    <a href="https://open.spotify.com/track/2yPoXCs7BSIUrucMdK5PzV" target="_blank">
     Umbrella
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    John Coltrane
   </td>
   <td>
    <a href="https://open.spotify.com/track/2JQqfVJhFnNADUJDDPmw63" target="_blank">
     After The Rain
    </a>
   </td>
   <td width="128">
    Minor thirds.
   </td>
   <td width="128">
    Gary Crosby
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Wolfgang Amadeus Mozart
    <br/>
    Lang Lang
   </td>
   <td>
    <a href="https://open.spotify.com/track/01krwPhJ04YilFViTRPU1O" target="_blank">
     12 Variations in C Major on "Ah, vous dirai-je Maman", K. 265: Variation No. 3
    </a>
   </td>
   <td width="128">
    Fifth-based melodies.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Sister Nancy
   </td>
   <td>
    <a href="https://open.spotify.com/track/7ixiCZEHWHc8FxaQXQh2P4" target="_blank">
     Bam Bam
    </a>
   </td>
   <td width="128">
    Repeated double notes.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Peter Frampton
   </td>
   <td>
    <a href="https://open.spotify.com/track/6BD1X1PeV5UzYUdiVaD2yL" target="_blank">
     Show Me The Way
    </a>
   </td>
   <td width="128">
    Echo/vocal effects.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00146jd" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Natalie Imbruglia
   </td>
   <td>
    <a href="https://open.spotify.com/track/1Jaah2tmN9Hv81A87KZ1MU" target="_blank">
     Torn
    </a>
   </td>
   <td width="128">
    Acoustic guitar opening.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Henry Purcell
    <br/>
    Elin Manahan Thomas
    <br/>
    Orchestra of the Age of Enlightenment
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Harry Christophers
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6E0aZdQHJwTYfA7h5brKAI" target="_blank">
     When I Am Laid In Earth (Dido's Lament)
    </a>
   </td>
   <td width="128">
    Recurring chord pattern/ground bass.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Samthing Soweto
   </td>
   <td>
    <a href="https://open.spotify.com/track/2s3DNGPdbghtwgpLVMQCTz" target="_blank">
     Ndofire/Skado
    </a>
   </td>
   <td width="128">
    Similar chromatic ground bass.
   </td>
   <td width="128">
    Abel Selaocoe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Justin Timberlake
   </td>
   <td>
    <a href="https://open.spotify.com/track/7Lf7oSEVdzZqTA0kEDSlS5" target="_blank">
     Cry Me a River
    </a>
   </td>
   <td width="128">
    Overlapping multi-layered vocals.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Paprika
   </td>
   <td>
    <a href="https://open.spotify.com/track/5sm8HkgRgSKANJU9B7dsU7" target="_blank">
     Čaje, Šukarije
    </a>
   </td>
   <td width="128">
    Variety of "call and response" vocals.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0014gvc" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Andy Williams
   </td>
   <td>
    <a href="https://open.spotify.com/track/45FLu3nL1iMYXYPzhqLdko" target="_blank">
     Where Do I Begin - Love Theme from "Love Story"
    </a>
   </td>
   <td width="128">
    Minor sixth interval.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Dmitri Shostakovich
   </td>
   <td>
    <a href="https://open.spotify.com/track/0P0LAsqiavYc6V54JSeseB" target="_blank">
     Symphony No. 5 in D Minor, Op. 47: I. Moderato
    </a>
   </td>
   <td width="128">
    Minor sixth interval.
   </td>
   <td width="128">
    Rebekah Reid
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Miklós Rózsa
   </td>
   <td>
    <a href="https://open.spotify.com/track/3GOws7Ctzx108y7auLutGJ" target="_blank">
     Suite - Double Indemnity, 1944
    </a>
   </td>
   <td width="128">
    "Distressing"/contrasting harmonies; tri-tone.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Fereydoon Farrokhzad
   </td>
   <td>
    <a href="https://open.spotify.com/track/3qwhpZblKk5gkEox1CglqF" target="_blank">
     Ashyaneh
    </a>
   </td>
   <td width="128">
    Distinctive two-beat "bum-bum" pulse.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    The Lijadu Sisters
   </td>
   <td>
    <a href="https://open.spotify.com/track/4AEWyNHcETsA5WO1iELm9g" target="_blank">
     Gbowo Mi
    </a>
   </td>
   <td width="128">
    "Free-flowing bass under a very regular rhythm".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0014qdx" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Elia y Elizabeth
   </td>
   <td>
    <a href="https://open.spotify.com/track/4mNU7ddD6fRyjMRBOOfj28" target="_blank">
     Alegria
    </a>
   </td>
   <td width="128">
    Sister act; defined, striking intro.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Olivier Messiaen
    <br/>
    Roger Muraro
    <br/>
    Jean-Jacques Justafré
    <details>
     <summary>
      <em>
       +4 more
      </em>
     </summary>
     Francis Petit
     <br/>
     Renaud Muzzolini
     <br/>
     Orchestre Philharmonique de Radio France
     <br/>
     Myung-Whun Chung
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/5zAiMb6LAvn6wdxlqTjLNB" target="_blank">
     Des Canyons aux étoiles, pour piano solo, cor, xylorimba, glockenspiel et orchestre (1971-74) / Part 3: 11. Omao, leiothrix, elepaio, shama
    </a>
   </td>
   <td width="128">
    Brass-led syncopation; same time period (early 1970s); joyful; both artists were Catholic; about the outdoors.
   </td>
   <td width="128">
    Jeremy Summerly
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Minnie Riperton
   </td>
   <td>
    <a href="https://open.spotify.com/track/4XCGfHpGVq8xw800o5cwWs" target="_blank">
     Les Fleurs
    </a>
   </td>
   <td width="128">
    About nature/the natural world.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Heitor Villa-Lobos
    <br/>
    Bidu Sayão
    <br/>
    Leonard Rose
   </td>
   <td>
    <a href="https://open.spotify.com/track/6VNJ32MJF5DAKPzileg5am" target="_blank">
     Aria - Cantilena from Bachiana brasileira No. 5
    </a>
   </td>
   <td width="128">
    High and low voices in unison.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Tom Jones
   </td>
   <td>
    <a href="https://open.spotify.com/track/0Cq5h2Xnn6EqA5dhDQUcss" target="_blank">
     Thunderball
    </a>
   </td>
   <td width="128">
    Very long, sustained note at the end.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0014xy8" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Igor Stravinsky
    <br/>
    Budapest Festival Orchestra
    <br/>
    Iván Fischer
   </td>
   <td>
    <a href="https://open.spotify.com/track/0rku1F2yMDGgXSS54jW0E0" target="_blank">
     L'oiseau de feu, K. 10. Suite 1919: V. Danse infernale du roi Kastchei
    </a>
   </td>
   <td width="128">
    Features orchestral hits.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Nikolai Rimsky-Korsakov
   </td>
   <td>
    <a href="https://open.spotify.com/track/6weAJf248OVDpE2lP1luqy" target="_blank">
     Scheherazade, Op. 35: I. The Sea and Sinbad's Ship
    </a>
   </td>
   <td width="128">
    Rimsky-Korsakov mentored Stravinsky; both based on fairy tales.
   </td>
   <td width="128">
    Bogdan Văcărescu
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Britney Spears
   </td>
   <td>
    <a href="https://open.spotify.com/track/6I9VzXrHxO9rA9A5euc8Ak" target="_blank">
     Toxic
    </a>
   </td>
   <td width="128">
    "Eastern" scale.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Hariprasad Chaurasia
   </td>
   <td>
    <a href="https://open.spotify.com/track/09KpCeDQDUKVVt8a4qofmR" target="_blank">
     Raga Madhuvanti
    </a>
   </td>
   <td width="128">
    Four note hook uses notes from Madhuvanti raga.
   </td>
   <td width="128">
    Gillian Moore
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    John Farnham
   </td>
   <td>
    <a href="https://open.spotify.com/track/721DwsHOeKf7zHRABCR2rh" target="_blank">
     You're the Voice
    </a>
   </td>
   <td width="128">
    Use of drone.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00154qh" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Who
   </td>
   <td>
    <a href="https://open.spotify.com/track/7B9F9nLxe7MZgZ68Jj86Fn" target="_blank">
     I Can See For Miles - Mono Version
    </a>
   </td>
   <td width="128">
    Repeating same notes (similar to drone).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Sergei Prokofiev
    <br/>
    Dinara Klinton
   </td>
   <td>
    <a href="https://open.spotify.com/track/2x0E3fCH2pPcOFfZBU2Lxc" target="_blank">
     Piano Sonata No. 6 in A Major, Op. 82: I. Allegro Moderato
    </a>
   </td>
   <td width="128">
    Major-minor juxtaposition.
   </td>
   <td width="128">
    Dinara Klinton
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Samuel Barber
    <br/>
    Leonard Slatkin
    <br/>
    St. Louis Symphony
   </td>
   <td>
    <a href="https://open.spotify.com/track/1emdMnglWKwMS8XitagHzT" target="_blank">
     Adagio For Strings Op. 11
    </a>
   </td>
   <td width="128">
    Invokes a sense of grieving/sadness (which one feels as a response to war).
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Little Simz
   </td>
   <td>
    <a href="https://open.spotify.com/track/1Tva251P6CYwQWpJOedwQ8" target="_blank">
     Introvert
    </a>
   </td>
   <td width="128">
    "The power of strings to draw introspection and reflection".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Duke Ellington
   </td>
   <td>
    <a href="https://open.spotify.com/track/506xNpMVd0yiRu4huAFNtM" target="_blank">
     Blue Pepper (Far East of the Blues)
    </a>
   </td>
   <td width="128">
    "Strident and impactful" introduction.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0015bc3" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Johann Sebastian Bach
    <br/>
    Klemens Schnorr
   </td>
   <td>
    <a href="https://open.spotify.com/track/49ed3KfnlZemQi5NlqUTFW" target="_blank">
     Toccata and Fugue in D Minor, BWV 565
    </a>
   </td>
   <td width="128">
    Chromatic runs.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Hans Zimmer
   </td>
   <td>
    <a href="https://open.spotify.com/track/5aaXqH8rgKZxg61HjECldi" target="_blank">
     No Time for Caution
    </a>
   </td>
   <td width="128">
    Organ.
   </td>
   <td width="128">
    Howard Goodall
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Moises Vivanco
    <br/>
    Yma Sumac
    <br/>
    Billy May
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     The Rico Mambo Orchestra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/31EKf1HRXKA3lD2LOjJJNX" target="_blank">
     Malambo No. 1
    </a>
   </td>
   <td width="128">
    "Dramatic atmosphere".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    The Bad Plus
   </td>
   <td>
    <a href="https://open.spotify.com/track/72z9MU95EiNzOhcQmQY6dg" target="_blank">
     Big Eater
    </a>
   </td>
   <td width="128">
    Oscillation between two chords; "tightness" between brass section and the band.
   </td>
   <td width="128">
    Yshani Perinpanayagam
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Sweet
   </td>
   <td>
    <a href="https://open.spotify.com/track/7nvqg2Lkn7mYnmtP5egCmr" target="_blank">
     Blockbuster
    </a>
   </td>
   <td width="128">
    Previous track's repeated intervals of thirds and fifths reminiscent of sirens.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0015l17" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Koko Taylor
   </td>
   <td>
    <a href="https://open.spotify.com/track/0HDVrhFUpCvPpTntHeqnxT" target="_blank">
     I'm A Woman
    </a>
   </td>
   <td width="128">
    Inspired by Bo Diddley's "I'm a Man".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Dolly Parton
   </td>
   <td>
    <a href="https://open.spotify.com/track/4w3tQBXhn5345eUXDGBWZG" target="_blank">
     9 to 5
    </a>
   </td>
   <td width="128">
    Strong/influential women; blues feel.
   </td>
   <td width="128">
    Joe Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Leroy Anderson
    <br/>
    Alasdair Malloy
    <br/>
    BBC Concert Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Leonard Slatkin
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4VVU7vZh4GAq6Hcc1zxqJy" target="_blank">
     The Typewriter
    </a>
   </td>
   <td width="128">
    Features typewriter sounds.
   </td>
   <td width="128">
    Ayanna Witter-Johnson
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Uk Apache
    <br/>
    SHY FX
   </td>
   <td>
    <a href="https://open.spotify.com/track/55K24vPjLgAX8yLAq8fErj" target="_blank">
     Original Nuttah 25
    </a>
   </td>
   <td width="128">
    Frenetic, high-pulse pace.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    The Beach Boys
   </td>
   <td>
    <a href="https://open.spotify.com/track/17QTsL4K9B9v4rI8CAIdfC" target="_blank">
     God Only Knows - Remastered 1996
    </a>
   </td>
   <td width="128">
    Issued as a B-side.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
 </tbody>
</table>

## Series 3

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5" title="This episode was a one-off special.">
    <a href="https://www.bbc.co.uk/programmes/m0017tjx" target="_blank">
     1*
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Hughes
    <br/>
    williams
    <br/>
    Treorchy Male Voice Choir
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     John Cynan-Jones
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/0JY4jOEIb8FsLQuRULasHI" target="_blank">
     Cwm Rhondda
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Giuseppe Verdi
    <br/>
    Luciano Pavarotti
   </td>
   <td>
    <a href="https://open.spotify.com/track/2n0qwCZzpU5aoDZr1mUXY6" target="_blank">
     La Donna E Mobile - Rigoletto
    </a>
   </td>
   <td width="128">
    Ascending phrases; strophic form.
   </td>
   <td width="128">
    Wynne Evans
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Lady Gaga
   </td>
   <td>
    <a href="https://open.spotify.com/track/5R8dQOPq8haW94K7mgERlO" target="_blank">
     Poker Face
    </a>
   </td>
   <td width="128">
    Repeated "melodic stutter".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Claude-Michel Schönberg
    <br/>
    Alain Boublil
    <br/>
    Jean-Marc Natel
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     The Texas Tenors
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/02CatnonkuDat6xkcaHZW9" target="_blank">
     One Day More (From "Les Misérables")
    </a>
   </td>
   <td width="128">
    Same note intervals used in chorus.
   </td>
   <td width="128">
    Anne Denholm
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Ludwig van Beethoven
    <br/>
    Flanders Symphony Orchestra
    <br/>
    Kristiina Poska
   </td>
   <td>
    <a href="https://open.spotify.com/track/0OfDWwJs1xZW96Tk394XPX" target="_blank">
     Symphony No. 3 in E-Flat Major, Op. 55 “Eroica”: I. Allegro con brio
    </a>
   </td>
   <td width="128">
    Victor Hugo (author of Les Misérables) became disillusioned with the French establishment, as did Beethoven several decades earlier.
   </td>
   <td width="128">
    Patrick Rimes
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00181mm" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Weeknd
   </td>
   <td>
    <a href="https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b" target="_blank">
     Blinding Lights
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Vangelis
   </td>
   <td>
    <a href="https://open.spotify.com/track/1u1ATklwZesAvq1whHsI8Z" target="_blank">
     Blade Runner - End Titles
    </a>
   </td>
   <td width="128">
    Synthetic, atmospheric sound similar to film music.
   </td>
   <td width="128">
    David Arnold
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Camille Saint-Saëns
    <br/>
    Olivier Latry
   </td>
   <td>
    <a href="https://open.spotify.com/track/0Ys3Hgnrt8buhXCC0wzFGq" target="_blank">
     Saint-Saëns: Danse macabre, Op. 40 (Arr. Lemare)
    </a>
   </td>
   <td width="128">
    Organ "similar to synthesisers"; often used in film scores.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Spice Girls
   </td>
   <td>
    <a href="https://open.spotify.com/track/1Je1IMUlBXcx1Fz0WE7oPT" target="_blank">
     Wannabe
    </a>
   </td>
   <td width="128">
    Song lyrics contain "zig-a-zig", similar to the Henri Cazalis poem containing "Zig, zig, zig" which Danse macabre is based on.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Mariachi Las Adelitas UK
   </td>
   <td>
    <a href="https://open.spotify.com/track/4PHrbP3pFzudRGFxScjIAi" target="_blank">
     Viva Mexico
    </a>
   </td>
   <td width="128">
    All-female band; laughter at the beginning.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001886f" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Johnny Cash
   </td>
   <td>
    <a href="https://open.spotify.com/track/6YffUZJ2R06kyxyK6onezL" target="_blank">
     Ring of Fire
    </a>
   </td>
   <td width="128">
    Mariachi horns.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Barry Stoller
   </td>
   <td>
    <a href="https://open.spotify.com/track/1hz7N70HYFzR9tnAyjls9A" target="_blank">
     Match of the Day Theme (The Original Complete Release)
    </a>
   </td>
   <td width="128">
    Trumpets; three note leading melody.
   </td>
   <td width="128">
    Hannah Peel
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Sonny Rollins
    <br/>
    Sonny Clark
    <br/>
    Roy Haynes
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Percy Heath
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/2clhkvcSFFdrLLYNJEqqjG" target="_blank">
     Brown Skin Girl
    </a>
   </td>
   <td width="128">
    Simple walking bassline that allows syncopation.
   </td>
   <td width="128">
    Soweto Kinch
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Calypso Rose
   </td>
   <td>
    <a href="https://open.spotify.com/track/2bPdJqmpRMqKMNgYHC9JEl" target="_blank">
     Abatina
    </a>
   </td>
   <td width="128">
    Calypso rhythms.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Winifred Atwell
   </td>
   <td>
    <a href="https://open.spotify.com/track/3xKw2izcI7mDSYAg4KaCDA" target="_blank">
     Jubilee Rag
    </a>
   </td>
   <td width="128">
    Trinidadian-born female artist.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0018h1y" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Léo Delibes
    <br/>
    Orchestra of the Royal Opera House, Covent Garden
    <br/>
    Mark Ermler
   </td>
   <td>
    <a href="https://open.spotify.com/track/6obBx07c3W9S8HrMXarqUb" target="_blank">
     Coppélia: Coppélia, Act III: Galop final
    </a>
   </td>
   <td width="128">
    "Music that makes you want to move".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Jean-Philippe Rameau
    <br/>
    Les Talens Lyriques
    <br/>
    Christophe Rousset
   </td>
   <td>
    <a href="https://open.spotify.com/track/2xya03rJGed1qoV0bRWqra" target="_blank">
     Acante et Céphise, ou La sympathie: Overture: Voeux de la Nation
    </a>
   </td>
   <td width="128">
    Celebratory.
   </td>
   <td width="128">
    Hannah French
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Cy Coleman
    <br/>
    Dorothy Fields
    <br/>
    Shirley Maclaine
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Joseph Gershenson
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/72n52xZr4r55OQVKOVKxOk" target="_blank">
     If My Friends Could See Me Now - 1969 Motion Picture Department
    </a>
   </td>
   <td width="128">
    Fireworks (in a figurative sense); delight.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Missy Elliott
   </td>
   <td>
    <a href="https://open.spotify.com/track/6zsk6uF3MxfIeHPlubKBvR" target="_blank">
     Get Ur Freak On
    </a>
   </td>
   <td width="128">
    Syncopation of lyrics (previous song's lyrics fit over this song's beat).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Kishore Kumar
   </td>
   <td>
    <a href="https://open.spotify.com/track/1mUsUTmmuoQlbMrV3XtUXM" target="_blank">
     Eena Meena Deeka (from "Aasha")
    </a>
   </td>
   <td width="128">
    Bhangra elements.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0018p1s" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Jake Thackray
   </td>
   <td>
    <a href="https://open.spotify.com/track/7zFiSdjQgd7L8CYAklSR08" target="_blank">
     Old Molly Metcalfe
    </a>
   </td>
   <td width="128">
    Lyrics related to counting.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ralph Vaughan Williams
    <br/>
    Nicky Spence
    <br/>
    Roderick Williams
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     William Vann
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/02ZITBx2pMKnh72Ebs0nlK" target="_blank">
     9 English Folk Songs from the Southern Appalachian Mountains (Ed. C. Sharp): No. 9, The Twelve Apostles
    </a>
   </td>
   <td width="128">
    Lyrics related to counting.
   </td>
   <td width="128">
    Iain Burnside
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Elton John
    <br/>
    Kiki Dee
   </td>
   <td>
    <a href="https://open.spotify.com/track/7HW5WIw7ZgZORCzUxv5gW5" target="_blank">
     Don't Go Breaking My Heart
    </a>
   </td>
   <td width="128">
    Singing duet.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    David Bowie
   </td>
   <td>
    <a href="https://open.spotify.com/track/0pQskrTITgmCMyr85tb9qq" target="_blank">
     Starman - 2012 Remaster
    </a>
   </td>
   <td width="128">
    Guitar; prominent octave interval.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Ana Moura
   </td>
   <td>
    <a href="https://open.spotify.com/track/3F5iul8UYuoBINN0x4pob5" target="_blank">
     Desfado
    </a>
   </td>
   <td width="128">
    Vocal vibrato.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0018xky" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Los Lobos
   </td>
   <td>
    <a href="https://open.spotify.com/track/0uMMLry3hzWGn3q3loqMkm" target="_blank">
     La Bamba
    </a>
   </td>
   <td width="128">
    Cyclical chord progression (I-IV-V).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Florence Beatrice Price
    <br/>
    Philadelphia Orchestra
    <br/>
    Yannick Nézet-Séguin
   </td>
   <td>
    <a href="https://open.spotify.com/track/6iT1sP9pKsIoZ0inXnnPfy" target="_blank">
     Symphony No. 1 in E Minor: III. Juba Dance. Allegro
    </a>
   </td>
   <td width="128">
    Folk music that's been reworked and made famous in America.
   </td>
   <td width="128">
    Linton Stephens
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Frédéric Chopin
    <br/>
    Dinara Klinton
   </td>
   <td>
    <a href="https://open.spotify.com/track/1vsTT3reoe9X6KBjRNZ2QS" target="_blank">
     Études, Op. 10: Etude No. 5 in G-Flat Major, Op. 10, No. 5, "Black Keys"
    </a>
   </td>
   <td width="128">
    Pentatonic scale.
   </td>
   <td width="128">
    Dinara Klinton
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Stormzy
   </td>
   <td>
    <a href="https://open.spotify.com/track/4P8dRfSz0LBgyWfjod6v3J" target="_blank">
     Shut Up
    </a>
   </td>
   <td width="128">
    Pentatonic scale.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Tom Jones
   </td>
   <td>
    <a href="https://open.spotify.com/track/5JnHzjo25FY1fMQMQVOawB" target="_blank">
     She's A Lady
    </a>
   </td>
   <td width="128">
    Chorus contains similar melody to instrumental from previous track ("Functions on the Low").
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00194cn" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Michael Kiwanuka
   </td>
   <td>
    <a href="https://open.spotify.com/track/3zJ5RDG0bLQAV2rntFgUtb" target="_blank">
     You Ain't The Problem
    </a>
   </td>
   <td width="128">
    Five quickly-repeated notes occurring every second bar.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Nuyorican Soul
   </td>
   <td>
    <a href="https://open.spotify.com/track/0qZctuvYFQHOjtKSTlJpbE" target="_blank">
     I Am The Black Gold Of The Sun - 4 Hero Remix
    </a>
   </td>
   <td width="128">
    Chromatic chord movement; big chorus with choir.
   </td>
   <td width="128">
    Nitin Sawhney
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Ralph Vaughan Williams
    <br/>
    Nicola Benedetti
    <br/>
    London Philharmonic Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Andrew Litton
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/2TxxLPHPHOsd3i5104tFv2" target="_blank">
     The Lark Ascending
    </a>
   </td>
   <td width="128">
    Free, cadenza-like opening; "music that emulates things or places"; three-note beginning (previous track stretches the word "sun" to three notes).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Heinrich Ignaz Franz von Biber
    <br/>
    Romanesca
    <br/>
    Andrew Manze
   </td>
   <td>
    <a href="https://open.spotify.com/track/5SkQ6F72hRoMPZdSi1PNva" target="_blank">
     Sonata Representativa: Sonata Representativa: VII. Die Katz (Cat)
    </a>
   </td>
   <td width="128">
    Music that depicts animals.
   </td>
   <td width="128">
    Gabriella Swallow
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Kate Bush
   </td>
   <td>
    <a href="https://open.spotify.com/track/4Q3vc39QZjLpGG7cS33kiC" target="_blank">
     Wuthering Heights - 2018 Remaster
    </a>
   </td>
   <td width="128">
    Sliding notes/glissandi.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0019b63" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Ozark Mountain Daredevils
   </td>
   <td>
    <a href="https://open.spotify.com/track/3C5H3mL9Tbq2t3TzEGDl72" target="_blank">
     Beauty In The River
    </a>
   </td>
   <td width="128">
    Hand saws, when played as a musical instrument, are capable of glissando (this track uses a saw percussively).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Dervish
   </td>
   <td>
    <a href="https://open.spotify.com/track/0ZmrVHEPb1yYBYNu2mEKKK" target="_blank">
     The Green Gowned Lass
    </a>
   </td>
   <td width="128">
    Unusual instrumentation (this track uses bones percussively).
   </td>
   <td width="128">
    Camilla George
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Amadou Balaké
   </td>
   <td>
    <a href="https://open.spotify.com/track/5VSZqBVwSTEMTxtTIOnM9U" target="_blank">
     Taximen
    </a>
   </td>
   <td width="128">
    Continuous, unrelenting rhythm.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Incantation
   </td>
   <td>
    <a href="https://open.spotify.com/track/59qdX5AKEd0fCRhSVwrS3N" target="_blank">
     Scarborough Fair
    </a>
   </td>
   <td width="128">
    Eclectic mix of cultures and styles.
   </td>
   <td width="128">
    Sean Shibe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Gustav Holst
    <br/>
    Royal Philharmonic Orchestra
    <br/>
    Owain Arwel Hughes
   </td>
   <td>
    <a href="https://open.spotify.com/track/1TRXjzFQvzHI6X4f6MCYI9" target="_blank">
     Jupiter (From The Planets)
    </a>
   </td>
   <td width="128">
    Opening three notes of Jupiter's second theme use the same intervals as the "parsley sage" lyric of the previous track.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0019kdt" target="_blank">
     9
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Fleetwood Mac
   </td>
   <td>
    <a href="https://open.spotify.com/track/5e9TFTbltYBg2xThimr0rU" target="_blank">
     The Chain - 2004 Remaster
    </a>
   </td>
   <td width="128">
    "Sounds grand/huge"; "broad and generous arrangement".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Earth, Wind &amp; Fire
   </td>
   <td>
    <a href="https://open.spotify.com/track/2GH5jo15wbTv1Ll7zXEzSg" target="_blank">
     Fantasy
    </a>
   </td>
   <td width="128">
    Use of "harmonies/percussion/layers".
   </td>
   <td width="128">
    Uchenna Ngwe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Hukwe Zawose
   </td>
   <td>
    <a href="https://open.spotify.com/track/4qnp1dthmxX4JELxnGnOuV" target="_blank">
     Twendeni Sote Na Mwanga WA Amani
    </a>
   </td>
   <td width="128">
    Circle of fifths chord progression; use of kalimba (the previous track on its original album precedes an instrumental track, "In the Marketplace (Interlude)", played on kalimba).
   </td>
   <td width="128">
    Gabriel Prokofiev
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Leonard Bernstein
    <br/>
    Ariana DeBose
    <br/>
    David Alvarez
    <details>
     <summary>
      <em>
       +30 more
      </em>
     </summary>
     Ana Isabelle
     <br/>
     Jennifer Florentino
     <br/>
     Natalie Toro
     <br/>
     Arianna Rosario
     <br/>
     Ilda Mason
     <br/>
     Jeanette Delgado
     <br/>
     Annelise Cepero
     <br/>
     Tanairi Sade Vazquez
     <br/>
     Jamila Velazquez
     <br/>
     Edriz E. Rosa Pérez
     <br/>
     Melody Martí
     <br/>
     Gaby Diaz
     <br/>
     Juliette Feliciano
     <br/>
     Isabella Ward
     <br/>
     Maria Alexis Rodriguez
     <br/>
     Yesenia Ayala
     <br/>
     Gabriela M. Soto
     <br/>
     Sebastian Serra
     <br/>
     Julius Anthony Rubio
     <br/>
     Ricardo A. Zayas
     <br/>
     Yurel Echezarreta
     <br/>
     Kelvin Delgado
     <br/>
     Ricky Ubeda
     <br/>
     Carlos Sánchez Falú
     <br/>
     Adriel Flete
     <br/>
     Jacob Guzman
     <br/>
     Carlos E. Gonzalez
     <br/>
     David Avilés Morales
     <br/>
     Andrei Chagas
     <br/>
     David Guzman
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/7guz8LWGuiHSvp19OUxmbQ" target="_blank">
     America
    </a>
   </td>
   <td width="128">
    Starts with solo wooden percussion.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Camaron De La Isla
   </td>
   <td>
    <a href="https://open.spotify.com/track/6yZZx2sFG2VLN4B1SjmxyX" target="_blank">
     Tangos De La Sultana - Tangos - Remastered 2018
    </a>
   </td>
   <td width="128">
    Hand claps; Latin music.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 4

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001cq8c" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ennio Morricone
   </td>
   <td>
    <a href="https://open.spotify.com/track/2IJJszwGK4NWmh3bNK6CPD" target="_blank">
     The Good, The Bad and The Ugly - Il Buono, Il Brutto, Il Cattivo (Titles)
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Elvis Presley
   </td>
   <td>
    <a href="https://open.spotify.com/track/7iBBcw61QVJxI3NDzlpX2E" target="_blank">
     Love Me Tender
    </a>
   </td>
   <td width="128">
    Perfect fourth interval.
   </td>
   <td width="128">
    Richard Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Madonna
   </td>
   <td>
    <a href="https://open.spotify.com/track/7DOtIhTTpPZyjvbO509hSC" target="_blank">
     Don't Tell Me
    </a>
   </td>
   <td width="128">
    Reimagining of an existing song.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Henryk Górecki
    <br/>
    Dawn Upshaw
    <br/>
    London Sinfonietta
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     David Zinman
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/7Mx00Ye1ypcK1hToeKyrVl" target="_blank">
     Symphony No. 3, Op. 36: I. Lento - Sostenuto Tranquillo Ma Cantabile
    </a>
   </td>
   <td width="128">
    Use of strings.
   </td>
   <td width="128">
    Alina Bzhezhinska
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Melanie De Biasio
   </td>
   <td>
    <a href="https://open.spotify.com/track/3CaFlvMtboeeNFRKHHdsud" target="_blank">
     Afro Blue
    </a>
   </td>
   <td width="128">
    Slow, four note beginning of a minor scale.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001cxsl" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Wayne Smith
   </td>
   <td>
    <a href="https://open.spotify.com/track/1YjBJlLZh4wwnfYZCr3jrE" target="_blank">
     Under Me Sleng Teng
    </a>
   </td>
   <td width="128">
    Simple, synthesised ground bass.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Reynaldo Hahn
    <br/>
    Susan Graham
   </td>
   <td>
    <a href="https://open.spotify.com/track/4pRn4mVhANBKiy5qYJBTql" target="_blank">
     À Chloris
    </a>
   </td>
   <td width="128">
    Pastiche; borrowing melodies.
   </td>
   <td width="128">
    Nicky Spence
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Deerhoof
   </td>
   <td>
    <a href="https://open.spotify.com/track/27q5GvvMYZCM0ovjMuQHRE" target="_blank">
     Whither the Invisible Birds?
    </a>
   </td>
   <td width="128">
    "Influenced by/reflective of music of the past".
   </td>
   <td width="128">
    Laura Jurd
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Gregorio Allegri
    <br/>
    The Choir Of Trinity College, Cambridge
    <br/>
    Richard Marlow
   </td>
   <td>
    <a href="https://open.spotify.com/track/6es7DmrhnDoKj5rsFvh3XU" target="_blank">
     Miserere mei, Deus
    </a>
   </td>
   <td width="128">
    High, child-like vocals.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Cilla Black
   </td>
   <td>
    <a href="https://open.spotify.com/track/2IqtBxwRgNOt7YWMmulrUZ" target="_blank">
     Alfie - 2003 Remaster
    </a>
   </td>
   <td width="128">
    Uses a "U-shape" melodic phrase (similar to an inverted mordent).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001d5rb" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Alfredo Gryciuk
    <br/>
    Marcelo Rojas
    <br/>
    Ariel Burgos
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Martín Portillo
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/5h5GE46r6P5kKEyYFpH6iI" target="_blank">
     Pájaro campana (The Bell Bird)
    </a>
   </td>
   <td width="128">
    Harp; glissandi.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Birdy
   </td>
   <td>
    <a href="https://open.spotify.com/track/7wRijQK8vRmGLK0RYW7Vr1" target="_blank">
     Quietly Yours
    </a>
   </td>
   <td width="128">
    Arpeggios.
   </td>
   <td width="128">
    Catrin Finch
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Joan Armatrading
   </td>
   <td>
    <a href="https://open.spotify.com/track/6Mnne5V9ZifNID59dswUcZ" target="_blank">
     Love And Affection
    </a>
   </td>
   <td width="128">
    "Similar singing technique".
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Clarence "Frogman" Henry
   </td>
   <td>
    <a href="https://open.spotify.com/track/06r30bE8T4VXXN7hI9o93L" target="_blank">
     Ain't Got No Home
    </a>
   </td>
   <td width="128">
    Singing in low vocal register (previous track had low backing vocals sung by Clarke Peters).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Wolfgang Amadeus Mozart
    <br/>
    Ludwig Weber
    <br/>
    Wiener Philharmoniker
   </td>
   <td>
    <a href="https://open.spotify.com/track/72PEPng3rB75QrMlgx5WpI" target="_blank">
     O, wie will ich triumphieren (Die Entführung aus dem Serail)
    </a>
   </td>
   <td width="128">
    "Bayreuth bark"; singing in low vocal register.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001df0h" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Modest Mussorgsky
   </td>
   <td>
    <a href="https://open.spotify.com/track/5rPqo5uyPn5MDoJkkiu8Nr" target="_blank">
     Night on Bald Mountain
    </a>
   </td>
   <td width="128">
    "Melodramatic, operatic tone".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Jacob Collier
   </td>
   <td>
    <a href="https://open.spotify.com/track/3QUU7ZECjXncEhUd6Aggcq" target="_blank">
     Hideaway
    </a>
   </td>
   <td width="128">
    Tension and release; musical "sunrise"; semi-tone key signature change.
   </td>
   <td width="128">
    Patrick Rimes
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Juliette Gréco
   </td>
   <td>
    <a href="https://open.spotify.com/track/7wBt4gAavPWOalhZTk2YsF" target="_blank">
     Un petit poisson un petit oiseau
    </a>
   </td>
   <td width="128">
    High, repeated "bell-like" notes played in the background.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Louis Armstrong
   </td>
   <td>
    <a href="https://open.spotify.com/track/3GMxobnrcay3xl6jJ7fbVz" target="_blank">
     When The Saints Go Marching In
    </a>
   </td>
   <td width="128">
    Anacrusis (musical upbeat).
   </td>
   <td width="128">
    Anne Dudley
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Willie Colón
    <br/>
    Héctor Lavoe
   </td>
   <td>
    <a href="https://open.spotify.com/track/4ztAIzF7WKU9I4MCI0nSQa" target="_blank">
     Ché Ché Colé
    </a>
   </td>
   <td width="128">
    Call and response.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001dp3f" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Lonnie Liston Smith
    <br/>
    The Cosmic Echoes
   </td>
   <td>
    <a href="https://open.spotify.com/track/1DoWUjcc5sqpRioFPioogU" target="_blank">
     Expansions
    </a>
   </td>
   <td width="128">
    Triangle (musical instrument) playing a similar rhythm.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    La Bottine Souriante
   </td>
   <td>
    <a href="https://open.spotify.com/track/70UjPO5h37u4bgF5ksh8Qd" target="_blank">
     Ouverture
    </a>
   </td>
   <td width="128">
    Similar Quebec/French-Canadian "foot-tapping" rhythm.
   </td>
   <td width="128">
    Kathryn Tickell
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Leonard Bernstein
    <br/>
    New York Philharmonic
   </td>
   <td>
    <a href="https://open.spotify.com/track/6yul9NbwH5cK7T0Pu6Twtu" target="_blank">
     Overture to Candide
    </a>
   </td>
   <td width="128">
    Overture.
   </td>
   <td width="128">
    Joe Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Hossam Ramzy Egyptian Ensemble
   </td>
   <td>
    <a href="https://open.spotify.com/track/5723lWTogsI3AeastYZyOO" target="_blank">
     Khusara Khusara (What a Loss)
    </a>
   </td>
   <td width="128">
    Similar repeated, emphasised notes that "anchor" the music.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Louis Armstrong
   </td>
   <td>
    <a href="https://open.spotify.com/track/5OhersWDAFaUwY6VawMqiS" target="_blank">
     Basin Street Blues
    </a>
   </td>
   <td width="128">
    Metallic percussion over a main melody.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001dxqc" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ella Fitzgerald
   </td>
   <td>
    <a href="https://open.spotify.com/track/3LEAXQg3vnyLK184wPOGyT" target="_blank">
     It Don't Mean A Thing (If It Ain't Got That Swing)
    </a>
   </td>
   <td width="128">
    Scat singing.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Outkast
   </td>
   <td>
    <a href="https://open.spotify.com/track/2PpruBYCo4H7WOBJ7Q2EwM" target="_blank">
     Hey Ya!
    </a>
   </td>
   <td width="128">
    "Pop music of the day"; catchy, very popular hit tune.
   </td>
   <td width="128">
    Zara McFarlane
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Son Lux
    <br/>
    Lily &amp; Madeleine
   </td>
   <td>
    <a href="https://open.spotify.com/track/4kP7BPJ1d3WUGhykQBVEjH" target="_blank">
     Lost It To Trying
    </a>
   </td>
   <td width="128">
    Anxious energy; feeling of propulsion; strange sound effects.
   </td>
   <td width="128">
    Ollie Howell
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Moondog
    <br/>
    Julie Andrews
    <br/>
    Martyn Green
   </td>
   <td>
    <a href="https://open.spotify.com/track/1CjkOIc0DlmLnv2t5gKGa1" target="_blank">
     Songs of Fun and Nonsense
    </a>
   </td>
   <td width="128">
    "Strange dance" between top flute line and a "robot auto-sounding" rhythm underneath.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Julie Andrews
    <br/>
    Nicholas Hammond
    <br/>
    Debbie Turner
    <details>
     <summary>
      <em>
       +5 more
      </em>
     </summary>
     Duane Chase
     <br/>
     Heather Menzies
     <br/>
     Angela Cartwright
     <br/>
     Kym Karath
     <br/>
     Charmian Carr
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6aNMGfwdGyELNGCuqs5ldU" target="_blank">
     Do-Re-Mi
    </a>
   </td>
   <td width="128">
    Julie Andrews; playfulness alongside instructive teacher-like sensibility.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001f5kc" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Flaco Jimenez
   </td>
   <td>
    <a href="https://open.spotify.com/track/7lFFgni4XpRY2bGV7qeH2q" target="_blank">
     Ay Te Dejo en San Antonio
    </a>
   </td>
   <td width="128">
    Polka rhythm in the cello section of Do Re Mi.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    George Frideric Handel
    <br/>
    Musica Sequenza
    <br/>
    Burak Ozdemir
   </td>
   <td>
    <a href="https://open.spotify.com/track/6COsXMcFNE7KR72vX49Cvk" target="_blank">
     Scherza infida
    </a>
   </td>
   <td width="128">
    Lyrics about betrayal.
   </td>
   <td width="128">
    Gillian Moore
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Vashti Bunyan
   </td>
   <td>
    <a href="https://open.spotify.com/track/1SVbLtv66jl9djDekvnMTq" target="_blank">
     Diamond Day
    </a>
   </td>
   <td width="128">
    Cyclical melodies.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Benjamin Britten
    <br/>
    André Previn
    <br/>
    London Symphony Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/4vkw5tNky8LG4UcxWDqE0J" target="_blank">
     Britten: Four Sea Interludes from Peter Grimes, Op. 33a: No. 4, Storm
    </a>
   </td>
   <td width="128">
    A storm contrasts the pastoral calm of the previous track; pentatonic melody.
   </td>
   <td width="128">
    Gavin Higgins
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Ana Moura
   </td>
   <td>
    <a href="https://open.spotify.com/track/5325tAtahMQabyAqcx75Mg" target="_blank">
     Lilac Wine
    </a>
   </td>
   <td width="128">
    Melodic echo of Britten's pentatonic "glimmer of hope".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001fdb7" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Idina Menzel
   </td>
   <td>
    <a href="https://open.spotify.com/track/0qcr5FMsEO85NAQjrlDRKo" target="_blank">
     Let It Go - From "Frozen"/Soundtrack Version
    </a>
   </td>
   <td width="128">
    Recitativo style and three-syllable hook ("Let It Go" / "Lilac Wine").
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Duke Ellington
    <br/>
    Duke Ellington Orchestra
    <br/>
    Al Hibbler
   </td>
   <td>
    <a href="https://open.spotify.com/track/5Dwi2FkqVrLPIJSb9CAnNF" target="_blank">
     Liberian Suite / I Like the Sunrise
    </a>
   </td>
   <td width="128">
    Harmonic progression (I-V-vi-IV) in "Let It Go" mirrors Ellington's piece.
   </td>
   <td width="128">
    Giacomo Smith
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Ethel Smyth
    <br/>
    Chorus Of The Plymouth Music Series
    <br/>
    Eiddwen Harrhy
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Philip Brunelle
     <br/>
     Orchestra Of The Plymouth Music Series
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4RzE64uta8ntAIwhr4Dw10" target="_blank">
     Smyth: Songs of Sunrise: No. 3, The March of the Women. "Shout, Shout, Up with Your Song!"
    </a>
   </td>
   <td width="128">
    "Sunrise" theme links to hope/new day; simple melody like Ellington's track.
   </td>
   <td width="128">
    Esther Abrami
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Serge Gainsbourg
   </td>
   <td>
    <a href="https://open.spotify.com/track/6Z1487JY6p3cVxs5JVXkMZ" target="_blank">
     Aux armes et caetera
    </a>
   </td>
   <td width="128">
    Anthem-like quality ties to Gainsbourg's reggae "La Marseillaise".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Booker T. &amp; the M.G.'s
   </td>
   <td>
    <a href="https://open.spotify.com/track/4fQMGlCawbTkH9yPPZ49kP" target="_blank">
     Green Onions
    </a>
   </td>
   <td width="128">
    Hammond organ.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001fn6s" target="_blank">
     9
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ibrahim Maalouf
   </td>
   <td>
    <a href="https://open.spotify.com/track/64xWIjAe9NhyJCSqQWzp9s" target="_blank">
     Will Soon Be a Woman (Live au Babylon Istanbul, 2013)
    </a>
   </td>
   <td width="128">
    Live audience sounds becoming part of the recording.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Leonard Cohen
   </td>
   <td>
    <a href="https://open.spotify.com/track/3mFzIFFFmEXTQs6BDAK2ZZ" target="_blank">
     Dance Me to the End of Love
    </a>
   </td>
   <td width="128">
    Communal voices/choral element and descending melodic line ("falling line").
   </td>
   <td width="128">
    Isobel Waller-Bridge
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Georges Bizet
    <br/>
    Maria Callas
    <br/>
    Choeurs Rene Duclos
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Georges Prêtre
     <br/>
     Orchestre du Théâtre National de l'Opéra de Paris
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/5Adxsld8lL9MLcaULeoSKu" target="_blank">
     Bizet: Carmen, WD 31, Act 1: Habanera. "L'amour est un oiseau rebelle" (Carmen, Chœur)
    </a>
   </td>
   <td width="128">
    Greek Hasapico dance rhythm in Cohen's track and Maria Callas' Greek heritage.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Wiley
   </td>
   <td>
    <a href="https://open.spotify.com/track/38LNwmhNpQMEfg5wvdF4Qg" target="_blank">
     Eskimo
    </a>
   </td>
   <td width="128">
    Direct musical inspiration from Bizet's "Habanera" bassline, creating the grime genre's foundational sound.
   </td>
   <td width="128">
    Michael 'Mikey J' Asante
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Nat King Cole
   </td>
   <td>
    <a href="https://open.spotify.com/track/0eVjtPhqsZMWbg9ewHvJhY" target="_blank">
     Deck The Halls
    </a>
   </td>
   <td width="128">
    Linked through Wiley's use of Christmas lyrics in "Eskimo" and shared non-lexical vocables ("fa-la-la").
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
 </tbody>
</table>

## Series 5

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001hxc5" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Yiddish Glory
    <br/>
    Loyko
    <br/>
    Alexander Sevastian
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Psoy Korolenko
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/5sfUky4aWK7heDtHGfW5gD" target="_blank">
     Nitsokhn Lid (Victory Song)
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Olivier Messiaen
    <br/>
    Jeanne Hourez
    <br/>
    Zongheng Zhang
   </td>
   <td>
    <a href="https://open.spotify.com/track/27rNfT7DaNwVGLUBUFRZ1D" target="_blank">
     Quatuor pour la Fin du Temps: VIII. Louange à l'immortalité de Jésus
    </a>
   </td>
   <td width="128">
    Music born from war experiences.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Madonna
   </td>
   <td>
    <a href="https://open.spotify.com/track/27QvYgBk0CHOVHthWnkuWt" target="_blank">
     Vogue
    </a>
   </td>
   <td width="128">
    Similar melodic structure to Messiaen's opening.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Douglas Sills
   </td>
   <td>
    <a href="https://open.spotify.com/track/2gnlaEcF4oHUjJngXgUGkJ" target="_blank">
     The Creation of Man
    </a>
   </td>
   <td width="128">
    Themes of flamboyance.
   </td>
   <td width="128">
    Linton Stephens
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Stevie Wonder
   </td>
   <td>
    <a href="https://open.spotify.com/track/4pNiE4LCVV74vfIBaUHm1b" target="_blank">
     Sir Duke
    </a>
   </td>
   <td width="128">
    Doubled melodies technique from Scarlet Pimpernel.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001j4kn" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Gangbé Brass Band
    <br/>
    Femi Kuti
   </td>
   <td>
    <a href="https://open.spotify.com/track/6aPp32B3XeiztvfwBmchv6" target="_blank">
     Yoruba
    </a>
   </td>
   <td width="128">
    Use of brass instruments.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Eliza Carthy
   </td>
   <td>
    <a href="https://open.spotify.com/track/5i9BsnZLYpqrSgymzm99Gx" target="_blank">
     Rolling Sea
    </a>
   </td>
   <td width="128">
    Shares a similar chord pattern and is in Dorian mode.
   </td>
   <td width="128">
    Gareth Malone
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Igor Stravinsky
   </td>
   <td>
    <a href="https://open.spotify.com/track/1stsCnrbAZJFYqBYxmkGH9" target="_blank">
     The Rite of Spring (Scenes of Pagan Russia in Two Parts): Part One - Spring Rounds (1921 Version)
    </a>
   </td>
   <td width="128">
    Dorian mode and folk elements in "Rolling Sea"; features dramatic orchestration.
   </td>
   <td width="128">
    Gillian Moore
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Camila Cabello
    <br/>
    Young Thug
   </td>
   <td>
    <a href="https://open.spotify.com/track/1rfofaqEpACxVEHIZBJe6W" target="_blank">
     Havana (feat. Young Thug)
    </a>
   </td>
   <td width="128">
    Descending melodic motif reminiscent of the Stravinsky piece.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Erik Satie
    <br/>
    Alena Cherny
   </td>
   <td>
    <a href="https://open.spotify.com/track/5fdp9rXfEixCGLM1Og4EN1" target="_blank">
     Gnossienne No. 1
    </a>
   </td>
   <td width="128">
    Shares a swaying, piano-driven rhythm and mysterious quality with "Havana."
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001jcgj" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Horace Silver
   </td>
   <td>
    <a href="https://open.spotify.com/track/1CDBaGlisZlOJzvx88lL8A" target="_blank">
     Song For My Father
    </a>
   </td>
   <td width="128">
    Melodic continuity and F minor key.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Earth, Wind &amp; Fire
   </td>
   <td>
    <a href="https://open.spotify.com/track/6GFoIM443A1mwOBr5qOX2s" target="_blank">
     Africano / Power - Live
    </a>
   </td>
   <td width="128">
    Live performance energy, call-and-response, and rhythmic intensity.
   </td>
   <td width="128">
    James Taylor
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Sona Jobarteh
   </td>
   <td>
    <a href="https://open.spotify.com/track/5lVADANQpWlnuKdQklBm3v" target="_blank">
     Bannaya
    </a>
   </td>
   <td width="128">
    Tension-and-release structure; features the Gambian kora.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Sergei Rachmaninoff
    <br/>
    Vladimir Ashkenazy
    <br/>
    London Symphony Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     André Previn
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6wTayipnJ5tiiuactulUpP" target="_blank">
     Piano Concerto No. 3 in D Minor, Op. 30: I. Allegro ma non tanto - Remastered 2013
    </a>
   </td>
   <td width="128">
    Ascending melodic motifs and the kora's resemblance to piano virtuosity.
   </td>
   <td width="128">
    Dinara Klinton
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Bachar Mar-Khalifé
   </td>
   <td>
    <a href="https://open.spotify.com/track/6DLylbY93X5wKOPxhLfUHE" target="_blank">
     Kyrie Eleison
    </a>
   </td>
   <td width="128">
    Percussive piano intensity and emotional force.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001jldr" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Antonio Vivaldi
    <br/>
    The Monteverdi Choir
    <br/>
    English Baroque Soloists
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     John Eliot Gardiner
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4R4oGXRhmuS5ykjru4u8mE" target="_blank">
     Gloria: Gloria in excelsis Deo
    </a>
   </td>
   <td width="128">
    Liturgical text (Kyrie/Gloria) and triumphant release.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Music Without Borders
    <br/>
    Sara Marielle Gaup Beaska
    <br/>
    Rony Barrak
    <details>
     <summary>
      <em>
       +6 more
      </em>
     </summary>
     Anubrata Chatterjee
     <br/>
     Prabhu Raj Dhakal
     <br/>
     Bjørn Ole Rasch
     <br/>
     Sigurd Brokke
     <br/>
     Kirsten Bråten Berg
     <br/>
     Annbjørg Lien
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/0HIoPU4hRMnwFweTgq8Egw" target="_blank">
     Nordafjells/Liti Kjersti
    </a>
   </td>
   <td width="128">
    Repetitive ostinato rhythms and Norwegian hardanger fiddle's drone-like resonance.
   </td>
   <td width="128">
    Bjarte Eike
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Donna Summer
   </td>
   <td>
    <a href="https://open.spotify.com/track/7B7lf3sIze5VR2WuYttn18" target="_blank">
     I Feel Love - 12" Version
    </a>
   </td>
   <td width="128">
    Rhythmic propulsion, Moog bassline's drone-like sustain, and global collaboration ethos.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Michael Jackson
   </td>
   <td>
    <a href="https://open.spotify.com/track/0sKlV58cODrjxGFOyf9IXY" target="_blank">
     The Way You Make Me Feel - 2012 Remaster
    </a>
   </td>
   <td width="128">
    Similar bassline and minor pentatonic ambiguity, with added swing rhythm.
   </td>
   <td width="128">
    Natalie Duncan
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    String Harmonies
   </td>
   <td>
    <a href="https://open.spotify.com/track/7qYE9ns6t3tUMrOAPXo9cs" target="_blank">
     Khnjooyki Yerk / Hars Oo Pesa
    </a>
   </td>
   <td width="128">
    Rhythmic innovation (10/8 time signature mirroring Jackson's scat syllables).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001jsww" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Stone Roses
   </td>
   <td>
    <a href="https://open.spotify.com/track/6JvEXmRh3l2acBzvqavgT9" target="_blank">
     Love Spreads
    </a>
   </td>
   <td width="128">
    Previous track features an unusual 10/8 time signature, which connects to the prominent quaver rhythm; shared key signature of D.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    George Frideric Handel
    <br/>
    Marian Anderson
    <br/>
    Charles O'Connell
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Victor Symphony Orchestra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/7HzdUiq99AYWIzRKoC8yOw" target="_blank">
     Messiah, HWV 56, Part II: Aria "He was Despised and Rejected of Men" - 2021 Remastered Version
    </a>
   </td>
   <td width="128">
    The lyrics of "Love Spreads" portray Jesus as a black woman, linking to Marian Anderson's rendition of Handel's Messiah.
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    MC Hammer
   </td>
   <td>
    <a href="https://open.spotify.com/track/1B75hgRqe7A4fwee3g3Wmu" target="_blank">
     U Can't Touch This
    </a>
   </td>
   <td width="128">
    Dramatic word painting.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Miles Davis
    <br/>
    John Coltrane
    <br/>
    Cannonball Adderley
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Bill Evans
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4vLYewWIvqHfKtJDk8c8tq" target="_blank">
     So What (feat. John Coltrane, Cannonball Adderley &amp; Bill Evans)
    </a>
   </td>
   <td width="128">
    Energy and charisma of MC Hammer's performance reminiscent of Miles Davis' innovative jazz style.
   </td>
   <td width="128">
    Julian Joseph
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Googoosh
   </td>
   <td>
    <a href="https://open.spotify.com/track/66BFeLNXz3ivsQy8Shl5sm" target="_blank">
     Makhloogh
    </a>
   </td>
   <td width="128">
    The twinkling metal work on the drums in "So What" connects to the Persian instrumentation in "Makhloogh.".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001k17h" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Imamyar Hasanov
    <br/>
    Hamid Motebassem
    <br/>
    Pejman Hadadi
   </td>
   <td>
    <a href="https://open.spotify.com/track/7ALLXDGx08cVs2M88FGU6U" target="_blank">
     Infinity
    </a>
   </td>
   <td width="128">
    Kamanche (Persian bowed string instrument) and rhythmic metalwork.
   </td>
   <td width="128">
    Ruairi Glasheen
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Mehter Takimi
   </td>
   <td>
    <a href="https://open.spotify.com/track/3n4902glpopb77sblNUFNe" target="_blank">
     Mehter Vuruyor
    </a>
   </td>
   <td width="128">
    Percussion focus (clashing cymbals, military rhythms) and shared Turkish/Persian instrumentation.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Daryl Hall &amp; John Oates
   </td>
   <td>
    <a href="https://open.spotify.com/track/5dFoWIiJ2814hRwMYDcFiU" target="_blank">
     She's Gone
    </a>
   </td>
   <td width="128">
    Octave doubling in vocals (mirroring the octaves in the Turkish march’s pipe melody).
   </td>
   <td width="128">
    Anne Dudley
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Johann Sebastian Bach
    <br/>
    Janine Jansen
    <br/>
    Boris Brovtsyn
    <details>
     <summary>
      <em>
       +10 more
      </em>
     </summary>
     Cindy Albracht
     <br/>
     Frederik Paulsson
     <br/>
     Julia-Maria Kretz
     <br/>
     Tijmen Huisingh
     <br/>
     Monika Urbonaite
     <br/>
     Nimrod Guez
     <br/>
     Pauline Sachse
     <br/>
     Maarten Jansen
     <br/>
     Rick Stotijn
     <br/>
     Jan Jansen
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6NfVensuKfUMP3FOaLOmb1" target="_blank">
     Orchestral Suite No. 3 in D, BWV 1068: 2. Air
    </a>
   </td>
   <td width="128">
    Descending bassline.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Jimmy Cliff
   </td>
   <td>
    <a href="https://open.spotify.com/track/1dZxI6OuzwJ283y3gOU1Kq" target="_blank">
     Many Rivers To Cross
    </a>
   </td>
   <td width="128">
    "Spiritual" organ intro similar to Bach's church music roots and shared themes of yearning/resilience.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001k84y" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Tapiola Choir
   </td>
   <td>
    <a href="https://open.spotify.com/track/4BS8qyrchk9WhWdpWuQA55" target="_blank">
     Kilisee, kilisee kulkunen (Jingling, Jingling Sleigh Bells Ring) - Iloinen joululaulu (Happy Christmas Song)
    </a>
   </td>
   <td width="128">
    Group vocal harmonies.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Kate Bush
   </td>
   <td>
    <a href="https://open.spotify.com/track/21FKjWeXnJecoU2jRLk6lb" target="_blank">
     Snowflake - 2018 Remaster
    </a>
   </td>
   <td width="128">
    Children's voices and winter theme.
   </td>
   <td width="128">
    John Lunn
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    The Smiths
   </td>
   <td>
    <a href="https://open.spotify.com/track/1YrnDTqvcnUKxAIeXyaEmU" target="_blank">
     How Soon Is Now? - 2011 Remaster
    </a>
   </td>
   <td width="128">
    Tremolo/oscillations.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Claude Debussy
    <br/>
    Carolina Eyck
   </td>
   <td>
    <a href="https://open.spotify.com/track/1K50XkDEXi6f9jSIedlrsx" target="_blank">
     Clair de lune - Arr. for Theremin and Voice by Carolina Eyck
    </a>
   </td>
   <td width="128">
    Theremin's ethereal oscillations (like Morrissey's voice).
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Biluka y Los Canibales
   </td>
   <td>
    <a href="https://open.spotify.com/track/4VNNYKMbf6OSvj0pBGrOrL" target="_blank">
     Huashca De Corales
    </a>
   </td>
   <td width="128">
    Unconventional instrumentation (played on a leaf).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001kh5v" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Mura Masa
    <br/>
    A$AP Rocky
   </td>
   <td>
    <a href="https://open.spotify.com/track/3sTN90bIP2cJ1783ctHykO" target="_blank">
     Love$ick (feat. A$AP Rocky)
    </a>
   </td>
   <td width="128">
    "Parade of instruments" technique; focuses on repeated melodies played by different instruments.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Claudio Monteverdi
    <br/>
    Ian Partridge
    <br/>
    Nigel Rogers
    <details>
     <summary>
      <em>
       +4 more
      </em>
     </summary>
     Christopher Keyte
     <br/>
     Colin Tilney
     <br/>
     Jürgen Jürgens
     <br/>
     The Monteverdi Choir
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4rXRbqyoxxGULVnnSiRDhC" target="_blank">
     Madrigals - Book 6: Zefiro Torna E Di Soavi Accenti
    </a>
   </td>
   <td width="128">
    Harmonic groove and rhythmic drive (continuo); playful word-painting.
   </td>
   <td width="128">
    Roderick Williams
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Esbe
   </td>
   <td>
    <a href="https://open.spotify.com/track/61edvFIu22esbuNHVt0MeB" target="_blank">
     Sumer Is Icumen In
    </a>
   </td>
   <td width="128">
    Zephyr (west wind) theme and the use of rounds/canons; highlights spring's arrival and vocal weaving.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    David Byrne
   </td>
   <td>
    <a href="https://open.spotify.com/track/5SD6B2lXRsZt46RKz173gq" target="_blank">
     A Long Time Ago
    </a>
   </td>
   <td width="128">
    Nature sounds (birds) and the "cuckoo" motif; explores nostalgia and sonic storytelling.
   </td>
   <td width="128">
    Isobel Waller-Bridge
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Meat Loaf
   </td>
   <td>
    <a href="https://open.spotify.com/track/3mCeeoBvTTpg8Xy2Wuvirw" target="_blank">
     Bat Out of Hell
    </a>
   </td>
   <td width="128">
    Inverted "cuckoo" motif and dramatic narrative scope.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 6

### Notes

#### Ep. 5, Track 3
Both this track and the next were chosen as similar yet separate playlist tracks (dubbed "3a" and "3b"), bringing the episode's track total to six.
#### Ep. 9, Track 4
The second guest presenter was ill and did not appear in this episode. They still contributed a track to the playlist, but their identity was not revealed.
<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001mm1c" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Dolly Parton
   </td>
   <td>
    <a href="https://open.spotify.com/track/1XChvxIUbR911TOb0HhNJi" target="_blank">
     Mule Skinner Blues (Blue Yodel No. 8)
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Glykeria
   </td>
   <td>
    <a href="https://open.spotify.com/track/0cdimJNlWzGVfsyqWINXEw" target="_blank">
     Mes Sto Aigaiou Ta Nisia
    </a>
   </td>
   <td width="128">
    Vocal technique (melisma); extended vocal ornamentation.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Vincenzo Bellini
    <br/>
    Maria Callas
    <br/>
    Coro Del Teatro Alla Scala Di Milano
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Tullio Serafin
     <br/>
     Orchestra Del Teatro Alla Scala, Milano
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4GcvvRHKe8CkVxWGeNDCGy" target="_blank">
     Bellini: Norma, Act 1: "Casta diva" (Norma, Coro)
    </a>
   </td>
   <td width="128">
    Glykeria's Greek origins (Maria Callas was Greek) and continued focus on melismatic singing.
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Noordpool Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/4XiRjUElwREYMDh74caLKu" target="_blank">
     Weird Fishes
    </a>
   </td>
   <td width="128">
    Arpeggiated accompaniment style.
   </td>
   <td width="128">
    Gavin Higgins
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Duarte
   </td>
   <td>
    <a href="https://open.spotify.com/track/4M1mgxSKACXl0MG4Juz7sy" target="_blank">
     Vai de Roda
    </a>
   </td>
   <td width="128">
    Cross-rhythms.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001mtfw" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Édith Piaf
   </td>
   <td>
    <a href="https://open.spotify.com/track/3dkIE8P7hvl3tHl9KSb6dA" target="_blank">
     Non, je ne regrette rien
    </a>
   </td>
   <td width="128">
    Rolling "R" vocal delivery (Duarte’s Portuguese fado-style phrasing/Piaf’s dramatic French articulation).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Claudio Villa
   </td>
   <td>
    <a href="https://open.spotify.com/track/7AZ5asjKNGJ9n9PqOvpUc7" target="_blank">
     Claudio Villa a mezza voce (Stornelli amorosi - Parte I)
    </a>
   </td>
   <td width="128">
    Triplet rhythms.
   </td>
   <td width="128">
    Kate St. John
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    The Pyramids
   </td>
   <td>
    <a href="https://open.spotify.com/track/1DPjAGUiOq9ePJxsDpj807" target="_blank">
     Train Tour to Rainbow City
    </a>
   </td>
   <td width="128">
    Claudio Villa’s guitar rhythm similar to ska’s offbeat momentum.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    John Adams
    <br/>
    Bournemouth Symphony Orchestra
    <br/>
    Marin Alsop
   </td>
   <td>
    <a href="https://open.spotify.com/track/39lN1yTJ5gz5AGypvQcq5D" target="_blank">
     Short Ride in a Fast Machine
    </a>
   </td>
   <td width="128">
    Echoes The Pyramids’ clave rhythm via relentless woodblock pulse (mechanical vs. ska’s shuffle).
   </td>
   <td width="128">
    Joe Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Ástor Piazzolla
    <br/>
    José Bragato
    <br/>
    Zürcher Klaviertrio
   </td>
   <td>
    <a href="https://open.spotify.com/track/4uKQPketvYKhfEpr9hHteP" target="_blank">
     The Four Seasons - Four Tangos, Version for Piano Trio: I. Spring in Buenos Aires
    </a>
   </td>
   <td width="128">
    Mirrors Adams’ disjunctive melody (jagged horn leaps/Piazzolla’s zigzagging nuevo tango violin).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001n238" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Technotronic
   </td>
   <td>
    <a href="https://open.spotify.com/track/21qnJAMtzC6S5SESuqQLEK" target="_blank">
     Pump Up The Jam
    </a>
   </td>
   <td width="128">
    Rhythmic intensity (tango's staccato chords → techno's punchy synth stabs).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Bernard Herrmann
   </td>
   <td>
    <a href="https://open.spotify.com/track/0LIc6Ktjr7XnwnRylXWSIM" target="_blank">
     The Murder
    </a>
   </td>
   <td width="128">
    Short, repetitive "stabs" (synth chords → Herrmann’s violent string slashes).
   </td>
   <td width="128">
    Hannah Peel
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Gustav Mahler
    <br/>
    Berliner Philharmoniker
    <br/>
    Claudio Abbado
   </td>
   <td>
    <a href="https://open.spotify.com/track/1Z1DK8nlqNmV9RywT9QRCB" target="_blank">
     Symphony No. 5: IV. Adagietto. Sehr langsam
    </a>
   </td>
   <td width="128">
    Contrasts Herrmann’s dissonance with resolving suspensions (minor seconds → lush major sevenths), using the same string ensemble.
   </td>
   <td width="128">
    Keelan Carew
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Beyoncé
    <br/>
    JAY-Z
   </td>
   <td>
    <a href="https://open.spotify.com/track/5IVuqXILoxVWvWEPm82Jxr" target="_blank">
     Crazy In Love (feat. Jay-Z)
    </a>
   </td>
   <td width="128">
    Ambiguous minor-third opening (C–A oscillation → Beyoncé’s sampled horn riff).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    David Soul
   </td>
   <td>
    <a href="https://open.spotify.com/track/2EDWTamwVRo9XZ6LapRDGA" target="_blank">
     Don't Give up on Us
    </a>
   </td>
   <td width="128">
    Brass motif (sampled from The Chi-Lites → echoed in Soul’s soaring string/piano arrangement).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001n8ym" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Chip Wickham
   </td>
   <td>
    <a href="https://open.spotify.com/track/7u9Om8t1fkRMvDEu7YiA5s" target="_blank">
     Rebel No.23
    </a>
   </td>
   <td width="128">
    "Understated but definite chord repetition" (piano nudge effect).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    The Who
   </td>
   <td>
    <a href="https://open.spotify.com/track/0DkCOLwvtxVPs3ri0XbDLK" target="_blank">
     Bell Boy
    </a>
   </td>
   <td width="128">
    Shared "percussion driving the track" and "maintained harmony."
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Anna Meredith
   </td>
   <td>
    <a href="https://open.spotify.com/track/63kJNbVTG8PtHlshoOMiZa" target="_blank">
     Nautilus
    </a>
   </td>
   <td width="128">
    "Swagger" and relentless rhythm; chromatic experimentation.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Dick Dale
   </td>
   <td>
    <a href="https://open.spotify.com/track/3OnCnEWgy79xR5pr2kv4TX" target="_blank">
     Misirlou
    </a>
   </td>
   <td width="128">
    "Repeating notes and ascending melody" structure.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Warda
   </td>
   <td>
    <a href="https://open.spotify.com/track/2A4xTe1uOdRKKJUyilAqrF" target="_blank">
     Batwanes Beek
    </a>
   </td>
   <td width="128">
    Links to Misirlou's tremolo guitar (mimicking an oud) and Middle Eastern scales.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="6">
    <a href="https://www.bbc.co.uk/programmes/m001nh47" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    George Frideric Handel
    <br/>
    Trevor Pinnock
    <br/>
    The English Concert
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Simon Preston
     <br/>
     The Choir Of Westminster Abbey
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/30bQxViotttoZ7x2iUP2L9" target="_blank">
     Zadok the Priest (Coronation Anthem No. 1, HWV 258)
    </a>
   </td>
   <td width="128">
    Grand orchestral introductions and "emotional string arrangements".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Bolivia Manta
   </td>
   <td>
    <a href="https://open.spotify.com/track/6pHoa0oAEc6EuArLohNaD1" target="_blank">
     Carnaval Ayacuchano
    </a>
   </td>
   <td width="128">
    Ostinato patterns and semi-quaver rhythms.
   </td>
   <td width="128">
    Rakhi Singh
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Eve
    <br/>
    Gwen Stefani
   </td>
   <td>
    <a href="https://open.spotify.com/track/3RmKpob8xzv1pzHEQrMJah" target="_blank">
     Let Me Blow Ya Mind
    </a>
   </td>
   <td width="128">
    Opens with excited crowd chatter (studio voices vs. festival sounds); shared pentatonic scale usage.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Central Cee
   </td>
   <td>
    <a href="https://open.spotify.com/track/3LtpKP5abr2qqjunvjlX5i" target="_blank">
     Doja
    </a>
   </td>
   <td width="128">
    Direct sample/sped-up version of Eve's track that went viral on TikTok.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Kaija Saariaho
    <br/>
    Peter Herresthal
    <br/>
    Oslo Philharmonic Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Clément Mao-Takacs
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/7IKTDUfwzjAjrxnomrrEjN" target="_blank">
     Vers toi qui es si loin
    </a>
   </td>
   <td width="128">
    Pentatonic exploration and microtonal "in-between notes" sensibility.
   </td>
   <td width="128">
    Alexis Ffrench
   </td>
  </tr>
  <tr>
   <td align="center">
    6
   </td>
   <td>
    Bob Dylan
   </td>
   <td>
    <a href="https://open.spotify.com/track/6os5B6xjuke9YfBKH3tu1e" target="_blank">
     Highway 61 Revisited
    </a>
   </td>
   <td width="128">
    Sliding pitch techniques (slide whistle/violin harmonics); biblical lyrical themes.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001npgc" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    -M-
   </td>
   <td>
    <a href="https://open.spotify.com/track/19UacICIUpQyCSaqqUbhsU" target="_blank">
     Belleville rendez-vous - Version française
    </a>
   </td>
   <td width="128">
    Lead guitar's "pocket" improvisation in song gaps.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Aretha Franklin
   </td>
   <td>
    <a href="https://open.spotify.com/track/1wGvueGYFPUmQUtVglgcPt" target="_blank">
     Spirit in the Dark
    </a>
   </td>
   <td width="128">
    Call-and-response structure (like Belleville's vocal/instrument dialogue); shared gospel/jazz energy.
   </td>
   <td width="128">
    Natalie Duncan
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Franz Liszt
    <br/>
    Vladimir Horowitz
   </td>
   <td>
    <a href="https://open.spotify.com/track/7CIoJE0JfVFcmmUY3fFojH" target="_blank">
     Hungarian Rhapsody No. 2 in C-Sharp Minor, S. 244/2
    </a>
   </td>
   <td width="128">
    Shares "gears" concept with Aretha - building intensity through tempo shifts and virtuosic flair.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Miles Davis
    <br/>
    Michel Legrand
   </td>
   <td>
    <a href="https://open.spotify.com/track/3C4TaiUak2l8gQcN0Ygeax" target="_blank">
     Concert on the Runway
    </a>
   </td>
   <td width="128">
    Both tracks showcase virtuosic spectacle.
   </td>
   <td width="128">
    Gabriella Swallow
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Colt Ford
   </td>
   <td>
    <a href="https://open.spotify.com/track/1kMEwjZubAuZfsFeJpx5u5" target="_blank">
     Cricket on a Line Featuring Rhett Akins
    </a>
   </td>
   <td width="128">
    Inspired by insect sounds in Miles' track (Outback flies → Southern crickets).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001nw1r" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ghazalaw
   </td>
   <td>
    <a href="https://open.spotify.com/track/4nen8SVjhK1wlFFAzH8yeC" target="_blank">
     Moliannwn
    </a>
   </td>
   <td width="128">
    Shared theme of birds (the "whip-poor-will" in the lyrics).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    James Taylor
   </td>
   <td>
    <a href="https://open.spotify.com/track/0DTzNcTTUZRFhJqMcBh34s" target="_blank">
     My Blue Heaven
    </a>
   </td>
   <td width="128">
    Mention of "whip-poor-will" in the lyrics.
   </td>
   <td width="128">
    Rick Wakeman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Coolio
    <br/>
    L.V.
   </td>
   <td>
    <a href="https://open.spotify.com/track/1DIXPcTDzTj8ZMHt3PDt8p" target="_blank">
     Gangsta's Paradise
    </a>
   </td>
   <td width="128">
    The use of strings in the arrangement connects to the violin in James Taylor's version of "My Blue Heaven."
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Hans Zimmer
   </td>
   <td>
    <a href="https://open.spotify.com/track/6PHMAqyTi2zjs6aXneg0EC" target="_blank">
     What Are You Going to Do When You Are Not Saving the World?
    </a>
   </td>
   <td width="128">
    Ostinato violin figure similar in key and rhythm to the strings in "Gangsta's Paradise."
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Raffaella Carrà
   </td>
   <td>
    <a href="https://open.spotify.com/track/4RGMka1jhff27B8zMkMWRO" target="_blank">
     A far l'amore comincia tu
    </a>
   </td>
   <td width="128">
    Punctuated, rhythmic drums.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001p22d" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Sam Fonteyn
   </td>
   <td>
    <a href="https://open.spotify.com/track/73fMv1iFBRBOy0UEAJEUzz" target="_blank">
     Ski Sunday Theme (2018)
    </a>
   </td>
   <td width="128">
    Staccato rhythms and percussive energy.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Spiro
   </td>
   <td>
    <a href="https://open.spotify.com/track/6wHKUVOjl0HLIFgpA6GkVo" target="_blank">
     We Will Be Absorbed
    </a>
   </td>
   <td width="128">
    Minimalist technique of repeating motifs ("bouncing off" notes).
   </td>
   <td width="128">
    Sam Sweeney
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Moça Prosa
   </td>
   <td>
    <a href="https://open.spotify.com/track/782usIZhWSjPWfQSDl9FW4" target="_blank">
     PONTO DAS CABOCLAS
    </a>
   </td>
   <td width="128">
    Layering of rhythmic patterns (like clockwork mechanics); hypnotic, revolving nature of the music.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Maurice Ravel
    <br/>
    Arpad Joo
    <br/>
    London Symphony Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/0C2f9MGp2cqDrBwVIOdbAk" target="_blank">
     Boléro, M. 81
    </a>
   </td>
   <td width="128">
    Insistent, dance-like rhythm (samba → bolero); gradual orchestral build mirroring the vocal layers in the previous track.
   </td>
   <td width="128">
    Debbie Wiseman
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Etta James
   </td>
   <td>
    <a href="https://open.spotify.com/track/1kPBT8S2wJFNAyBMnGVZgL" target="_blank">
     I'd Rather Go Blind
    </a>
   </td>
   <td width="128">
    Repeating triplets (piano/organ) that sustain tension, mirroring Ravel's snare drum motif.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001p7rt" target="_blank">
     9
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Johnny Cash
   </td>
   <td>
    <a href="https://open.spotify.com/track/2fDHuS1PTkHBbCWWZF1ph9" target="_blank">
     Folsom Prison Blues - Live at Folsom State Prison, Folsom, CA - January 1968
    </a>
   </td>
   <td width="128">
    Prison narrative (both songs involve incarceration).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ludwig van Beethoven
   </td>
   <td>
    <a href="https://open.spotify.com/track/5m3D0yRJBtXS7gYp3kIzPI" target="_blank">
     Symphony No. 9 in D Minor, Op. 125 "Choral": IV. Finale. Presto - Live
    </a>
   </td>
   <td width="128">
    Four-note motif and thematic shift from incarceration to freedom (Berlin Wall performance).
   </td>
   <td width="128">
    Richard Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Foo Fighters
   </td>
   <td>
    <a href="https://open.spotify.com/track/44wXefe8WB9Fd6xwtmAwbR" target="_blank">
     Monkey Wrench
    </a>
   </td>
   <td width="128">
    Emphatic, on-beat vocal delivery (matching "Ode to Joy"’s pounding rhythm) and melodic hooks.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Tina Turner
   </td>
   <td>
    <a href="https://open.spotify.com/track/3ErsOxqe2RmXkR65wkygDz" target="_blank">
     What's Love Got to Do with It - 2015 Remaster
    </a>
   </td>
   <td width="128">
    Key of B major and synthetic instrumentation (synth harmonica mimicking Dave Grohl’s guitar energy).
   </td>
   <td width="128">
    <em>
     Unknown
    </em>
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Wolfgang Amadeus Mozart
    <br/>
    Teddy Tahu Rhodes
    <br/>
    Ola Rudner
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Tasmanian Symphony Orchestra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6VmYJZryH4PAWS533B9A8Z" target="_blank">
     The Magic Flute: Der Vogelfänger bin ich ja (Birdcatcher's Song)
    </a>
   </td>
   <td width="128">
    Dialogue between voice and wind-like sounds (synth pipes in Turner → panpipes/flute in The Magic Flute).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
 </tbody>
</table>

## Series 7

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001r7ww" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Gala
    <br/>
    Molella
    <br/>
    Phil Jay
   </td>
   <td>
    <a href="https://open.spotify.com/track/3u5N55tHf7hXATSQrjBh2q" target="_blank">
     Freed From Desire - prod. Molella, Phil Jay
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    George Gershwin
    <br/>
    Oscar Levant
    <br/>
    Paul Whiteman &amp; His Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Paul Whiteman
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/66sNIqDeLGOqzkZb2tZFeZ" target="_blank">
     Piano Concerto in F Major: 3rd movement
    </a>
   </td>
   <td width="128">
    Repetitive nature and jazzy chords; organ's early jump-ins to the beat.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Queen
   </td>
   <td>
    <a href="https://open.spotify.com/track/7tFiyTwD0nx5a1eklYtX2J" target="_blank">
     Bohemian Rhapsody - Remastered 2011
    </a>
   </td>
   <td width="128">
    Dramatic switch-ups in style connect to Gershwin's unpredictable changes; both have "agitated" sections.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Gustav Mahler
    <br/>
    Borodin Quartet
   </td>
   <td>
    <a href="https://open.spotify.com/track/1PNEoPCdPpzvSTwkThWNMZ" target="_blank">
     Piano Quartet in A Minor: I. Allegro
    </a>
   </td>
   <td width="128">
    Mahler was born in Bohemia; symphonic nature and sweeping intervals.
   </td>
   <td width="128">
    Isata Kanneh-Mason
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Stevie Wonder
   </td>
   <td>
    <a href="https://open.spotify.com/track/6SvMoVRctg7Z3jDtlYIYlL" target="_blank">
     Fingertips, Pt. 2 - Live/1962
    </a>
   </td>
   <td width="128">
    "Unexpected musical sections and scale runs"; similar motif in minor and major key.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001rh85" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ramona Singh
   </td>
   <td>
    <a href="https://open.spotify.com/track/43JkPkAXVCcyuZK8WqBZT3" target="_blank">
     Mary Had a Little Lamb
    </a>
   </td>
   <td width="128">
    Stevie teased the melody of "Mary Had a Little Lamb" on harmonica during the live recording.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    The Doobie Brothers
   </td>
   <td>
    <a href="https://open.spotify.com/track/2yBVeksU2EtrPJbTu4ZslK" target="_blank">
     What a Fool Believes
    </a>
   </td>
   <td width="128">
    "Mary Had a Little Lamb" melody virtually identical to the piano riff of "What a Fool Believes".
   </td>
   <td width="128">
    Keelan Carew
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Igor Stravinsky
    <br/>
    Sir Simon Rattle
    <br/>
    City Of Birmingham Symphony Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Peter Donohoe
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/1N61edclDbsq8qEOzIdgxe" target="_blank">
     Stravinsky: Petrushka, Pt. 1 "The Shrovetide Fair": The Charlatan's Booth - Russian Dance (1947 Version)
    </a>
   </td>
   <td width="128">
    Repeating piano chord pattern/riff.
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Mari Kalkun
   </td>
   <td>
    <a href="https://open.spotify.com/track/2xYbbYHaCUYorpYMyqEEOM" target="_blank">
     Kui Kivid Olid Veel Pehmed (When the Stones Were Still Soft)
    </a>
   </td>
   <td width="128">
    The orchestral stabs and brass work in "Petrushka" connect to the experimental brass sounds (trumpet and tuba).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Mike Post
   </td>
   <td>
    <a href="https://open.spotify.com/track/79POofM42lXOY10DaSfkBU" target="_blank">
     The A-Team
    </a>
   </td>
   <td width="128">
    Brass harmonies and powerful horns reminiscent of colliery bands and military-style brass; helicopter sounds.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001rqzr" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Eric Mingus
    <br/>
    David Amram
    <br/>
    Larry Simon
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     The Langston Hughes Project
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/3RZgDERiWt0mqWeESZK0Bw" target="_blank">
     Life Is Fine
    </a>
   </td>
   <td width="128">
    Spoken-word narration; use of rhythmic speech as a musical texture.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Alberto Ginastera
    <br/>
    Simón Bolívar Youth Orchestra of Venezuela
    <br/>
    Gustavo Dudamel
   </td>
   <td>
    <a href="https://open.spotify.com/track/3miLxRVR1pUWByasPGjDLd" target="_blank">
     Estancia / Danzas del Ballet: IV. Danza final (Malambo) - Live
    </a>
   </td>
   <td width="128">
    Percussive taps and groove, "supersized" into orchestral energy.
   </td>
   <td width="128">
    Ben Gernon
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Baccara
   </td>
   <td>
    <a href="https://open.spotify.com/track/5bNAkLtsyrzktQkFkWfA9R" target="_blank">
     Yes Sir, I Can Boogie
    </a>
   </td>
   <td width="128">
    Ascending glissando/xylophone runs mirror Ginastera’s orchestral flourishes.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Madison Cunningham
   </td>
   <td>
    <a href="https://open.spotify.com/track/79NCNvyJMKSCVSGQZjSLf4" target="_blank">
     Something To Believe In
    </a>
   </td>
   <td width="128">
    Shares the harmonic movement (5th → sharp 5th → 6th) from Baccara’s chorus.
   </td>
   <td width="128">
    Emma Rawicz
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Cherry Bullet
   </td>
   <td>
    <a href="https://open.spotify.com/track/6KxACudfT4vVXnDUkjU6lN" target="_blank">
     Hands Up
    </a>
   </td>
   <td width="128">
    Samples Beethoven’s "Für Elise", echoing Cunningham’s classical-inspired tension in hyper-pop.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001rysb" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Wolfgang Amadeus Mozart
    <br/>
    Daniel Barenboim
    <br/>
    English Chamber Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/1MkN0NejhZFZGHRfxkTB8U" target="_blank">
     Mozart: Symphony No. 40 in G Minor, K. 550: I. Molto allegro
    </a>
   </td>
   <td width="128">
    Similar, repeated-note melodic hook.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Oscar Peterson Trio
   </td>
   <td>
    <a href="https://open.spotify.com/track/0RIQBKhveHc4LA4BhtkstS" target="_blank">
     Easy Does It
    </a>
   </td>
   <td width="128">
    Reinterprets Mozart’s chromatic second theme as a jazz "walking bass" line.
   </td>
   <td width="128">
    Matilda Lloyd
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Whitney Houston
   </td>
   <td>
    <a href="https://open.spotify.com/track/4eHbdreAnSOrDDsFfc4Fpm" target="_blank">
     I Will Always Love You
    </a>
   </td>
   <td width="128">
    Neighboring tones and emotional phrasing.
   </td>
   <td width="128">
    Leon Foster Thomas
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Mwana Cotide
   </td>
   <td>
    <a href="https://open.spotify.com/track/6iROK7vllzW09UtEVQ8UWL" target="_blank">
     Kwa Heri Mafisadi
    </a>
   </td>
   <td width="128">
    "Sound world" of electronic keyboards; "goodbye" songs.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    David Tomlinson
    <br/>
    Dick Van Dyke
    <br/>
    The Londoners
   </td>
   <td>
    <a href="https://open.spotify.com/track/3BHxMGVE3tN2dZsVU1l487" target="_blank">
     Let's Go Fly a Kite - From "Mary Poppins"/Soundtrack Version
    </a>
   </td>
   <td width="128">
    3/4 waltz rhythm and "communal joy".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001s63y" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Unknown
   </td>
   <td>
    <a href="https://www.youtube.com/watch?v=AhxvtFlUX-4" target="_blank">
     God Save the Queen (from 1888 and 1898)
    </a>
   </td>
   <td width="128">
    Three-note melodic motif and descending chorus interval; lyrical imperatives (e.g., "Let's go..." vs. "Send him...").
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Charles Ives
    <br/>
    Patrick Carfizzi
    <br/>
    J.J. Penna
   </td>
   <td>
    <a href="https://open.spotify.com/track/1EmFfQIfTCl8ziiKJBpTOZ" target="_blank">
     In Flanders Fields
    </a>
   </td>
   <td width="128">
    Five-note melodic fragment from "God Save the Queen" transformed into a dissonant, anti-war setting with ironic references to national anthems.
   </td>
   <td width="128">
    Roderick Williams
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    John Williams
   </td>
   <td>
    <a href="https://open.spotify.com/track/1NyfmLAx3qpxUru5ssrSZy" target="_blank">
     Main Title And First Victim - From "Jaws" Soundtrack
    </a>
   </td>
   <td width="128">
    Two alternating notes creating suspense.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Maurice Ravel
    <br/>
    Jennifer Pike
    <br/>
    Martin Roscoe
   </td>
   <td>
    <a href="https://open.spotify.com/track/26LeAo56dN3L2KoRbAy0zb" target="_blank">
     Violin Sonata No. 2 in G Major, M. 77: III. Perpetuum mobile. Allegro
    </a>
   </td>
   <td width="128">
    Semitones, silences, and ostinato.
   </td>
   <td width="128">
    Jennifer Pike
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Labi Siffre
   </td>
   <td>
    <a href="https://open.spotify.com/track/20VuO95A8RxUPlShnfYArW" target="_blank">
     I Got The... - 2006 Remaster
    </a>
   </td>
   <td width="128">
    Minimal notes, pauses, and bluesy harmonies.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001sdyx" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Snoop Dogg
   </td>
   <td>
    <a href="https://open.spotify.com/track/39QBkWKnap8wRSW4WB9OK0" target="_blank">
     Gin and Juice
    </a>
   </td>
   <td width="128">
    High-pitched sustained whistle motif.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    McCoy Tyner
   </td>
   <td>
    <a href="https://open.spotify.com/track/0lELi5BqmUO4hXTFfAUf60" target="_blank">
     Passion Dance
    </a>
   </td>
   <td width="128">
    Phrygian mode; tonal ambiguity and quartal harmony.
   </td>
   <td width="128">
    Amanda Whiting
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Steely Dan
   </td>
   <td>
    <a href="https://open.spotify.com/track/0xeBC6N81ZBYDtxuBFGSuO" target="_blank">
     Deacon Blues
    </a>
   </td>
   <td width="128">
    Quartal harmony and layering techniques (e.g. saxophone/piano interplay).
   </td>
   <td width="128">
    Fraser T. Smith
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Florence Beatrice Price
    <br/>
    Sphinx Virtuosi
   </td>
   <td>
    <a href="https://open.spotify.com/track/4dAudDd5aYKHSrVzMSR8HI" target="_blank">
     String Quartet No. 2 in A Minor: II. Andante cantabile (Arr. Colbert for String Ensemble)
    </a>
   </td>
   <td width="128">
    Two-note motif mirroring the song’s foundational melody.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Eliane Elias
   </td>
   <td>
    <a href="https://open.spotify.com/track/74oxKgbwsAbRjNN9oOsypN" target="_blank">
     Oye Como Va
    </a>
   </td>
   <td width="128">
    Shifts from two-note motifs to two-chord progressions.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001smvw" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Drifters
   </td>
   <td>
    <a href="https://open.spotify.com/track/65jrjEhWfAvysKfnojk1i0" target="_blank">
     Under the Boardwalk
    </a>
   </td>
   <td width="128">
    Guiro percussion and Latin rhythmic feel.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ludwig van Beethoven
    <br/>
    Lang Lang
   </td>
   <td>
    <a href="https://open.spotify.com/track/0H2VhGUC3P3hvwz8rdGIpC" target="_blank">
     Für Elise, Bagatelle in A Minor, WoO 59
    </a>
   </td>
   <td width="128">
    Chromatic melody.
   </td>
   <td width="128">
    Debbie Wiseman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Cesária Evora
   </td>
   <td>
    <a href="https://open.spotify.com/track/6MC0QTKf4VTZ6HWeTmNPGp" target="_blank">
     Tchintchirote
    </a>
   </td>
   <td width="128">
    Melodic suspense (two-note motif mirrored in Evora’s vocals).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Captain Beefheart &amp; His Magic Band
   </td>
   <td>
    <a href="https://open.spotify.com/track/18gacaQNAUOab7tnWaeb5L" target="_blank">
     Golden Birdies
    </a>
   </td>
   <td width="128">
    Lyrical bird imagery ("golden birdies" → Cape Verde warbler).
   </td>
   <td width="128">
    Rhodri Marsden
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Aram Khachaturian
    <br/>
    Wiener Philharmoniker
    <br/>
    Constantin Silvestri
   </td>
   <td>
    <a href="https://open.spotify.com/track/3pbKcSUisBm1aii57W7S7d" target="_blank">
     Khachaturian: Gayaneh, Op. 50: Sabre Dance
    </a>
   </td>
   <td width="128">
    Wooden percussion prominence (xylophone in "Sabre Dance" and marimba in "Golden Birdies").
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001sv9b" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Salimata Diabaté
   </td>
   <td>
    <a href="https://open.spotify.com/track/3mypo33Aud0XbaRDFY1G5l" target="_blank">
     El hadji n'fa djigui Diabaté
    </a>
   </td>
   <td width="128">
    Use of idiophones (xylophone and balafon).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Matt Calvert
   </td>
   <td>
    <a href="https://open.spotify.com/track/5lbuWfe2iafc5Vd8DaDufE" target="_blank">
     Mute Heart
    </a>
   </td>
   <td width="128">
    Interplay of instruments creating a "wash of sonic warmth".
   </td>
   <td width="128">
    Natalie Duncan
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Dean Shostak
   </td>
   <td>
    <a href="https://open.spotify.com/track/2WzJ2ji2XWz86aBGHSoXUa" target="_blank">
     Jingle Bells
    </a>
   </td>
   <td width="128">
    Playful ascending lines and the glass harmonica sound.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Gaetano Donizetti
    <br/>
    Maria Callas
    <br/>
    Tullio Serafin
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Orchestra del Maggio Musicale Fiorentino
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/3nVFZo0bZx9gHRXzWTnL2o" target="_blank">
     Donizetti: Lucia di Lammermoor, Act 3: "Il dolce suono" (Lucia)
    </a>
   </td>
   <td width="128">
    Glass harmonica; simplicity of the opening minor chord.
   </td>
   <td width="128">
    Martin Phipps
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Cher
   </td>
   <td>
    <a href="https://open.spotify.com/track/2goLsvvODILDzeeiT4dAoR" target="_blank">
     Believe
    </a>
   </td>
   <td width="128">
    Melisma (natural in opera, artificially created with Auto-Tune in this pop song).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001t33x" target="_blank">
     9
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ma Rainey
   </td>
   <td>
    <a href="https://open.spotify.com/track/3czcSX2L2FmQZX7dQTiEt5" target="_blank">
     Prove It On Me Blues
    </a>
   </td>
   <td width="128">
    Themes of resilience and LGBTQ+ anthems.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Laurie Anderson
   </td>
   <td>
    <a href="https://open.spotify.com/track/421Gp1eSmOIcD6alTWowFR" target="_blank">
     O Superman
    </a>
   </td>
   <td width="128">
    Pioneering women in music and the use of vocal manipulation.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    The Chakachas
   </td>
   <td>
    <a href="https://open.spotify.com/track/6KmeJB34wVVqar5b2uxWrE" target="_blank">
     Yo Soy Cubano
    </a>
   </td>
   <td width="128">
    Sampled robotic vocal phrase in Kendrick Lamar's "Backseat Freestyle", linking back to Anderson's vocoder effects.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Igor Stravinsky
    <br/>
    Brussels Philharmonic
    <br/>
    Alexander Rahbari
   </td>
   <td>
    <a href="https://open.spotify.com/track/01oTznxLZoqz7DhCocedz9" target="_blank">
     The Firebird Suite (1919 Version): VII. Finale
    </a>
   </td>
   <td width="128">
    Use of major seventh chords and celebratory, joyful transitions.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    ABBA
   </td>
   <td>
    <a href="https://open.spotify.com/track/4euAGZTszWPrriggYK0HG9" target="_blank">
     Lay All Your Love On Me
    </a>
   </td>
   <td width="128">
    Grandiose chord progressions and orchestral-like arrangements in disco.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
 </tbody>
</table>

## Series 8

### Notes

#### Ep. 1, Track 1
Sung live in the studio.
#### Ep. 3
Linton Stephens sat in for Cerys (who was recovering from surgery on a broken arm).
#### Ep. 4
Jess Gillam sat in for Cerys.
#### Ep. 8
Although indicating she would return in six months (November 2024), this is Cerys' last appearance on the show as of July 2025.
<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001w1gw" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    London Bulgarian Choir
   </td>
   <td>
    <a href="https://open.spotify.com/track/4DBbQBAPrh6wRcDPy4loex" target="_blank">
     Povela E Yova / Dilmano Dilbero
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Philip Glass
    <br/>
    Christopher Keene
    <br/>
    New York City Opera Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/3pryCnejhwCIAJ5519ysPN" target="_blank">
     Satyagraha: Act II: Confrontation and Rescue
    </a>
   </td>
   <td width="128">
    Primal vocal techniques and anatomical resonance.
   </td>
   <td width="128">
    Nicky Spence
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Billie Eilish
   </td>
   <td>
    <a href="https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m" target="_blank">
     bad guy
    </a>
   </td>
   <td width="128">
    Syncopation and offbeat vocal rhythms.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Antônio Carlos Jobim
    <br/>
    Frank Sinatra
   </td>
   <td>
    <a href="https://open.spotify.com/track/2nwamC3x9eHLhLnGTrvh3w" target="_blank">
     Meditation (Meditação)
    </a>
   </td>
   <td width="128">
    Syncopation and bossa nova's rhythmic interplay.
   </td>
   <td width="128">
    Corinne Bailey Rae
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Adele
   </td>
   <td>
    <a href="https://open.spotify.com/track/73CMRj62VK8nUS4ezD2wvi" target="_blank">
     Set Fire to the Rain
    </a>
   </td>
   <td width="128">
    Physically impossible lyrical themes (sun falling out of the sky; setting fire to rain); themes of longing and a shared "U-shaped" melodic motif.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001w8sy" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Bavarian Oompah Band
   </td>
   <td>
    <a href="https://open.spotify.com/track/776JkZeW95fyv0pC5yUoA5" target="_blank">
     In Munchen Steht Ein Hofbrauhaus
    </a>
   </td>
   <td width="128">
    Dactyl rhythm pattern (strong-weak-weak) found in both the bridge of Adele's song and the oompa rhythm.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Georg Philipp Telemann
    <br/>
    Collegium Musicum 90
    <br/>
    Simon Standage
   </td>
   <td>
    <a href="https://open.spotify.com/track/79YVAhJgjUJwx0O6v5tmht" target="_blank">
     Orchestral Suite in B-Flat Major, TWV 55:B8, "Ouverture burlesque": I. Ouverture
    </a>
   </td>
   <td width="128">
    Dactyl rhythm pattern; folkloric vibe.
   </td>
   <td width="128">
    Benjamin Appl
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Béla Bartók
    <br/>
    Eytan Arditi
    <br/>
    Rea Meir
   </td>
   <td>
    <a href="https://open.spotify.com/track/3ptUlOYvsEFwborwmbuAXU" target="_blank">
     Romanian Folk Dances: No.6 Aprózó / Mărunțel / Fast Dance
    </a>
   </td>
   <td width="128">
    Folkloric element; percussive drive.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Jacques Dutronc
   </td>
   <td>
    <a href="https://open.spotify.com/track/2CLeotsLhEUu0qkj56vbUj" target="_blank">
     Il est cinq heures, Paris s'éveille
    </a>
   </td>
   <td width="128">
    Relentless energy and action that "forces you out of slumber".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Van Morrison
   </td>
   <td>
    <a href="https://open.spotify.com/track/683b4ikwa62JevCjwrmfg6" target="_blank">
     Moondance - 2013 Remaster
    </a>
   </td>
   <td width="128">
    Prominent flute parts.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001wjt0" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Samuel Coleridge-Taylor
    <br/>
    Kaleidoscope Chamber Collective
   </td>
   <td>
    <a href="https://open.spotify.com/track/1CPln7dAV6U4pHppewfPBd" target="_blank">
     Nonet in F Minor, Op. 2 "Gradus ad Parnassum": I. Allegro moderato
    </a>
   </td>
   <td width="128">
    Minor third piano riff that goes round and round.
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Loyle Carner
   </td>
   <td>
    <a href="https://open.spotify.com/track/6n3gJBvi9jZB9kkzHqmZ8P" target="_blank">
     Nobody Knows (Ladas Road)
    </a>
   </td>
   <td width="128">
    Samuel Coleridge-Taylor and Loyle Carner are artists from Croydon with mixed heritage.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Clara Schumann
    <br/>
    Isata Kanneh-Mason
   </td>
   <td>
    <a href="https://open.spotify.com/track/2cP5RfeE19S7OneumxMayY" target="_blank">
     Piano Sonata in G Minor: II. Adagio
    </a>
   </td>
   <td width="128">
    Descending bassline; thematic connection contrasting absent father (Loyle Carner) with domineering father (Clara Schumann).
   </td>
   <td width="128">
    Debbie Wiseman
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Alicia Keys
   </td>
   <td>
    <a href="https://open.spotify.com/track/3XVBdLihbNbxUwZosxcGuJ" target="_blank">
     If I Ain't Got You
    </a>
   </td>
   <td width="128">
    Connected through the use of diminished seventh chords, which appear prominently in both Clara Schumann's piece and this song.
   </td>
   <td width="128">
    Linton Stephens
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Glenn Miller
   </td>
   <td>
    <a href="https://open.spotify.com/track/54h1RKrrFJDsNOfhwmqu9o" target="_blank">
     In the Mood - Live
    </a>
   </td>
   <td width="128">
    Melodic climb followed by a single low note at the end of both tracks.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001wrm8" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Johann Sebastian Bach
    <br/>
    András Schiff
   </td>
   <td>
    <a href="https://open.spotify.com/track/2XxC430QMotGdympDP1aBo" target="_blank">
     The Well-Tempered Clavier, Book 1, BWV 846-869: Prelude and Fugue in C Major, BWV 846
    </a>
   </td>
   <td width="128">
    Straightening out the swinging arpeggios leads to Bach's broken chord arpeggios.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Lady Gaga
   </td>
   <td>
    <a href="https://open.spotify.com/track/0SiywuOBRcynK0uKGWdCnn" target="_blank">
     Bad Romance
    </a>
   </td>
   <td width="128">
    Music video opens with Bach's B minor fugue from the same Well-Tempered Clavier collection.
   </td>
   <td width="128">
    Leo Geyer
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Ming Flute Ensemble
   </td>
   <td>
    <a href="https://open.spotify.com/track/39SrgDbkBDeJvACI9gveGe" target="_blank">
     A Tayal Folk Song
    </a>
   </td>
   <td width="128">
    "Ra Ra Ra Ra" hook in "Bad Romance" has similar rhythmic pattern (one-two, one-two-three) and uses the same perfect fifth interval.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Gustav Mahler
   </td>
   <td>
    <a href="https://open.spotify.com/track/45xKL1tIdKMBc8y6CcX8Iu" target="_blank">
     Symphony No. 9 in D Major: Ia. Andante comodo
    </a>
   </td>
   <td width="128">
    Human/heartbeat connection - the Tayal word meaning "human" connects to music based on the human heartbeat, specifically Mahler's arrhythmic heartbeat rhythm.
   </td>
   <td width="128">
    Gillian Moore
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    David Bowie
   </td>
   <td>
    <a href="https://open.spotify.com/track/7rFN0DhIFPjAWG1EaHO2F0" target="_blank">
     Lazarus
    </a>
   </td>
   <td width="128">
    Final works/swan songs - both Mahler's 9th and Bowie's "Lazarus" were the composers' final completed works before death.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001wy3f" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Hugh Masekela
   </td>
   <td>
    <a href="https://open.spotify.com/track/2P6Buc8kWRgShx7aHIadqu" target="_blank">
     Grazing In The Grass
    </a>
   </td>
   <td width="128">
    Three descending notes from "Lazarus" by David Bowie, but creating an uplifting effect with brass instead of the mournful sound.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Paul Simon
   </td>
   <td>
    <a href="https://open.spotify.com/track/0qxYx4F3vm1AOnfux6dDxP" target="_blank">
     You Can Call Me Al
    </a>
   </td>
   <td width="128">
    Three note descent in pentatonic scale; South African musical connection.
   </td>
   <td width="128">
    Joe Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Guillaume de Machaut
    <br/>
    The Hilliard Ensemble
   </td>
   <td>
    <a href="https://open.spotify.com/track/2T6j4ZH7hQp9Xq5v8W6rk1" target="_blank">
     Ma fin est mon commencement, Rondeau 14
    </a>
   </td>
   <td width="128">
    Forward and backward musical movement, like the reversed bass solo in "You Can Call Me Al".
   </td>
   <td width="128">
    Anna Meredith
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Bala Desejo
    <br/>
    Dora Morelenbaum
    <br/>
    Julia Mestre
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Lucas Nunes
     <br/>
     Zé Ibarra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/46nVimyGfbnKUMU9rDvnUG" target="_blank">
     Baile De Máscaras (Recarnaval)
    </a>
   </td>
   <td width="128">
    Momentum and perpetual motion; walking bassline.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Henry Mancini
   </td>
   <td>
    <a href="https://open.spotify.com/track/0juPSJLFnLFim7BK6VzTes" target="_blank">
     The Pink Panther Theme - From "The Pink Panther"
    </a>
   </td>
   <td width="128">
    "Sloping da da-da, da da-da" rhythm pattern.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001x5c6" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Kate Bush
   </td>
   <td>
    <a href="https://open.spotify.com/track/4DkKgGqqfx8C79RFo8ZuTl" target="_blank">
     Babooshka - 2018 Remaster
    </a>
   </td>
   <td width="128">
    Shared "swing medium" rhythm.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Edvard Grieg
    <br/>
    Radu Lupu
    <br/>
    London Symphony Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     André Previn
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/35Vlk3QLL1hUpI5OEOQ04H" target="_blank">
     Piano Concerto in A Minor, Op. 16: I. Allegro molto moderato
    </a>
   </td>
   <td width="128">
    Descending riff pattern; first inversions both present in Babooshka.
   </td>
   <td width="128">
    Anne Dudley
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Lalo Schifrin
    <br/>
    Alan Silvestri
    <br/>
    Cincinnati Pops Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Erich Kunzel
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/3UVhPoxIuqqDFNQq3n6lr5" target="_blank">
     Theme from "Mission Impossible" (Arr. A. Silvestri)
    </a>
   </td>
   <td width="128">
    The "spy chord" (minor major seventh) found in the opening piano flourish of the Grieg concerto (A-G♯-E-C).
   </td>
   <td width="128">
    Emily Sun
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Brendan Quinn
    <br/>
    John McSherry
    <br/>
    Francis Mc Iduff
   </td>
   <td>
    <a href="https://open.spotify.com/track/2BOVMBpQXh2L7tZ2M51zZh" target="_blank">
     The Roaring Promenade (Live)
    </a>
   </td>
   <td width="128">
    Similar energetic five-beat pulse; wind instruments taking flight after rhythm established.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Eagles
   </td>
   <td>
    <a href="https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv" target="_blank">
     Hotel California - 2013 Remaster
    </a>
   </td>
   <td width="128">
    Dueling soloists.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001xfxf" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Johann Strauss II
    <br/>
    Kiri Te Kanawa
    <br/>
    Edita Gruberova
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Wiener Philharmoniker
     <br/>
     André Previn
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/7vqwXcALbeRPfHZaUIxm8F" target="_blank">
     Die Fledermaus / Act 1: "Ach, ich darf nicht hin zu dir!"
    </a>
   </td>
   <td width="128">
    Twin instruments (guitars vs. twin operatic sopranos) playing off each other in competition.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Trallaleri of Genoa
    <br/>
    Alan Lomax
   </td>
   <td>
    <a href="https://open.spotify.com/track/0EpXJrURPHypnGOr9Er6Js" target="_blank">
     La Partenza (The Parting)
    </a>
   </td>
   <td width="128">
    Thematic connection with comedy, partings, and reunions in "Die Fledermaus"; musical form featuring voices competing and complementing each other.
   </td>
   <td width="128">
    Eliza Carthy
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Giorgio Mainerio
    <br/>
    Il Giardino Armonico
    <br/>
    Giovanni Antonini
   </td>
   <td>
    <a href="https://open.spotify.com/track/6eAqxGKS7ZYkL7UKvfUdOK" target="_blank">
     Gagliarda
    </a>
   </td>
   <td width="128">
    Wayward tuning and harmonies that don't happen at exactly the same time, deliberately seeking "wayward musical children".
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Ella Fitzgerald
   </td>
   <td>
    <a href="https://open.spotify.com/track/2cvztQuBIxwV38kg1Ydaww" target="_blank">
     How High The Moon - 1st Take
    </a>
   </td>
   <td width="128">
    Level of ornamentation and improvisation, connecting the recorder player's improvisational style to Ella Fitzgerald's jazz improvisation mastery.
   </td>
   <td width="128">
    Tim Rhys-Evans
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Colin Lucas
   </td>
   <td>
    <a href="https://open.spotify.com/track/7m9QpC8iqp4GrQ6Ag0BICY" target="_blank">
     Dollar Wine
    </a>
   </td>
   <td width="128">
    Volume of drum hits that announce tempo changes and repeated single words to "keep the party going", similar to Ella's performance style.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001xng0" target="_blank">
     8
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Richard Wagner
    <br/>
    Oda Balsborg
    <br/>
    Hetty Plümacher
    <details>
     <summary>
      <em>
       +4 more
      </em>
     </summary>
     Ira Malaniuk
     <br/>
     Gustav Neidlinger
     <br/>
     Wiener Philharmoniker
     <br/>
     Sir Georg Solti
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/2jRpXalS2vBxNDPWJyYPQ7" target="_blank">
     Das Rheingold, Scene 1: Weia! Waga! Woge du Welle! - 2012 Remaster
    </a>
   </td>
   <td width="128">
    Shares core chord changes; theme of precious commodities (gold vs. money).
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Charles Koechlin
    <br/>
    Mireille Guillaume
   </td>
   <td>
    <a href="https://open.spotify.com/track/4jXVddXyE3dnH4qtTAPsfY" target="_blank">
     Nouvelles sonatines No. 3, Op. 87: II. Mouvement de Sicilienne
    </a>
   </td>
   <td width="128">
    The swinging rhythm pattern is identical to the Renaissance Sicilian dance rhythm.
   </td>
   <td width="128">
    Keelan Carew
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    De La Soul
   </td>
   <td>
    <a href="https://open.spotify.com/track/4hB8J06D2ZaGkWZDOMpYZB" target="_blank">
     The Magic Number
    </a>
   </td>
   <td width="128">
    The four-note descending melody from Koechlin's piece becomes a three-note melody when compressed, which matches the "magic number" theme.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Toufic Farroukh
   </td>
   <td>
    <a href="https://open.spotify.com/track/3zpuZniLvXiLTMot9fCIwU" target="_blank">
     Ya nassim alrouh
    </a>
   </td>
   <td width="128">
    Fun, infectious beat that links to the hip-hop rhythm.
   </td>
   <td width="128">
    Maya Youssef
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Beyoncé
   </td>
   <td>
    <a href="https://open.spotify.com/track/7wLShogStyDeZvL0a6daN5" target="_blank">
     TEXAS HOLD 'EM
    </a>
   </td>
   <td width="128">
    Same tempo and strong beat as the Farroukh track, with acoustic guitar-picking replacing the bubbling sequencer.
   </td>
   <td width="128">
    Cerys Matthews
   </td>
  </tr>
 </tbody>
</table>

## Series 9

### Notes

#### Ep. 4, Track 5
No recording selected as it was sang live in the studio.
<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001zdv1" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Bangles
   </td>
   <td>
    <a href="https://open.spotify.com/track/00vYs0qZA40Z8AAaN7xmMO" target="_blank">
     Manic Monday
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    John Williams
    <br/>
    The City of Prague Philharmonic Orchestra
    <br/>
    James Fitzpatrick
   </td>
   <td>
    <a href="https://open.spotify.com/track/5gaXj4k0Na6X6610zOjPnG" target="_blank">
     The Knight Bus - From "Harry Potter and the Prisoner of Azkaban"
    </a>
   </td>
   <td width="128">
    The "manic" theme - looking for what sounds truly manic in music.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Sergei Prokofiev
    <br/>
    Eugene Ormandy
    <br/>
    David Bowie
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Philadelphia Orchestra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6hOLXdcITMQM0gDtEEwddL" target="_blank">
     Peter and the Wolf, Op. 67 (Remastered): The Duck, Dialogue with the Bird, Attack of the Cat
    </a>
   </td>
   <td width="128">
    Opening clarinet in "Knight Bus" reminiscent of the cartoon-like clarinet/oboe interplay in "Peter and the Wolf".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    King Crimson
   </td>
   <td>
    <a href="https://open.spotify.com/track/1FRi4xi7dnViWnxatYwnxh" target="_blank">
     Matte Kudasai
    </a>
   </td>
   <td width="128">
    Animals and music theme - music that draws directly from sounds in the animal kingdom (seagull noises).
   </td>
   <td width="128">
    Natalie Duncan
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Blondie
   </td>
   <td>
    <a href="https://open.spotify.com/track/7HKxTNVlkHsfMLhigmhC0I" target="_blank">
     Call Me
    </a>
   </td>
   <td width="128">
    12/8 time signature - speeding up the triplet rhythm from the previous track.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001zmbr" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ron Grainer
    <br/>
    Delia Derbyshire
   </td>
   <td>
    <a href="https://open.spotify.com/track/5dxWU9epbOtZ0XHv60tydp" target="_blank">
     Doctor Who (Original Theme) [From "Doctor Who"]
    </a>
   </td>
   <td width="128">
    Synth solo similarity.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Felix Mendelssohn
    <br/>
    André Previn
    <br/>
    London Symphony Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/0Q0FAKjbbtMOuAoCdkgk1V" target="_blank">
     Mendelssohn: A Midsummer Night's Dream, Op. 61, MWV M13: No. 9, Wedding March
    </a>
   </td>
   <td width="128">
    Triplet rhythm pattern.
   </td>
   <td width="128">
    Debbie Wiseman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Beyoncé
   </td>
   <td>
    <a href="https://open.spotify.com/track/2NTp1e0sRMHiw368rfCGvE" target="_blank">
     Freedom - Homecoming Live
    </a>
   </td>
   <td width="128">
    Bold brass fanfare opening.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Lisa Knapp
   </td>
   <td>
    <a href="https://open.spotify.com/track/6NKEgI6yvub0R8cZYaf9Pl" target="_blank">
     Padstow May Song
    </a>
   </td>
   <td width="128">
    Tribal/community drumming and group singing.
   </td>
   <td width="128">
    Sam Lee
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Fleetwood Mac
   </td>
   <td>
    <a href="https://open.spotify.com/track/0iINibMKtoS8duvexsqnm5" target="_blank">
     Tusk - 2015 Remaster
    </a>
   </td>
   <td width="128">
    Pounding drums and enigmatic opening.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m001zw60" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Muddy Waters
   </td>
   <td>
    <a href="https://open.spotify.com/track/58PSYdY0GFg0LFb2PxYk4T" target="_blank">
     Mannish Boy
    </a>
   </td>
   <td width="128">
    Three notes (A-C-D) from the hypnotic repeating bass riff in "Tusk" by Fleetwood Mac.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Benjamin Britten
    <br/>
    Andrew Davis
    <br/>
    BBC Symphony Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/3P22pwKcgQEqEvhBL5SLWR" target="_blank">
     Britten: Passacaglia from Peter Grimes, Op. 33b
    </a>
   </td>
   <td width="128">
    Ostinato bassline (repeated pattern) similar to "Mannish Boy"; both use the "passacaglia" form.
   </td>
   <td width="128">
    Gavin Higgins
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Marius Neset
    <br/>
    The Danish Radio Big Band
    <br/>
    Miho Hazama
   </td>
   <td>
    <a href="https://open.spotify.com/track/2FQd7hPLVQuVtta3HIKnEU" target="_blank">
     Bicycle Town, Pt. 1
    </a>
   </td>
   <td width="128">
    Bell chords in the brass section that descend, connecting to the orchestration and layering techniques in the Britten piece.
   </td>
   <td width="128">
    Emma Rawicz
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Jonathan Richman &amp; The Modern Lovers
   </td>
   <td>
    <a href="https://open.spotify.com/track/27lIgIDPyApD9F6rC2gUaT" target="_blank">
     Egyptian Reggae (Live)
    </a>
   </td>
   <td width="128">
    Near-identical melodic pattern to "Bicycle Town".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Joan Jett &amp; the Blackhearts
   </td>
   <td>
    <a href="https://open.spotify.com/track/7pu8AhGUxHZSCWTkQ2eb5M" target="_blank">
     Bad Reputation
    </a>
   </td>
   <td width="128">
    Producer Kenny Laguna worked on both "Egyptian Reggae" and "Bad Reputation".
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00202ss" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Dawn Penn
   </td>
   <td>
    <a href="https://open.spotify.com/track/7DhObRhHUtmpFXnTTMw4zQ" target="_blank">
     No, No, No
    </a>
   </td>
   <td width="128">
    Repeated guitar chords and the word "no" being repeated over and over again.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    James Newton Howard
    <br/>
    Jennifer Lawrence
   </td>
   <td>
    <a href="https://open.spotify.com/track/416MsJxvxSKY96DCmbJIRs" target="_blank">
     The Hanging Tree
    </a>
   </td>
   <td width="128">
    Endless repetition creating a trance-like quality; themes of social justice and people coming together to fight oppression.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    The Rolling Stones
   </td>
   <td>
    <a href="https://open.spotify.com/track/6lFZbCc7pn6Lme1NP7qQqQ" target="_blank">
     You Can't Always Get What You Want
    </a>
   </td>
   <td width="128">
    Use of classical choir to create cinematic grandeur and epic quality.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Tabu Ley Rochereau
   </td>
   <td>
    <a href="https://open.spotify.com/track/3J4lQBBLmuDz7IvkBKhdsv" target="_blank">
     Ngonga Ebeti
    </a>
   </td>
   <td width="128">
    Guitar and keyboard work, particularly the flowery guitar riffs reminiscent of West African music.
   </td>
   <td width="128">
    Andrew Roachford
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    <em>
     n/a
    </em>
   </td>
   <td>
    Happy Birthday to You
   </td>
   <td width="128">
    Opening vocal phrases that have the same melodic pattern.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00208pz" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ramones
   </td>
   <td>
    <a href="https://open.spotify.com/track/6SYAkJQoasyrSvAj5abGDJ" target="_blank">
     I Don't Want To Grow Up
    </a>
   </td>
   <td width="128">
    Theme of aging and celebrating another year on earth.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    The Irish Rovers
   </td>
   <td>
    <a href="https://open.spotify.com/track/720Uq2Tcr5N48CAL6DN78Z" target="_blank">
     The Barleymow
    </a>
   </td>
   <td width="128">
    Cumulative songs where verses build by adding new elements each time.
   </td>
   <td width="128">
    Anne Dudley
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Carl Orff
    <br/>
    Chor der Deutschen Oper Berlin
    <br/>
    Orchester der Deutschen Oper Berlin
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Eugen Jochum
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/1Lc1t2qMTUsTv733LADmO6" target="_blank">
     Carmina Burana: XIV. In taberna quando sumus
    </a>
   </td>
   <td width="128">
    Drinking songs - "The Barleymow" celebrates beer while "In taberna" means "when we are in the tavern".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Shobha Gurtu
   </td>
   <td>
    <a href="https://open.spotify.com/track/7ow50DUqpZvWLi71hz3jya" target="_blank">
     Humri Atariyape Aajare ( Dadra : Bhairavi )
    </a>
   </td>
   <td width="128">
    Melodic motif in the Carl Orff piece matches Bhairavi raga in Indian classical music.
   </td>
   <td width="128">
    Jasdeep Singh Degun
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Björk
   </td>
   <td>
    <a href="https://open.spotify.com/track/5G9LvzXcBoIBXOd2jzdJTs" target="_blank">
     Venus as a Boy
    </a>
   </td>
   <td width="128">
    Instrumentation using Indian strings and tabla; sensual romantic theme linking to Thumri tradition.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0020jfd" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Kay Kyser &amp; His Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/4a5fzw7uaQJsRX1XFzr3NH" target="_blank">
     Woody Woodpecker Song
    </a>
   </td>
   <td width="128">
    Subtle climbing melody introduced on celeste reminiscent of the "Woody Woodpecker" theme.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Anonymous
    <br/>
    Stefan Temmingh
   </td>
   <td>
    <a href="https://open.spotify.com/track/7eqmiXUMYDRX32y7p2vMAa" target="_blank">
     The Division Flute: Faronell's Ground
    </a>
   </td>
   <td width="128">
    Repetition as a musical feature, connecting the repeated "pecking" sounds to the repetitive nature of baroque variations.
   </td>
   <td width="128">
    Heidi Fardell
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Nicholas Britell
   </td>
   <td>
    <a href="https://open.spotify.com/track/0bSHwuTOZVJUXWT03H9oD2" target="_blank">
     Succession (Main Title Theme)
    </a>
   </td>
   <td width="128">
    Courtly grandeur and use of variations on a theme (both hallmarks of baroque music).
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Nikolai Medtner
    <br/>
    Geoffrey Tozer
   </td>
   <td>
    <a href="https://open.spotify.com/track/0m02eyVmR06zpHE8DkkmIQ" target="_blank">
     Forgotten Melodies, Op. 39: V. Sonata tragica
    </a>
   </td>
   <td width="128">
    C minor key signature; similar falling bassline patterns.
   </td>
   <td width="128">
    Keelan Carew
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Incredible Bongo Band
   </td>
   <td>
    <a href="https://open.spotify.com/track/51ml2bJs9zDLv1PbzNQzPP" target="_blank">
     Apache
    </a>
   </td>
   <td width="128">
    Uneven staccato chord stabs that punctuate the Medtner sonata, connecting to the rhythmic emphasis in "Apache".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 10

### Notes

#### Ep. 4, Track 1
Does not appear to be on any streaming services.
<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0021xvw" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Kylie Minogue
   </td>
   <td>
    <a href="https://open.spotify.com/track/3E7ZwUMJFqpsDOJzEkBrQ7" target="_blank">
     Can't Get You out of My Head
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Stephen Sondheim
    <br/>
    Bernadette Peters
   </td>
   <td>
    <a href="https://open.spotify.com/track/4oqBhS0Az0yv625qI6rFnX" target="_blank">
     Losing My Mind
    </a>
   </td>
   <td width="128">
    Theme of obsessive thoughts about someone you can't forget.
   </td>
   <td width="128">
    Isata Kanneh-Mason
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Alfred Deller
    <br/>
    Gustav Leonhardt
   </td>
   <td>
    <a href="https://open.spotify.com/track/5QPGEvyXpZFrbI3ahO6AWH" target="_blank">
     John Blow: The Self-Banished --
    </a>
   </td>
   <td width="128">
    Themes of lost love; falsetto/male voice register.
   </td>
   <td width="128">
    Richard Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    The Beach Boys
   </td>
   <td>
    <a href="https://open.spotify.com/track/5t9KYe0Fhd5cW6UYT4qP8f" target="_blank">
     Good Vibrations - Remastered 2001
    </a>
   </td>
   <td width="128">
    The ethereal nature of the countertenor voice; Brian Wilson's high vocals.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Nina Simone
   </td>
   <td>
    <a href="https://open.spotify.com/track/7M9pPyt8Gr41THLhbz4NSB" target="_blank">
     Don't Let Me Be Misunderstood
    </a>
   </td>
   <td width="128">
    Andalusian cadence chord progression.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00224t0" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Village People
   </td>
   <td>
    <a href="https://open.spotify.com/track/4YOJFyjqh8eAcbKFfv88mV" target="_blank">
     Y.M.C.A.
    </a>
   </td>
   <td width="128">
    String arrangements by Horace Ott, same arranger as "Don't Let Me Be Misunderstood".
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Johannes Brahms
    <br/>
    Leonidas Kavakos
    <br/>
    Yuja Wang
   </td>
   <td>
    <a href="https://open.spotify.com/track/7xfZpCaWtFrxbZ7eEKjTiq" target="_blank">
     Scherzo in C Minor for Violin and Piano (from the F-A-E Sonata)
    </a>
   </td>
   <td width="128">
    Acronyms - Y.M.C.A. connects to F-A-E ("Frei aber einsam").
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    John C. Williams
   </td>
   <td>
    <a href="https://open.spotify.com/track/1BrCsHOlpUAIId0Y38w2j1" target="_blank">
     Canarios
    </a>
   </td>
   <td width="128">
    Hemiola rhythmic patterns present in both pieces.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Jules Massenet
    <br/>
    Alfredo Kraus
    <br/>
    Georges Prêtre
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Orchestra Del Teatro Alla Scala, Milano
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/3RnDNwr7SK5GptrCfdo4za" target="_blank">
     Werther: Act III, "Pourquoi me réveiller"
    </a>
   </td>
   <td width="128">
    Geographic connection - Canary Islands (Canarios dance origins, Alfredo Kraus from Canary Islands).
   </td>
   <td width="128">
    Roderick Williams
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Ella Fitzgerald
    <br/>
    Bobby Orton's Teen-Aces
   </td>
   <td>
    <a href="https://open.spotify.com/track/7mugdr48xfGULw99NSphZ6" target="_blank">
     My Bonnie Lies Over The Ocean
    </a>
   </td>
   <td width="128">
    Major sixth interval featured prominently in both pieces.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0022cq5" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Musical Youth
   </td>
   <td>
    <a href="https://open.spotify.com/track/1BkY0N8ChFk2mdLbAUu8ZK" target="_blank">
     Pass The Dutchie
    </a>
   </td>
   <td width="128">
    Young musicians deliberately assembled for commercial purposes.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Domenico Scarlatti
    <br/>
    Yuja Wang
   </td>
   <td>
    <a href="https://open.spotify.com/track/5VhfVAfRS0ofWSXpHvchm8" target="_blank">
     Keyboard Sonata in G Major, KK. 455
    </a>
   </td>
   <td width="128">
    Repeated notes technique; youthful/playful sound.
   </td>
   <td width="128">
    Dinara Klinton
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Liza Minnelli
   </td>
   <td>
    <a href="https://open.spotify.com/track/2Oam4p5G5GfyzLLBuMTJty" target="_blank">
     Maybe This Time
    </a>
   </td>
   <td width="128">
    Famous parent-child pairing in same profession.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Andrew Lloyd Webber
    <br/>
    Phantom Of The Opera Original London Cast
    <br/>
    Michael Crawford
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Sarah Brightman
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/5qlABWwod6dgDCmRAAF5J5" target="_blank">
     The Phantom Of The Opera
    </a>
   </td>
   <td width="128">
    Theatricality and chromatic musical lifts.
   </td>
   <td width="128">
    Nicky Spence
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Daft Punk
   </td>
   <td>
    <a href="https://open.spotify.com/track/5W3cjX2J3tjhG8zb6u0qHn" target="_blank">
     Harder, Better, Faster, Stronger
    </a>
   </td>
   <td width="128">
    Robotic synthesized production with pulsing rhythm.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0022l1k" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ludwig van Beethoven
    <br/>
    Wendy Carlos
    <br/>
    Rachel Elkind
   </td>
   <td>
    March – from A Clockwork Orange
   </td>
   <td width="128">
    Use of the vocoder.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Billy Joel
   </td>
   <td>
    <a href="https://open.spotify.com/track/6ZTRRn6pGCt2qxkiUKgqqk" target="_blank">
     This Night
    </a>
   </td>
   <td width="128">
    Features Beethoven (Piano Sonata No. 8 in C minor, Op. 13, "Sonata Pathétique").
   </td>
   <td width="128">
    Joe Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    The Turbans
   </td>
   <td>
    <a href="https://open.spotify.com/track/4rXndJbjTYZ4ISX3pBGxfL" target="_blank">
     When You Dance
    </a>
   </td>
   <td width="128">
    Doo-wop style/genre.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Yma Sumac
    <br/>
    Billy May
    <br/>
    Gozzo
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     The Rico Mambo Orchestra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6TsE30wjcOmuQRheHdtaAF" target="_blank">
     Gopher Mambo - Remastered 2009
    </a>
   </td>
   <td width="128">
    Mambo rhythm.
   </td>
   <td width="128">
    Gabriella Swallow
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Grace Jones
   </td>
   <td>
    <a href="https://open.spotify.com/track/3di2SUB3jU1v5HPQCkc84L" target="_blank">
     Slave To The Rhythm - Hot Blooded Version
    </a>
   </td>
   <td width="128">
    Both artists as fashion icons and style muses, connected through Greg Gorman's sunglasses photography campaigns.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0022skv" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Elton John
   </td>
   <td>
    <a href="https://open.spotify.com/track/5Wj1rJnCLpMHdLaxsFtJLs" target="_blank">
     Bennie And The Jets - Remastered 2014
    </a>
   </td>
   <td width="128">
    Artificial applause added in post-production, similar to Grace Jones' "Slave To The Rhythm".
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Sean Mason
   </td>
   <td>
    <a href="https://open.spotify.com/track/4kXhNbZIkWx6OXovo60dGC" target="_blank">
     SilkyM
    </a>
   </td>
   <td width="128">
    Piano-driven stomping groove reminiscent of Elton John's style.
   </td>
   <td width="128">
    Julian Joseph
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Betty Davis
   </td>
   <td>
    <a href="https://open.spotify.com/track/7yQpHgbDPweCZhTD5ZtXES" target="_blank">
     They Say I'm Different
    </a>
   </td>
   <td width="128">
    North Carolina heritage connection to Sean Mason's Southern roots.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Sam Amidon
   </td>
   <td>
    <a href="https://open.spotify.com/track/6qOo5ulOMo1afciMYkw8cu" target="_blank">
     Walkin' Boss
    </a>
   </td>
   <td width="128">
    Static musical backdrop allowing focus on storytelling, similar to Betty Davis' approach.
   </td>
   <td width="128">
    Emma Rawicz
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Esukolaal
   </td>
   <td>
    <a href="https://open.spotify.com/track/4IgvGdAvqGkUO4srSjfKQ1" target="_blank">
     Bapaalaay
    </a>
   </td>
   <td width="128">
    Banjo's ancestral connection to West African akonting instrument.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002309s" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Johann Sebastian Bach
    <br/>
    Isabelle Faust
    <br/>
    Bernhard Forck
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Akademie für Alte Musik Berlin
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/6r9g1KN9Qwj32mxiDSMkS8" target="_blank">
     Concerto for Two Violins in D Minor, BWV 1043: I. Vivace
    </a>
   </td>
   <td width="128">
    Both the West African akonting and Baroque violins used gut strings.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Gryphon
   </td>
   <td>
    <a href="https://www.youtube.com/watch?v=0_Dwn3E7Nts" target="_blank">
     A Futuristic Auntyquarian
    </a>
   </td>
   <td width="128">
    Baroque musical elements and musicians showing off their skill.
   </td>
   <td width="128">
    Rick Wakeman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    White Town
   </td>
   <td>
    <a href="https://open.spotify.com/track/3UBItNVbFQiVC5hBQlBvnr" target="_blank">
     Your Woman
    </a>
   </td>
   <td width="128">
    Progressive rock recipe: combining old music with new sounds, cutting it up and adding heavy drums.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Ella Fitzgerald
    <br/>
    Louis Armstrong
   </td>
   <td>
    <a href="https://open.spotify.com/track/2gNjmvuQiEd2z9SqyYi8HH" target="_blank">
     Summertime
    </a>
   </td>
   <td width="128">
    Trumpet sample at the beginning and similar bass line intervals.
   </td>
   <td width="128">
    Fenella Humphreys
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Zdob si Zdub
    <br/>
    Fratii Advahov
   </td>
   <td>
    <a href="https://open.spotify.com/track/0IcFeQZD19y54GGhUeCQD7" target="_blank">
     Trenulețul (cu Frații Advahov) - Eurovision 2022
    </a>
   </td>
   <td width="128">
    Norman Granz (producer of previous track) was born to Jewish immigrants from Tiraspol, Moldova - linking to Moldova musical heritage.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00237nb" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Lys Assia
   </td>
   <td>
    <a href="https://open.spotify.com/track/0OtKMBmhEuQ4hGPbMmtErz" target="_blank">
     Refrain
    </a>
   </td>
   <td width="128">
    Both Eurovision entries.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Stanley Holloway
   </td>
   <td>
    <a href="https://open.spotify.com/track/6viFYlENfkpKph58zT4yyK" target="_blank">
     The Honeysuckle and the Bee
    </a>
   </td>
   <td width="128">
    Nostalgia and themes of pure love in gardens with scented flowers.
   </td>
   <td width="128">
    Errollyn Wallen
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Oasis
   </td>
   <td>
    <a href="https://open.spotify.com/track/6EMynpZ10GVcwVqiLZj6Ye" target="_blank">
     Champagne Supernova
    </a>
   </td>
   <td width="128">
    Stanley Holloway's cinematic association with Ealing Studios (where Oasis' music video was filmed).
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    The Kinks
   </td>
   <td>
    <a href="https://open.spotify.com/track/09Plbz3Ja2gxU9xCsqA5KY" target="_blank">
     Sunny Afternoon
    </a>
   </td>
   <td width="128">
    Warring brothers in bands; melodica instrument appearance.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Marvin Gaye
    <br/>
    Tammi Terrell
   </td>
   <td>
    <a href="https://open.spotify.com/track/7tqhbajSfrz2F7E1Z75ASX" target="_blank">
     Ain't No Mountain High Enough
    </a>
   </td>
   <td width="128">
    Descending bass line in the opening.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 11

<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00254hv" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Carole King
   </td>
   <td>
    <a href="https://open.spotify.com/track/1BWsOxeMx83OrKGCV4gxly" target="_blank">
     I Feel the Earth Move
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Joe Henderson
    <br/>
    Alice Coltrane
   </td>
   <td>
    <a href="https://open.spotify.com/track/5tR80sypNbMyWIbDfiBBXh" target="_blank">
     Earth
    </a>
   </td>
   <td width="128">
    Main melody of chorus slowed down resembles the melodic phrase.
   </td>
   <td width="128">
    Jess Gillam
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Tom Lehrer
   </td>
   <td>
    <a href="https://open.spotify.com/track/1cIjktJ9flEMBrjlbPJCBY" target="_blank">
     The Elements
    </a>
   </td>
   <td width="128">
    From concept album about four elements (earth, water, wind, fire) to scientific elements.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Billy Watson And His International Silver String Submarine Band
   </td>
   <td>
    <a href="https://open.spotify.com/track/58lrXsvj6NlZI0mrkZVEgf" target="_blank">
     Shave and a Haircut
    </a>
   </td>
   <td width="128">
    Both tracks feature the seven-note musical resolution phrase.
   </td>
   <td width="128">
    Richard Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Bob Dylan
   </td>
   <td>
    <a href="https://open.spotify.com/track/3RkQ3UwOyPqpIiIvGVewuU" target="_blank">
     Mr. Tambourine Man
    </a>
   </td>
   <td width="128">
    Musicians who are both visual artists and harmonica players (Billy Watson and Bob Dylan).
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0025c0p" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Wolfgang Amadeus Mozart
    <br/>
    Academy of St. Martin in the Fields
    <br/>
    Sir Neville Marriner
   </td>
   <td>
    <a href="https://open.spotify.com/track/7dUd5t5yyQR7MaSOg7eRbH" target="_blank">
     Ballet Intermezzo, K. 299c (Compl. &amp; Orch. Smith): VIII. Tambourin
    </a>
   </td>
   <td width="128">
    Early tambourine use in classical music.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Mary Bergin
    <br/>
    Alec Finn
    <br/>
    Johnny McDonagh
   </td>
   <td>
    <a href="https://open.spotify.com/track/3cEzrdu5YIBNfbREze22zr" target="_blank">
     Ríl Gan Ainm / Ah Surely / The Union Reel
    </a>
   </td>
   <td width="128">
    Lively melody and folk ties to Mozart.
   </td>
   <td width="128">
    Sam Amidon
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Jimi Hendrix
   </td>
   <td>
    <a href="https://open.spotify.com/track/2AxCeJ6PSsBYiTckM0HLY7" target="_blank">
     Voodoo Child (Slight Return)
    </a>
   </td>
   <td width="128">
    Left-handed virtuosos (Bergin and Hendrix).
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    George Frideric Handel
    <br/>
    Elin Manahan Thomas
    <br/>
    Orchestra of the Age of Enlightenment
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Harry Christophers
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/0drHxdDHQr20RWySE9TM7I" target="_blank">
     Eternal Source Of Light Divine (Ode For The Birthday Of Queen Anne), HWV 74
    </a>
   </td>
   <td width="128">
    Shared London address (25 Brook Street, Mayfair).
   </td>
   <td width="128">
    Heidi Fardell
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Hugh Masekela
   </td>
   <td>
    <a href="https://open.spotify.com/track/7jXFz9TJBLQ8FcVWMtg2G5" target="_blank">
     Bring Him Back Home (Nelson Mandela)
    </a>
   </td>
   <td width="128">
    Songs for world leaders (Queen Anne and Mandela).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0025lcp" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Harry Belafonte
   </td>
   <td>
    <a href="https://open.spotify.com/track/1zW2csx1vVJrKfvDrFQNVt" target="_blank">
     Jump in the Line
    </a>
   </td>
   <td width="128">
    Biographical link: Hugh Masekela's friendship with Belafonte during exile.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Danny Elfman
    <br/>
    The City of Prague Philharmonic Orchestra
    <br/>
    The Williams Family Singers
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     James Fitzpatrick
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/1ipM6x72sFUJvNkmZxedl2" target="_blank">
     Theme - From "The Simpsons"
    </a>
   </td>
   <td width="128">
    Featured in Beetlejuice which uses Belafonte's "Jump in the Line".
   </td>
   <td width="128">
    Rhodri Marsden
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Majaz
   </td>
   <td>
    <a href="https://open.spotify.com/track/5VKc8PPiqkei1pIsBYTCTs" target="_blank">
     Ala Wain
    </a>
   </td>
   <td width="128">
    Arabic scales (Lydian dominant) tied to The Simpsons theme's harmonic structure.
   </td>
   <td width="128">
    Yazz Ahmed
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Kyu Sakamoto
   </td>
   <td>
    <a href="https://open.spotify.com/track/2IP8BZGYNmZbF3yjHkvd3f" target="_blank">
     Ue O Muite Aruko (Sukiyaki)
    </a>
   </td>
   <td width="128">
    Sakamoto's song uses cheerful whistling to mask lyrics about political despair, mirroring Ala Wain's satire about musicians resisting societal stigma in the Persian Gulf/Arabian Peninsula.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    James Conway
    <br/>
    Eric Idle
   </td>
   <td>
    <a href="https://open.spotify.com/track/6AEXuVITLfu2DWs2GShILN" target="_blank">
     Always Look On the Bright Side of Life (From "Life of Brian")
    </a>
   </td>
   <td width="128">
    Whistling as resilience (extending Sukiyaki's theme).
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0025w2d" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Adriano Celentano
   </td>
   <td>
    <a href="https://open.spotify.com/track/0HQf0bd3oSZei450iKuUFR" target="_blank">
     Prisencolinensinainciusol
    </a>
   </td>
   <td width="128">
    Use of playful nonsense language/vocals (Celentano's fake English vs. cockney affectation).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    György Ligeti
    <br/>
    Reinbert de Leeuw
    <br/>
    Asko Ensemble
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Cappella Amsterdam
     <br/>
     Schönberg Ensemble
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/0pGRB4wAGt4edxCeFkDCVX" target="_blank">
     Ligeti: Clocks and Clouds
    </a>
   </td>
   <td width="128">
    Experimental vocal treatments (Ligeti's choir vs. Celentano's gibberish).
   </td>
   <td width="128">
    Lucy Shaw
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Richard Strauss
    <br/>
    Berliner Philharmoniker
    <br/>
    Herbert von Karajan
   </td>
   <td>
    <a href="https://open.spotify.com/track/43YwOmGUOS3zzGvj1Feszb" target="_blank">
     Also sprach Zarathustra, Op. 30: I. Prelude. Sonnenaufgang
    </a>
   </td>
   <td width="128">
    Kubrick's use of both Ligeti and Strauss in "2001: A Space Odyssey".
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    John Coltrane
   </td>
   <td>
    <a href="https://open.spotify.com/track/0CLbmkYmQIWiEwnsbOkLpd" target="_blank">
     A Love Supreme, Pt. I – Acknowledgement
    </a>
   </td>
   <td width="128">
    Spiritual grandeur (Strauss's cosmic dawn vs. Coltrane's divine offering).
   </td>
   <td width="128">
    Ben Nobuto
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Candi Staton
   </td>
   <td>
    <a href="https://open.spotify.com/track/1kIgA49bo8f2qyyKoJ9u2d" target="_blank">
     You Got The Love
    </a>
   </td>
   <td width="128">
    Direct spiritual appeals (Coltrane's jazz prayer vs. Staton's gospel house anthem).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5" title="This episode was a one-off special.">
    <a href="https://www.bbc.co.uk/programmes/m002622x" target="_blank">
     5*
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Henry Gauntlet
    <br/>
    Choir of King's College, Cambridge
    <br/>
    Stephen Cleobury
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Guy Johnston
     <br/>
     David Goode
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/2O8en4nuwOSMT87zldfRL4" target="_blank">
     Once in Royal David's City
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Moishe Oysher
   </td>
   <td>
    <a href="https://www.youtube.com/watch?v=s_Cc3btDedI" target="_blank">
     Drei Dreidel
    </a>
   </td>
   <td width="128">
    Both written for children; Hanukkah coincided with Christmas for the year of this episode's broadcast (2024).
   </td>
   <td width="128">
    Francesca Ter-Berg
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Pyotr Ilyich Tchaikovsky
    <br/>
    Lior Rosner
    <br/>
    Scott Dunn
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Royal Philharmonic Orchestra
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4QTFU7BukoyDtyyemGPNCX" target="_blank">
     Dance of the Sugar Plum Fairy
    </a>
   </td>
   <td width="128">
    Eastern European traditions; E minor key; toys theme.
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Mariah Carey
   </td>
   <td>
    <a href="https://open.spotify.com/track/0bYg9bo50gSsH3LtXe2SQn" target="_blank">
     All I Want for Christmas Is You
    </a>
   </td>
   <td width="128">
    Features a celeste.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Nat King Cole
   </td>
   <td>
    <a href="https://open.spotify.com/track/4PS1e8f2LvuTFgUs1Cn3ON" target="_blank">
     The Christmas Song (Merry Christmas To You)
    </a>
   </td>
   <td width="128">
    Both written in summer heat waves; Christmas list imagery.
   </td>
   <td width="128">
    Roderick Williams
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00268xn" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Prince
   </td>
   <td>
    <a href="https://www.youtube.com/watch?v=Rp4DUGK-XbI" target="_blank">
     Cindy C.
    </a>
   </td>
   <td width="128">
    Both "You Got The Love" and "Cindy C" had popular bootleg versions.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    David Wise
   </td>
   <td>
    <a href="https://www.youtube.com/watch?v=Xqf8jID9TsE" target="_blank">
     Donkey Kong Country Theme
    </a>
   </td>
   <td width="128">
    Prince's multimedia interests - he released a PC video game in 1994, the same year as "Donkey Kong Country".
   </td>
   <td width="128">
    Tess Tyler
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Ottorino Respighi
    <br/>
    Tamás Vásáry
    <br/>
    Bournemouth Sinfonietta
   </td>
   <td>
    <a href="https://open.spotify.com/track/4UEp7XPCmmgvO4OjQomxuO" target="_blank">
     Trittico Botticelliano for Small Orchestra, P. 151: I. La primavera
    </a>
   </td>
   <td width="128">
    Music inspired by images (Respighi composed after seeing Botticelli paintings).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Mory Kanté
   </td>
   <td>
    <a href="https://open.spotify.com/track/7yuF2FK7adgzGiIfEpR7Km" target="_blank">
     Yeke Yeke
    </a>
   </td>
   <td width="128">
    Both Respighi and Kanté achieved worldwide fame with pieces written at age 37.
   </td>
   <td width="128">
    Seckou Keita
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Gipsy Kings
   </td>
   <td>
    <a href="https://open.spotify.com/track/3VnwIIjxOrdkbYmp402CIo" target="_blank">
     No Volvere
    </a>
   </td>
   <td width="128">
    Producer Nick Patrick produced both "Yeke Yeke" and the Gipsy Kings album "Este Mundo".
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0026961" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Isata Kanneh-Mason
    <br/>
    Jeneba Kanneh-Mason
    <br/>
    Braimah Kanneh-Mason
    <details>
     <summary>
      <em>
       +4 more
      </em>
     </summary>
     Konya Kanneh-Mason
     <br/>
     Aminata Kanneh-Mason
     <br/>
     Sheku Kanneh-Mason
     <br/>
     Mariatu Kanneh-Mason
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/5TiqHF71qQK7RsP6EHkQRW" target="_blank">
     Redemption Song (Arr. Kanneh-Mason)
    </a>
   </td>
   <td width="128">
    Family musical dynasty with multiple members; genre fusion; strings and instruments in conversation.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ishmael Ensemble
   </td>
   <td>
    <a href="https://open.spotify.com/track/3pS5mSMg7ueQUTIZgrantM" target="_blank">
     Cold Light
    </a>
   </td>
   <td width="128">
    Themes of redemption and artist struggle with pain.
   </td>
   <td width="128">
    Georgie Ward
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Peter Gabriel
   </td>
   <td>
    <a href="https://open.spotify.com/track/2j4HxCMrAf3QFnoKDoYxKf" target="_blank">
     The Feeling Begins
    </a>
   </td>
   <td width="128">
    Recorded at the same studio as Cold Light (Real World Studios), founded by Peter Gabriel.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    The Zawose Queens
   </td>
   <td>
    <a href="https://open.spotify.com/track/6Ps5HlYHqNLgWsQI4uui4k" target="_blank">
     Mapendo
    </a>
   </td>
   <td width="128">
    Hugo Zawose worked with Peter Gabriel; intergenerational musical family (daughter and grandchild).
   </td>
   <td width="128">
    Abel Selaocoe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Frank Sinatra
    <br/>
    Nancy Sinatra
   </td>
   <td>
    <a href="https://open.spotify.com/track/4feXcsElKIVsGwkbnTHAfV" target="_blank">
     Somethin' Stupid
    </a>
   </td>
   <td width="128">
    Two-part harmony; intergenerational family duet (father and daughter).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 12

### Notes

#### Ep. 5, Track 5
Jeffrey picked the original Copland "Hoe-Down" in the first ever episode.
<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0028388" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Ezra Collective
    <br/>
    Yazmin Lacey
   </td>
   <td>
    <a href="https://open.spotify.com/track/2mxQ3VWWk47YCo9RB2fkOk" target="_blank">
     God Gave Me Feet For Dancing (feat. Yazmin Lacey)
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Frédéric Chopin
    <br/>
    Mikhail Pletnev
   </td>
   <td>
    <a href="https://open.spotify.com/track/2MSgFefjK0T7Iwjvr3OKqV" target="_blank">
     Chopin: Nocturne No. 20 in C-Sharp Minor, Op. Posth.
    </a>
   </td>
   <td width="128">
    Opening piano riff similarity.
   </td>
   <td width="128">
    Aoife Ní Bhriain
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Barry Manilow
   </td>
   <td>
    <a href="https://open.spotify.com/track/0dRlo4YkIMIHou8oLxAcB9" target="_blank">
     Could It Be Magic
    </a>
   </td>
   <td width="128">
    Uses Chopin's Prelude Op. 28, No. 20 as its foundation.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    John McLaughlin
    <br/>
    Shankar Mahadevan
    <br/>
    Zakir Hussain
   </td>
   <td>
    <a href="https://open.spotify.com/track/2i6jWNxRAKWr9RWki0Mlk9" target="_blank">
     Kabir
    </a>
   </td>
   <td width="128">
    Both artists took existing material and transformed it into something new.
   </td>
   <td width="128">
    Julian Joseph
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Philip Glass
    <br/>
    Marielle Labèque
    <br/>
    Katia Labèque
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Gustavo Dudamel
     <br/>
     Los Angeles Philharmonic
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/3anlmKYcs3dXGqDXNJ2pEl" target="_blank">
     Double Concerto for Two Pianos &amp; Orchestra: Movement I
    </a>
   </td>
   <td width="128">
    John McLaughlin's personal relationship with Katia Labèque (one of the Labèque sisters who perform this piece).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00289xp" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Kid Ory
   </td>
   <td>
    <a href="https://open.spotify.com/track/6ZRsVuvtvim8tY5H3gWBxG" target="_blank">
     The Bucket's Got a Hole in It
    </a>
   </td>
   <td width="128">
    Architecture - the previous track was premiered at Walt Disney Concert Hall in Los Angeles, designed by Frank Gehry, who is a jazz fan and spent time with Kid Ory in Hollywood jazz bars.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ronald Goodwin
    <br/>
    Central Band Of The Royal Air Force
   </td>
   <td>
    <a href="https://open.spotify.com/track/4Xu5iNkNKM79Osz4CCRVdD" target="_blank">
     Those Magnificent Men in Their Flying Machines
    </a>
   </td>
   <td width="128">
    Trombone slide technique - connecting Kid Ory's trombone glissandos to the musical representation of planes going up and down in the film score.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Joni Mitchell
   </td>
   <td>
    <a href="https://open.spotify.com/track/1wcbiRER4ChnikvcLc2OE6" target="_blank">
     Conversation
    </a>
   </td>
   <td width="128">
    Word painting and wide intervals - both tracks use musical techniques where the melody reflects the lyrical content (going up/down musically matching the words).
   </td>
   <td width="128">
    Emma Rawicz
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Les Paul
    <br/>
    Mary Ford
   </td>
   <td>
    <a href="https://open.spotify.com/track/6bLNg7IUmw1IFpCZ3pcvz4" target="_blank">
     How High The Moon
    </a>
   </td>
   <td width="128">
    Multi-tracking recording techniques - both tracks use innovative layering of vocals and instruments.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Guns N' Roses
   </td>
   <td>
    <a href="https://open.spotify.com/track/7snQQk1zcKl8gZ92AnueZW" target="_blank">
     Sweet Child O' Mine
    </a>
   </td>
   <td width="128">
    Gibson Les Paul guitar - connecting Les Paul the inventor/musician to the famous guitar that bears his name, which Slash used on this track.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0028l3c" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Otis Redding
   </td>
   <td>
    <a href="https://open.spotify.com/track/3zBhihYUHBmGd2bcQIobrF" target="_blank">
     (Sittin' On) the Dock of the Bay
    </a>
   </td>
   <td width="128">
    Departure from band or artist's image; both songs feature "placeholder" lyrics or ad libs that were kept in the final version.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Lena Chamamyan
   </td>
   <td>
    <a href="https://open.spotify.com/track/2IIkBb2r2s8wDPekeFn69i" target="_blank">
     Ala Mowj El-Bahr
    </a>
   </td>
   <td width="128">
    Themes of the sea and leisurely pacing.
   </td>
   <td width="128">
    Maya Youssef
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Felix Mendelssohn
    <br/>
    MDR Leipzig Radio Chorus
    <br/>
    GewandhausKinderchor
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Gewandhausorchester
     <br/>
     Kurt Masur
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/4uCmG6wiNfLGcOBZLZUOUp" target="_blank">
     Paulus, Op. 36, MWV A14 / Part 1: No. 15 Chor: "Mache dich auf! Werde Licht!"
    </a>
   </td>
   <td width="128">
    Damascus link: Shamamyan’s birthplace; Mendelssohn’s oratorio depicts St. Paul’s "Damascene conversion".
   </td>
   <td width="128">
    Ben Gernon
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Taylor Swift
   </td>
   <td>
    <a href="https://open.spotify.com/track/45wMBGri1PORPjM9PwFfrS" target="_blank">
     Blank Space (Taylor's Version)
    </a>
   </td>
   <td width="128">
    Mendelssohn had (and Taylor Swift has) scoliosis.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Frankie Lymon &amp; The Teenagers
   </td>
   <td>
    <a href="https://open.spotify.com/track/6vL5Kx5LmZzcL12DZl2OiY" target="_blank">
     Why Do Fools Fall in Love
    </a>
   </td>
   <td width="128">
    Similar chord progression (I-vi-IV-V vs. I-vi-ii-V).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0028v4s" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Amy Winehouse
   </td>
   <td>
    <a href="https://open.spotify.com/track/570ZDO2Lmh6NQChOU5xPUL" target="_blank">
     Love Is A Losing Game
    </a>
   </td>
   <td width="128">
    Shares the lyric "love is a losing game" with Frankie Lyman's song.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Claude Debussy
    <br/>
    Pascal Rogé
   </td>
   <td>
    <a href="https://open.spotify.com/track/2JoW78NNzmlMnImAvFzF51" target="_blank">
     Pour le piano, CD 95: II. Sarabande
    </a>
   </td>
   <td width="128">
    The use of rich seventh chords, similar to those in Amy Winehouse's song.
   </td>
   <td width="128">
    Anne Dudley
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Pinduca
   </td>
   <td>
    <a href="https://open.spotify.com/track/5GuJ1ds116WaHNGyKRBALj" target="_blank">
     Lambada
    </a>
   </td>
   <td width="128">
    The sarabande's origins as a banned dance led to another controversial dance, the lambada.
   </td>
   <td width="128">
    Geoffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    John Kirkpatrick
   </td>
   <td>
    <a href="https://open.spotify.com/track/3k9KBU2amftEagqKKI9ulk" target="_blank">
     The Bristol Sailorman / Will the Waggoner
    </a>
   </td>
   <td width="128">
    The two-chord structure of the lambada mirrors the limited chord options on the one-row melodeon.
   </td>
   <td width="128">
    Cohen Braithwaite-Kilcoyne
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Mitsune
   </td>
   <td>
    <a href="https://open.spotify.com/track/4GEQ1TLQF82JpOW2Nk5Rfd" target="_blank">
     Kaigara Bushi
    </a>
   </td>
   <td width="128">
    A rhythmic work song for fishermen, modernised with folk fusion instrumentation.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00290fc" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Winifred Atwell
   </td>
   <td>
    <a href="https://open.spotify.com/track/5h0D0mxHfsHevakcpXvNbH" target="_blank">
     Tickle the Ivories
    </a>
   </td>
   <td width="128">
    Instruments made from ivory (shamisen tuning pegs to piano keys).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Pyotr Ilyich Tchaikovsky
    <br/>
    Sir Simon Rattle
    <br/>
    Berliner Philharmoniker
   </td>
   <td>
    <a href="https://open.spotify.com/track/2oUX4i8ByoaDrHHz9z5Bga" target="_blank">
     Tchaikovsky: The Nutcracker, Op. 71, Act 2: No. 14a, Pas de deux. Andante maestoso
    </a>
   </td>
   <td width="128">
    Descending major scale (F major in Atwell's piece to G major in Tchaikovsky).
   </td>
   <td width="128">
    Keelan Carew
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Eminem
    <br/>
    Dido
   </td>
   <td>
    <a href="https://open.spotify.com/track/3UmaczJpikHgJFyBTAJVoz" target="_blank">
     Stan
    </a>
   </td>
   <td width="128">
    Letter writing (Tchaikovsky's correspondence with Nadezhda von Meck to Stan's fan letters).
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Clean Bandit
    <br/>
    Jess Glynne
   </td>
   <td>
    <a href="https://open.spotify.com/track/0TVV2gFROJaB3kIZyCUvIY" target="_blank">
     Rather Be (feat. Jess Glynne)
    </a>
   </td>
   <td width="128">
    Key signature (both in G-sharp minor).
   </td>
   <td width="128">
    Carol Jarvis
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Emerson, Lake &amp; Palmer
   </td>
   <td>
    <a href="https://open.spotify.com/track/2uCbohY5WHobKMtrs1ckWk" target="_blank">
     Hoedown
    </a>
   </td>
   <td width="128">
    Classical-electronic crossover genre.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m00297f4" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    The Scottish Fiddle Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/2RrIMGsITtWFf7ASF2ytxN" target="_blank">
     Eightsome Reel
    </a>
   </td>
   <td width="128">
    Folk dancing traditions, evolving from the hoedown's roots in social gatherings and plantation culture.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    William Walton
    <br/>
    The English Opera Group Ensemble
    <br/>
    Dame Edith Sitwell
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     Anthony Collins
     <br/>
     Sir Peter Pears
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/2yyyLKCtrQDXfrud5B1Ild" target="_blank">
     Facade: Scotch Rhapsody
    </a>
   </td>
   <td width="128">
    Shifting from communal folk music to an avant-garde, upper-class spoken-word performance.
   </td>
   <td width="128">
    Richard Stilgoe
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Sheryl Crow
   </td>
   <td>
    <a href="https://open.spotify.com/track/41F8XHQ9kIGwEkDYJCCbN8" target="_blank">
     All I Wanna Do
    </a>
   </td>
   <td width="128">
    Poetry being used as inspiration for a song.
   </td>
   <td width="128">
    Geoffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    The Rolling Stones
   </td>
   <td>
    <a href="https://open.spotify.com/track/0t7ttzoe3dV0mah4lBI2kx" target="_blank">
     Gimme Shelter
    </a>
   </td>
   <td width="128">
    Percussion focus, particularly the guiro used in both tracks.
   </td>
   <td width="128">
    Natalie Duncan
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Gustav Holst
    <br/>
    London Philharmonic Orchestra
    <br/>
    Sir Adrian Boult
   </td>
   <td>
    <a href="https://open.spotify.com/track/172XX3A17xK23czfaWWVdk" target="_blank">
     Holst: The Planets, Op. 32: I. Mars, the Bringer of War
    </a>
   </td>
   <td width="128">
    War themes.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m0029hwy" target="_blank">
     7
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    John Williams
    <br/>
    London Symphony Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/2bw4WgXyXP90hIex7ur58y" target="_blank">
     The Imperial March (Darth Vader's Theme)
    </a>
   </td>
   <td width="128">
    Holst's "Mars, Bringer of War" influence on film music; dramatic military might.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Leonard Bernstein
    <br/>
    David Zinman
    <br/>
    Philharmonia
   </td>
   <td>
    <a href="https://open.spotify.com/track/6OXJDmkgJaj0uwVo7ikNdu" target="_blank">
     Maria from West Side Story Suite - Instrumental
    </a>
   </td>
   <td width="128">
    Leitmotif - musical themes representing characters.
   </td>
   <td width="128">
    Linton Stephens
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Roy Brown
   </td>
   <td>
    <a href="https://open.spotify.com/track/6HW0s9uyFK7al3AJFp5YXE" target="_blank">
     Boricua en la Luna
    </a>
   </td>
   <td width="128">
    Identity and immigration themes; Puerto Rican diaspora experience.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Erykah Badu
   </td>
   <td>
    <a href="https://open.spotify.com/track/1Df4urfsVBB0CGQVBPIFHi" target="_blank">
     Orange Moon
    </a>
   </td>
   <td width="128">
    Songs about the moon; spiritual reflection.
   </td>
   <td width="128">
    Tawiah
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Paul Simon
   </td>
   <td>
    <a href="https://open.spotify.com/track/5vZ1BKMSLgrxxPYGMR904n" target="_blank">
     Mother and Child Reunion
    </a>
   </td>
   <td width="128">
    Mother's love interpretation; parent-child relationships.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>

## Series 13

### Notes

#### Ep. 6, Track 4
Grieg's piano concerto was also selected as track #2 in series 8, episode 6 (1st movement).
<table>
 <thead>
  <tr>
   <th align="left">
    Ep.
   </th>
   <th align="left">
    Track
   </th>
   <th align="left">
    Artist(s)
   </th>
   <th align="left">
    Name
   </th>
   <th align="left" width="192">
    Connection to Previous Track
   </th>
   <th align="left">
    Chosen By
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002cf4j" target="_blank">
     1
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Lady Gaga
   </td>
   <td>
    <a href="https://open.spotify.com/track/5ZLUm9eab8y3tqQ1OhQSHI" target="_blank">
     Abracadabra
    </a>
   </td>
   <td width="128">
    -
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Paul Dukas
    <br/>
    Charles Münch
    <br/>
    Boston Symphony Orchestra
   </td>
   <td>
    <a href="https://open.spotify.com/track/7lmJXpFiXlbuX4wIO4BMym" target="_blank">
     The Sorcerer's Apprentice
    </a>
   </td>
   <td width="128">
    Magical mystery theme; same key as "Abracadabra".
   </td>
   <td width="128">
    Errollyn Wallen
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Andrew Gold
   </td>
   <td>
    <a href="https://open.spotify.com/track/4UMOJCNSeVD0Ja5N6cBYa0" target="_blank">
     Never Let Her Slip Away - Rerecorded
    </a>
   </td>
   <td width="128">
    Similar triplet rhythm pattern.
   </td>
   <td width="128">
    Neil Brand
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Carly Simon
   </td>
   <td>
    <a href="https://open.spotify.com/track/3A9mNhGSekM3EhpUZDWOuF" target="_blank">
     You're So Vain - Live
    </a>
   </td>
   <td width="128">
    Alleged uncredited backing vocals by Freddie Mercury.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Paquita La Del Barrio
   </td>
   <td>
    <a href="https://open.spotify.com/track/5yuD7nMUWQJ0ZmveIx4yAA" target="_blank">
     Rata De Dos Patas
    </a>
   </td>
   <td width="128">
    Songs about insults and revenge.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002cq5w" target="_blank">
     2
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Neil Diamond
    <br/>
    André Rieu
    <br/>
    Johann Strauss Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     Phil Bee
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/1hsEYgG2QWca3QIrm1QzuY" target="_blank">
     Sweet Caroline - Live
    </a>
   </td>
   <td width="128">
    Crowd participation and sing-along tradition.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ben Salisbury
    <br/>
    Geoff Barrow
   </td>
   <td>
    <a href="https://open.spotify.com/track/5Mm6GFCpDXNNGLxyU96AC1" target="_blank">
     The Alien
    </a>
   </td>
   <td width="128">
    Iconic, short melodic motifs that become instantly recognisable.
   </td>
   <td width="128">
    Gavin Higgins
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Deep Purple
    <br/>
    Martin Pullan
   </td>
   <td>
    <a href="https://open.spotify.com/track/7hP2UPqyQWO9juHkJl9Uhv" target="_blank">
     Smoke On The Water - Live In Osaka, Japan / 15th August 1972 / Original 1972 Mix
    </a>
   </td>
   <td width="128">
    Four to five-note memorable phrases/riffs, focusing on the power of simple, iconic musical motifs in rock music.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Igor Stravinsky
    <br/>
    Jayne West
    <br/>
    Jon Garrison
    <details>
     <summary>
      <em>
       +7 more
      </em>
     </summary>
     Arthur Woodley
     <br/>
     John Cheek
     <br/>
     Shirley Love
     <br/>
     Wendy White
     <br/>
     Melvin Lowery
     <br/>
     Jeffrey Johnson
     <br/>
     Gregg Smith Singers
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/2u5BFkwaBYk25dElULBGNe" target="_blank">
     The Rake's Progress: Act III Scene 3: Duet: In a foolish dream… (Tom, Anne)
    </a>
   </td>
   <td width="128">
    Geographic link to Montreux (Stravinsky performed at the classical festival there before it became known for jazz).
   </td>
   <td width="128">
    Claire Booth
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Blondie
   </td>
   <td>
    <a href="https://open.spotify.com/track/6F2vo4sxRNQ58VYe3pdiaL" target="_blank">
     Rapture
    </a>
   </td>
   <td width="128">
    Music inspired by visual art in urban settings (Stravinsky's opera was based on Hogarth's London paintings, while this track captures 1970s/80s New York street art and graffiti culture).
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002czpv" target="_blank">
     3
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Baloji
   </td>
   <td>
    <a href="https://open.spotify.com/track/3PvzUJq9SsP6a8NG9764PR" target="_blank">
     Spoiler
    </a>
   </td>
   <td width="128">
    French language hip-hop connection; Debbie Harry's French line in "Rapture" referencing DJ François Kevorkian.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    César Franck
    <br/>
    Luciano Pavarotti
    <br/>
    Wandsworth School Boys Choir
    <details>
     <summary>
      <em>
       +2 more
      </em>
     </summary>
     National Philharmonic Orchestra
     <br/>
     Kurt Herbert Adler
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/20i3SstUIIk1mMfG4EYGR1" target="_blank">
     Franck: Panis angelicus, CFF 209 (Re-Orch. Gamley)
    </a>
   </td>
   <td width="128">
    Belgian connection; both Baloji and César Franck are from Belgium (Baloji moved there as a child, Franck born in Liège).
   </td>
   <td width="128">
    Nicky Spence
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Elton John
   </td>
   <td>
    <a href="https://open.spotify.com/track/1plcM0XlbKdjND7Ufokuzb" target="_blank">
     Honky Cat
    </a>
   </td>
   <td width="128">
    Hands connection; contrasting César Franck's notably large hands with Elton John's famously small "cocktail sausage" fingers.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Antonio Vivaldi
    <br/>
    Lucie Horsch
    <br/>
    Amsterdam Vivaldi Players
   </td>
   <td>
    <a href="https://open.spotify.com/track/1RmCzMHaVlph2E1Zm9lKKJ" target="_blank">
     Flautino Concerto In C, RV 443 - Arr. in G Major for Recorder: 2. Largo
    </a>
   </td>
   <td width="128">
    Student support connection; Elton John's Global Exchange Program for young artists parallels Vivaldi's teaching role at the Ospedale della Pietà in Venice.
   </td>
   <td width="128">
    Heidi Fardell
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Joni Mitchell
   </td>
   <td>
    <a href="https://open.spotify.com/track/2zTlByELcZXPeLYxFLf66e" target="_blank">
     The Magdalene Laundries
    </a>
   </td>
   <td width="128">
    Institutional care for abandoned girls; both the Ospedale della Pietà and Ireland's Magdalene Laundries housed unwanted or "fallen" women and girls.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002dc9t" target="_blank">
     4
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    David Bowie
   </td>
   <td>
    <a href="https://open.spotify.com/track/5oVIQ3vm2eRC566cEheDOV" target="_blank">
     Modern Love - 2002 Remaster
    </a>
   </td>
   <td width="128">
    Both artists released influential 15th studio albums that redefined their careers.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Ludwig van Beethoven
    <br/>
    Daniel Barenboim
   </td>
   <td>
    <a href="https://open.spotify.com/track/3H0cDToZY0us6FjmcTgOLq" target="_blank">
     Piano Sonata No. 32 In C Minor, Op. 111: 2. Arietta (Adagio molto semplice e cantabile)
    </a>
   </td>
   <td width="128">
    Boogie-woogie piano style; argued that Beethoven's syncopated bass line and blues harmonics in the Arietta prefigure the genre.
   </td>
   <td width="128">
    Amy Harman
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Thelonious Monk
   </td>
   <td>
    <a href="https://open.spotify.com/track/6kMxlzWZS9BRZCQpNDpmlo" target="_blank">
     Epistrophy - Live
    </a>
   </td>
   <td width="128">
    Both composers were revolutionary bridge figures who modernised musical forms through unconventional harmonic approaches and syncopated rhythmic figures.
   </td>
   <td width="128">
    Ashley Henry
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Charli xcx
    <br/>
    The Japanese House
   </td>
   <td>
    <a href="https://open.spotify.com/track/1PJe42QnCMD6JqhcooaWzc" target="_blank">
     Apple featuring the japanese house
    </a>
   </td>
   <td width="128">
    Musical manifestos; Thelonious Monk famously wrote handwritten manifesto advice for band members, while Charli XCX launched her album with a social media manifesto.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Marvin Gaye
   </td>
   <td>
    <a href="https://open.spotify.com/track/37j56IWzpplKE5zrlQRmxc" target="_blank">
     I Heard It Through The Grapevine
    </a>
   </td>
   <td width="128">
    Both songs use fruit-related idioms ("the apple doesn't fall far from the tree" vs "heard it through the grapevine") to convey how information spreads through families and communities.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002dlj1" target="_blank">
     5
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Julius Fučík
    <br/>
    Phil Kelsall
   </td>
   <td>
    <a href="https://open.spotify.com/track/0vkvSuKDcouVnh3c3CN1zV" target="_blank">
     Entrance of the Gladiators
    </a>
   </td>
   <td width="128">
    Wurlitzer organ sounds.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    John Williams
    <br/>
    Harald Feller
   </td>
   <td>
    <a href="https://open.spotify.com/track/1ny2EWNkOBMzrBQedmP1fF" target="_blank">
     Star Wars Suite (arr. H. Feller): V. Throne Room - End Title
    </a>
   </td>
   <td width="128">
    Theatre organs in early film music.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    A.R. Rahman
    <br/>
    The Pussycat Dolls
    <br/>
    Nicole Scherzinger
   </td>
   <td>
    <a href="https://open.spotify.com/track/7Kpqjspw4Y7HrvItIRcBiW" target="_blank">
     Jai Ho! (You Are My Destiny)
    </a>
   </td>
   <td width="128">
    Oscar-winning end credits songs.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Israel Kamakawiwo'ole
   </td>
   <td>
    <a href="https://open.spotify.com/track/3oQomOPRNQ5NVFUmLJHbAV" target="_blank">
     Over the Rainbow
    </a>
   </td>
   <td width="128">
    Both Nicole Scherzinger (Pussycat Dolls lead singer) and Israel Kamakawiwo'ole were born in Honolulu, Hawaii.
   </td>
   <td width="128">
    Andrew Roachford
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Cesária Evora
   </td>
   <td>
    <a href="https://open.spotify.com/track/5XTdgvMiVHNSzzFrKAXU91" target="_blank">
     Petit Pays
    </a>
   </td>
   <td width="128">
    Island nation cultural ambassadors.
   </td>
   <td width="128">
    Anna Lapwood
   </td>
  </tr>
  <tr>
   <td align="center" rowspan="5">
    <a href="https://www.bbc.co.uk/programmes/m002f01w" target="_blank">
     6
    </a>
   </td>
   <td align="center">
    1
   </td>
   <td>
    Sandie Shaw
   </td>
   <td>
    <a href="https://open.spotify.com/track/7f5w4aiYgVZrp9w4bNaBLu" target="_blank">
     Puppet On A String
    </a>
   </td>
   <td width="128">
    Musicians known for performing barefoot.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
  <tr>
   <td align="center">
    2
   </td>
   <td>
    Johann Strauss II
    <br/>
    Christian Thielemann
    <br/>
    Wiener Philharmoniker
   </td>
   <td>
    <a href="https://open.spotify.com/track/5vv6vPSDAVii5qefbXS9TA" target="_blank">
     An der schönen blauen Donau, Walzer, Op. 314
    </a>
   </td>
   <td width="128">
    Eurovision 1967 held in Vienna at Hofburg Palace, where Strauss was court music director.
   </td>
   <td width="128">
    Ben Gernon
   </td>
  </tr>
  <tr>
   <td align="center">
    3
   </td>
   <td>
    Elena Roizen
   </td>
   <td>
    <a href="https://open.spotify.com/track/19WEFGlaw2TbL7X0jaRdUq" target="_blank">
     Hai, Dunărea mea
    </a>
   </td>
   <td width="128">
    The River Danube flowing through Romania.
   </td>
   <td width="128">
    Anna Phoebe
   </td>
  </tr>
  <tr>
   <td align="center">
    4
   </td>
   <td>
    Edvard Grieg
    <br/>
    Radu Lupu
    <br/>
    London Symphony Orchestra
    <details>
     <summary>
      <em>
       +1 more
      </em>
     </summary>
     André Previn
    </details>
   </td>
   <td>
    <a href="https://open.spotify.com/track/16CkjFgh277pXei2sQcUn3" target="_blank">
     Piano Concerto in A Minor, Op. 16: III. Allegro moderato molto e marcato
    </a>
   </td>
   <td width="128">
    Folk music inspiring classical composers.
   </td>
   <td width="128">
    Debbie Wiseman
   </td>
  </tr>
  <tr>
   <td align="center">
    5
   </td>
   <td>
    Motörhead
   </td>
   <td>
    <a href="https://open.spotify.com/track/4XvvR8F6qOcnzgChO1uTIO" target="_blank">
     Overkill
    </a>
   </td>
   <td width="128">
    Songs with dramatic false endings that restart unexpectedly.
   </td>
   <td width="128">
    Jeffrey Boakye
   </td>
  </tr>
 </tbody>
</table>
