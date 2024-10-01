from colors import cf
from fetches import distro_id

logos = {
    "arch" : {
        "logo": f"""{cf[5]}
                   -`
                  .o+`
                 `ooo/,
                `+oooo:,
               `+oooooo:,
              , `!-oooo+:,
             `/+;.:-oooo+:,
            `/+++-;+++++++:,
           `/+++++++++++ooo:.
          `/+++ooooooooooooo/`
        ./ooosssso++ossssss-:+`                 
        .oossssso-````-oss-!,`+'
       -osssssso.      :ssss:;.,
      :osssssss/        osssso-++.
     /ossssssss/        +ssssooo/.\\
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+:
 \\.`                               ``/
    """,
        "main_color": cf[5] 
    },

    "fallback": {

        "logo" : f"""{cf[8]}
      ________
  _jgN########Ngg_
_N##N@@""  ""9NN##Np_
d###P            N####p
"^^"              T####
                d###P
            _g###@F
            _gN##@P
         gN###F"
         d###F
         0###F
         0###F
         0###F
         "NN@'

          ___
         q###r
          ---
        """,

        "main_color": cf[8] 

    } 
}

def get_logos_values(key=''):
    if key == '':
        key = distro_id()

    if key in logos:
        return logos[key]
    
    return logos["fallback"]