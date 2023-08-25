import pyinputplus as pyip
import math
from datetime import date
import calendar
import tabulate
listMobil =[
    {
        'Brand' : 'Toyota',
        'Tipe' : 'Innova',
        'PlatNomor' : 'B123ABC',
        'Harga/malam' : 500000,
        'Tersedia' : 'Ya'
    },
     {
        'Brand' : 'Toyota',
        'Tipe' : 'Avanza',
        'PlatNomor' : 'B123DEF',
        'Harga/malam' : 475000,
        'Tersedia' : 'Tidak'
    },
     {
        'Brand' : 'Honda',
        'Tipe' : 'Mobilio',
        'PlatNomor' : 'B456ABC',
        'Harga/malam' : 470000,
        'Tersedia' : 'Ya'
    },
    {
        'Brand' : 'Honda',
        'Tipe' : 'Brio   ',
        'PlatNomor' : 'B456DEF',
        'Harga/malam' : 385000,
        'Tersedia' : 'Ya'
    },
    {
        'Brand' : 'Toyota',
        'Tipe' : 'Agya   ',
        'PlatNomor' : 'B789ABC',
        'Harga/malam' : 377000,
        'Tersedia' : 'Ya'
    }
]
listUser=[{'username' : 'Admin',
           'privileges': 'Adm',
           'password' : 'Admin1234'},
           {'username' : 'Manager',
           'privileges': 'SUP',
           'password' : 'Pass1234!'}]
brand = ['Toyota','Honda']
listNopol = []
tempBin = []
usernameG = [{'username':'Default',
              'privileges':'Default'}]
runningNumber=0
ctrlogin = 1
sorting = 0
harga = 0
def if_exist(listcheck):
    if len(listcheck) != len(set(listcheck)):
        return True
    else:
        return False
def grabnoPol(check):
    if check != 'Proses Booking' :
        for i in range (len(listMobil)) :
            listNopol.append(listMobil[i]['PlatNomor'])
    else :
        for i in range (len(listMobil)) :
            if listMobil[i]['Tersedia'] == 'Ya' :
                listNopol.append(listMobil[i]['PlatNomor'])
            else :
                continue        
def readMobil(any,sorting,harga) :
    orderlist=[]
    if any == 'Proses Booking' :
        while True :
            for i in range(len(listMobil)) :
                if listMobil[i]['Tersedia'] == 'Ya' :
                    orderlist.append({
                        'Brand' : listMobil[i]['Brand'],
                        'Tipe' : listMobil[i]['Tipe'],
                        'PlatNomor' : listMobil[i]['PlatNomor'],
                        'Harga/malam' : listMobil[i]['Harga/malam'],
                        })
                else :
                    continue
            orderlist=sorted(orderlist, key=lambda d: d['PlatNomor'])
            print('===========List Mobil Auto Rental===========')
            header = orderlist[0].keys()
            rows =  [x.values() for x in orderlist]
            print(tabulate.tabulate(rows, header,tablefmt='rst'))
            orderlist.clear()
            break
    else :
        print('=================List Mobil Auto Rental=================')
        if sorting == 'Brand' :
            orderlist=sorted(listMobil, key=lambda d: d['Brand'])
            header = orderlist[0].keys()
            rows =  [x.values() for x in orderlist]
            print(tabulate.tabulate(rows, header,tablefmt='rst'))
            orderlist.clear()
        elif sorting == 'Harga' :
            if harga == 'Tertinggi' :
                orderlist=sorted(listMobil, key=lambda d: d['Harga/malam'],reverse=True)
                header = orderlist[0].keys()
                rows =  [x.values() for x in orderlist]
                print(tabulate.tabulate(rows, header,tablefmt='rst'))
                orderlist.clear()
            else : 
                orderlist=sorted(listMobil, key=lambda d: d['Harga/malam'],reverse=False)
                header = orderlist[0].keys()
                rows =  [x.values() for x in orderlist]
                print(tabulate.tabulate(rows, header,tablefmt='rst'))
                orderlist.clear()
        else :
            orderlist=sorted(listMobil, key=lambda d: d['PlatNomor'])
            header = orderlist[0].keys()
            rows =  [x.values() for x in orderlist]
            print(tabulate.tabulate(rows, header,tablefmt='rst'))
            orderlist.clear()
