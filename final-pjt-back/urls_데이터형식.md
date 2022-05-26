# url 앤드슬래쉬 주의!!!!!





# 로그인

- /accounts/login/

  - method: 

    - POST

  - body:

    ```json
    {
        "username": "아이디",
        "password": "비번"
    }
    ```



# 회원가입

- /accounts/signup/

  - method:

    - POST

  - body:

    - ```json
      {	
          "username": "아이디",
          "password1": "비번",
          "password2": "비번"
      }
      ```



# 로그아웃

- /accounts/logout/
  - method:
    - POST
  - header:
    - key: Authorization
    - value: 로그인, 회원가입시 받은  토큰값



# 로그인중인 유저 정보(로그인 필요)

- /user/user-info
  - method:
    - GET
  - header:
    - key: Authorization
    - value: 로그인, 회원가입시 받은  토큰값



- 리턴형식

  - ```json
    {	
    	// 배우기준 추천영화    
        "by_actor_recomend": {
            // 추천영화 3개
            // 없으면 'no_movie'
            "first_actor": {
                "watched": "false",
                "like": "false",
                "title": "킹덤: 아신전",
                "local_id": 845222,
                "poster_url": "/dBz61uAt6xjJt4yqhiZXQt0a1bB.jpg",
                "release_date": 20210723,
                "genre": "드라마 판타지 스릴러",
                "popularity": 139.349
            },
            "second_actor": {
                "watched": "false",
                "like": "false",
                "title": "마약왕",
                "local_id": 497370,
                "poster_url": "/vXqDNIp7CrUpkcBc8eMBtDPch4J.jpg",
                "release_date": 20181219,
                "genre": "범죄 액션 드라마",
                "popularity": 14.991
            },
            "third_actor": "no_movie",
            
            // 레벨높은배우 3명 정보
            // 없으면 'no_actor'
            "first_actor_info": {
                "profile_url": "/bGHnBUrBKk2ItXDZJrBDnBeQJvj.jpg",
                "name": "Kim Roi-ha",
                "popularity": 18.541,
                "id": 6593
            },
            "second_actor_info": {
                "profile_url": "/dyWUKQlNyr7SUAjo58VZXvPODkr.jpg",
                "name": "Song Kang-ho",
                "popularity": 10.581,
                "id": 14650
            },
            "third_actor_info": {
                "profile_url": "/91FB6jpqgH6kcWb0PARCXswCidm.jpg",
                "name": "Lee Dong-yong",
                "popularity": 1.646,
                "id": 14666
            },
            
            // 배우별 레벨정보
            "first_actor_level": 66.66666666666666,
            "second_actor_level": 40.0,
            "third_actor_level": 66.66666666666666
        },
        
        // 감독기준 추천영화
        "by_director_recomend": {
            "first_director": {
                "watched": "false",
                "like": "false",
                "title": "설국열차",
                "local_id": 110415,
                "poster_url": "/pRZMtKQpP3fH84YXs02yytUk4ee.jpg",
                "release_date": 20130801,
                "genre": "액션 SF 드라마",
                "popularity": 50.007
            },
            "second_director": "no_movie",
            "third_director": "no_movie",
            
            // 레벨높은배우 3명 정보
            // 없으면 'no_actor'
            "first_director_info": {
                "profile_url": "/tKLJBqbdH6HFj2QxLA5o8Zk7IVs.jpg",
                "name": "Bong Joon-ho",
                "popularity": 4.095,
                "id": 307
            },
            "second_director_info": "no_director",
            "third_director_info": "no_director",
            
            // 감독별 레벨정보
            "first_director_level": 40.0,
            "second_director_level": "no_director",
            "third_director_level": "no_director"
        },
        
        // 로그인중인 유저 정보
        // 좋아하는 배우, 감독 없으면 -1
        "user_data": {
            "id": 2,
            "username": "test1",
            "favorite_director_id": -1,
            "favorite_actor_id": -1,
            "first_director_id": 307,
            "second_director_id": -1,
            "third_director_id": -1,
            "first_actor_id": 6593,
            "second_actor_id": 14650,
            "third_actor_id": 14666
        },
        
        // 유저가 본 영화 목록
        // 무비카드랑 같은 데이터
        "user_watched": [
            {
                "watched": "true",
                "like": "true",
                "title": "괴물",
                "local_id": 1255,
                "poster_url": "/5lgyNwFqyaMMNW484rLgw7aRRZs.jpg",
                "release_date": 20060727,
                "genre": "공포 드라마 SF",
                "popularity": 32.28
            },
            {
                "watched": "true",
                "like": "false",
                "title": "옥자",
                "local_id": 387426,
                "poster_url": "/miHNA5DcheO7ax2qon9CmC7qa9j.jpg",
                "release_date": 20170629,
                "genre": "모험 드라마 SF",
                "popularity": 19.478
            },
            {
                "watched": "true",
                "like": "true",
                "title": "살인의 추억",
                "local_id": 11423,
                "poster_url": "/sujAihJHmNMfeMNQ004KYIPvrGA.jpg",
                "release_date": 20030502,
                "genre": "범죄 드라마 스릴러",
                "popularity": 17.82
            },
            {
                "watched": "true",
                "like": "false",
                "title": "기생충",
                "local_id": 496243,
                "poster_url": "/jjHccoFjbqlfr4VGLVLT7yek0Xn.jpg",
                "release_date": 20190530,
                "genre": "코미디 스릴러 드라마",
                "popularity": 79.985
            }
        ]
    }
    ```



