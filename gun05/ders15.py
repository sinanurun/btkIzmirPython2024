class Fatura():
    baslik = "Halil Pazarlama"
    odeme = True
    icerik = {}
    def __init__(self, m_adi, v_no, tarih):
        self.m_adi = m_adi
        self.v_no = v_no
        self.tarih = tarih
        self.tutar = 0

    def __str__(self):
        return self.m_adi+" adlı müşterinin faturası"


musteri = Fatura("hamza","1452","bugün")
print(musteri)
