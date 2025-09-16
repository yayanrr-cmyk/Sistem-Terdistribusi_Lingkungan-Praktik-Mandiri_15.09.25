Berikut ini dokumentasi GitHub untuk repo **Sistem-Terdistribusi\_Lingkungan-Praktik-Mandiri\_15.09.25** dalam format *Markdown*. Kamu bisa pakai ini sebagai isi file `README.md` di repo kamu atau laporan.

---

```markdown
# Eksplorasi Protokol Sistem Terdistribusi

Repo ini adalah praktik eksplorasi beberapa protokol komunikasi yang digunakan dalam sistem terdistribusi: **MQTT, ZMQ, TCP, REST** — beserta protokol/pola lainnya seperti CORBA, RPC, SOAP, Sync, Oneway, Upcall.  

---

## 📁 Struktur Repo

```

.
├── CORBA/
├── MQTT/
├── REST/
├── RPC/
├── Reqresp/
├── SOAP/
├── Sync/
├── ZMQ/
├── code\_process/
├── compose/
├── oneway/
├── upcall/
├── LICENSE
├── README.md
├── logMQTT.pcap
├── logTCP.pcap
├── logzmqclientserver.pcap
├── logzmqpubsub.pcap
├── logzmqpushpull.pcap
├── rest.pcap
└── ...

````

- **Folder protokol/pola** seperti `MQTT/`, `ZMQ/`, `REST/`, `Reqresp/` berisi kode demo untuk tiap protokol atau pola komunikasi.  
- **compose/** berisi file Docker Compose untuk mempermudah menjalankan beberapa service container yang dibutuhkan untuk setiap protokol.  
- **File `.pcap`** (logMQTT, logTCP, logzmq…) adalah hasil capture jaringan (tcpdump / Wireshark) untuk tiap eksperimen protokol/pola.

---

## 🔧 Protokol / Pola yang Terdokumentasi

Berikut protokol/pola yang dieksplorasi di repo ini:

| Protokol / Pola | Deskripsi Singkat |
|------------------|-------------------|
| **MQTT** | Publish/Subscribe ringan cocok IoT; ada broker + publisher/subscriber. |
| **ZMQ (ZeroMQ)** | Mendukung banyak pola – REQ/REP, PUB/SUB, PUSH/PULL dalam satu library messaging cepat. |
| **TCP / ReqResp** | Pola komunikasi socket dasar: client kirim request → server balas response. |
| **REST** | Web API berbasis HTTP / JSON, operasi GET/POST/PUT/DELETE. |
| **RPC** | Remote procedure call, client memanggil fungsi di server. |
| **SOAP** | Web service XML, menggunakan protokol SOAP dan WSDL. |
| **CORBA** | Middleware klasik untuk objek remote dengan IDL, cocok studi sejarah. |
| **Sync / Oneway / Upcall** | Pola komunikasi sinkron / asynchronous / callback. |
| **code_process** | Contoh concurrency / paralelisme (threads / processes). |

---

## ⚙️ Cara Menjalankan

Berikut langkah umum untuk melakukan eksperimen protokol:

1. Masuk ke direktori kerja repo:  
   ```bash
   cd Sistem-Terdistribusi_Lingkungan-Praktik-Mandiri_15.09.25
````

2. Pilih protokol yang mau dieksplorasi, misalnya *REST* atau *ZMQ*.

3. Jalankan environment container jika ada lewat Docker Compose:

   ```bash
   docker compose -f compose/<nama_protokol>.yml up -d
   ```

4. Jalankan service / client sesuai pola, misalnya untuk tcp req/resp:

   ```bash
   docker compose -f compose/reqresp.yml exec reqresp-server python server.py
   docker compose -f compose/reqresp.yml exec reqresp-client python client.py
   ```

5. Capture log jaringan (opsional) dengan tcpdump / Wireshark. Misalnya di jaringan docker / interface yang sesuai.

---

## 🛰 Contoh Pola Jalannya

Berikut beberapa contoh pola yang sudah dibuat:

* **Req/Resp (TCP)**
  Client dan server saling mengirim/menunggu pesan dengan socket TCP.

* **ZMQ**
  Terdapat beberapa pola:

  * *REQ/REP* → client & server bergantian request / reply
  * *PUB/SUB* → publish ke banyak subscriber
  * *PUSH/PULL* → distribusi pekerjaan ke worker

* **REST**
  Server REST API bisa menerima HTTP request dan membalas HTTP response.

* **MQTT**
  Menggunakan broker + publisher/subscriber; data dikirim lewat topic.

---

## 📊 Hasil Capture / Log

File `.pcap` di repo merekam komunikasi jaringan nyata dari tiap eksperimen:

| Nama File                 | Protokol / Eksperimen | Keterangan                                 |
| ------------------------- | --------------------- | ------------------------------------------ |
| `logMQTT.pcap`            | MQTT                  | Capture pesan publish/subscriber MQTT      |
| `logTCP.pcap`             | TCP ReqResp           | Capture komunikasi request/response TCP    |
| `logzmqclientserver.pcap` | ZMQ REQ/REP           | Client-server pola REQ/REP menggunakan ZMQ |
| `logzmqpubsub.pcap`       | ZMQ PUB/SUB           | Broadcast pesan memakai ZMQ                |
| `logzmqpushpull.pcap`     | ZMQ PUSH/PULL         | Distribusi task ke worker memakai ZMQ      |
| `rest.pcap`               | REST                  | Capture HTTP request & response            |

---

## 📋 Catatan & Hambatan

* Beberapa port mungkin sudah digunakan oleh service lain → muncul error “Address already in use”. Penting untuk pastikan port di `compose` tidak bentrok.
* Tool capture (`tcpdump`, Wireshark) kadang tidak tersedia di container default → perlu install tambahan atau capture dari host.
* Perbedaan antara capture aplikasi (print di Python) dan capture jaringan (raw pakai tcpdump/Wireshark) harus dicatat.

---

## ✅ Kesimpulan

* Eksperimen ini memberikan pemahaman nyata terhadap perbedaan **protokol komunikasi**: mulai dari socket paling dasar (TCP), komunikasi berbasis pesan (MQTT & ZMQ), hingga komunikasi web (REST).
* Masing-masing protokol punya keunggulan & kelemahan tersendiri, tergantung use case: kebutuhan latency, overhead, skalabilitas, multipel penerima, dll.
* Untuk laporan atau presentasi, bisa tunjukkan keunggulan / trade-off antara protokol + hasil capture pakai `.pcap` sebagai bukti nyata.

---

## 📚 Referensi

* Documentasi resmi ZeroMQ: [https://zeromq.org/](https://zeromq.org/)
* Flask (untuk REST API): [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* MQTT (Mosquitto) dokumentasi: [https://mosquitto.org/documentation/](https://mosquitto.org/documentation/)
* TCP/IP basics dan socket programming

---

### 🛠 Tambahan Opsional

Jika ingin memperluas:

* Tambahkan eksperimen *gRPC* sebagai perbandingan modern RPC.
* Analisis performa (latency, throughput) tiap protokol dengan beban pesan berbeda.
* Uji keamanan (misalnya TLS, autentikasi) di REST/MQTT/ZMQ.

---

## 📄 Lisensi

Repo ini dilisensikan di bawah **MIT License**.

---

```

---

Kalau kamu mau, aku bisa modifikasi agar cuma fokus ke 4 protokol yang kamu eksplorasi (MQTT, TCP, REST, ZMQ) supaya README-nya lebih ringkas untuk tugas kamu. Mau aku buat versi ringkasnya juga?
::contentReference[oaicite:0]{index=0}
```