# 로그인 선택정보 로그인 안되있으면 'not_login'



# 홈페이지

- /movies/
  - method:
    - GET
  - header
    - 로그인, 비로그인 둘다 가능

- 리턴형식

  - ```json
    {	
        // 최신영화 6개
        "recent_movie": [
            {
                "watched": "false",
                "like": "false",
                "title": "몽키킹: 전설의 시작",
                "local_id": 634210,
                "poster_url": "/4EaMMsKs0g6gucK9dJwo1B5BOGn.jpg",
                "release_date": 20221102,
                "genre": "",
                "popularity": 31.636
            },
            {
                "watched": "false",
                "like": "false",
                "title": "탑 건: 매버릭",
                "local_id": 361743,
                "poster_url": "/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg",
                "release_date": 20220622,
                "genre": "액션 드라마",
                "popularity": 426.787
            },
            {
                "watched": "false",
                "like": "false",
                "title": "쥬라기 월드: 도미니언",
                "local_id": 507086,
                "poster_url": "/odxdUZWZ7fBfy3ZRj063wuJnZvo.jpg",
                "release_date": 20220601,
                "genre": "모험 액션 SF 스릴러",
                "popularity": 355.259
            },
            {
                "watched": "false",
                "like": "false",
                "title": "더 노비스",
                "local_id": 821427,
                "poster_url": "/xjd6s1jgB1rwKQsiHv995aQbamY.jpg",
                "release_date": 20220525,
                "genre": "드라마 스릴러",
                "popularity": 207.405
            },
            {
                "watched": "false",
                "like": "false",
                "title": "파이어스타터",
                "local_id": 532710,
                "poster_url": "/ko1iKcUp4iIjTNAYFOWFVG8tUi7.jpg",
                "release_date": 20220519,
                "genre": "스릴러 판타지 공포",
                "popularity": 195.276
            },
            {
                "watched": "false",
                "like": "false",
                "title": "범죄도시 2",
                "local_id": 619803,
                "poster_url": "/9oonDgLkh42GsLkbVmW7nU1ib6u.jpg",
                "release_date": 20220518,
                "genre": "범죄 액션",
                "popularity": 126.058
            }
        ],
        // user로그인시 나오는 추천영화
        // user-info에서랑 같은형식
        "by_actor_recomend": {
            "first_actor": {
                "watched": "false",
                "like": "false",
                "title": "킹덤: 아신전",
                "local_id": 845222,
                "poster_url": "/dBz61uAt6xjJt4yqhiZXQt0a1bB.jpg",
                "release_date": 20210723,
                "genre": "드라마 판타지 스릴러",
                "popularity": 139.349
            },
            "second_actor": {
                "watched": "false",
                "like": "false",
                "title": "마약왕",
                "local_id": 497370,
                "poster_url": "/vXqDNIp7CrUpkcBc8eMBtDPch4J.jpg",
                "release_date": 20181219,
                "genre": "범죄 액션 드라마",
                "popularity": 14.991
            },
            "third_actor": "no_movie",
            "first_actor_info": {
                "profile_url": "/bGHnBUrBKk2ItXDZJrBDnBeQJvj.jpg",
                "name": "Kim Roi-ha",
                "popularity": 18.541,
                "id": 6593
            },
            "second_actor_info": {
                "profile_url": "/dyWUKQlNyr7SUAjo58VZXvPODkr.jpg",
                "name": "Song Kang-ho",
                "popularity": 10.581,
                "id": 14650
            },
            "third_actor_info": {
                "profile_url": "/91FB6jpqgH6kcWb0PARCXswCidm.jpg",
                "name": "Lee Dong-yong",
                "popularity": 1.646,
                "id": 14666
            },
            "first_actor_level": 66.66666666666666,
            "second_actor_level": 40.0,
            "third_actor_level": 66.66666666666666
        },
        "by_director_recomend": {
            "first_director": {
                "watched": "false",
                "like": "false",
                "title": "설국열차",
                "local_id": 110415,
                "poster_url": "/pRZMtKQpP3fH84YXs02yytUk4ee.jpg",
                "release_date": 20130801,
                "genre": "액션 SF 드라마",
                "popularity": 50.007
            },
            "second_director": "no_movie",
            "third_director": "no_movie",
            "first_director_info": {
                "profile_url": "/tKLJBqbdH6HFj2QxLA5o8Zk7IVs.jpg",
                "name": "Bong Joon-ho",
                "popularity": 4.095,
                "id": 307
            },
            "second_director_info": "no_director",
            "third_director_info": "no_director",
            "first_director_level": 40.0,
            "second_director_level": "no_director",
            "third_director_level": "no_director"
        },
        
        // 24시간내에 추천수 가장 많은 영화
        // 영화카드 형식
        "hot_movie": [
            {
                "watched": "true",
                "like": "false",
                "title": "기생충",
                "local_id": 496243,
                "poster_url": "/jjHccoFjbqlfr4VGLVLT7yek0Xn.jpg",
                "release_date": 20190530,
                "genre": "코미디 스릴러 드라마",
                "popularity": 79.985
            }
        ]
    }
    ```



