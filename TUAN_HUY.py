import time

n = input("Enter your password :")

code = ["start loading......................................................................******",
    "just a moment.......loading 0%",
    "just a moment.......loading 10%",
    "just a moment.......loading 20%",
    "just a moment.......loading 30%",
    "just a moment.......loading 40%",
    "just a moment.......loading 50%",
    "just a moment.......loading 60%",
    "just a moment.......loading 70%",
    "just a moment.......loading 80%",
    "just a moment.......loading 90%",
    "just a moment.......loading 100%",

"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QMmmKKmKPGPKmKKsmZQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#MzXWQ@@@@@@@@@@@@@@#gGXzb#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$wz$@@@@@@@@@@@K@@@@@@@@@@#9yyg@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$uK#@@@@@@@@@@@@Q*$@@@@@@@@@@@@Bzl8@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#XG@@@@@@@@@@#0O9$B$``=}MB@@@@@@@@@#IT@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#iM@@@@@@@#Rbd9B@@@B$G3wx=_!xP#@@@@@@@DT#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#xd@@@@@@@@#g#Qggg00Q8rxuwzm3miO@@@@@@@@K}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@VX@@@@@@@@@@@IkOO3O#@g `_=**rd@@@@@@@@@@@lm@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@0v@@@@@@@@@@@@OKD^MDQ@g      -Q@@@@@@@@@@@#vB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@wX@@@@@@@@@@@@gO#W##Qgd!_.`  -Q@@@@@@@@@@@@cM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}O@@@@@@@@@@@@OD88QQB#Ybx!___!d@@@@@@@@@@@@mw@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@uZ@@@@@@@@@#OgI@@@@@@@TggDx,,,_;}Z#@@@@@@@@IX@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Mc@@@@@@@#KV$BI@#YzD@@l#@@*    `._I@@@@@@@@LD@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#xB@@@@@@OK@@@I@sl@@@@u@@@r       l@@@@@@@8v#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@WT#@@@@@ZG@@@I@}s@@@@u@@@r       Y@@@@@@#iD@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ZGWMWMM3Q@@@8@0Q@@@@$@@@bVVVVVyVIMMMMMMPR@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@dV|^^^^^^)VIQ@@@@GTr^^)uD#3V)^^^^^^*YTTYxr^^^^)B@@dyx^^^^^^rLTTYxr^^^<i#@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@8,````-9@@@@@@@@@9_:Q@@@@@Q!`````X@@@@@#$z:`-Q@@@@#)````'G@@@@@#$y,`=#@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@#<````!#@@@@@@@@@@^*@@@@@@@)`````b@@@@@@@@#*-Q@@@@@V````'$@@@@@@@@Q!!#@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@#<````!#@@@@@@@@@@^*@@@@@@@r`````Z@@@@9|#@@BxB@@@@@V````'$@@@@ML@@@gi#@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@#<````!#@@@@@@@@@@^*@@@@@@@)`````Z@@@#<!#@@@@@@@@@@V````.$@@@Q:*@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@#<````!#@@@@@@@@@@^*@@@@@@@)`````kgOk!`!#@@@@@@@@@@V````'KgOy@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@#<````!#@@@@@@@@@@^*@@@@@@@)`````rTv!``!#@@@@@@@@@@V````'vTv!``*@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@#<````!#@@@@@@@@@@^*@@@@@@@)`````b@@@g:!#@@@@@@@@@@V````'$@@@O,r@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@^````:#@@@@@@@@@#=|@@@@@@@)`````b@@@@G!#@@@@Q9@@@@V````'$@@@@kr@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@y````.R@@@@@@@@@d-P@@@@@@@r`````Z@@@@#8@@@@9@c@@@@y````.$@@@@#Q@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@#v````~8@@@@@@@M:l@@@@@@@@r`````Z@@@@@@@@Bl--$@@@@V````.0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@Qc;-``:)L}x)^cQ@@@@@@gOu-`````<GbbMmVv:```v@@QOy,`````^390#@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@#QDOdbO$B@@@@@@@@@9bddddddddddOdddOOdddB@@8OOO9OOOOOO99#@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"Q0$0$$$0$$D$0D$0D0$$$$0D$000000$$$$00000000000000000$0000$$00000$0$00000$$0$000$00000$0000$00$0D000$0000$0g@",
"#@#@#@@@##@@####@##@@##@@#####@@#@@@#@@###@@##@@##@@##@#@@@@##@@#@#@#@#B@@##@@@@#@@@######@@@@#@@#@@@@B#@###",
"v#vc!PxXvl3VG))YO~i|W<v3lVX^dMiLO@$xWxL=x$@X=xZcy3dyVGYrYzTlk3ix*M:wvzxWZlrxQ@#)rQ@@vrTVL)3Y93=X0!PL3vPsR^)T",
"*s)kLK!XxB)T#)vud*G|Oi)xLGQv@@VV@@0xPxxxg#@k;}Zucmdwu3}|M^Ylymivv=vy|kxPZmx<G@b~~v#@vKQKLxG!k*w*kxG!KvKID;xV",

"██████╗░███████╗░██████╗██╗░██████╗░███╗░░██╗  ██████╗░██╗░░░██╗",
"██╔══██╗██╔════╝██╔════╝██║██╔════╝░████╗░██║  ██╔══██╗╚██╗░██╔╝",
"██║░░██║█████╗░░╚█████╗░██║██║░░██╗░██╔██╗██║  ██████╦╝░╚████╔╝░",
"██║░░██║██╔══╝░░░╚═══██╗██║██║░░╚██╗██║╚████║  ██╔══██╗░░╚██╔╝░░",
"██████╔╝███████╗██████╔╝██║╚██████╔╝██║░╚███║  ██████╦╝░░░██║░░░",
"╚═════╝░╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░╚══╝  ╚═════╝░░░░╚═╝░░░",

"████████╗██╗░░░██╗░█████╗░███╗░░██╗  ██╗░░██╗██╗░░░██╗██╗░░░██╗",
"╚══██╔══╝██║░░░██║██╔══██╗████╗░██║  ██║░░██║██║░░░██║╚██╗░██╔╝",
"░░░██║░░░██║░░░██║███████║██╔██╗██║  ███████║██║░░░██║░╚████╔╝░",
"░░░██║░░░██║░░░██║██╔══██║██║╚████║  ██╔══██║██║░░░██║░░╚██╔╝░░",
"░░░██║░░░╚██████╔╝██║░░██║██║░╚███║  ██║░░██║╚██████╔╝░░░██║░░░",
"░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░"
]


if n == "UEF":
    for a in code:
        print(a,flush=True)
        time.sleep(0.1)
else:
    print("mật khẩu không hợp lệ !")
    print("vui lòng nhập lại !")
