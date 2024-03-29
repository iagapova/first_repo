text = """Подзимняя посадка овощей - не прихоть избалованных теплым климатом южан. Даже за Уралом можно практиковать такой вид посадок.
Правда, у осеннего посева овощей и трав есть свои тонкости, но ради раннего урожая можно и потрудиться.
В чем же плюсы и минусы осенней посадки ово-щей, как правильно подготовить гряды, выбрать семена и на что обратить внимание весной, чтобы получить урожай без лишних хлопот?
Как подготовить грядки для подзимнего сева овощей
Подготовка гряд играет немаловажную роль в процессе подзимнего сева. Ведь только качествен: ные, надежно защищенные грядки с питательным грунтом способны стать достойной защитой для семян, которым предстоит перенести зиму под открытым небом.
Если же снега в ваших краях и так немного, не за-будьте заранее заготовить слой лапниа им дау-гой мульчи, которая заменит снежный ской вашим, грядкам.
Для посева овощей лучше будет выбрать высокие грядки, однако если вы не сторонник их устрой-ства, подойдут и обычные, надежно защищенные по периметру досками, шифером, поликарбона-10М или другим материалом. Такое ограждение не даст весенним водам смыть посевы и задержит снег на грядах.
нечном и приподнятом месте, там, где весной в первую очередь тает снег. Однако осли у вас такое место находится на открытом пространстве, позаботьтесь о ветрозащитных конструкциях, на-пример, установите щиты с наветренной стороны.
Как и при посеве цветов на зиму, гряды нужно готовить заранее, пока держится плюсовая темпера-тура. Прополите грунт, внесите в него удобрения с низким содержанием азота (AVA, Осень, диаммо-
Фоска, нитрофоска), нарисуйте утлом плоскореза или граблей борозды для семян глубиной 3-5 см, а затем накройте гряду пленкой, чтобы избежать переузлажнения. В отдельных мешках запасите субстрат для мульчирования посадок (садовый грунт с торфом и песком в пропорции 1:2:1) и ждите морозов.
Когда установится стабильная отрицательная тем. пература, высевайте семена в 1,5-2 раза больше нормы, засыпайте их подготовленным грунтом, а затем мульчируйте лапником, сланбондом или здоровым листовым опадом.
Толщина укрытия
должна быть около 15 см, но помните, что латкле листья может разнести по участку ветром, так что они нуждаются в закреплении.
Поливать осенние посевы не нужно - весеннего тающего снега будет достаточно, чтобы напоить семена влагой.
Что сажают под зиму на огороде
Не можете рошить, что сажать под, зиму на дане, чтобы следующим летом насладиться свежими овощами и травами, и боитесь зре потратить силы и семена? Мы расскажем, каме культуры и сорта точно перенесут подзинний позев и порадуют дружными всходами."""

text = text.lower()

rua = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

mas = {}

for i in range(len(rua)):
    mas[rua[i]] = text.count(rua[i])

mas_sorted = sorted(mas.items(), key=lambda x: x[1], reverse=True)

for key, value in mas_sorted:
    print(key, value)

print(type(mas_sorted))
# print(list(zip()))