# 해당영화 좋아요(로그인 필요)

- /movie/like/<영화id>/
  - method:
    - POST
  - header
    - key: Authorization
    - value: 로그인, 회원가입시 받은  토큰값

- 리턴형식

  - user-info랑 동일

  

# 해당영화 봤어요(로그인 필요)

- /movies/watched/<영화id>/
  - method:
    - POST
  - header
    - key: Authorization
    - value: 로그인, 회원가입시 받은  토큰값

- 리턴형식

  - user-info랑 동일

  

# 감독 프로필

- /movies/director/<감독id>/
  - method:
    - GET
  - header
    - 로그인, 비로그인 둘다 가능

- 리턴형식

  - ```json
    {	
        // 로그인시 나오는 레벨정보
        "director_level": 0.0,
        // 감독정보
        "director_info": {
            "profile_url": "/7HZIthu9DIGbIhjmCmWGiAOJmk6.jpg",
            "name": "Peter Lyons Collister",
            "popularity": 3.586,
            "id": 1
        },
        // 이사람이 감독한 영화목록
        // 영화카드 형식
        "directed_movies": [
            {
                "watched": "false",
                "like": "false",
                "title": "로스트 시티",
                "local_id": 752623,
                "poster_url": "/8kZapNBZYGJu7AUbJVBDMmQgO1D.jpg",
                "release_date": 20220420,
                "genre": "액션 모험 코미디 로맨스",
                "popularity": 10211.875
            }
        ],
        // 로그인시에만 나오는 추천영화 정보
        "recomend_movie": {
            "watched": "false",
            "like": "false",
            "title": "로스트 시티",
            "local_id": 752623,
            "poster_url": "/8kZapNBZYGJu7AUbJVBDMmQgO1D.jpg",
            "release_date": 20220420,
            "genre": "액션 모험 코미디 로맨스",
            "popularity": 10211.875
        }
    }
    ```



# 배우 프로필

- /movies/actor/<배우id>/
  - method:
    - GET
  - header
    - 로그인, 비로그인 둘다 가능

