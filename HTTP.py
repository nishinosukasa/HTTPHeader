from urllib import urlopen as o

print ('''
\033[91m
           .                            
    .... ..................             
    ...''..','''..',...';,,;,'.         
    .  .'..,c:'..',,,;::::;:c::'.       
   ....'','.;l:,'',;;:;,;c::cc;,..      
   ....,',;;;;;cc;;;',;cc:cc:cc,...     
   .. ...'';::;,,,,'.',,::::clc;;,.     
   .....,'';:c:,,;,',,,:oOOo':xd:,.     
     ..,'.'',:c,';,;:;,,;oo:,cdc:;.     
      .',;:,',:cloc,,,'..,' .cc,,'.     
     ....,;'...'cll:'''.....'ll:,..     
      ..........':l::;:dol:'clc:;..     
           ...'.';:;,';xko,,;;;...      
           ....',;:;,.'ldl::,'..        
              ...,;,',,,;::'...         
                   ........             
''')
\033[0m
target = open(raw_input('IP list file name: '), 'r').read().split('\n')
for ip in target:
    print 'Mencari', ip
    ambil = 'null'
    try:
        ambil = o('https://api.hackertarget.com/httpheaders/?q=' + ip).read()
    except:
        continue
    if 'pemeriksaan kesalahan' in grab:
        print 'Periksa format domain dalam file input'
        continue
    if 'Tidak ada catatan' in grab:
        print 'Tidak ada catatan domain dalam mesin serach again'
        continue
    ambil = ambil.split('\n')
    for domain in grab:
        open('hasil.txt', 'a+').write(domain + '\n')