mmm = {}
rrr = ['000', '001', '010', '011', '100', '101', '110', '111']
text1 = ['101', '001', '111', '110', '100', '000', '001', '101', '000', '001', '000', '110', '101', '110', '110', '110', '110', '001', '101', '001', '110', '010', '011', '110', '001', '110', '110', '011', '101', '101', '100', '010', '101', '110', '110', '010', '011', '100', '100', '110', '110', '101', '001', '101', '110', '101', '010', '101', '101', '110', '001', '001', '110', '100', '111', '010', '110', '101', '011', '010', '101', '101', '110', '100', '001', '110', '100', '111', '101', '001', '110', '000', '111', '110', '010', '000', '110', '000', '110', '110', '101', '111', '110', '010', '001', '010', '110', '101', '000', '011', '001', '001', '001', '111', '101', '001', '010', '010', '100', '001', '110', '010', '010', '010', '110', '101', '110', '001', '011', '110', '001', '001', '000', '000', '010', '101', '000', '001', '110', '001', '101', '001', '001', '100', '111', '001', '010', '101', '001', '110', '010', '010', '000', '110', '110', '011', '000', '000', '011', '110', '101', '101', '010', '110', '000', '100', '101', '100', '000', '010', '101',
         '100', '010', '010', '110', '001', '001', '111', '001', '111', '111', '110', '000', '100', '000', '101', '000', '111', '011', '110', '010', '110', '000', '100', '010', '010', '011', '110', '110', '011', '010', '010', '100', '110', '110', '001', '110', '000', '011', '110', '000', '010', '111', '101', '001', '110', '010', '101', '001', '101', '111', '100', '110', '001', '010', '001', '101', '101', '011', '101', '001', '001', '000', '101', '101', '111', '110', '101', '000', '110', '001', '010', '101', '010', '111', '110', '001', '010', '100', '010', '001', '101', '010', '001', '110', '100', '011', '100', '001', '110', '101', '010', '101', '100', '010', '111', '000', '010', '001', '010', '101', '001', '110', '100', '001', '000', '100', '001', '010', '101', '100', '110', '101', '111', '101', '101', '110', '011', '111', '001', '010', '010', '000', '010', '001', '001', '111', '010', '101', '100', '100', '010', '011', '101', '010', '011', '101', '110', '110', '110', '010', '010', '011', '010', '011', '001', '111', '001', '011', '101', '111', '101', '110', '001']

# text1 = ['110', '101', '101', '111', '010', '111', '001', '001', '011', '100', '110', '111', '101', '001', '101', '010', '100', '000', '011', '110', '110', '110', '000', '011', '111', '111', '110', '100', '110', '001', '110', '011', '011', '001', '110', '110', '000', '001', '010', '111', '110', '010', '010', '001', '100', '100', '100', '010', '101', '010', '010', '100', '000', '101', '111', '101', '101', '001', '001', '011', '011', '010', '110', '000', '010', '011', '010', '110', '101', '110', '101', '100', '101', '111', '100', '111', '110', '100', '101', '011', '011', '110', '110', '101', '010', '110', '100', '100', '110', '100', '001', '101', '010', '010', '011', '000', '010', '101', '111', '101', '100', '011', '100', '101', '110', '001', '101', '100', '101', '111', '001', '110', '011', '100', '000', '100', '110', '110', '110', '101', '110', '100', '111', '101', '111', '110', '001', '001', '011', '111', '100', '101', '000', '010', '101', '110', '110', '001', '011', '001', '110', '001', '000', '111', '110', '011', '101', '000', '011', '111', '011', '101', '010',
#          '101', '101', '101', '011', '110', '111', '000', '111', '010', '011', '001', '110', '100', '000', '000', '000', '010', '000', '111', '110', '011', '010', '110', '000', '011', '000', '010', '010', '101', '111', '010', '100', '000', '000', '111', '011', '010', '011', '111', '001', '100', '001', '001', '001', '001', '011', '100', '001', '011', '110', '101', '001', '100', '011', '100', '011', '010', '010', '101', '010', '100', '011', '000', '110', '001', '011', '011', '111', '011', '101', '101', '100', '010', '011', '011', '010', '101', '001', '001', '001', '100', '000', '101', '011', '011', '010', '010', '111', '011', '011', '011', '010', '011', '011', '111', '111', '011', '101', '110', '101', '000', '011', '001', '010', '110', '010', '001', '111', '011', '011', '110', '101', '010', '101', '111', '101', '000', '100', '101', '000', '110', '010', '100', '001', '011', '101', '011', '111', '110', '001', '100', '100', '100', '101', '010', '101', '011', '100', '011', '011', '101', '000', '101', '101', '000', '101', '010', '111', '001', '101', '100', '100', '100', '010', '010']


def count_items(rrr, text1):
    for i in range(len(rrr)):
        mmm[rrr[i]] = text1.count(rrr[i])
    mmm_sorted = sorted(mmm.items(), key=lambda x: x[1], reverse=True)
    return (mmm_sorted)


RRR = []
k = 0
while k <= 7:
    for i in rrr:
        RRR.append(str(rrr[k]) + str(i))
    k += 1

print(len(text1))
TEXT1 = []
for i in range(0, len(text1), 2):
    TEXT1.append(str(text1[i]) + str(text1[i+1]))
# print(TEXT1)

# print(count_items(RRR, TEXT1))
for key, value in count_items(RRR, TEXT1):
    print(key, value)
