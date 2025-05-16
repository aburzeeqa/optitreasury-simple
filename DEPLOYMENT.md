# تعليمات نشر تطبيق OptiTreasury

هذا الملف يحتوي على تعليمات تفصيلية لنشر تطبيق OptiTreasury على منصة استضافة خارجية.

## المتطلبات الأساسية

- Python 3.8 أو أحدث
- MySQL 5.7 أو أحدث
- مساحة استضافة تدعم تطبيقات Flask

## خطوات النشر

### 1. إعداد قاعدة البيانات MySQL

```sql
CREATE DATABASE optitreasury;
CREATE USER 'optiuser'@'localhost' IDENTIFIED BY 'optipassword';
GRANT ALL PRIVILEGES ON optitreasury.* TO 'optiuser'@'localhost';
FLUSH PRIVILEGES;
```

### 2. إعداد بيئة Python الافتراضية

```bash
# إنشاء بيئة افتراضية جديدة
python -m venv venv

# تفعيل البيئة الافتراضية
# في نظام Linux/Mac
source venv/bin/activate
# في نظام Windows
venv\Scripts\activate

# تثبيت التبعيات البرمجية
pip install -r requirements.txt
```

### 3. ضبط متغيرات البيئة

قم بإنشاء ملف `.env` في المجلد الرئيسي للتطبيق وأضف المتغيرات التالية:

```
DB_USERNAME=optiuser
DB_PASSWORD=optipassword
DB_HOST=localhost
DB_PORT=3306
DB_NAME=optitreasury
```

### 4. تشغيل التطبيق

#### للتطوير المحلي

```bash
# تشغيل التطبيق في وضع التطوير
python -m src.main
```

#### للإنتاج

يُفضل استخدام خادم WSGI مثل Gunicorn:

```bash
# تثبيت Gunicorn
pip install gunicorn

# تشغيل التطبيق باستخدام Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 'src.main:app'
```

## خيارات النشر على منصات استضافة خارجية

### 1. Heroku

1. قم بإنشاء حساب على [Heroku](https://heroku.com)
2. قم بتثبيت [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. أضف ملف `Procfile` بالمحتوى التالي:
   ```
   web: gunicorn src.main:app
   ```
4. قم بتنفيذ الأوامر التالية:
   ```bash
   heroku login
   heroku create optitreasury
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a optitreasury
   git push heroku master
   ```
5. قم بإعداد قاعدة بيانات MySQL:
   ```bash
   heroku addons:create cleardb:ignite
   ```
6. قم بضبط متغيرات البيئة:
   ```bash
   heroku config:set DB_USERNAME=xxx DB_PASSWORD=xxx DB_HOST=xxx DB_PORT=3306 DB_NAME=xxx
   ```

### 2. DigitalOcean App Platform

1. قم بإنشاء حساب على [DigitalOcean](https://digitalocean.com)
2. انتقل إلى App Platform وأنشئ تطبيقًا جديدًا
3. اختر GitHub أو GitLab كمصدر للكود
4. حدد المجلد الرئيسي للتطبيق
5. اختر Python كلغة البرمجة
6. حدد أمر البدء: `gunicorn src.main:app`
7. أضف متغيرات البيئة اللازمة
8. أنشئ قاعدة بيانات MySQL من خلال Managed Databases

### 3. AWS Elastic Beanstalk

1. قم بإنشاء حساب على [AWS](https://aws.amazon.com)
2. قم بتثبيت [AWS CLI](https://aws.amazon.com/cli/)
3. أضف ملف `Procfile` بالمحتوى التالي:
   ```
   web: gunicorn src.main:app
   ```
4. أضف ملف `.ebignore` لتجاهل المجلدات غير الضرورية
5. قم بتنفيذ الأوامر التالية:
   ```bash
   pip install awsebcli
   eb init
   eb create optitreasury-env
   eb deploy
   ```
6. قم بإعداد قاعدة بيانات MySQL من خلال RDS

## ملاحظات هامة

- تأكد من تغيير كلمات المرور وبيانات الاتصال بقاعدة البيانات في بيئة الإنتاج
- قم بتعطيل وضع التصحيح (Debug Mode) في بيئة الإنتاج
- تأكد من تكوين HTTPS لتأمين الاتصالات
- قم بإعداد نظام نسخ احتياطي لقاعدة البيانات

## الدعم والمساعدة

إذا واجهتك أي مشكلة أثناء النشر، يرجى الرجوع إلى وثائق المنصة المستضيفة أو التواصل مع فريق الدعم الفني.
