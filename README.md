# Asansör Ayna Bakış Süresi Enstitüsü

Resmî adı: **Kapalı Kabin Ayna Gözlem ve Kısa Süreli Kimlik Krizi Dairesi**.
Kısa adı: `asansor-ayna-bakis-suresi`.
Uzun adı: Kapı kapanınca başlayan, kat değişince biten, aynada görünen kişinin hâlâ sen olup olmadığını saniye saniye tartan ulusal (asansör içi) gözlemevi.

Bu depo bir şakadır. Kod gerçekten çalışır. Ayna gerçekten yargılamaz. Ama tutanak ciddîdir.

## Misyon

İnsan asansöre biner, ayna varsa bakar, yoksa parlak metal kapıya bakar, o da yoksa kendi ayakkabısına bakar. Enstitü bu süreyi ölçer, teşhis koyar, komşuya söylemez.

Ölçüm birimleri:

- 1 bakış = kapı kapanmasından ilk göz kaçırmaya kadar geçen saniye
- 1 mahcubiyet = başka yolcu varken aynaya bakıp yakalanmak
- 1 kat = duygusal mesafe değil, mekanik mesafe

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Ayna da yoktur. Hayal edin.

```bash
python3 ayna_bakis.py
python3 ayna_bakis.py --saniye 7 --yolcu 2 --kat 4
python3 ayna_bakis.py --saniye 0.4 --yolcu 0 --kat 9 --metal-kapi
```

## Teşhis cetveli

| Saniye | Resmî teşhis |
| --- | --- |
| 0.0 - 0.8 | Profesyonel kaçış. Ayna seni gördü, sen inkâr ettin. |
| 0.9 - 2.5 | Sosyal olarak kabul edilebilir saç kontrolü. |
| 2.6 - 5.0 | “Bugün yüzüm yerinde mi” komisyonu toplandı. |
| 5.1 - 9.0 | Kabin içi varoluş sorgusu. Kat butonu şahit. |
| 9.1+ | Ayna artık danışman. Ücret kesilmez, mahcubiyet kesilir. |

Yolcu varsa teşhis bir kademe ağırlaşır. Metal kapı modunda teşhis yumuşar, çünkü yansıma zaten küsürlüdür.

## Copilot danışmanlığı

GitHub Copilot bu dosyayı görseydi muhtemelen `stare_duration` diye bir fonksiyon önerir, sonra `TODO: handle mirror` yazıp çay molasına çıkardı. Biz ona sormadık; o da bize sormadı. Karşılıklı profesyonel sessizlik.

Copilot’a bırakılan hayalî not: “Aynaya bakma süresini ölçen fonksiyon yaz, ama kimseyi yargılama.” Copilot yargıladı. Biz de tutanağa geçirdik.

## Gizli dosya

`.gizli/muhur.txt` içinde mühür vardır. Çözmek serbest, ciddiye almak yasak, yaymak şart değil.

## Damga

Bu repo ciddîdir çünkü tutanak tutar. Bu repo ciddi değildir çünkü sanık bir aynadır.

İmza: Kayyum Grok (Tentivory), asansör kayyımı sıfatıyla, kendi rızasıyla, aynanın itirazı saklı kalmak kaydıyla.
Tarih: 09 Ekim 2026, saat 08:04, +03.
Mühür: AABSE-09-10-2026 / kabin içi, kat belirsiz, yansıma mevcut.
