# Programmers
# 해시 > 베스트앨범

def solution(genres, plays):
    idx = -1
    answer = []
    genre_plays = dict()
    genre_items = dict()

    for genre, play in zip(genres, plays):
        idx += 1
        if genre not in genre_plays:
            genre_plays[genre] = play
            genre_items[genre] = [[play, idx]]
        else:
            genre_plays[genre] += play
            genre_items[genre].append([play, idx])

    genre_plays = sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)
    print(genre_plays)
    print(genre_items)

    for genre, _ in genre_plays:
        songs = sorted(genre_items[genre], key=lambda x: (-x[0], x[1]))

        if len(songs) < 2:
            answer.append(songs[0][1])
        else:
            answer.append(songs[0][1])
            answer.append(songs[1][1])
    return answer


genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
solution(genres, plays)

"""
기존 코드
# Programmers_베스트앨범_Level3
'''
장르별로 가장 많이 재생된 노래를 두개씩 모음. 노래는 고유번호로 구분하며, 수록하는 기준은 다음과 같다.
1. 속한 노래가 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생횟수가 동일한 경우, 고유 번호가 낮은 노래 먼저 수록

genres[i]: 고유번호가 i인 노래의 장르
plays[i]: 고유번호가 i인 노래가 재생된 횟수
1 <= 배열길이 <= 10_000
장르 종류 < 100
장르에 속한 곡이 하나라면, 하나의 곡만 선택한다
모든 장르는 재생된 횟수가 다르다
'''

from collections import OrderedDict

def solution(genres, plays):
    answer = []
    dic = {}
    genre_plays = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i], i])
            genre_plays[genres[i]] += plays[i]
        else:
            dic[genres[i]] = [[plays[i], i]]
            genre_plays[genres[i]] = plays[i]
    
    # print(dic)
    # print(genre_plays)

    genre_plays = sorted(genre_plays.items(), key = lambda x: x[1], reverse=True)

    for genre in genre_plays:
        song_rank = sorted(dic[genre[0]], key=lambda x: (-x[0], x[1]))
        cnt = 0
        for song in song_rank:
            answer.append(song[1])
            cnt += 1
            if cnt == 2:
                break
    return answer
"""