def orderDraft(anylist,disc,x,y) :
    subtotal= 0
    tglPesan = date.today()
    print('Nama Pemesan: {}\t\t    Nomor Dokumen : ORD|{}|{}'.format(x,calendar.month_name[tglPesan.month],y+1))
    print('                   \t\t    Tanggal Pemesanan :{}\n'.format(tglPesan))
    print('\nDetail Pemesanan:')
    header = anylist[0].keys()
    rows =  [x.values() for x in anylist]
    print(tabulate.tabulate(rows, header,tablefmt='rst'))
    for i in range (len(anylist)) :
        subtotal+= anylist[i]['jml Hari']*anylist[i]['Harga/malam']
    print('\nJumlah mobil \t:{} unit'.format(len(anylist)))
    print('Subtotal \t:IDR {}'.format(subtotal))
    if disc == 0 :
        disc +=0
    else :
        print('Discount \t:IDR ({})'.format(disc))
    print('Tax(10%) \t:IDR {}'.format(int(math.floor(subtotal*10/100))))
    print('Grand Total\t:IDR {}\n'.format(int(math.floor(subtotal-disc)*1.1)))  
def deletemobil(x) :
    # grabnoPol(mainMenu)
    while True :
        getIndex = next((i for (i, d) in enumerate(listMobil) if d['PlatNomor'] == x), None)
        if getIndex is None :
            print('Nopol tidak ditemukan')
            continue
        else :
            tempBin.append({
                            'Brand' : listMobil[getIndex]['Brand'],
                            'Tipe' : listMobil[getIndex]['Tipe'],
                            'PlatNomor' : listMobil[getIndex]['PlatNomor'],
                            'Harga/malam' : listMobil[getIndex]['Harga/malam'],
                            'Tersedia' : listMobil[getIndex]['Tersedia']
                            })
            listMobil.remove(listMobil[getIndex])
        break
def addItem() :
    pilih1=pyip.inputMenu(['Tambah Brand Baru','Tambah mobil baru'],prompt='Pilih salah 1\n',numbered=True)
    if pilih1 == 'Tambah mobil baru' :
        readMobil(mainMenu,sorting,harga)
        grabnoPol(mainMenu)
        while True:
            brandMobil = pyip.inputMenu(brand,numbered=True,prompt='Pilih brand Mobil\n')
            tipeMobil = input('Masukan Tipe Mobil :').title()
            noPolMobil = pyip.inputRegex(r'[a-zA-Z]{1,2}[0-9]{3}[A-Za-z]*',prompt='Masukan PlatNomor :').upper()
            listNopol.append(noPolMobil)
            if if_exist(listNopol) :
                    print('Nopol {} sudah ada dalam sistem, silahkan masukan value lain'.format(noPolMobil))
                    listNopol.pop(-1)
                    continue
            else :
                hargaMobil = pyip.inputInt('Masukan harga/malam :')
                tersedia = pyip.inputMenu(['Ya','Tidak'],numbered= True,prompt='Tersedia?\n')
                listMobil.append({
                            'Brand' : brandMobil,
                            'Tipe' : tipeMobil,
                            'PlatNomor' : noPolMobil,
                            'Harga/malam' : hargaMobil,
                            'Tersedia' : tersedia
                            })
            pilih=pyip.inputMenu(['Kembali','Lanjut(Add)'],prompt='Mobil dengan No-pol {} berhasil ditambahkan,Lanjut/Kembali?\n'.format(noPolMobil),numbered=True)
            if pilih == 'Kembali' :
                print('Terima kasih, anda akan kembali ke main menu')
                listNopol.clear()
                break
            else :
                continue
    else :
        while True :
            brandAdd = input('Masukan nama brand :')
            brand.append(brandAdd)
            if if_exist(brand) :
                print('Brand {} sudah ada silahkan input brand lain'.format(brandAdd))
                brand.pop(-1)
                continue
            else :
                pilih=pyip.inputMenu(['Lanjut','Kembali'],prompt='{} berhasil ditambahkan,Lanjut/Kembali?\n'.format(brandAdd),numbered=True)
                if pilih == 'Kembali' :
                    print('Terima kasih, anda akan kembali ke main menu')
                    listNopol.clear()
                    break
                else :
                    continue
