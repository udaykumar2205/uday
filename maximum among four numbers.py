csk=int(input())
mi=int(input())
rcb=int(input())
srh=int(input())
if csk==mi==rcb==srh:
    print('share the trophy')
elif csk>mi and mi>rcb and rcb>srh:
    print('trophy to csk')
elif mi>rcb and rcb>srh:
    print('trophy to mi')
elif rcb>srh:
    print('trophy to rcb')
else:
    print('trophy to srh')
    
