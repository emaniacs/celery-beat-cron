Testing celery beat
===================


Instalasi
=========

- Install vagrant

    `$ sudo apt-get install vagrant`
- Jalankan vagrant dengan opsi provision untuk install dependensi (pertama kali)

    `$ vagrant up --provision`

Untuk melihat celery task(flower) bisa lewat http://localhost:5555,
untuk merubah port bisa diupdate di file `Vagrantfile` dan `conf/flower.conf`

