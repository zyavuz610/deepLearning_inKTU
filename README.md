Bu depo, Karadeniz Teknik Üniversitesi'nde yapay zeka ile ilgili yaptığım çalışmalarla ilgili kodları paylaştığım platformdur. 

---
# Makine Öğrenmesi

Yapay Zeka, bu günlerde çok popüler bir konu veya çalışma alanıdır. Bu konuya hakim olmak ve arka planda neler olup bittiğini anlamak için aşağıdaki konuların sırasını takip etmenizi tavsiye ederim. 

**Lineer Regresyon**: Doğrusal regresyon, bir regresyon değeri hesaplamak için kullanılır. Tek değişkenli ve çok değişkenli versiyonları vardır. Temel olarak, ikisi arasında çok fazla fark yoktur. 

**Lojistik Resresyon**: İkili sınıflandırma için kullanılan bir regresyon türüdür. Doğrusal regresyona benzer şekilde çalışır. Temel fark, mantıksal regresyondaki çıktının aynı zamanda bir transfer fonksiyonuna (genellikle sigmoid) verilmesidir. Bu sayede lineer bir değer yerine 0 veya 1'e yakın değerler elde edilir. 0,5'lik bir eşik kullanılarak, sonuç 0 veya 1 olarak ikili dosyaya dönüştürülebilir. 

**Sinir Ağı**: Tek katmanlı veya çok katmanlı (yani farklı mimarilere sahip) sinir ağları aslında nöron dediğimiz birçok sinir hücresinden oluşur. Her bir nöron tek başına değerlendirildiğinde lojistik regresyon gerçekleştiren bir sınıflandırıcı olarak düşünülebilir. Derin öğrenme keşfedildikten sonra, bu tür ağlara sığ sinir ağları da denir. 

**Derin Öğrenme**: Yapay sinir ağlarının katman sayısı artırılmış, farklı mimariler ve yaklaşımlar kullanan özel sinir ağı modelleridir. Bunlara Derin Sinir Ağları da denir.

# Derin Öğrenmeye Giriş
Makineyle öğrenme yıllardır kullanılan bir yöntem olmasına rağmen, **iki yeni trend** makineyle öğrenmenin yaygın bir şekilde kullanılmasına yol açmıştır: 

1. çok büyük miktarlarda eğitim verisi ile 
2. GPU hesaplama ile elde edilen güçlü ve verimli paralel hesaplama.
 
Bunların sonucu olarak da **yeni model ve algoritmalar** geliştirildi.

Grafik işlemciler (GPU) klasik işlemcilere (CPU) göre 10-100 kat performanslı çalışmaktadırlar. Bu nedenle veri bilimciler büyük verileri işlerken GPU kullanmaktadırlar.
Derin öğrenmenin temeli, sığ yapay sinir ağlarının **katman sayısını arttırarak** ve **öğrenme için yeni yaklaşım ve optimizason teknikleri kullanarak** derin (evrişimsel) sinir ağları halini alması ile atılmıştır.

---
[_English draft_](https://github.com/zyavuz610/deepLearning_inKTU/blob/master/readme_eng.md)