- 리턴형식

  - ```json
    {	
        // 감독이랑 유사
        "actor_level": 0.0,
        "actor_info": {
            "profile_url": "/u2tnZ0L2dwrzFKevVANYT5Pb1nE.jpg",
            "name": "Sandra Bullock",
            "popularity": 34.677,
            "id": 1
        },
        "casted_movies": [
            {
                "watched": "false",
                "like": "false",
                "title": "로스트 시티",
                "local_id": 752623,
                "poster_url": "/8kZapNBZYGJu7AUbJVBDMmQgO1D.jpg",
                "release_date": 20220420,
                "genre": "액션 모험 코미디 로맨스",
                "popularity": 10211.875
            },
            {
                "watched": "false",
                "like": "false",
                "title": "프로포즈",
                "local_id": 18240,
                "poster_url": "/aYlnDia7ldvqFUst1O5S8LZeM2S.jpg",
                "release_date": 20090903,
                "genre": "코미디 로맨스 드라마",
                "popularity": 119.449
            },
            {
                "watched": "false",
                "like": "false",
                "title": "미니언즈",
                "local_id": 211672,
                "poster_url": "/bkWrtIS7vscRvK074BWn6WHuwuf.jpg",
                "release_date": 20150729,
                "genre": "가족 애니메이션 모험 코미디",
                "popularity": 54.641
            },
            {
                "watched": "false",
                "like": "false",
                "title": "오션스 8",
                "local_id": 402900,
                "poster_url": "/rBJfBKvSllVhQXHygSSfs3t2YJV.jpg",
                "release_date": 20180613,
                "genre": "범죄 코미디 액션",
                "popularity": 49.964
            },
            {
                "watched": "false",
                "like": "false",
                "title": "버드 박스",
                "local_id": 405774,
                "poster_url": "/dB7jNL5I3hb7b1zsGD5OEoSl2BQ.jpg",
                "release_date": 20181221,
                "genre": "스릴러 드라마 SF",
                "popularity": 48.173
            },
            {
                "watched": "false",
                "like": "false",
                "title": "이집트 왕자",
                "local_id": 9837,
                "poster_url": "/tnAvUWWI9gHt6Nej9BB1FaLKPZd.jpg",
                "release_date": 19981219,
                "genre": "모험 애니메이션 드라마 가족",
                "popularity": 35.381
            },
            {
                "watched": "false",
                "like": "false",
                "title": "데몰리션 맨",
                "local_id": 9739,
                "poster_url": "/mVL2P4U1VBLVVJ7rziVwg5c0BVy.jpg",
                "release_date": 19931113,
                "genre": "범죄 액션 SF",
                "popularity": 29.41
            },
            {
                "watched": "false",
                "like": "false",
                "title": "그래비티",
                "local_id": 49047,
                "poster_url": "/u8ffl7CRAS12KA8eQEtkLuHg8Fm.jpg",
                "release_date": 20131017,
                "genre": "SF 스릴러 드라마",
                "popularity": 22.771
            },
            {
                "watched": "false",
                "like": "false",
                "title": "타임 투 킬",
                "local_id": 1645,
                "poster_url": "/apUSR9WE7lMATBGYhzZ8RnPDYsK.jpg",
                "release_date": 19961102,
                "genre": "범죄 드라마 스릴러",
                "popularity": 15.702
            },
            {
                "watched": "false",
                "like": "false",
                "title": "레이크 하우스",
                "local_id": 2044,
                "poster_url": "/spLrKu6jNQrWiQTkQ64ty51UsY.jpg",
                "release_date": 20060831,
                "genre": "로맨스 드라마 미스터리",
                "popularity": 15.168
            }
        ],
        "recomend_movie": "no_movie"
    }
    ```

  

# 영화 디테일

- /movies/detail/<영화id>/
  - method:
    - GET
  - header
    - 로그인, 비로그인 둘다 가능

