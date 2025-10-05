from utils.colors import cf
from core.fetches import distro_id

logos = {
    "arch" : {
        "logo": fr"""{cf[5]}
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
     /ossssssss/        +ssssooo/.\
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+:
 \.`                               ``/
    """,
        "main_color": cf[5] 
    },

    "ubuntu" : {
        "logo": fr"""
            .-/+oossssoo+/-.
        `:+ssssssssssssssssss+:`
      -+ssssssssssssssssssyyssss+-
    .ossssssssssssssssss{cf[8]}dMMMNy{cf[2]}sssso.
   /sssssssssss{cf[8]}hdmmNNmmyNMMMMh{cf[2]}ssssss/
  +sssssssss{cf[8]}hm{cf[2]}yd{cf[8]}MMMMMMMNddddy{cf[2]}ssssssss+
 /ssssssss{cf[8]}hNMMM{cf[2]}yh{cf[8]}hyyyyhmNMMMNh{cf[2]}ssssssss/
.ssssssss{cf[8]}dMMMNh{cf[2]}ssssssssss{cf[8]}hNMMMd{cf[2]}ssssssss.
+ssss{cf[8]}hhhyNMMNy{cf[2]}ssssssssssss{cf[8]}yNMMMy{cf[2]}sssssss+
oss{cf[8]}yNMMMNyMMh{cf[2]}ssssssssssssss{cf[8]}hmmmh{cf[2]}ssssssso
oss{cf[8]}yNMMMNyMMh{cf[2]}sssssssssssssshmmmh{cf[2]}ssssssso
+ssss{cf[8]}hhhyNMMNy{cf[2]}ssssssssssss{cf[8]}yNMMMy{cf[2]}sssssss+
.ssssssss{cf[8]}dMMMNh{cf[2]}ssssssssss{cf[8]}hNMMMd{cf[2]}ssssssss.
 /ssssssss{cf[8]}hNMMM{cf[2]}yh{cf[8]}hyyyyhdNMMMNh{cf[2]}ssssssss/
  +sssssssss{cf[8]}dm{cf[2]}yd{cf[8]}MMMMMMMMddddy{cf[2]}ssssssss+
   /sssssssssss{cf[8]}hdmNNNNmyNMMMMh{cf[2]}ssssss/
    .ossssssssssssssssss{cf[8]}dMMMNy{cf[2]}sssso.
      -+sssssssssssssssss{cf[8]}yyy{cf[2]}ssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.
        """,
        "main_color": cf[2]
    },


    "debian" : {
        "logo": f"""
        _,met$$$$$gg.
    ,g$$$$$$$$$$$$$$$P.
  ,g$$P"     \"\"\"Y$$.".
 ,$$P'              `$$$.
',$$P       ,ggs.     `$$b:
`d$$'     ,$P"'   {cf[2]}.{cf[8]}    $$$
 $$P      d$'     {cf[2]},{cf[8]}    $$P
 $$:      $$.   {cf[2]}-{cf[8]}    ,d$$'
 $$;      Y$b._   _,d$P'
 Y$$.    {cf[2]}`.{cf[8]}`"Y$$$$P"'
{cf[8]} `$$b      {cf[2]}"-.__
{cf[8]}  `Y$$
   `Y$$.
     `$$b.
       `Y$$b.
          `"Y$b._
              `\"\"\"
        """,

        "main_color": cf[8]
    },

    "fedora" : {
        "logo": fr"""
         /:-------------:\
       :-------------------::
     :-----------{cf[8]}/shhOHbmp{cf[5]}---:\
   /-----------{cf[8]}omMMMNNNMMD  {cf[5]}---:
  :-----------{cf[8]}sMMMMNMNMP{cf[5]}.    ---:
 :-----------{cf[8]}:MMMdP{cf[5]}-------    ---\
,------------{cf[8]}:MMMd{cf[5]}--------    ---:
:------------{cf[8]}:MMMd{cf[5]}-------    .---:
:----    {cf[8]}oNMMMMMMMMMNho{cf[5]}     .----:
:--     .{cf[8]}+shhhMMMmhhy++{cf[5]}   .------/
:-    -------{cf[8]}:MMMd{cf[5]}--------------:
:-   --------{cf[8]}/MMMd{cf[5]}-------------;
:-    ------{cf[8]}/hMMMy{cf[5]}------------:
:--{cf[8]} :dMNdhhdNMMNo{cf[5]}------------;
:---{cf[8]}:sdNMMMMNds:{cf[5]}------------:
:------{cf[8]}:://:{cf[5]}-------------::
:---------------------:/
        """,
        
        "main_color": cf[5]
    }, 
    
    "centos" : {
        "logo": fr"""
                 ..
               .PLTJ.
              <><><><>
     {cf[3]}KKSSV' 4KKK {cf[4]}LJ{cf[6]} KKKL.'VSSKK
     {cf[3]}KKV' 4KKKKK {cf[4]}LJ{cf[6]} KKKKAL 'VKK
     {cf[3]}V' ' 'VKKKK {cf[4]}LJ{cf[6]} KKKKV' ' 'V
     {cf[3]}.4MA.' 'VKK {cf[4]}LJ{cf[6]} KKV' '.4Mb.
{cf[6]}   . {cf[3]}KKKKKA.' 'V {cf[4]}LJ{cf[6]} V' '.4KKKKK {cf[5]}.
{cf[6]} .4D {cf[3]}KKKKKKKA.'' {cf[4]}LJ{cf[6]} ''.4KKKKKKK {cf[5]}FA.
{cf[6]}<QDD ++++++++++++  {cf[5]}++++++++++++ GFD>
{cf[6]} 'VD {cf[5]}KKKKKKKK'.. {cf[3]}LJ {cf[4]}..'KKKKKKKK {cf[5]}FV
{cf[6]}   ' {cf[5]}VKKKKK'. .4 {cf[3]}LJ {cf[4]}K. .'KKKKKV {cf[5]}'
     {cf[5]} 'VK'. .4KK {cf[3]}LJ {cf[4]}KKA. .'KV'
     {cf[5]}A. . .4KKKK {cf[3]}LJ {cf[4]}KKKKA. . .4
     {cf[5]}KKA. 'KKKKK {cf[3]}LJ {cf[4]}KKKKK' .4KK
     {cf[5]}KKSSA. VKKK {cf[3]}LJ {cf[4]}KKKV .4SSKK
{cf[3]}              <><><><>
               'MKKM'
                 ''
        """,
        
        "main_color": cf[5]
    }, 
    
    "manjaro" : {
        "logo": fr"""
██████████████████  ████████
██████████████████  ████████
██████████████████  ████████
██████████████████  ████████
████████            ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
        """,
        
        "main_color": cf[3]
    },


    "alpine" : {
        "logo": fr"""
       .hddddddddddddddddddddddh.
      :dddddddddddddddddddddddddd:
     /dddddddddddddddddddddddddddd/
    +dddddddddddddddddddddddddddddd+
  `sdddddddddddddddddddddddddddddddds`
 `ydddddddddddd++hdddddddddddddddddddy`
.hddddddddddd+`  `+ddddh:-sdddddddddddh.
hdddddddddd+`      `+y:    .sddddddddddh
ddddddddh+`   `//`   `.`     -sddddddddd
ddddddh+`   `/hddh/`   `:s-    -sddddddd
ddddh+`   `/+/dddddh/`   `+s-    -sddddd
ddd+`   `/o` :dddddddh/`   `oy-    .yddd
hdddyo+ohddyosdddddddddho+oydddy++ohdddh
.hddddddddddddddddddddddddddddddddddddh.
 `yddddddddddddddddddddddddddddddddddy`
  `sdddddddddddddddddddddddddddddddds`
    +dddddddddddddddddddddddddddddd+
     /dddddddddddddddddddddddddddd/
      :dddddddddddddddddddddddddd:
       .hddddddddddddddddddddddh.
        """,
        
        "main_color": cf[5]
    },

     "linuxmint" : {
        "logo": fr"""
             ...-:::::-...
{cf[16]}          .-MMMMMMMMMMMMMMM-.
      .-MMMM{cf[11]}`..-:::::::-..`{cf[16]}MMMM-.
    .:MMMM{cf[11]}.:MMMMMMMMMMMMMMM:.{cf[16]}MMMM:.
   -MMM{cf[11]}-M---MMMMMMMMMMMMMMMMMMM.{cf[16]}MMM-
 `:MMM{cf[11]}:MM`  :MMMM:....::-...-MMMM:{cf[16]}MMM:`
 :MMM{cf[11]}:MMM`  :MM:`  ``    ``  `:MMM:{cf[16]}MMM:
.MMM{cf[11]}.MMMM`  :MM.  -MM.  .MM-  `MMMM.{cf[16]}MMM.
:MMM{cf[11]}:MMMM`  :MM.  -MM-  .MM:  `MMMM-{cf[16]}MMM:
:MMM{cf[11]}:MMMM`  :MM.  -MM-  .MM:  `MMMM:{cf[16]}MMM:
:MMM{cf[11]}:MMMM`  :MM.  -MM-  .MM:  `MMMM-{cf[16]}MMM:
.MMM{cf[11]}.MMMM`  :MM:--:MM:--:MM:  `MMMM.{cf[16]}MMM.
 :MMM{cf[11]}:MMM-  `-MMMMMMMMMMMM-`  -MMM-{cf[16]}MMM:
  :MMM{cf[11]}:MMM:`                `:MMM:{cf[16]}MMM:
   .MMM{cf[11]}.MMMM:--------------:MMMM.{cf[16]}MMM.
     '-MMMM{cf[11]}.-MMMMMMMMMMMMMMM-.{cf[16]}MMMM-'
       '.-MMMM{cf[11]}``--:::::--``{cf[16]}MMMM-.'
{cf[16]}            '-MMMMMMMMMMMMM-'
{cf[16]}               ``-:::::-``
        """,
        
        "main_color": cf[16]
    },

     "opensuse-leap" : {
        "logo": fr"""
                 `-++:`
               ./oooooo/-
            `:oooooooooooo:.
          -+oooooooooooooooo+-`
       ./oooooooooooooooooooooo/-
      :oooooooooooooooooooooooooo:
    `  `-+oooooooooooooooooooo/-   `
 `:oo/-   .:ooooooooooooooo+:`  `-+oo/.
`/oooooo:.   -/oooooooooo/.   ./oooooo/.
  `:+ooooo+-`  `:+oooo+-   `:oooooo+:`
     .:oooooo/.   .::`   -+oooooo/.
        -/oooooo:.    ./oooooo+-
          `:+ooooo+-:+oooooo:`
             ./oooooooooo/.
                -/oooo+:`
                  `:/.
        """,
        
        "main_color": cf[8]
    },

     "kali" : {
        "logo": fr"""
..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc',.
 .                   OMo           ':${cf[5]}dd{cf[8]}o.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..',;:cdOOd::,.
                                    .:d;.':;.
                                       'd,  .'
                                         ;l   ..
                                          .o
                                            c
                                            .'
                                             .
        """,
        
        "main_color": cf[5]
    },


    "parrot" : {
        "logo": fr"""
  `:oho/-`
`mMMMMMMMMMMMNmmdhy-
 dMMMMMMMMMMMMMMMMMMs`
 +MMsohNMMMMMMMMMMMMMm/
 .My   .+dMMMMMMMMMMMMMh.
  +       :NMMMMMMMMMMMMNo
           `yMMMMMMMMMMMMMm:
             /NMMMMMMMMMMMMMy`
              .hMMMMMMMMMMMMMN+
                  ``-NMMMMMMMMMd-
                     /MMMMMMMMMMMs`
                      mMMMMMMMsyNMN/
                      +MMMMMMMo  :sNh.
                      `NMMMMMMm     -o/
                       oMMMMMMM.
                       `NMMMMMM+
                        +MMd/NMh
                         mMm -mN`
                         /MM  `h:
                          dM`   .
                          :M-
                           d:
                           -+
                            -
        """,
        
        "main_color": cf[7]
    },


    "zorin" : {
        "logo": fr"""
         `osssssssssssssssssssso`
       .osssssssssssssssssssssso.
      .+oooooooooooooooooooooooo+.


  `::::::::::::::::::::::.         .:`
 `+ssssssssssssssssss+:.`     `.:+ssso`
.ossssssssssssssso/.       `-+ossssssso.
ssssssssssssso/-`      `-/osssssssssssss
.ossssssso/-`      .-/ossssssssssssssso.
 `+sss+:.      `.:+ssssssssssssssssss+`
  `:.         .::::::::::::::::::::::`


      .+oooooooooooooooooooooooo+.
       -osssssssssssssssssssssso-
        `osssssssssssssssssssso`
        """,
        
        "main_color": cf[5]
    },

    "slackware" : {
        "logo": fr"""
                  :::::::
            :::::::::::::::::::
         :::::::::::::::::::::::::
       ::::::::{cf[8]}cllcccccllllllll{cf[5]}::::::
    :::::::::{cf[8]}lc               dc{cf[5]}:::::::
   ::::::::{cf[8]}cl   clllccllll    oc{cf[5]}:::::::::
  :::::::::{cf[8]}o   lc{cf[5]}::::::::{cf[8]}co   oc{cf[5]}::::::::::
 ::::::::::{cf[8]}o    cccclc{cf[5]}:::::{cf[8]}clcc{cf[5]}::::::::::::
 :::::::::::{cf[8]}lc        cclccclc{cf[5]}:::::::::::::
::::::::::::::{cf[8]}lcclcc          lc{cf[5]}::::::::::::
::::::::::{cf[8]}cclcc{cf[5]}:::::{cf[8]}lccclc     oc{cf[5]}:::::::::::
::::::::::{cf[8]}o    l{cf[5]}::::::::::{cf[8]}l    lc{cf[5]}:::::::::::
 :::::{cf[8]}cll{cf[5]}:{cf[8]}o     clcllcccll     o{cf[5]}:::::::::::
 :::::{cf[8]}occ{cf[5]}:{cf[8]}o                  clc{cf[5]}:::::::::::
  ::::{cf[8]}ocl{cf[5]}:{cf[8]}ccslclccclclccclclc{cf[5]}:::::::::::::
   :::{cf[8]}oclcccccccccccccllllllllllllll{cf[5]}:::::
    ::{cf[8]}lcc1lcccccccccccccccccccccccco{cf[5]}::::
      ::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::
           ::::::::::::::::::::::
                ::::::::::::
        """,
        
        "main_color": cf[5]
    },


     "solus" : {
        "logo": fr"""
            -```````````
          `-+/------------.`
       .---:mNo---------------.
     .-----yMMMy:---------------.
   `------oMMMMMm/----------------`
  .------/MMMMMMMN+----------------.
 .------/NMMMMMMMMm-+/--------------.
`------/NMMMMMMMMMN-:mh/-------------`
.-----/NMMMMMMMMMMM:-+MMd//oso/:-----.
-----/NMMMMMMMMMMMM+--mMMMh::smMmyo:--
----+NMMMMMMMMMMMMMo--yMMMMNo-:yMMMMd/.
.--oMMMMMMMMMMMMMMMy--yMMMMMMh:-yMMMy-`
`-sMMMMMMMMMMMMMMMMh--dMMMMMMMd:/Ny+y.
`-/+osyhhdmmNNMMMMMm-/MMMMMMMmh+/ohm+
  .------------:://+-/++++++{cf[5]}oshddys:
   -hhhhyyyyyyyyyyyhhhhddddhysssso-
    `:ossssssyysssssssssssssssso:`
      `:+ssssssssssssssssssss+-
         `-/+ssssssssssso+/-`
              `.-----..`
        """,
        
        "main_color": cf[8]
    },


     "puppy" : {
        "logo": fr"""
           `-/osyyyysosyhhhhhyys+-
  -ohmNNmh+/hMMMMMMMMNNNNd+dMMMMNM+
 yMMMMNNmmddo/NMMMNNNNNNNNNo+NNNNNy
.NNNNNNmmmddds:MMNNNNNNNNNNNh:mNNN/
-NNNdyyyhdmmmd`dNNNNNmmmmNNmdd/os/
.Nm+shddyooo+/smNNNNmmmmNh.   :mmd.
 NNNNy:`   ./hmmmmmmmNNNN:     hNMh
 NMN-    -++- +NNNNNNNNNNm+..-sMMMM-
.MMo    oNNNNo hNNNNNNNNmhdNNNMMMMM+
.MMs    /NNNN/ dNmhs+:-`  yMMMMMMMM+
 mMM+     .. `sNN+.      hMMMMhhMMM-
 +MMMmo:...:sNMMMMMms:` hMMMMm.hMMy
  yMMMMMMMMMMMNdMMMMMM::/+o+//dMMd`
   sMMMMMMMMMMN+:oyyo:sMMMNNMMMNy`
    :mMMMMMMMMMMMmddNMMMMMMMMmh/
      /dMMMMMMMMMMMMMMMMMMNdy/`
        .+hNMMMMMMMMMNmdhs/.
            .:/+ooo+/:-.
        """,
        
        "main_color": cf[5]
    },


     "tails" : {
        "logo": fr"""
     ``
  ./yhNh
syy/Nshh         `:o/
N:dsNshh  █   `ohNMMd
N-/+Nshh      `yMMMMd
N-yhMshh       yMMMMd
N-s:hshh  █    yMMMMd so//.
N-oyNsyh       yMMMMd d  Mms.
N:hohhhd:.     yMMMMd  syMMM+
Nsyh+-..+y+-   yMMMMd   :mMM+
+hy-      -ss/`yMMMM     `+d+
  :sy/.     ./yNMMMMm      ``
    .+ys- `:+hNMMMMMMy/`
      `hNmmMMMMMMMMMMMMdo.
       dMMMMMMMMMMMMMMMMMNh:
       +hMMMMMMMMMMMMMMMMMmy.
         -oNMMMMMMMMMMmy+.`
           `:yNMMMds/.`
              .//`
        """,
        
        "main_color": cf[6]
    },

    "rhel" : {
        "logo": fr"""
         .MMM..:MMMMMMM
          MMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMM.
         MMMMMMMMMMMMMMMMMMMMMM
        ,MMMMMMMMMMMMMMMMMMMMMM:
        MMMMMMMMMMMMMMMMMMMMMMMM
  .MMMM'  MMMMMMMMMMMMMMMMMMMMMM
 MMMMMM    `MMMMMMMMMMMMMMMMMMMM.
MMMMMMMM      MMMMMMMMMMMMMMMMMM .
MMMMMMMMM.       `MMMMMMMMMMMMM' MM.
MMMMMMMMMMM.                     MMMM
`MMMMMMMMMMMMM.                 ,MMMMM.
 `MMMMMMMMMMMMMMMMM.          ,MMMMMMMM.
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            `MMMMMMMMMMMMMMMMMMMMMMMM:
                ``MMMMMMMMMMMMMMMMM'
        """,
        
        "main_color": cf[2]
    },

    "clear" : {
        "logo": fr"""
          BBB
       BBBBBBBBB
     BBBBBBBBBBBBBBB
   BBBBBBBBBBBBBBBBBBBB
   BBBBBBBBBBB         BBB
  BBBBBBBB{cf[4]}YYYYY
{cf[5]}  BBBBBBBB{cf[4]}YYYYYY
{cf[5]}  BBBBBBBB{cf[4]}YYYYYYY
{cf[5]}  BBBBBBBBB{cf[4]}YYYYY{cf[8]}W
{cf[7]} GG{cf[5]}BBBBBBBY{cf[4]}YYYY{cf[8]}WWW
{cf[7]} GGG{cf[5]}BBBBBBB{cf[4]}YY{cf[8]}WWWWWWWW
{cf[7]} GGGGGG{cf[5]}BBBBBB{cf[8]}WWWWWWWW
{cf[7]} GGGGGGGG{cf[5]}BBBB{cf[8]}WWWWWWWW
{cf[7]}GGGGGGGGGGG{cf[5]}BBB{cf[8]}WWWWWWW
{cf[7]}GGGGGGGGGGGGG{cf[5]}B{cf[8]}WWWWWW
{cf[7]}GGGGGGGG{cf[8]}WWWWWWWWWWW
{cf[7]}GG{cf[8]}WWWWWWWWWWWWWWWW
 WWWWWWWWWWWWWWWW
      WWWWWWWWWW
          WWW
        """,
        
        "main_color": cf[5]
    },

     "artix" : {
        "logo": fr"""
                  'o'
                 'ooo'
                'ooxoo'
               'ooxxxoo'
              'oookkxxoo'
             'oiioxkkxxoo'
            ':;:iiiioxxxoo'
               `'.;::ioxxoo'
          '-.      `':;jiooo'
         'oooio-..     `'i:io'
        'ooooxxxxoio:,.   `'-;'
       'ooooxxxxxkkxoooIi:-.  `'
      'ooooxxxxxkkkkxoiiiiiji'
     'ooooxxxxxkxxoiiii:'`     .i'
    'ooooxxxxxoi:::'`       .;ioxo'
   'ooooxooi::'`         .:iiixkxxo'
  'ooooi:'`                `'';ioxxo'
 'i:'`                          '':io'
'`                                   `'
        """,
        
        "main_color": cf[5]
    },

    "void" : {
        "logo": fr"""
               __.;=====;.__
            _.=+==++=++=+=+===;.
             -=+++=+===+=+=+++++=_
        .     -=:``     `--==+=++==.
       _vi,    `            --+=++++:
      .uvnvi.       _._       -==+==+.
     .vvnvnI`    .;==|==;.     :|=||=|.
{cf[8]}+QmQQm{cf[3]}pvvnv; {cf[8]}_yYsyQQWUUQQQm #QmQ#{cf[3]}:{cf[8]}QQQWUVQQm.
{cf[8]} -QQWQW{cf[3]}pvvo{cf[8]}wZ?.wQQQE{cf[3]}==<{cf[8]}QWWQ/QWQW.QQWW{cf[3]}(: {cf[8]}jQWQE
{cf[8]}  -$QQQQmmU'  jQQQ@{cf[3]}+=<{cf[8]}QWQQ)mQQQ.mQQQC{cf[3]}+;{cf[8]}jWQQ@'
{cf[8]}   -$WQ8Y{cf[3]}nI:   {cf[8]}QWQQwgQQWV{cf[3]}`{cf[8]}mWQQ.jQWQQgyyWW@!
{cf[3]}     -1vvnvv.     `~+++`        ++|+++
      +vnvnnv,                 `-|===
       +vnvnvns.           .      :=-
        -Invnvvnsi..___..=sv=.     `
          +Invnvnvnnnnnnnnvvnn;.
            ~|Invnvnvvnvvvnnv)+`
               -~|(*l)*|~
        """,
        
        "main_color": cf[3]
    },

    "opensuse-tumbleweed" : {
        "logo": fr"""
        ......
     .,cdxxxoc,.               .:kKMMMNWMMMNk:.
    cKMMN0OOOKWMMXo. ;        ;0MWk:.      .:OMMk.
  ;WMK;.       .lKMMNM,     :NMK,             .OMW;
 cMW;            'WMMMN   ,XMK,                 oMM'
.MMc               ..;l. xMN:                    KM0
'MM.                   'NMO                      oMM
.MM,                 .kMMl                       xMN
 KM0               .kMM0. .dl:,..               .WMd
 .XM0.           ,OMMK,    OMMMK.              .XMK
   oWMO:.    .;xNMMk,       NNNMKl.          .xWMx
     :ONMMNXMMMKx;          .  ,xNMWKkxllox0NMWk,
         .....                    .:dOOXXKOxl,
        """,
        
        "main_color": cf[8]
    },

    "peppermintos" : {
        "logo": fr"""
               PPPPPPPPPPPPPP
           PPPP{cf[16]}MMMMMMM{cf[2]}PPPPPPPPPPP
         PPPP{cf[16]}MMMMMMMMMM{cf[2]}PPPPPPPP{cf[16]}MM{cf[2]}PP
       PPPPPPPP{cf[16]}MMMMMMM{cf[2]}PPPPPPPP{cf[16]}MMMMM{cf[2]}PP
     PPPPPPPPPPPP{cf[16]}MMMMMM{cf[2]}PPPPPPP{cf[16]}MMMMMMM{cf[2]}PP
    PPPPPPPPPPPP{cf[16]}MMMMMMM{cf[2]}PPPP{cf[16]}M{cf[2]}P{cf[16]}MMMMMMMMM{cf[2]}PP
   PP{cf[16]}MMMM{cf[2]}PPPPPPPPPP{cf[16]}MMM{cf[2]}PPPPP{cf[16]}MMMMMMM{cf[2]}P{cf[16]}MM{cf[2]}PPPP
   P{cf[16]}MMMMMMMMMM{cf[2]}PPPPPP{cf[16]}MM{cf[2]}PPPPP{cf[16]}MMMMMM{cf[2]}PPPPPPPP
  P{cf[16]}MMMMMMMMMMMM{cf[2]}PPPPP{cf[16]}MM{cf[2]}PP{cf[16]}M{cf[2]}P{cf[16]}MM{cf[2]}P{cf[16]}MM{cf[2]}PPPPPPPPPPP
  P{cf[16]}MMMMMMMMMMMMMMMM{cf[2]}PP{cf[16]}M{cf[2]}P{cf[16]}MMM{cf[2]}PPPPPPPPPPPPPPPP
  P{cf[16]}MMM{cf[2]}PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP{cf[16]}MMMMM{cf[2]}P
  PPPPPPPPPPPPPPPP{cf[16]}MMM{cf[2]}P{cf[16]}M{cf[2]}P{cf[16]}MMMMMMMMMMMMMMMM{cf[2]}PP
  PPPPPPPPPPP{cf[16]}MM{cf[2]}P{cf[16]}MM{cf[2]}PPPP{cf[16]}MM{cf[2]}PPPPP{cf[16]}MMMMMMMMMMM{cf[2]}PP
   PPPPPPPP{cf[16]}MMMMMM{cf[2]}PPPPP{cf[16]}MM{cf[2]}PPPPPP{cf[16]}MMMMMMMMM{cf[2]}PP
   PPPP{cf[16]}MM{cf[2]}P{cf[16]}MMMMMMM{cf[2]}PPPPPP{cf[16]}MM{cf[2]}PPPPPPPPPP{cf[16]}MMMM{cf[2]}PP
    PP{cf[16]}MMMMMMMMM{cf[2]}P{cf[16]}M{cf[2]}PPPP{cf[16]}MMMMMM{cf[2]}PPPPPPPPPPPPP
    PP{cf[16]}MMMMMMM{cf[2]}PPPPPPP{cf[16]}MMMMMM{cf[2]}PPPPPPPPPPPP
      PP{cf[16]}MMMM{cf[2]}PPPPPPPPP{cf[16]}MMMMMMM{cf[2]}PPPPPPPP
        PP{cf[16]}MM{cf[2]}PPPPPPPP{cf[16]}MMMMMMMMMM{cf[2]}PPPP
           PPPPPPPPPP{cf[16]}MMMMMMMM{cf[2]}PPPP
               PPPPPPPPPPPPPP
        """,
        
        "main_color": cf[2]
    },

     "gentoo" : {
        "logo": fr"""
{cf[6]}         -/oyddmdhs+:.
     -o{cf[8]}dNMMMMMMMMNNmhy+{cf[6]}-`
   -y{cf[8]}NMMMMMMMMMMMNNNmmdhy{cf[6]}+-
 `o{cf[8]}mMMMMMMMMMMMMNmdmmmmddhhy{cf[6]}/`
 om{cf[8]}MMMMMMMMMMMN{cf[6]}hhyyyo{cf[8]}hmdddhhhd{cf[6]}o`
.y{cf[8]}dMMMMMMMMMMd{cf[6]}hs++so/s{cf[8]}mdddhhhhdm{cf[6]}+`
 oy{cf[8]}hdmNMMMMMMMN{cf[6]}dyooy{cf[8]}dmddddhhhhyhN{cf[6]}d.
  :o{cf[8]}yhhdNNMMMMMMMNNNmmdddhhhhhyym{cf[6]}Mh
    .:{cf[8]}+sydNMMMMMNNNmmmdddhhhhhhmM{cf[6]}my
       /m{cf[8]}MMMMMMNNNmmmdddhhhhhmMNh{cf[6]}s:
    `o{cf[8]}NMMMMMMMNNNmmmddddhhdmMNhs{cf[6]}+`
  `s{cf[8]}NMMMMMMMMNNNmmmdddddmNMmhs{cf[6]}/.
 /N{cf[8]}MMMMMMMMNNNNmmmdddmNMNdso{cf[6]}:`
+M{cf[8]}MMMMMMNNNNNmmmmdmNMNdso{cf[6]}/-
yM{cf[8]}MNNNNNNNmmmmmNNMmhs+/{cf[6]}-`
/h{cf[8]}MMNNNNNNNNMNdhs++/{cf[6]}-`
`/{cf[8]}ohdmmddhys+++/:{cf[6]}.`
  `-//////:--.
        """,
        
        "main_color": cf[6]
    },

    "cachyos": {
      "logo": fr"""
            {cf[11]}.{cf[3]}-------------------------:
          .{cf[5]}+={cf[3]}========================.
         :{cf[5]}++{cf[3]}==={cf[5]}++==={cf[3]}===============-       :{cf[5]}++{cf[3]}-
        :{cf[5]}*++{cf[3]}===={cf[5]}+++++=={cf[3]}===========-        .==:
       -{cf[5]}*+++{cf[3]}====={cf[5]}+***++={cf[3]}=========:
      ={cf[5]}*++++={cf[3]}=======------------:
     ={cf[5]}*+++++={cf[3]}====-                     {cf[11]}...{cf[3]}
   .{cf[5]}+*+++++{cf[3]}=-===:                    .{cf[5]}=+++={cf[3]}:
  :{cf[5]}++++{cf[3]}=====-==:                     -***{cf[5]}**{cf[3]}+
 :{cf[5]}++={cf[3]}=======-=.                      .=+**+{cf[11]}.{cf[3]}
.{cf[5]}+{cf[3]}==========-.                          {cf[11]}.{cf[3]}
 :{cf[5]}+++++++{cf[3]}====-                                {cf[11]}.{cf[3]}--==-{cf[11]}.{cf[3]}
  :{cf[5]}++{cf[3]}==========.                             {cf[11]}:{cf[5]}+++++++{cf[3]}{cf[11]}:
   {cf[3]}.-===========.                            =*****+*+
    {cf[3]}.-===========:                           .+*****+:
      {cf[3]}-======={cf[5]}++++{cf[3]}:::::::::::::::::::::::::-:  {cf[11]}.{cf[3]}---:
       :======{cf[5]}++++{cf[3]}===={cf[5]}+++******************=.
        {cf[3]}:====={cf[5]}+++{cf[3]}=========={cf[5]}++++++++++++++*-
         {cf[3]}.===={cf[5]}++{cf[3]}=============={cf[5]}++++++++++*-
          {cf[3]}.==={cf[5]}+{cf[3]}=================={cf[5]}+++++++:
           {cf[3]}.-======================={cf[5]}+++:
             {cf[11]}..........................
  """,
    "main_color": cf[3]
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