print('---Selamat Datang di Purwha Auto Car Owner program---')
print(' Membuat booking mobil menjadi lebih mudah dan cepat')
print('vr.1.0\t\t\t\t\t©Purwadhika\n')
while True :
    if ctrlogin <=3 :
        username=pyip.inputStr('Percobaan masuk ke-{}\nUsername :'.format(ctrlogin)).title()
        password=pyip.inputPassword('Password :')
        getIndex = next((i for (i, d) in enumerate(listUser) if d['username'] == username), 0)
        if listUser[getIndex]['username'] == username and listUser[getIndex]['password']==password :
            usernameG[0].update({'username': listUser[getIndex]['username']})
            usernameG[0].update({'privileges': listUser[getIndex]['privileges']})
            print('Berhasil Login')
            while True :
                mainMenu=pyip.inputMenu(['Menampilkan Item Master Data','Tambah Item Baru','Update Item Master Data',
                                        'Delete Item Master data','Restore deleted item','Proses Booking','Exit'],numbered=True,prompt='Pilih menu :\n')
                if mainMenu == 'Tambah Item Baru' :
                    addItem()
                elif mainMenu == 'Menampilkan Item Master Data' :
                    while True :
                        readMobil(mainMenu,sorting,harga)
                        menuRead = pyip.inputMenu(['Brand','Nopol','Harga'],prompt='urutkan data dengan:\n',numbered=True)
                        if menuRead == 'Brand' :
                            readMobil(mainMenu,menuRead,harga)
                        elif menuRead == 'Nopol' :
                            readMobil(mainMenu,menuRead,harga)
                        else :
                            harga=pyip.inputMenu(['Tertinggi','Terendah'],prompt='sort harga dari:\n',numbered=True)
                            readMobil(mainMenu,menuRead,harga)
                        pilih=pyip.inputMenu(['Kembali','Lanjut(read)'],prompt='Anda ingin kembali ke main menu?\n',numbered=True)
                        if pilih == 'Kembali' :
                            print('Terima kasih, anda akan kembali ke main menu')
                            break
                        else :
                            continue
                elif mainMenu == 'Update Item Master Data' :
                    grabnoPol(mainMenu)
                    while True :
                        readMobil(mainMenu,sorting,harga)
                        updateChoice=pyip.inputMenu(['Harga/Malam','Tersedia','Semua'],numbered=True,prompt='Pilih content yang ingin di update :\n')
                        readMobil(mainMenu,sorting,harga)
                        noPol = pyip.inputMenu(prompt='Pilih noPol untuk di update :\n',choices=listNopol,numbered=True)
                        if updateChoice == 'Harga/Malam' : 
                            getIndex = next((i for (i, d) in enumerate(listMobil) if d['PlatNomor'] == noPol), None) 
                            if listMobil[getIndex]['PlatNomor'] == noPol :
                                hargaMobil = pyip.inputInt('update Harga/Malam :')
                                listMobil[getIndex].update({'Harga/malam':hargaMobil})
                            else :
                                continue
                        elif updateChoice == 'Tersedia' :
                            getIndex = next((i for (i, d) in enumerate(listMobil) if d['PlatNomor'] == noPol), None) 
                            if listMobil[getIndex]['PlatNomor'] == noPol :
                                tersedia = pyip.inputMenu(['Ya','Tidak'],prompt='Tersedia?\n',numbered= True)
                                listMobil[getIndex].update({'Tersedia':tersedia})
                            else :
                                continue
                        else :
                            getIndex = next((i for (i, d) in enumerate(listMobil) if d['PlatNomor'] == noPol), None) 
                            if listMobil[getIndex]['PlatNomor'] == noPol :
                                hargaMobil = pyip.inputInt('update Harga/Malam :')
                                tersedia = pyip.inputMenu(['Ya','Tidak'],prompt='Tersedia?\n',numbered= True)
                                listMobil[getIndex].update({'Tersedia':tersedia})
                                listMobil[getIndex].update({'Harga/malam':hargaMobil,'Tersedia':tersedia})
                            else :
                                continue
                        pilih=pyip.inputMenu(['Kembali','Lanjut(update)'],prompt='Anda ingin kembali ke main menu?\n',numbered=True)
                        if pilih == 'Kembali' :
                            print('Terima kasih, anda akan kembali ke main menu')
                            listNopol.clear()
                            break
                        else :
                            continue
                elif mainMenu == 'Delete Item Master data' :
                    while True :
                        ctr=1
                        if usernameG[0]['privileges'] == 'SUP' :
                            grabnoPol(mainMenu)
                            noPol = pyip.inputRegex(r'[a-zA-Z]{1,2}[0-9]{3}[a-zA-Z]*',prompt='Pilih nopol yang ingin didelete {}:'.format(listNopol)).upper()
                            deletemobil(noPol)
                            pilih=pyip.inputMenu(choices=['Kembali','Lanjut(Delete)'],numbered=True)
                            if pilih == 'Kembali' :
                                print('Berikut list item yang anda delete :')
                                header = tempBin[0].keys()
                                rows =  [x.values() for x in tempBin]
                                print(tabulate.tabulate(rows, header,tablefmt='rst'))
                                listNopol.clear()
                                break
                            else :
                                listNopol.clear()
                                header = tempBin[0].keys()
                                rows =  [x.values() for x in tempBin]
                                print(tabulate.tabulate(rows, header,tablefmt='rst'))
                                continue
                        else :
                            if ctr<=3 :
                                password=pyip.inputPassword('Butuh Otorisasi Manager,percobaan ke-{}:'.format(ctr))
                                if password == listUser[1]['password'] :
                                    grabnoPol(mainMenu)
                                    noPol = pyip.inputRegex(r'[a-zA-Z]{1,2}[0-9]{3}[a-zA-Z]*',prompt='Pilih nopol yang ingin didelete {}:'.format(listNopol)).upper()
                                    deletemobil(noPol)
                                    pilih=pyip.inputMenu(choices=['Kembali','Lanjut(Delete)'],numbered=True)
                                    if pilih == 'Kembali' :
                                        print('Berikut list item yang anda delete :')
                                        header = tempBin[0].keys()
                                        rows =  [x.values() for x in tempBin]
                                        print(tabulate.tabulate(rows, header,tablefmt='rst'))
                                        listNopol.clear()
                                        break
                                    else :
                                        listNopol.clear()
                                        header = tempBin[0].keys()
                                        rows =  [x.values() for x in tempBin]
                                        print(tabulate.tabulate(rows, header,tablefmt='rst'))
                                        continue
                                else :
                                    print('Password salah')
                                    ctr +=1
                                    continue
                            else :
                                print('Terlalu banyak kesalahan terminate program')
                                quit()
                elif mainMenu == 'Proses Booking':
                    counter = 1
                    ordermobil= []
                    jmlHr = 0
                    disc = 0
                    nama=pyip.inputStr(prompt='masukkan Nama Pemesan: ', blockRegexes=[(r"[0-9]")])
                    while True :
                        readMobil(mainMenu,sorting,harga)
                        grabnoPol(mainMenu)
                        if len(listNopol) != 0 :
                            orderCheck=pyip.inputMenu(['Ya','Tidak'],prompt='Mulai order mobil ke-{}\n'.format(counter),numbered=True)
                            if orderCheck == 'Ya' and len(listNopol) > 0 :
                                while True :
                                    nopolb = pyip.inputRegex(r'[a-zA-Z]{1,2}\d{3}[a-zA-Z]*',prompt='Input noPol mobil yang ingin dibooking {}:\n'.format(listNopol)).upper()
                                    if nopolb not in listNopol :
                                        print('Plat nomor tidak ditemukan')
                                        continue
                                    else :
                                        break
                                while True :
                                    while True :
                                        dari=pyip.inputDate(prompt='Dari tanggal [mm/dd/yyyy]:')
                                        if dari <date.today() :
                                            print('Masukan tanggal lebih besar dari {}'.format(date.today()))
                                        else :
                                            break
                                    sampai=pyip.inputDate(prompt='Sampai tanggal [mm/dd/yyyy]:')
                                    if sampai > dari :
                                        if str(sampai-dari) == '1 day, 0:00:00' :
                                            bookingb=int(str(sampai-dari).replace(' day, 0:00:00',''))
                                        else :
                                            bookingb=int(str(sampai-dari).replace(' days, 0:00:00',''))
                                        getIndex = next((i for (i, d) in enumerate(listMobil) if d['PlatNomor'] == nopolb), 0)
                                        if nopolb == listMobil[getIndex]['PlatNomor'] :
                                            ordermobil.append({
                                                'No' : counter,
                                                'Brand' : listMobil[getIndex]['Brand'],
                                                'Tipe' : listMobil[getIndex]['Tipe'],
                                                'PlatNomor' : listMobil[getIndex]['PlatNomor'],
                                                'Harga/malam' : listMobil[getIndex]['Harga/malam'],
                                                'jml Hari' : bookingb,
                                                'Total' : listMobil[getIndex]['Harga/malam']*bookingb
                                            })
                                            listMobil[getIndex].update({'Tersedia' : 'Tidak'})
                                            counter+=1
                                            listNopol.clear()
                                        else : 
                                            continue
                                        break
                                    else :
                                        print('Tanggal sampai tidak boleh lebih kecil dari tanggal dari')
                                        continue
                            elif orderCheck == 'Tidak' and len(ordermobil) > 0:
                                print('Terima kasih, berikut detail pemesanan anda\n')
                                orderDraft(ordermobil,disc,nama,runningNumber)
                                discConf=pyip.inputMenu(choices=['Ya','Tidak'],prompt='Tambahkan discount?:\n',numbered=True)
                                if discConf == 'Ya' :
                                    if usernameG[0]['privileges'] == 'SUP' :
                                        disc1=pyip.inputInt('Masukan nominal discount :')
                                        orderDraft(ordermobil,disc1,nama,runningNumber)
                                        print('\nTerima kasih pesanan anda telah di finalisasi')
                                        ordermobil.clear()
                                        listNopol.clear()
                                        runningNumber+=1
                                    else :
                                        while True :
                                            ctr =1
                                            if ctr<=3 :
                                                password=pyip.inputPassword('Butuh Otorisasi Manager,percobaan ke-{}:'.format(ctr))
                                                if password == listUser[1]['password'] :
                                                    disc1=pyip.inputInt('Masukan nominal discount :')
                                                    orderDraft(ordermobil,disc1,nama,runningNumber)
                                                    print('\nTerima kasih pesanan anda telah di finalisasi')
                                                    ordermobil.clear()
                                                    listNopol.clear()
                                                    runningNumber+=1
                                                    break
                                                else :
                                                    print('Password salah')
                                                    ctr +=1
                                                    continue
                                            else :
                                                print('Terlalu banyak kesalahan terminate program')
                                                quit()   
                                else :
                                    print('\nTerima kasih pesanan anda telah di finalisasi')
                                    orderDraft(ordermobil,disc,nama,runningNumber)
                                    runningNumber+=1
                                    listNopol.clear()
                                    ordermobil.clear()
                                break
                            elif orderCheck == 'Ya' and len(listNopol) == 0 :
                                print('Tidak ada lagi mobil yang tersedia, berikut detail pemesanan anda\n')
                                orderDraft(ordermobil,disc,nama,runningNumber)
                                discConf=pyip.inputMenu(['Ya','Tidak'],prompt='Tambahkan discount?:\n',numbered=True)
                                if discConf == 'Ya' :
                                    if usernameG[0]['privileges'] == 'SUP' :
                                        disc1=pyip.inputInt('Masukan nominal discount :')
                                        orderDraft(ordermobil,disc1,nama,runningNumber)
                                        print('\nTerima kasih pesanan anda telah di finalisasi')
                                        ordermobil.clear()
                                        listNopol.clear()
                                        runningNumber+=1
                                    else :
                                        while True :
                                            ctr =1
                                            if ctr<=3 :
                                                password=pyip.inputPassword('Butuh Otorisasi Manager,percobaan ke-{}:'.format(ctr))
                                                if password == listUser[1]['password'] :
                                                    disc1=pyip.inputInt('Masukan nominal discount :')
                                                    print('\nTerima kasih pesanan anda telah di finalisasi')
                                                    orderDraft(ordermobil,disc1,nama,runningNumber)
                                                    ordermobil.clear()
                                                    runningNumber+=1
                                                    listNopol.clear()
                                                    break
                                                else :
                                                    print('Password salah')
                                                    ctr +=1
                                                    continue
                                            else :
                                                print('Terlalu banyak kesalahan terminate program')
                                                quit()
                                else :
                                    print('\nTerima kasih pesanan anda telah di finalisasi')
                                    orderDraft(ordermobil,disc,nama,runningNumber)
                                    ordermobil.clear()
                                    runningNumber+=1
                                    listNopol.clear()
                                break
                        else :
                            print('Tidak ada mobil yang tersedia,Silahkan tambahkan mobil baru')
                            break
                elif mainMenu == 'Restore deleted item' :
                    if len(tempBin) >0 :
                        ctr = 1
                        while True :
                            if ctr<=3 :
                                password=pyip.inputPassword('Butuh Otorisasi Manager,percobaan ke-{}:'.format(ctr))
                                if password == listUser[1]['password'] : 
                                    header = tempBin[0].keys()
                                    rows =  [x.values() for x in tempBin]
                                    print(tabulate.tabulate(rows, header,tablefmt='rst'))
                                    for i in range(len(tempBin)) :
                                        listMobil.append(tempBin[i])
                                    print('Data mobil sudah dikembalikan')
                                    tempBin.clear()
                                    break
                                else :
                                    print('Password salah')
                                    ctr +=1
                                    continue
                            else :
                                print('Terlalu banyak kesalahan, program dipaksa berhenti')
                                quit()
                    else :
                        print('Tidak ada data dalam bin')
                else:
                    pilih=pyip.inputMenu(['Ya','Tidak'],prompt='Anda yakin?\n',numbered=True)
                    if pilih == 'Ya' :
                        print('Program akan dimatikan, Terima kasih {} dan sampai jumpa'.format(usernameG[0]['username']))
                        break
                    else :
                        continue
            break
        else:
            print('Username atau password salah')
            ctrlogin+=1
            continue
    else :
        print('Terlalu banyak kesalahan, program dipaksa berhenti')
        break