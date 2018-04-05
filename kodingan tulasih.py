import texttable as tt
import getpass


def menu():
    print("==================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")

    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nkembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...........!!!")
        
def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x =[[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        nama.append(input("Masukan Nama: "))
        nim.append(input("Masukan Nim: "))
        tugas = int(input("Masukan Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("Nilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("Masukan UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("Tambah data [y/n]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['1','1','1','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'])
    print (tab.draw())

def pembayaran () :
    print ("\n==============================================")
    nama = input ("\nMasukan Nama : ")
    nim = input ("\nMasukan NIM: ")
    semester = input ("\nMasukan Semester : ")
    print ("\n\t---pilihan pembayaran---")
    print ("\t1. Pembayaran SPP")
    print ("\t2. Pembayaran UTS")
    print ("\t3. Pembayaran UAS")
    print ("\t4. Pembayaran SPP & UTS")
    print ("\t5. Pembayaran SPP & UAS")
    pilih = input ("\n\tSilahkan Pilih : ")
    if pilih == "1" :
        spp ()
    elif pilih == "2" :
        uts ()
    elif pilih == "3" :
        uas ()
    elif pilih == "4" :
        spp_uts ()
    elif pilih == "5" :
        spp_uas ()
    else :
        exit
        tanya ()

def spp() :
    bulan = int(input("\n\tjumlah bulan = "))
    bulan = float(bulan)
    total = 2000000 * bulan
    print ("=========================================")
    print ("\ttotal yang harus dibayar Rp. 2000000 * ",bulan," = Rp.",total)

def uas() :
    matkul_uas = int(input("\n\tjumlah mata kuliah = "))
    matkul_uas = float(matkul_uas)
    total = 2000000 * matkul_uas
    print ("=======================================")
    print ("\ttotal yang harus dibayar Rp. 2000000 * ",matkul_uas," = Rp.",byr_uas)

def uts () :
    matkul_uts = int(input("\n\tjumlah mata kuliah = "))
    matkul_uts = float(matkul_uts)
    total = 2000000 * matkul_uts
    print ("=======================================")
    print ("\ttotal yang harus dibayar Rp. 2000000 * ",matkul_uts," = Rp.",byr_uts)

def spp_uas() :
    bulan = int(input("\n\tjumlah bulan yang harus dibayar = "))
    matkul = int(input("\n\jumlah mata kuliah ="))
    matkul =float(matkul)
    bulan =float(bulan)
    total_spp = 2000000 * bulan
    byr_uas = 2000000 * matkul
    total = total_spp + byr_uas + 20000
    print ("\ttotal bayar spp Rp. 2000000 * ",bulan," = Rp. ", total_spp)
    print ("\ttotal bayar uas Rp. 20000 * ",matkul," = Rp. ", byr_uas)
    print ("\tbiaya tambahan server sebesar Rp. 20000")
    print ("========================================")
    print ("\ttotal yang harus dibayar", total)

def spp_uts() :
    bulan = int(input("\n\tjumlah bulan yang harus dibayar = "))
    matkul = int(input("\n\jumlah mata kuliah = "))
    bulan =float(bulan)
    matkul =float(matkul)      
    total_spp = 2000000 * bulan
    byr_uts = 2000000 * matkul
    total = total_spp + byr_uts + 20000
    print ("\ttotal bayar spp Rp. 2000000 * ",bulan," = Rp. ", total_spp)
    print ("\ttotal bayar uts Rp. 20000 * ",matkul," = Rp. ", byr_uts)
    print ("\tbiaya tambahan server sebesar Rp. 20000")
    print ("========================================")
    print ("\ttotal yang harus dibayar", total)


username = input("\nUsername : ")
password = getpass.getpass()
print ("=============================================")

if username == "novi" and password == "250?" :
           menu()

else :
    print ("maaf password atau username salah..!!!")
