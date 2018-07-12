import re
import pymysql
import time
from stemmer import ECSP


class Preprocessing():
    def __init__(self,con=None,keyword=[],qc=None):
        self.qc = qc
        self.oritext = {}
        self.stemmer = ECSP()
        self.keyword = keyword
        sql = "SELECT * from fix_word"
        self.con = None
        if con is not None:
            self.con = con
            unfixWord = self.con.query(sql)
        else:
            from db import Database
            self.con = Database()
            self.con.connect('localhost','root','','sentiment_analysis')
            unfixWord = self.con.query(sql)
        # else:
        #     self.con = pymysql.connect(host='localhost', user='root', passwd='', database='sentiment_analysis',charset='utf8')
        #     cursor = self.con.cursor()
        #     cursor.execute(sql)
        #     unfixWord = cursor.fetchall()
        if self.con is not None:
            self.fixedWords = []
            self.unfixedWords = []
            self.includeWord = []
            for i in unfixWord:
                self.unfixedWords.append(i[1])
                self.fixedWords.append(i[2])
                self.includeWord.append(i[3])
            # print(self.unfixedWords)
        else:
            print("No connection!")

    def removesymbol(self,text):
        cleantext = text
        cleantext = cleantext.lower()
        url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        # symbol_pattern = '[\[\]\(\)!@#$%^&*-+=_`~\{\}\\\/;:\'\"<>,.?]'
        # allowonlyletternumber_pattern = "(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
        allowonlyletternumber_pattern = "(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^A-Za-z \t])|(\w+:\/\/\S+)"
        # allowonlyletter_pattern = "([^A-Za-z \t])|(\w+:\/\/\S+)"
        cleantext = ' '.join(re.sub(allowonlyletternumber_pattern," ",cleantext).split())
        cleantext = re.sub(url_pattern,'',cleantext)
        # cleantext = re.sub(' +',' ',cleantext)
        cleantext = re.sub(r'\b\d+(?:\.\d+)?\s+','',cleantext)
        # cleantext = re.sub(' +',' ',text) #hapus spasi berlebih
        return cleantext

    def tokenize(self,text):
        tokenized = text.split(" ")
        return tokenized

    def fixword(self,texts):
        cleantext = []
        for text in texts:
            newtext = text
            if self.stemmer.isSixChar(newtext) and not self.isRootWordDB(newtext):
                newtext = self.checkWord(newtext)
            if newtext != None:
                cleantext.append(newtext)
            if self.qc:
                self.qc.processEvents()
        return cleantext

    def removestopword(self,texts):
        stopword = [
            'ada', 'adalah', 'adanya', 'adapun', 'agak', 'agaknya', 'agar', 'akan', 'akankah', 'aku', 'akulah', 'amat', 'amatlah', 'anda', 'andalah', 'antar', 'antara', 'antaranya', 'apabila', 'apakah', 'apalagi', 'apatah', 'artinya', 'asal', 'asalkan', 'atas', 'atau', 'ataukah', 'ataupun', 'awal', 'awalnya', 'bagai', 'bagaikan', 'bagaimana', 'bagaimanakah', 'bagaimanapun', 'bagi', 'bagian', 'bahkan', 'bahwa', 'bahwasanya', 'baik', 'bakal', 'bakalan', 'balik', 'banyak', 'bapak', 'baru', 'bawah', 'beberapa', 'begini', 'beginian', 'beginikah', 'beginilah', 'begitu', 'begitukah', 'begitulah', 'begitupun', 'belakang', 'belakangan', 'benar', 'benarkah', 'benarlah', 'berada', 'berapa', 'berapakah', 'berapalah', 'berapapun', 'berarti', 'berawal', 'berbagai', 'berdatangan', 'beri', 'berikan', 'berikut', 'berikutnya', 'berjumlah', 'berkali-kali', 'berkata', 'berkehendak', 'berkeinginan', 'berkenaan', 'berlainan', 'berlalu', 'berlangsung', 'berlebihan', 'bermacam', 'bermacam-macam', 'bermaksud', 'bermula', 'bersama', 'bersama-sama', 'bersiap', 'bersiap-siap', 'bertanya', 'bertanya-tanya', 'berturut', 'berturut-turut', 'bertutur', 'berujar', 'berupa', 'betul', 'betulkah' 'biasa', 'biasanya', 'bila', 'bilakah', 'bisa', 'bisakah', 'boleh', 'bolehkah', 'bolehlah', 'buat', 'bukan', 'bulan', 'bung', 'cara', 'caranya', 'cuma', 'dahulu', 'dalam', 'dan', 'dapat', 'dari', 'daripada', 'datang', 'dekat', 'demi', 'demikian', 'demikianlah', 'dengan', 'depan', 'di', 'dia', 'diakhiri', 'diakhirinya', 'dialah', 'diantara', 'diantaranya', 'diberi', 'diberikan', 'diberikannya', 'dibuat', 'dibuatnya', 'didapat', 'didatangkan', 'digunakan', 'diibaratkan', 'diibaratkannya', 'diingat', 'diingatkan', 'diinginkan', 'dijawab', 'dijelaskan', 'dijelaskannya', 'dikarenakan', 'dikatakan', 'dikatakannya', 'dikerjakan', 'diketahui', 'diketahuinya', 'dikira', 'dilakukan', 'dilalui', 'dilihat', 'dimaksud', 'dimaksudkan', 'dimaksudkannya', 'dimaksudnya', 'diminta', 'dimintai', 'dimisalkan', 'dimulai', 'dimulailah', 'dimulainya', 'dimungkinkan', 'dini', 'dipastikan', 'diperbuat', 'diperbuatnya', 'dipergunakan', 'diperkirakan', 'diperlihatkan', 'diperlukan', 'diperlukannya', 'dipersoalkan', 'dipertanyakan', 'dipunyai', 'diri', 'dirinya', 'disampaikan', 'disebut', 'disebutkan', 'disebutkannya', 'disini', 'disinilah', 'ditambahkan', 'ditandaskan', 'ditanya', 'ditanyai', 'ditanyakan', 'ditegaskan', 'ditujukan', 'ditunjuk', 'ditunjuki', 'ditunjukkan', 'ditunjukkannya', 'ditunjuknya', 'dituturkan', 'dituturkannya', 'diucapkan', 'diucapkannya', 'diungkapkan', 'dong', 'dua', 'dulu', 'empat', 'enggak', 'enggaknya', 'entah', 'entahlah', 'guna', 'gunakan', 'hal', 'hampir', 'hanya', 'hanyalah', 'hari', 'harus', 'haruslah', 'harusnya', 'hendak', 'hendaklah', 'hendaknya', 'hingga', 'ia', 'ialah', 'ibarat', 'ibaratkan', 'ibaratnya', 'ibu', 'ikut', 'ingat', 'ingat-ingat', 'ingin', 'inginkah', 'inginkan', 'ini', 'inikah', 'inilah', 'itu', 'itukah', 'itulah', 'jadi', 'jadilah', 'jadinya', 'jangan', 'jangankan', 'janganlah', 'jauh', 'jawab', 'jawaban', 'jawabnya', 'jelas', 'jelaskan', 'jelaslah', 'jelasnya', 'jika', 'jikalau', 'juga', 'jumlah', 'jumlahnya', 'justru', 'kala', 'kalau', 'kalaulah', 'kalaupun', 'kalian', 'kami', 'kamilah', 'kamu', 'kamulah', 'kan', 'kapan', 'kapankah', 'kapanpun', 'karena', 'karenanya', 'kasus', 'kata', 'katakan', 'katakanlah', 'katanya', 'ke', 'keadaan', 'kebetulan', 'kecil', 'kedua', 'keduanya', 'keinginan', 'kelamaan', 'kelihatan', 'kelihatannya', 'kelima', 'keluar', 'kembali', 'kemudian', 'kemungkinan', 'kemungkinannya', 'kenapa', 'kepada', 'kepadanya', 'kesampaian', 'keseluruhan', 'keseluruhannya', 'keterlaluan', 'ketika', 'khususnya', 'kini', 'kinilah', 'kira', 'kira-kira', 'kiranya', 'kita', 'kitalah', 'kok', 'kurang', 'lagi', 'lagian', 'lah', 'lain', 'lainnya', 'lalu', 'lama', 'lamanya', 'lanjut', 'lanjutnya', 'lebih', 'lewat', 'lima', 'luar', 'macam', 'maka', 'makanya', 'makin', 'malah', 'malahan', 'mampu', 'mampukah', 'mana', 'manakala', 'manalagi', 'masa', 'masalah', 'masalahnya', 'masih', 'masihkah', 'masing', 'masing-masing', 'mau', 'maupun', 'melainkan', 'melakukan', 'melalui', 'melihat', 'melihatnya', 'memang', 'memastikan', 'memberi', 'memberikan', 'membuat', 'memerlukan', 'memihak', 'meminta', 'memintakan', 'memisalkan', 'memperbuat', 'mempergunakan', 'memperkirakan', 'memperlihatkan', 'mempersiapkan', 'mempersoalkan', 'mempertanyakan', 'mempunyai', 'memulai', 'memungkinkan', 'menaiki', 'menambahkan', 'menandaskan', 'menanti', 'menanti-nanti', 'menantikan', 'menanya', 'menanyai', 'menanyakan', 'mendapat', 'mendapatkan', 'mendatang', 'mendatangi', 'mendatangkan', 'menegaskan', 'mengakhiri', 'mengapa', 'mengatakan', 'mengatakannya', 'mengenai', 'mengerjakan', 'mengetahui', 'menggunakan', 'menghendaki', 'mengibaratkan', 'mengibaratkannya', 'mengingat', 'mengingatkan', 'menginginkan', 'mengira', 'mengucapkan', 'mengucapkannya', 'mengungkapkan', 'menjadi', 'menjawab', 'menjelaskan', 'menuju', 'menunjuk', 'menunjuki', 'menunjukkan', 'menunjuknya', 'menurut', 'menuturkan', 'menyampaikan', 'menyangkut', 'menyatakan', 'menyebutkan', 'menyeluruh', 'menyiapkan', 'merasa', 'mereka', 'merekalah', 'merupakan', 'meski', 'meskipun', 'meyakini', 'meyakinkan', 'minta', 'mirip', 'misal', 'misalkan', 'misalnya', 'mula', 'mulai', 'mulailah', 'mulanya', 'mungkin', 'mungkinkah', 'nah', 'naik', 'namun', 'nanti', 'nantinya', 'nyaris', 'nyatanya', 'oleh', 'olehnya', 'pada', 'padahal', 'padanya', 'pak', 'paling', 'panjang', 'pantas', 'para', 'pasti', 'pastilah', 'penting', 'pentingnya', 'per', 'percuma', 'perlu', 'perlukah', 'perlunya', 'pernah', 'persoalan', 'pertama', 'pertama-tama', 'pertanyaan', 'pertanyakan', 'pihak', 'pihaknya', 'pukul', 'pula', 'pun', 'punya', 'rasa', 'rasanya', 'rata', 'rupanya', 'saat', 'saatnya', 'saja', 'sajalah', 'saling', 'sama', 'sama-sama', 'sambil', 'sampai', 'sampai-sampai', 'sampaikan', 'sana', 'sangat', 'sangatlah', 'satu', 'saya', 'sayalah', 'se', 'sebab', 'sebabnya', 'sebagai', 'sebagaimana', 'sebagainya', 'sebagian', 'sebaik', 'sebaik-baiknya', 'sebaiknya', 'sebaliknya', 'sebanyak', 'sebegini', 'sebegitu', 'sebelum', 'sebelumnya', 'sebenarnya', 'seberapa', 'sebesar', 'sebetulnya', 'sebisanya', 'sebuah', 'sebut', 'sebutlah', 'sebutnya', 'secara', 'secukupnya', 'sedang', 'sedangkan', 'sedemikian', 'sedikit', 'sedikitnya', 'seenaknya', 'segala', 'segalanya', 'segera', 'seharusnya', 'sehingga', 'seingat', 'sejak', 'sejauh', 'sejenak', 'sejumlah', 'sekadar', 'sekadarnya', 'sekali', 'sekali-kali', 'sekalian', 'sekaligus', 'sekalipun', 'sekarang', 'sekarang', 'sekecil', 'seketika', 'sekiranya', 'sekitar', 'sekitarnya', 'sekurang-kurangnya', 'sekurangnya', 'sela', 'selain', 'selaku', 'selalu', 'selama', 'selama-lamanya', 'selamanya', 'selanjutnya', 'seluruh', 'seluruhnya', 'semacam', 'semakin', 'semampu', 'semampunya', 'semasa', 'semasih', 'semata', 'semata-mata', 'semaunya', 'sementara', 'semisal', 'semisalnya', 'sempat', 'semua', 'semuanya', 'semula', 'sendiri', 'sendirian', 'sendirinya', 'seolah', 'seolah-olah', 'seorang', 'sepanjang', 'sepantasnya', 'sepantasnyalah', 'seperlunya', 'seperti', 'sepertinya', 'sepihak', 'sering', 'seringnya', 'serta', 'serupa', 'sesaat', 'sesama', 'sesampai', 'sesegera', 'sesekali', 'seseorang', 'sesuatu', 'sesuatunya', 'sesudah', 'sesudahnya', 'setelah', 'setempat', 'setengah', 'seterusnya', 'setiap', 'setiba', 'setibanya', 'setidak-tidaknya', 'setidaknya', 'setinggi', 'seusai', 'sewaktu', 'siap', 'siapa', 'siapakah', 'siapapun', 'sini', 'sinilah', 'soal', 'soalnya', 'suatu', 'sudah', 'sudahkah', 'sudahlah', 'supaya', 'tadi', 'tadinya', 'tahu', 'tahun', 'tak', 'tambah', 'tambahnya', 'tampak', 'tampaknya', 'tandas', 'tandasnya', 'tanpa', 'tanya', 'tanyakan', 'tanyanya', 'tapi','telah', 'tempat', 'tengah', 'tentang', 'tentu', 'tentulah', 'tentunya', 'tepat', 'terakhir', 'terasa', 'terbanyak', 'terdahulu', 'terdapat', 'terdiri', 'terhadap', 'terhadapnya', 'teringat', 'teringat-ingat', 'terjadi', 'terjadilah', 'terjadinya', 'terkira', 'terlalu', 'terlebih', 'terlihat', 'termasuk', 'ternyata', 'tersampaikan', 'tersebut', 'tersebutlah', 'tertentu', 'tertuju', 'terus', 'terutama', 'tetap', 'tetapi', 'tiap', 'tiba', 'tiba-tiba', 'tidakkah', 'tidaklah', 'tiga', 'tinggi', 'toh', 'tunjuk', 'turut', 'tutur', 'tuturnya', 'ucap', 'ucapnya', 'ujar', 'ujarnya', 'umum', 'umumnya', 'ungkap', 'ungkapnya', 'untuk', 'usah', 'usai', 'waduh', 'wah', 'wahai', 'waktu', 'waktunya', 'walau', 'walaupun', 'wong', 'yaitu', 'yakin', 'yakni', 'yang',
            'kak','aja','kakak','ku','sang','ya','kek','tuk']
        # ,'tidak' 'apa',
        cleantext = []
        for text in texts:
            if text in stopword or len(text) < 2:
                pass
            else:
                cleantext.append(text)

            if self.qc:
                self.qc.processEvents()
        return cleantext

    def isRootWordDB(self,text):
        sql = "SELECT id_rootword from root_word where rootword='{0}'"
        if self.con is not None:
            row = self.con.queryWithRowCount(sql.format(text))
            if row is not None and row['count'] < 1:
                return False
        else:
            print("No connection![isRootWordDB]")
        return True

    def checkWord(self,text):
        abbreviation_word = None
        # if len(self.unfixedWords) > 0: # assume that word have no vocal character -> and re.search(r'^[^aeiou]+$',abbreviation_word)
        if text in self.unfixedWords:
            indexWord = self.unfixedWords.index(text)
            if self.fixedWords[indexWord]:
                abbreviation_word = self.fixedWords[indexWord]
            elif self.includeWord[indexWord]=='1':
                abbreviation_word = self.unfixedWords[indexWord]

        # print(abbreviation_word)

        return abbreviation_word

    def stemming(self,texts):
        cleantext = []
        for text in texts:
            if text:
                newtext = self.stemmer.doStemming(text)
                self.oritext[newtext] = text
                cleantext.append(newtext)
        cleantext = ' '.join(cleantext)
        return cleantext

    def process(self,text,logdis=None):
        # print("Original text : ",text)
        start_time = time.time()
        if logdis != None:
            logdis.appendPlainText("Cleaning symbols ...")
        # 1 Symbol removal & casefolding
        text = self.removesymbol(text)
        # print(text)
        if logdis != None:
            logdis.appendPlainText("Creating token from text ...")
        # 2 Tokenize
        token_text = self.tokenize(text)
        # print(token_text)
        if logdis != None:
            logdis.appendPlainText("Fixing token ...")
        # 2.1 Check in dict db if any abbreviation(singkatan)
        fixedword = self.fixword(token_text)
        # print(fixedword)
        if logdis != None:
            logdis.appendPlainText("Deleting stopword ...")
        # 3 Stopword removal
        removedstopword_text = self.removestopword(fixedword)
        # print(removedstopword_text)
        if logdis != None:
            logdis.appendPlainText("Stemming ...")
        # 4 stemmer
        stemmed_text = self.stemming(removedstopword_text)
        # print(stemmed_text)
        # 5 Feature selection & TF-IDF

        # result = stemmed_text
        res = {}
        res['stemmed_text'] = stemmed_text
        res['oritext'] = self.oritext
        # print("--- %s seconds ---" % (time.time() - start_time))
        return res

    def processNoPre(self,text,logdis=None):
        start_time = time.time()
        if logdis != None:
            logdis.appendPlainText("Cleaning symbols ...")
        text = self.removesymbol(text)

        return text


# t = "sy engga suka dgn dia, selalu melakukan pencitraan!"
# p = Preprocessing()
# print(p.process(t))
