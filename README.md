# Proje Adı

Bu projede, ziyaretçi defteri uygulaması ve kullanıcı bilgilerini yöneten bir API bulunmaktadır.

## Kurulum Adımları

1. **Virtualenv Oluşturma:**
   
   Projenin bağımlılıklarını izole etmek için bir sanal ortam oluşturun:
   
   ``` virtualenv env ```


2. **Sanal Ortamı Aktifleştirme (Linux/Mac):**

Oluşturduğunuz sanal ortamı aktifleştirin:
   ``` source env/bin/activate ```

3. **Bağımlılıkların Kurulumu:**

Projenin gereksinimlerini yükleyin:
   ```pip install -r requirements.txt```

4. **Veritabanının Migrate Edilmesi:**

Django veritabanını oluşturmak için gerekli tabloları oluşturun:
   ```python manage.py makemigrations && python manage.py migrate```

5. **Geliştirme Sunucusunun Başlatılması:**

Django geliştirme sunucusunu başlatın:
   ```python manage.py runserver```

6. **API'yi Görüntüleme:**

Tarayıcınızda `http://localhost:8000/` adresine giderek API'yi kullanabilirsiniz.

7. **Testlerin Çalıştırılması:**

Projenin testlerini çalıştırmak için aşağıdaki komutu kullanabilirsiniz:
   ```python manage.py test api.test```

## API Kullanımı

- Guest Book Oluşturma:

`POST /api/guest-book/`

- Kullanıcı Bilgilerini Alma:

`GET /api/users/`


