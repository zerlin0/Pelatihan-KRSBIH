class Mobil():
    def __init__(self, pemilik, merk, plat, seri):
        self.pemilik = pemilik
        self.merk = str(merk)
        self.plat = plat
        self.seri = seri

    def infoLengkap(self):
        print("=" * 40)
        print("Pemilik Mobil : {} \n"
              "Merk Mobil: {} \n"
              "Seri Mobil: {} \n"
              "Plat Mobil: {}".format(self.pemilik, self.merk, self.seri, self.plat))
        print("=" * 40)

    def infoSeriMobil(self):
        print("Seri Mobil : " + self.seri)

    def infoPlatMobil(self):
        print("Plat Mobil-nya {} : {}".format(self.pemilik, self.plat))

class SepedaMotor():
    def __init__(self, pemilik: str, merk: str, plat: str, seri: str):
        """
        Clas Untuk Objek Sepeda Motor BRO

        :param pemilik: Deskripsi Pemilik SepedaMotor
        :param merk:
        :param plat:
        :param seri:
        """

        self.pemilik = pemilik
        self.merk = merk
        self.plat = plat
        self.seri = seri

    def infoLengkap(self):
        print("=" * 40)
        print("Pemilik Sepeda Motor : {} \n"
              "Merk Sepeda Motor: {} \n"
              "Seri Sepeda Motor: {} \n"
              "Plat Sepeda Motor: {}".format(self.pemilik, self.merk, self.seri, self.plat))
        print("=" * 40)

    def infoSeriMobil(self):
        print("Seri Sepeda Motor : " + self.seri)

    def infoPlatMobil(self):
        print("Plat Sepeda Motor-nya {} : {}".format(self.pemilik, self.plat))


def main():
    # mobil => merk plat seri_mobil status_lampu
    mobilDedi = Mobil("Dedi", "Toyota", "N 1234 P", "Avanza")
    mobilIwan = Mobil("Iwan", "Honda", "N 4211 P", "Avanza 2142")
    mobilFirza = Mobil("Firza", 2412415, "N 55151 P", "Avanza 999")

    mobilFirza.infoLengkap()
    sepedaMotor_Tyo = SepedaMotor("Mas Tyo", "Honda", "A 2221 P", "Supra X")

    # spd_mtr1 = SepedaMotor()

    sepedaMotor_Tyo.infoLengkap()

if __name__ == '__main__':
    main()
