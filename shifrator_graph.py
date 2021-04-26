from tkinter import *
alfavit = ' abcdefghijklmnopqrstuvwxyz@$-?!:1234567890абвгдеёжзийклмнопрстуфхцчшщьъыэюя'
t = {  ' ': 'psihfyiftushtsuhdtdhdtr56r7tgyu45e6rt7gtf45ert6wdsdwdwdwerrrrq',
       'a': 'hdiejwupqpuyahjagidjvyee45t768gyuvht6dtr5t76gytf67gyu66363t6q6',
       'b': 'pwpwiowkwhssfdghjkrstzwesr45ctydr76gye45t76fdr6e45t7q6gyde65r6',
       'c': 'paighrgudihhfgydhgdfudtr76y8dtr76xde4rfgghvfrdfh65tqgh3e3e3e3e',
       'd': 'uegdhejgqhqoshhdudhdgddtr76y8gdtr76drserfguhjhguy78uihgqvrt76u',
       'e': 'iegeheieyuwgwguqoqigvfdtr76y8t6u89y7hwe45t76y8gdsqwerfdwsertyh',
       'f': 'yiehshudydheijegdydre45t76r76te45xrs456tdre45f6d5we5q2wsefrre3',
       'g': 'ueypqyggijgtuyfghsisohddtrf76y89gutf76y8u9t76y8h9guct7q6gyuf6t',
       'h': 'p4ujjhahsiwswjssafaft67ytr567y3t6e7ywe765edfgu33ye78q3iue6738e',
       'i': 'e9phssgxhsnvgxyseerdssar4567yt67ijhgtyuijt6u3eyw5erfg3qhte53t3',
       'j': '78nhshdhsudsbdbjkajndt567uhgt67uhgtyuyu65rfghgret6yhy33qyjegey',
       'k': '0shdbhshqduw77sbtstrf76y8gut76y8guvyuij876r5e4rgder5yuhgfrtyt3',
       'l': 'ghxdvsghhd84gbd6w792tvr567uyt567uyt5637ugefrt7uet6w7iuejqhsydu',
       'm': 'uid88vdzhhqud9o89ahsij89dabakr5678ujhgfr567ujhbfewsxzaq345676j',
       'n': '0826wbhsj72hsb27sn2b7safrtyhgfrt6yuht67uytuh5678uhbfrq5678i339',
       'o': 'osjd892gsbn72bs91bshjhdhdsjne56yhgvfdertyujhgfyujhvfghqbhgvgyh',
       'p': 'jh782hs278s1i9sb819jsnbaj92bsu34567yteasdfghjjbvce4567q8uygfrt',
       'q': 'w7sb27sj2bsujsnjajskajhssnuiuhdde45678iknbgshjdiytrr56qugfvnnv',
       'r': 'byusyudys928782ctbhr5678uyt67uyt567u3beft7uijdmnbvsftqyudjhhhd',
       's': 'iy878hw8w89ddbatyyuhd839hs8567uhgt567uh35tgdst56d7uw7q8disudiw',
       't': '02jsbsgshbdguibyaibydwj8bsu82bsujbr567ytr567uyhtrt67quiuhtyuhd',
       'u': 'h8ysjbw8sjnuiikshwkosbdfer768ygufdtre45t76er76d5678ytygqgfgftg',
       'v': '93bsyj3bhisj39snsh839sn38sou3us8sgtyhgftyuhbgtyhjhgyqujhujyuhh',
       'w': 'fjkbduw9892gbsb89suy278s9289sbyungfghgvcftyhvcfyuhgyhgfqtyhghj',
       'x': 'jhbyuwui89hshsggyusgyudgyuyuw76gv627sygu78345yuhgfdqe4567ygfff',
       'y': '8bhsh2u8suhahyusu2y7sajskgaisusfr567ygfr56ygfr567yfr56q7ytrftd',
       'z': 'jsjw927jsh28sns7s2hsh2s72sn27s8ajsnagyi2bfuyfrtyhgfrtqyhgrtygt',
       '@': '01jhs9sjh28sf27s7hs8sjbtbgssjjahsiw828sb57ygfr56ygfftyqhgftyhh',
       '$': '09sbhdus8wuhsb27suasy8jyw7s8jwy7s28sbya8ht7t76gqyudrt76yuydrui',
       '-': '76sybuhdiyhzyjwgyuik7u2gys7sj2g7s2877s82stiagsft678ugft7qr56yf',
       '?': '28sbhbdyusajndyuy89db78wudnsdv89udjwjhdvw8r5678ugfr678ihgqtfty',
       '!': 'w88hsgusjjagswjdhsgdwdgwudhudhywui3vduzse5erftredfg8q7tr67uhgf',
       ':': 'ajhdguiuiwidafyut7893dt7sijhkdwafudt7yuh3678uihdbxt5q6tu87ygfc',
       '1': '28whgsuhsvy8sgyysyufgwsyhtqtyu2gys7yus76a82snsghaj45q67tfgrth3',
       '2': 'trgerr5tyddqrgxdfvsdgjhbftyuhyussyuy78g7ugyfr567uhgft67ujgt67u',
       '3': 'xtygsbhusaswyqdgsgydy727wt6dgb7dhgd8shgdwggdshdhwh567uhgfrt67u',
       '4': 'gsgdwu7sgy3ss683jvsyshsayhi8wt72t78dusgyudjyfau567uhgqt67y3333',
       '5': '9sbdsghdywgdtaydi8w27hsyhsuhagygujvfhfyh2tfgys7dybsgqyd567yhgf',
       '6': '42fgsuashfayjys63fdstdts7dhshdy7gdsdyusdh567uyhgfr5q6yh7ui7uy7',
       '7': '6suivgstyaisg7hsysasfasesghdhgfdhhgyy83gsuiasit678ujbgfqtyujh3',
       '8': '12sdsfefeesdsdshgghhbcj72jhsghdsdjhsdj567uhgft67uhbgtqy3dfdfe3',
       '9': 'xtgz77s7hsuajhxay8s8b2sviasih2usj2t678uhgftyuhbgtyuhqgty3yuyuh',
       '0': 'fdjcndjcnjdbui3yu89d38bd779su8duagu8di3guyui4567yuhgvftqryuhgy',
       'а': 'n7xn27nx7wtxhsjhbgdxjgdwd8dwufdy8iby7ijdwy7y8hi45q67yujhgvftry',
       'б': 'btysg8u2bs92kssudjw0dju2diudw9gdw8dshdsudvysyd4rgfr56hqgtyhbgg',
       'в': 'mdied8i29sh2suausjau28sh8d9hwgd8wuihdgs8uidhwg78567uhqbtuh3tyj',
       'г': 'sdu2hsiau8s2id88929idh8su9idjuwwhduwii2678ujhgftyujhgqtyy3he77',
       'д': '72su9a9s98usghidh872sidhgsud728dw0d9d0w0dis29dygsdu6q78uhgty67',
       'е': 'dsid2jad92ujqd2u8d9uwidbu89jtryuijjrt45676tgjh67uhgt67ygftygdd',
       'ё': 'sd762uysdrtyu7gw7dwudgysyihd7sdw89iajd8wjihsuiduw7dw56q7yhgf56',
       'ж': 'jsd280ausahhdshd8gdwuidspodiw8dgsjiodu9wgydbjkwd768uygqhft56ye',
       'з': 'xzvctysyauhsq8sy792008wsygvud67dw7ydfiahduuhw7wudu8w23q345tgff',
       'и': 'y78dsy8dhbjhwduhsjoidg78w09dbyuhsjioplwdg78wu8dsgvyqd567uhgtyh',
       'й': 'sdyusdhwujioyjhs78ujhwdy78wdh89h8h898h89g8tf7serswew7q68uiyt6y',
       'к': 'sgydsdwdshdtqsydh7876w5wtdg76sd564a7gdwdd7676uihgtr5678uytr6y4',
       'л': 'w8su88sgsjsjajsdhajdaid892vsas89jhgy8htyhbhgtyhbtfyu26gdq5e67w',
       'м': 'fd7uw9ygdf6w7q8dbsydghnwdvg6s7dy762fgsuhvdctuhdagudyhd6gswyssh',
       'н': '82ysyvdtysuhjdnbvctfxgyh88w7dtvbhsgvcfdtsgyuhdwby7u6q8gusdhsud',
       'о': '627u8hsbgvycjiosnbhvyu89jiongu6y7wjiohd7wyvdysujhkbdvfytsqyuhi',
       'п': '8ussydgs7dwydgvtysuighdvtysdgvwtyugdyuwigdvyuwidvtqyuduhwdygdd',
       'р': 'w82jijihsdudhw8dw78ijsbydgsujidny78wudh8isdhusdhusdjisiqdw2r4r',
       'с': '72usisdhsuhduhsdywudgsh8diwidisihdhiwidhshdiwdwdqsiduhwjidji34',
       'т': '28usd8sdudsudgw7dwu8dsyudgywgy7dhsuhdysuhdsgydhwhuqdwudgsydbfa',
       'у': '267y78sy7qsdj9wbuduh8sji9dgyudu8stgudy6y7ujihfyguhjiwbvty345rs',
       'ф': 'w8288shajkgyeuegfdtyuhsnbgvtfgyuhsxvcrf56w7w56stzyuhrtyqshisj8',
       'х': 'uytrfde4rty2q5678ss67y8hgdfw67udf7wy7d56sg7usdgduwywd6wdgwydhs',
       'ц': 't6wsswtu76wsy7682889shi8gd87wuhdgwd78wiydg7w8dwydqw89dsgd78sdy',
       'ч': 'euugshyhdnbstyduhjnsvydtgyuhj78w9jnbwt7ydisbdusvtdhivydqvyaudv',
       'ш': '0912786wftvgfc7654erdfgvhui78y65trfgvwhsuhygtcdftyauhqbg7ywgw7',
       'щ': '9ijbyikjhsduijbygu82jiuygjdnsgjdyahjdbhajkdbjadbhajdhbqyw7ywgd',
       'ь': '827uyhsgby7ujisnhbvuwg789duhbhsudyg78wvdysuhdsuyhsd78qwuplkjhb',
       'ъ': '278suhbvgyqduhsnhdghjwtdyhustvdysutd7shdtybdvtywhvtyhvthjsud3d',
       'ы': '8276tfsygvfdtrqt76yhuwtf576g8duhwvtf7d8svydfgusjibhdguywhigd7q',
       'э': 'rftgyuhbvcfx2dtr567t8yhinjbhgvcty678ydtwy9dguwf76t8dguiyuqdw7d',
       'ю': '2ushs9ihsudjisbuydhujiabydhuijdbyauhdwyudhuwdjiwduyquwdjwwdhuw',
       'я': '80bsydhwudhuduwdh7wyt5r4e3erfgvfdrtyghgdrgygvfdrftgydrq5t25s4d'
       }

