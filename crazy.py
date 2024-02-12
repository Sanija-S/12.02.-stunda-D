import PySimpleGUI as sg # pip vajadzigs
# izkārtojuma definīcija- jānosauc visas loga daļas 
def red_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file# jo tas faila nosaukums ir mainigs tape filename
       #jaatver vala fails ar open window
        #konstrukcija kas izstradat iznemumus/kludas, nodrosina pareizu izpildi pat ja notiek kludas
            saturs=file.read()
            return saturs 

    except Exception as e:
        return f"Notika kļūda:{e}"
daļas=[
[sg.Text("Izvēlies failu, kuru nolasīt:")]
[sg.InputText(key="filename"), sg.FileBrowse()]
[sg.Button("Nolasīt"),sg.Button("Iziet"),sg.Button("Nolasīt"), sg.Button("Teikt")]
[sg.Multiline(size=(50,10), key="Output"), disabled=True]# pysimple komponents kas lauj ievietot tekstu vairakas rindas, un izveidot teksta ievades lauku kur vares redzet vairakas teksta rindas vienlaicigi, lo ti daudz parametru, sim komponentam daudz iespejas mainit lielumu, nokluseto tekstu, fontu utt, ja nepieciesams lietotajam rediget garu tekstu, komentari, ieraksti utt.
]
#loga definicija- definejam objektu- logs

logs=sg.Window("Loga nosaukums", daļas)
#galvenais notikums
#lai tas logs visulaiku paliek vaļā ar while true
while True:
    notikums, vertibas=logs.read()
    # ka iziet ar x lai neuzrada erroru vai ir poga iziet nospiesta 
    if notikums==sg.WINDOW_CLOSED or notikums=="Iziet":
        break
    # janolasa un jaievieto teksta laukaa info
    if notikums=="Nolasīt":
        filename=vertibas["filename"]
        if filename:
            saturs=read_file(filename)
            #atjauninat musu logu?
            # ievieto tekstu teksta ramiti pa rindam
            logs=["Output"].update(saturs) # logariks kas noradu no kurienes nolasa
            