- ```json
  {	
      // 영화정보
      // 영화카드 형태
      "movie_info": [
          {
              "watched": "false",
              "like": "false",
              "title": "로스트 시티",
              "local_id": 752623,
              "poster_url": "/8kZapNBZYGJu7AUbJVBDMmQgO1D.jpg",
              "release_date": 20220420,
              "genre": "액션 모험 코미디 로맨스",
              "popularity": 10211.875
          }
      ],
      
      // 감독 정보
      "director": [
          {
              "profile_url": "/7HZIthu9DIGbIhjmCmWGiAOJmk6.jpg",
              "name": "Peter Lyons Collister",
              "popularity": 3.586,
              "id": 1
          }
      ],
      
      // 출연한 배우목록
      "actor": [
          {
              "profile_url": "/u2tnZ0L2dwrzFKevVANYT5Pb1nE.jpg",
              "name": "Sandra Bullock",
              "popularity": 34.677,
              "id": 1
          },
          {
              "profile_url": "/bhTmp6FA8fOQnGlNk75tdmj2bpu.jpg",
              "name": "Channing Tatum",
              "popularity": 34.71,
              "id": 2
          },
          {
              "profile_url": "/uAICvHxj4cwSGjEY9B09Mhqxrk.jpg",
              "name": "Daniel Radcliffe",
              "popularity": 22.514,
              "id": 3
          },
          {
              "profile_url": "/oAvLuGuTaNcjY3R5huBQdfrZN6j.jpg",
              "name": "Brad Pitt",
              "popularity": 30.829,
              "id": 4
          },
          {
              "profile_url": "/awNT6lltD8zItbGtolmO8IGT8ot.jpg",
              "name": "Da'Vine Joy Randolph",
              "popularity": 9.267,
              "id": 5
          },
          {
              "profile_url": "/xcTRN4vILwgFBiAKszes8qUaRuM.jpg",
              "name": "Patti Harrison",
              "popularity": 6.996,
              "id": 6
          },
          {
              "profile_url": "/UBILHiRphJdlshvsyH920QSAhk.jpg",
              "name": "Oscar Nunez",
              "popularity": 12.815,
              "id": 7
          },
          {
              "profile_url": "/jOqMWGWRIjRZBboV4XwCh6yLxva.jpg",
              "name": "Bowen Yang",
              "popularity": 2.588,
              "id": 8
          },
          {
              "profile_url": "/h7ZoTwpELoz1IlIgx0ujoA2p9Sp.jpg",
              "name": "Stephen Lang",
              "popularity": 19.42,
              "id": 9
          },
          {
              "profile_url": "/5PU9da9gJrZFizL0teCm7YCosPT.jpg",
              "name": "Héctor Aníbal",
              "popularity": 4.368,
              "id": 10
          },
          {
              "profile_url": "/27nLNazohldNo17vqLRdWTHT147.jpg",
              "name": "Thomas Forbes-Johnson",
              "popularity": 1.592,
              "id": 11
          },
          {
              "profile_url": "/x2UdCvS0j3QL5NlebV6571xwIpt.jpg",
              "name": "Adam Nee",
              "popularity": 1.788,
              "id": 12
          },
          {
              "profile_url": "/1wRkhVFgVtEWoO9F61IHYB2FFvg.jpg",
              "name": "Raymond Lee",
              "popularity": 3.094,
              "id": 13
          },
          {
              "profile_url": "/nmAtvMZ6zVKw8EMBTRy8s3WYHRJ.jpg",
              "name": "Katherine Montes",
              "popularity": 1.099,
              "id": 14
          },
          {
              "profile_url": null,
              "name": "Danny Radhames Vasquez Castillo",
              "popularity": 0.6,
              "id": 15
          },
          {
              "profile_url": "/v7PsTbwOWeTkwischCuIPgmEHIT.jpg",
              "name": "Sli Lewis",
              "popularity": 0.98,
              "id": 16
          },
          {
              "profile_url": null,
              "name": "Olga Bucarelli",
              "popularity": 0.6,
              "id": 17
          },
          {
              "profile_url": null,
              "name": "Omar Patin",
              "popularity": 0.6,
              "id": 18
          },
          {
              "profile_url": "/fEnG0srYtnevTYBcVvO0fne499N.jpg",
              "name": "Anthony Alvarez",
              "popularity": 1.4,
              "id": 19
          },
          {
              "profile_url": null,
              "name": "Ryan Orr",
              "popularity": 0.6,
              "id": 20
          },
          {
              "profile_url": "/AapZKRgzlpBkcN3YmcFeynx4ZSm.jpg",
              "name": "Alex Schoenauer",
              "popularity": 1.38,
              "id": 21
          },
          {
              "profile_url": null,
              "name": "Edwin Polanco",
              "popularity": 0.6,
              "id": 22
          },
          {
              "profile_url": "/r6nduz2TD4VqwE0ogEuARSsZOkb.jpg",
              "name": "Marcy Jarreau",
              "popularity": 1.284,
              "id": 23
          },
          {
              "profile_url": null,
              "name": "Cynthia Oroz",
              "popularity": 0.6,
              "id": 24
          },
          {
              "profile_url": null,
              "name": "Carolina Rohana",
              "popularity": 0.98,
              "id": 25
          },
          {
              "profile_url": null,
              "name": "Jonathan Lev",
              "popularity": 0.6,
              "id": 26
          },
          {
              "profile_url": null,
              "name": "Toussaint Merionne",
              "popularity": 0.6,
              "id": 27
          },
          {
              "profile_url": null,
              "name": "Luinis Olaverria",
              "popularity": 0.6,
              "id": 28
          },
          {
              "profile_url": null,
              "name": "Emerson Gonzalez",
              "popularity": 0.648,
              "id": 29
          },
          {
              "profile_url": null,
              "name": "Wilson Ureña",
              "popularity": 0.6,
              "id": 30
          },
          {
              "profile_url": "/fsrFuTzkgK7rNzTbwrQigDWVWo3.jpg",
              "name": "Roger Wasserman",
              "popularity": 0.98,
              "id": 31
          },
          {
              "profile_url": null,
              "name": "Ryan Judd",
              "popularity": 0.6,
              "id": 32
          },
          {
              "profile_url": null,
              "name": "Zachary Steel",
              "popularity": 0.6,
              "id": 33
          },
          {
              "profile_url": null,
              "name": "Marcos Sánchez",
              "popularity": 0.6,
              "id": 34
          },
          {
              "profile_url": null,
              "name": "Zain Ullah",
              "popularity": 1.4,
              "id": 35
          }
      ]
  }
  ```