def reverse(string): 
    string = "".join(reversed(string)) 
    return string

def badab(strong):
	badabum1 = len(strong)
	badabum2 = int(badabum1) / 2
	badabum3 = int(badabum2) + 1
	strong = strong[int(badabum2):int(badabum1)]+ strong[0:int(badabum2)]
	return strong

def superbadab(streng):
	der = len(streng)
	gab = int(der) - 10
	bad1 = int(gab) - 1
	streng = reverse(streng[int(gab):int(der)]) + streng[0:int(gab)]
	return streng

def minusovoisb(stryeng):
	badgh = len(stryeng)
	stryeng = stryeng[10:int(badgh)] + reverse(stryeng[0:10])
	return stryeng

def shifr(z):
	a = 0
	b = 1
	itog = ''
	for i in range(len(z)):
		itog = itog + t[str(z[a:b])]
		a += 1
		b += 1
	return itog

def deshifr(z):
	z = minusovoisb(z)
	z = badab(z)
	z = reverse(z)
	a = 0
	b = 62
	itog = ''
	for i in range(len(z)//62):
		a2 = 0
		b2 = 1
		for i in range(len(alfavit)):
			pp = alfavit[a2:b2]
			if t[pp] == z[a:b]:
				itog = itog + pp
			a2 += 1
			b2 += 1
		a += 62
		b += 62
	return itog

def del1():
	message_entry.delete(0, END)

def shifr1():
	a2672 = message_entry.get()
	a63737 = superbadab(badab(reverse(shifr(a2672))))
	del1()
	message_entry.insert(0, a63737)

def deshifr1():
	b26271 = message_entry.get()
	b2457 = deshifr(b26271)
	del1()
	message_entry.insert(0, b2457)

root = Tk()
root.title("shifrator")
root.geometry("400x300")

btn = Button(text='шифровать', command=shifr1)
btn.place(relx=.6, rely=.5)

btn2 = Button(text='дешифровать', command=deshifr1)
btn2.place(relx=.1, rely=.5)

message = StringVar()
 
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.4, anchor='c')

root.mainloop()