fi=-1 #fi değeri hangi durum baz alınarak belirlenir?
landa=0.5
portakal=[1,0]
portakalBeklenen=1
elma=[0,1]
elmaBeklenen=0
cikti = {"elma":elmaBeklenen,"portakal":portakalBeklenen}


def persepteron(**params):
    """
    x ve w değerleri girilir.
    Format;
    persepteron(x1=1,x2=2,w1=3,w2=4)
    """
    w=[]
    x=[]
    for key, value in params.items():
        if key[0]=='x':
            x.append(value)
        else:
            w.append(value)
    net=(x[0]*w[0])+(x[1]*w[1])
    print(f'x: {x} , w: {w} , net : {net} , beklenen: {1 if x==portakal else 0 }')
    if x==portakal and net>fi:
        sonuc=1
        if sonuc==portakalBeklenen:
            print("portakal\n")
    if x==portakal and net<=fi:
        sonuc=0
        if sonuc!=portakalBeklenen:
            persepteron(x1=x[0],x2=x[1],w1=(w[0]+(landa*x[0])),w2=(w[1]+(landa*x[1])))            
            
    if x==elma and net<=fi:
        sonuc=0
        if sonuc==elmaBeklenen:
            print("elma\n")
    if x==elma and net>fi:
        sonuc=1
        if sonuc!=elmaBeklenen:
            persepteron(x1=x[0],x2=x[1],w1=(w[0]-(landa*x[0])),w2=(w[1]-(landa*x[1])))                            

#verisetine uyarlama
deneme=[[1,0],[0,1],[1,0],[0,1],[0,1]]
for i in range(len(deneme)):
    for j in range(len(deneme[i])):
        x1=deneme[i][j]
        x2=deneme[i][j+1]
        print(f'{i+1}. Veri-----------> x1: {x1} , x2: {x2}')
        break
    persepteron(x1=x1,x2=x2,w1=1,w2=2)
    
#sonuc=persepteron(x1=0,x2=1,w1=1,w2=2)

# for key, value in cikti.items():
#     if sonuc==value:
#         print(key)
#         break




        




