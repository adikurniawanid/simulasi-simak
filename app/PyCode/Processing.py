from Preprocessing import tokenizing
from Model import querySQL
from numpy import hstack


class database:
    __daftarTabel = hstack(querySQL(
        "SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_TYPE LIKE 'VIEW' AND TABLE_SCHEMA LIKE 'simak_simulasi'"))
    __daftarKolom = hstack(querySQL("SELECT col.column_name FROM information_schema.columns col JOIN information_schema.views vie ON vie.table_schema=col.table_schema AND vie.table_name=col.table_name where col.table_schema not in ('sys', 'information_schema','mysql', 'performance_schema') AND vie.table_schema='simak_simulasi'"))


def isPerintah(token):
    kalimatPerintah = ["tampil", "apa", "berapa",
                       "siapa", "cari", "lihat", "temu"]

    for w in token:
        if w in kalimatPerintah:
            result = True
        else:
            result = False
    return result


def indetifikasiTabel(token):
    daftarTabel = querySQL(
        "SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_TYPE LIKE 'VIEW' AND TABLE_SCHEMA LIKE 'simak_simulasi'")

    daftarTabel = hstack(daftarTabel)

    teridentifikasi = []

    for w in token:
        if w in daftarTabel:
            teridentifikasi.append(w)

    return teridentifikasi


def indetifikasiKolom(token):
    daftarKolom = querySQL("SELECT col.column_name FROM information_schema.columns col JOIN information_schema.views vie ON vie.table_schema=col.table_schema AND vie.table_name=col.table_name where col.table_schema not in ('sys', 'information_schema','mysql', 'performance_schema') AND vie.table_schema='simak_simulasi'")

    daftarKolom = hstack(daftarKolom)

    teridentifikasi = []

    for w in token:
        if w in daftarKolom:
            teridentifikasi.append(w)

    return teridentifikasi