- 





# 검색

- /search/
  - method:
    - GET
    
  - body:
  
    - ```json
      {
          "keyword": "검색어"
      }
      ```
  
  - header
    - 로그인, 비로그인 둘다 가능

- 리턴형식

  - ```json
    {	
        // 완전히 일치하는 배우, 감독, 영화 정보
        "perfect": {
            "actor": [],
            "director": [
                {
                    "director_level": 40.0,
                    "director_info": {
                        "profile_url": "/tKLJBqbdH6HFj2QxLA5o8Zk7IVs.jpg",
                        "name": "Bong Joon-ho",
                        "popularity": 4.095,
                        "id": 307
                    },
                    // 감독이 완전 일치할 경우 
                    // 감독디테일이랑 같음
                    // 유저 완전일치, 영화 완전일치에서도 디테일, 프로필이랑 같은형식으로 리턴
                    "directed_movies": [
                        {
                            "watched": "true",
                            "like": "false",
                            "title": "기생충",
                            "local_id": 496243,
                            "poster_url": "/jjHccoFjbqlfr4VGLVLT7yek0Xn.jpg",
                            "release_date": 20190530,
                            "genre": "코미디 스릴러 드라마",
                            "popularity": 79.985
                        },
                        {
                            "watched": "false",
                            "like": "false",
                            "title": "설국열차",
                            "local_id": 110415,
                            "poster_url": "/pRZMtKQpP3fH84YXs02yytUk4ee.jpg",
                            "release_date": 20130801,
                            "genre": "액션 SF 드라마",
                            "popularity": 50.007
                        },
                        {
                            "watched": "true",
                            "like": "true",
                            "title": "괴물",
                            "local_id": 1255,
                            "poster_url": "/5lgyNwFqyaMMNW484rLgw7aRRZs.jpg",
                            "release_date": 20060727,
                            "genre": "공포 드라마 SF",
                            "popularity": 32.28
                        },
                        {
                            "watched": "true",
                            "like": "true",
                            "title": "살인의 추억",
                            "local_id": 11423,
                            "poster_url": "/sujAihJHmNMfeMNQ004KYIPvrGA.jpg",
                            "release_date": 20030502,
                            "genre": "범죄 드라마 스릴러",
                            "popularity": 17.82
                        },
                        {
                            "watched": "true",
                            "like": "false",
                            "title": "옥자",
                            "local_id": 387426,
                            "poster_url": "/miHNA5DcheO7ax2qon9CmC7qa9j.jpg",
                            "release_date": 20170629,
                            "genre": "모험 드라마 SF",
                            "popularity": 19.478
                        }
                    ],
                    "recomend_movie": {
                        "watched": "false",
                        "like": "false",
                        "title": "설국열차",
                        "local_id": 110415,
                        "poster_url": "/pRZMtKQpP3fH84YXs02yytUk4ee.jpg",
                        "release_date": 20130801,
                        "genre": "액션 SF 드라마",
                        "popularity": 50.007
                    }
                }
            ],
            "movie": []
        },
        "director": [],
        "actor": [],
        "movie": []
    }
    
    
    ==================================================================================
    
    
    // 검색어가 포함만 됐을 경우
    {
    
        "perfect": {
            "actor": [],
            "director": [],
            "movie": []
        },
        "director": [
            {
                "profile_url": "/tKLJBqbdH6HFj2QxLA5o8Zk7IVs.jpg",
                "name": "Bong Joon-ho",
                "popularity": 4.095,
                "id": 307
            },
            {
                "profile_url": null,
                "name": "Do Bong-san",
                "popularity": 0.692,
                "id": 1011
            }
        ],
        "actor": [
            {
                "profile_url": "/yLRKX9DPDGgTRKBQRFTUh3pvbU0.jpg",
                "name": "Sayaka Senbongi",
                "popularity": 5.273,
                "id": 747
            },
            {
                "profile_url": "/6NS02ljZ2ssoFyxEM0Jp2SpWYC5.jpg",
                "name": "Hyun Bong-sik",
                "popularity": 4.206,
                "id": 13783
            },
            {
                "profile_url": "/yI8xBqEi5IAeyoEgGcdbcyEc9vO.jpg",
                "name": "Patrick Sabongui",
                "popularity": 13.671,
                "id": 13872
            },
            {
                "profile_url": "/iDnwRIPELK41iaYT32G5UpiIPFx.jpg",
                "name": "Ahn Seong-bong",
                "popularity": 0.996,
                "id": 14663
            },
            {
                "profile_url": null,
                "name": "Sivu Nobongoza",
                "popularity": 0.6,
                "id": 15557
            },
            {
                "profile_url": "/jByYhcxIlAdEqpGnHiLzGXsTJ2b.jpg",
                "name": "Bongo Mbutuma",
                "popularity": 0.838,
                "id": 17198
            },
            {
                "profile_url": null,
                "name": "Siyabonga Radebe",
                "popularity": 0.6,
                "id": 17204
            },
            {
                "profile_url": null,
                "name": "Aguendia Fotabong",
                "popularity": 0.828,
                "id": 21629
            },
            {
                "profile_url": "/ft43oV8EpxAcWgCb4cIapnUEeLK.jpg",
                "name": "Bongkoj Khongmalai",
                "popularity": 7.844,
                "id": 21888
            },
            {
                "profile_url": null,
                "name": "Federico Bongiorno",
                "popularity": 0.6,
                "id": 23310
            },
            {
                "profile_url": null,
                "name": "Han Seok-bong",
                "popularity": 9.597,
                "id": 30665
            },
            {
                "profile_url": "/fV8BtRziGqUsBozd1G6lEwmW2b5.jpg",
                "name": "Byun Hee-bong",
                "popularity": 2.155,
                "id": 35886
            },
            {
                "profile_url": null,
                "name": "Sibongile Nojila",
                "popularity": 0.6,
                "id": 40960
            },
            {
                "profile_url": null,
                "name": "Kim Bong-soo",
                "popularity": 0.6,
                "id": 41380
            },
            {
                "profile_url": "/6M2WHQhrWoQxL22VkJBAfdHWchW.jpg",
                "name": "Eric Kabongo",
                "popularity": 0.643,
                "id": 42646
            },
            {
                "profile_url": null,
                "name": "Jeong Bong-jae",
                "popularity": 1.943,
                "id": 43938
            },
            {
                "profile_url": "/uliB2ZpdxcnDqPCG34YB69qR8vp.jpg",
                "name": "Ki Joo-bong",
                "popularity": 3.536,
                "id": 48258
            },
            {
                "profile_url": "/tcISELPMYywXwcCzcjWAfohhJm3.jpg",
                "name": "Lee Bong-ryeon",
                "popularity": 3.179,
                "id": 48764
            },
            {
                "profile_url": "/6zxYdbUr0nu2ibA3C0iGabNoEBP.jpg",
                "name": "Emmanuel Kabongo",
                "popularity": 1.312,
                "id": 49289
            },
            {
                "profile_url": "/yReZHDKtKn7pUh7bArC7RvFx8g.jpg",
                "name": "Baek Bong-ki",
                "popularity": 0.6,
                "id": 49834
            },
            {
                "profile_url": "/eSsi0SrWwp3TfXeUo7HfXqlROjG.jpg",
                "name": "Bodhi Sabongui",
                "popularity": 1.105,
                "id": 51702
            }
        ],
        "movie": []
    }
    
    
    ```