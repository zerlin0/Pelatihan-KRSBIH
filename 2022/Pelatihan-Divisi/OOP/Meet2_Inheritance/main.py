class Manusia():
    def __init__(self):
        self.nama = ""
        self.usia = ""

    # Method
    def setNama(self, nama):
        self.nama = nama

    def setUsia(self, usia):
        self.usia = usia

    def infoNama(self):
        print("Nama Saya : ", self.nama)

    def infoUsia(self):
        print("Usia Saya : ", self.usia)

class Mahasiswa(Manusia):
    def __init__(self, nama, usia, kampus, jurusan, prodi):
        super(Mahasiswa, self).__init__()

        self.setNama(nama)
        self.setUsia(usia)

        self.kampus = kampus
        self.jurusan = jurusan
        self.prodi = prodi

    def infoKampus(self):
        print("Saya Kuliah Di : {} dan Saya Bangga".format(self.kampus))

class Pelajar(Manusia):
    def __init__(self, nama, usia, sekolah, kelas):
        super(Pelajar, self).__init__()

        self.setNama(nama)
        self.setUsia(usia)

        self.sekolah = sekolah
        self.kelas = kelas

    def infoSekolah(self):
        print("Saya({}) Sekolah Di : {} dan Saya Bangga".format(self.nama, self.sekolah))


class Karyawan(Manusia):
    def __init__(self):
        super(Karyawan, self).__init__()
        self.posisi = ""
        self.tempat_kerja = ""

def main():
    dedi = Mahasiswa("Dedi", 30, "Polinema", "TE", "D3 TE")
    iwan = Pelajar("Iwan ", 40, "SMK 1 Malang ", "12")

    dedi.infoKampus()
    iwan.infoSekolah()


if __name__ == '__main__':
    main()
