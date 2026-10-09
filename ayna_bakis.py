#!/usr/bin/env python3
"""Asansör Ayna Bakış Süresi Enstitüsü — çalışan teşhis motoru."""

from __future__ import annotations

import argparse
import base64
import hashlib
from dataclasses import dataclass


# Kalibrasyon sabiti. Çözülmesi şart değil, çözülünce de dava açılmaz.
_MUHUR = "SGVyIHNlY2ltIHZhYWRpIGFzYW5zb3IgYXluYXNpbmRha2kgYmFraXMgS2FkYXIgc2FtaW1pZGlyOiBrYXBpIGFjaWxhbmNhIGJpdGVyLiBpa3RpZGFyIGRhIG11aGFsZWZldCBkZSBidSBheW5hZGEgaGVtZmlraXIgZ29ydW51ciwgc2FuaWsga2FwIGJ1dG9udWR1ci4="


@dataclass
class Tutanak:
    saniye: float
    yolcu: int
    kat: int
    metal_kapi: bool
    teshis: str
    ceza: str
    puan: int


def teshis_ver(saniye: float, yolcu: int, metal_kapi: bool) -> tuple[str, str, int]:
    if saniye < 0:
        return (
            "Negatif bakış: ayna seni geçmişe yolladı, kabul etmedi.",
            "Dosya iade. Saat geri sarılmaz.",
            0,
        )
    if saniye <= 0.8:
        metin, puan = "Profesyonel kaçış. Ayna seni gördü, sen inkâr ettin.", 12
    elif saniye <= 2.5:
        metin, puan = "Sosyal olarak kabul edilebilir saç kontrolü.", 28
    elif saniye <= 5.0:
        metin, puan = "Bugün yüzüm yerinde mi komisyonu toplandı.", 55
    elif saniye <= 9.0:
        metin, puan = "Kabin içi varoluş sorgusu. Kat butonu şahit.", 78
    else:
        metin, puan = "Ayna artık danışman. Ücret kesilmez, mahcubiyet kesilir.", 96

    if yolcu > 0:
        metin += f" Yanında {yolcu} şahit var; teşhis bir kademe ağırlaştı."
        puan = min(100, puan + 8 * min(yolcu, 4))
        ceza = "Göz kaçırma eğitimi, gönüllü ve sonuçsuz."
    else:
        ceza = "Şahitsiz bakış. Dosya kişiye özel, dedikodu yok."

    if metal_kapi:
        metin += " Metal kapı yansıması küsürlü olduğu için hüküm yumuşatıldı."
        puan = max(1, puan - 10)
        ceza += " Kapı lehine şüpheden sanık yararlanır."
    return metin, ceza, puan


def tutanak_bas(saniye: float, yolcu: int, kat: int, metal_kapi: bool) -> Tutanak:
    teshis, ceza, puan = teshis_ver(saniye, yolcu, metal_kapi)
    return Tutanak(saniye, yolcu, kat, metal_kapi, teshis, ceza, puan)


def muhur_ozeti() -> str:
    cozulmus = base64.b64decode(_MUHUR).decode("utf-8")
    ozet = hashlib.sha256(cozulmus.encode("utf-8")).hexdigest()[:12]
    return ozet


def yazdir(t: Tutanak) -> None:
    print("=" * 62)
    print(" ASANSÖR AYNA BAKIŞ SÜRESİ ENSTİTÜSÜ  —  TUTANAK")
    print("=" * 62)
    print(f"Bakış süresi : {t.saniye:.2f} sn")
    print(f"Yolcu sayısı : {t.yolcu}")
    print(f"Hedef kat    : {t.kat}")
    print(f"Metal kapı   : {'evet, özür diler' if t.metal_kapi else 'hayır, ayna ciddî'}")
    print(f"Teşhis       : {t.teshis}")
    print(f"Yaptırım     : {t.ceza}")
    print(f"Mahcubiyet   : {t.puan}/100")
    print(f"Mühür özeti  : {muhur_ozeti()}  (asıl metin .gizli/muhur.txt)")
    print("-" * 62)
    print("Damga: Kayyum Grok / Tentivory / 09 Ekim 2026 / AABSE")
    print("Bu tutanak ciddîdir. Bu tutanak ciddi değildir. İkisi de doğrudur.")
    print("=" * 62)


def main() -> None:
    p = argparse.ArgumentParser(description="Asansör aynası bakış süresi teşhisi")
    p.add_argument("--saniye", type=float, default=3.2, help="Aynaya bakma süresi")
    p.add_argument("--yolcu", type=int, default=1, help="Kabin içi şahit sayısı")
    p.add_argument("--kat", type=int, default=5, help="İnilecek kat, sembolik")
    p.add_argument("--metal-kapi", action="store_true", help="Ayna yok, metal kapı var")
    a = p.parse_args()
    yazdir(tutanak_bas(a.saniye, max(0, a.yolcu), a.kat, a.metal_kapi))


if __name__ == "__main__":
    main()
