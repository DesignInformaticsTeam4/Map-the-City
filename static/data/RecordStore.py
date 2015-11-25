import json
a = [ ]                                         
b = {}
b['title'] = 'Vox Box Records'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/hEf4JwC.jpg'
b['latitude'] = 55.957586
b['longitude'] = -3.207072
b['description'] = "We set off in Stockbridge, with a fairly new addition to Edinburgh's music store scene, VoxBox records. A cozy, small record store, VoxBox offers both used and new records, mostly Indie and Alternative. The store is also home to FoxBox Records, a label co-run with Super Inuit aka Brian Pokora."

a.append(b)                                
b = {}                                          

                                  
b['title'] = 'Fopp'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/ivDVvEj.jpg'
b['latitude'] = 55.953219
b['longitude'] = -3.194904
b['description'] = "The next stop on our route is Fopp, a chain store selling media of various forms including music, films, and books. It features a large selection of CDs and a decent sized vinyl stock too. On a busy day on Princes Street, parallel street Rose Street, home of Fopp, offer a small respite from the throngs of people."

a.append(b)                                
b = {}   

                                 
b['title'] = 'Underground Solushn'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/6F19U6D.jpg'
b['latitude'] = 55.950674
b['longitude'] = -3.190837
b['description'] = 'Next up is Underground Solushn, the last surviving electronics and dance music specialist in Edinburgh, running continously since 1995. Not only does it stock electronic and dance music, but also Indie, Classical, Jazz, Hip/Hop and World Music. Aside from a massive collection of new and used records, the store also sells music and DJ equipment. It regularly features in store dj sets from great musicians, and you can also catch local musicians Fudge Fingas and Percy Main manning the till. Come in for a peruse and the friendly staff will definitely find you something that you like. Also offers a wide selection of Record Store Day releases. '   

a.append(b)                                
b = {}   

                                 
b['title'] = 'Coda'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/xxADFuO.jpg'
b['latitude'] = 55.949947
b['longitude'] = -3.193212
b['description'] = "Coda is a traditional, contemporary, folk and scottish music specialist operating in Edinburgh since 2007. Although it mostly stocks CDs, they have a growing vinyl selection too. Super nice location on the mound - there are some great sights to be found out the window and nearby!"

a.append(b)                                
b = {}  

                                  
b['title'] = 'Avalanche Records'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/l6NTfZO.jpg'
b['latitude'] = 55.950164
b['longitude'] = -3.184065
b['description'] = "Avalanche Records is constantly moving around but its latest spot is on Roseneath Street. Avalanche used to be a chain with stores strewn all throughout Edinburgh, but as physical music sales dropped, the Avalancehs closed. Now only one store remains, but Avalanche remains important as ever to the local music scene, and has a steady stream of regular customers itching to get their hands on whatever Kevalanche, the owner, is into."

a.append(b)                                
b = {}  

b = {}                                   
b['title'] = 'Paradise Vinyl'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/nqA0eCy.jpg'
b['latitude'] = 55.946273
b['longitude'] = 55.946273
b['description'] = "Next up is Edinburgh's newest record store, having just opened in October 2015. It is located within the premises of the Paradise Palms bar, and is corun by Paradise Palms and local artist Matt Belcher. It hosts a small but growing selection of records chosen by Matt, as well as some second hand offerings from local DJs, Dj Yves and others. Come by on a tuesday to play a free round of pinball when you buy a record!"

a.append(b)                                
b = {}  

b = {}                                   
b['title'] = 'BackBeat Records'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/LzYufb7.jpg'
b['latitude'] = 55.943767
b['longitude'] = -3.182778
b['description'] = "With records stacked from floor to ceiling, there really isn't much room to walk around in BackBeat Records, but there is a lot to listen to! Off of Nicholson Street, BackBeat has been an Edinburgh Staple for many years, and offers a staggeringly massive collection of second hand vinyl. You won't be able to find anything there yourself, but ask the very knowledgeable owner and he'll find something for you for sure."

a.append(b)                                
b = {} 

b = {}                                   
b['title'] = 'Record Shak'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/r3cyBSk.jpg'
b['latitude'] = 55.941668
b['longitude'] = -3.181803
b['description'] = "Record Shak is your typical record shop, offering more popular selections of mainly second hand vinyl. If you're looking for a bygone hit, this is the place to check."

a.append(b)                                
b = {} 

b = {}                                   
b['title'] = 'Living Mountain'
b['file'] = {}
b['file']['url'] = 'http://imgur.com/1mfzKhE.jpg'
b['latitude'] = 55.940538
b['longitude'] = -3.181467
b['description'] = "One of Edinburgh's newest record stores, the Living Mountain definitely deserves the title of hardest to find. Located deep in the bowels of Summerhall, the Living Mountain is a small paradise of weird records, exotic plants, and great art. Run by local musician and artist Lindsay Todd AKA House of Traps, the shop doubles as a screenprinting studio, often the birthplace of many of the sleeves of the vinyl featured in store. It offers a selection of oddball house, weird techno, Japanese imports, as well as second hand stock from local DJ David Barbarossa. Come by on a Saturday (the only day it's open) for some coffee, chat with Lindsay, and great records."

a.append(b)                                
b = {}
print(a)
json.dump(a, open('RecordStore.json','w'))