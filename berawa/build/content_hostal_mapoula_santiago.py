# Contenido de la demo Mapoula Pensión Boutique (Santiago de Compostela) (es/en/fr/de). Hechos de mapoula.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitaciones de madera y piedra','Servicios para tu estancia'],'en':['Rooms of wood and stone','Services for your stay'],'fr':['Chambres en bois et pierre','Services pour votre séjour'],'de':['Zimmer aus Holz und Stein','Services für Ihren Aufenthalt']}
RD={
'es':['Fusión de lo clásico y lo actual, con climatización frío/calor, minibar, wifi gratuito, TV vía satélite, teléfono y caja fuerte.','Servicio de desayunos, cafetería y sala de estar, ascensor, lavandería, cuna y camas supletorias, y late check-out según disponibilidad.'],
'en':['A blend of classic and contemporary, with heating and air conditioning, minibar, free wifi, satellite TV, telephone and safe.','Breakfast service, café and lounge, lift, laundry, cot and extra beds, and late check-out subject to availability.'],
'fr':['Un mélange de classique et d’actuel, avec climatisation chaud/froid, minibar, wifi gratuit, TV satellite, téléphone et coffre-fort.','Service de petit-déjeuner, cafétéria et salon, ascenseur, blanchisserie, lit bébé et lits d’appoint, et départ tardif selon disponibilité.'],
'de':['Eine Verbindung von Klassik und Moderne, mit Klimaanlage für warm und kalt, Minibar, kostenlosem WLAN, Satelliten-TV, Telefon und Safe.','Frühstücksservice, Cafeteria und Aufenthaltsraum, Aufzug, Wäscherei, Kinderbett und Zustellbetten sowie später Check-out je nach Verfügbarkeit.']}
ART={
'hero':('arches',9911,['#232629','#9c8a6e','#ebe4d6','#5c6166','#3a3e42','#181a1c']),
'intro':('columns',9912,['#efeeea','#f9f8f5','#4d5a3c','#575c61','#232629']),
'r1':('arches',9921,['#eae8e2','#c6b894','#4d5a3c','#575c61','#232629']),
'r2':('waves',9922,['#232629','#a79474','#eee7d9','#666b70','#43474b','#1a1c1e']),
'g1':('skyline',9931,['#232629','#9c8a6e','#ebe4d6','#5c6166','#3a3e42','#181a1c']),
'g2':('hills',9932,['#e5e4df','#e3dcc8','#c6b894','#8b8c8a','#646562','#424340']),
'g3':('columns',9933,['#efeeea','#f9f8f5','#4d5a3c','#575c61','#232629']),
'g4':('arches',9934,['#232629','#a79474','#eee7d9','#666b70','#43474b','#1a1c1e'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Mapoula Pensión Boutique · Santiago de Compostela, a 5 minutos de la Catedral',see_rooms='Ver alojamiento',hero_k='Santiago · Entremurallas, 10',hero_t='Descansa en el corazón de Santiago',hero_s='Encanto y confort a 5 minutos de la Catedral, en un edificio tradicional de granito del casco histórico.',
 intro_t='Pensión familiar en la zona monumental',intro_p1='Mapoula es una pensión familiar en la esquina de la Plaza de Galicia, a la entrada de la zona monumental. Une el encanto clásico con el confort actual y destaca por su trato cercano.',
 intro_p2='El edificio, de granito, es de la primera mitad del siglo XX y se ha renovado hace poco. Cuidan la sostenibilidad: bombillas LED, menos plásticos y productos de proximidad.',
 stats=['A 5 min de la Catedral','Trato familiar','Desayuno con producto local','Wifi gratuito'],nav_rooms='Alojamiento',rooms_t='Alojamiento',rooms_s='Habitaciones con madera, piedra, climatización, amenities, minibar, wifi y caja fuerte.',
 svcs=['Desayuno con productos gallegos y de proximidad','Parking público a 20 m','Estación de tren a unos 300 metros','Bus directo al aeropuerto cada media hora en la plaza','Excursiones por Galicia con organizadores locales','Ordenador público con internet e impresora'],
 loc_p='Entremurallas, 10-3º · Santiago de Compostela, zona monumental. Teléfono: 981 58 01 24 · Móvil: 659 57 81 22. Correo: mapoula@mapoula.com.',
 chips=['¿Qué tienen las habitaciones?','¿Hay desayuno?','¿Dónde aparco?','¿Cómo reservo?']),
'en':dict(title='Mapoula Boutique Guesthouse · Santiago de Compostela, 5 minutes from the Cathedral',see_rooms='See accommodation',hero_k='Santiago · Entremurallas, 10',hero_t='Rest in the heart of Santiago',hero_s='Charm and comfort 5 minutes from the Cathedral, in a traditional granite building in the old town.',
 intro_t='Family guesthouse in the monumental area',intro_p1='Mapoula is a family-run guesthouse on the corner of Plaza de Galicia, at the entrance to the monumental area. It blends classic charm with modern comfort and stands out for its friendly service.',
 intro_p2='The granite building dates from the first half of the XX. century and was recently renovated. They care about sustainability: LED bulbs, fewer plastics and local products.',
 stats=['5 min from the Cathedral','Family service','Breakfast with local produce','Free wifi'],nav_rooms='Accommodation',rooms_t='Accommodation',rooms_s='Rooms with wood, stone, air conditioning, toiletries, minibar, wifi and safe.',
 svcs=['Breakfast with Galician and local products','Public car park 20 m away','Train station about 300 metres away','Direct airport bus every half hour from the square','Excursions around Galicia with local organisers','Public computer with internet and printer'],
 loc_p='Entremurallas, 10-3º · Santiago de Compostela, monumental area. Phone: +34 981 58 01 24 · Mobile: +34 659 57 81 22. Email: mapoula@mapoula.com.',
 chips=['What do the rooms include?','Is there breakfast?','Where can I park?','How do I book?']),
'fr':dict(title='Mapoula Pension Boutique · Saint-Jacques-de-Compostelle, à 5 minutes de la cathédrale',see_rooms='Voir l’hébergement',hero_k='Santiago · Entremurallas, 10',hero_t='Reposez-vous au cœur de Santiago',hero_s='Charme et confort à 5 minutes de la cathédrale, dans un bâtiment traditionnel en granit de la vieille ville.',
 intro_t='Pension familiale dans la zone monumentale',intro_p1='Mapoula est une pension familiale à l’angle de la Plaza de Galicia, à l’entrée de la zone monumentale. Elle allie charme classique et confort actuel et se distingue par son accueil chaleureux.',
 intro_p2='Le bâtiment en granit date de la première moitié du XXe siècle et a été rénové récemment. Engagement durable : ampoules LED, moins de plastique et produits locaux.',
 stats=['À 5 min de la cathédrale','Accueil familial','Petit-déjeuner aux produits locaux','Wifi gratuit'],nav_rooms='Hébergement',rooms_t='Hébergement',rooms_s='Chambres en bois et pierre, avec climatisation, produits d’accueil, minibar, wifi et coffre-fort.',
 svcs=['Petit-déjeuner aux produits galiciens et locaux','Parking public à 20 m','Gare à environ 300 mètres','Bus direct pour l’aéroport toutes les demi-heures sur la place','Excursions en Galice avec des organisateurs locaux','Ordinateur public avec internet et imprimante'],
 loc_p='Entremurallas, 10-3º · Saint-Jacques-de-Compostelle, zone monumentale. Téléphone : +34 981 58 01 24 · Portable : +34 659 57 81 22. E-mail : mapoula@mapoula.com.',
 chips=['Que comprennent les chambres ?','Y a-t-il un petit-déjeuner ?','Où me garer ?','Comment réserver ?']),
'de':dict(title='Mapoula Pensión Boutique · Santiago de Compostela, 5 Minuten von der Kathedrale',see_rooms='Unterkunft ansehen',hero_k='Santiago · Entremurallas, 10',hero_t='Erholung im Herzen von Santiago',hero_s='Charme und Komfort 5 Minuten von der Kathedrale, in einem traditionellen Granitgebäude der Altstadt.',
 intro_t='Familienpension im Monumentalbereich',intro_p1='Mapoula ist eine familiengeführte Pension an der Ecke der Plaza de Galicia, am Eingang zum Monumentalbereich. Sie verbindet klassischen Charme mit modernem Komfort und persönlicher Betreuung.',
 intro_p2='Das Granitgebäude stammt aus der ersten Hälfte des XX. Jahrhunderts und wurde kürzlich renoviert. Nachhaltigkeit zählt: LED-Lampen, weniger Plastik und regionale Produkte.',
 stats=['5 Min. zur Kathedrale','Familiäre Betreuung','Frühstück mit regionalen Produkten','Kostenloses WLAN'],nav_rooms='Unterkunft',rooms_t='Unterkunft',rooms_s='Zimmer mit Holz und Stein, Klimaanlage, Pflegeartikeln, Minibar, WLAN und Safe.',
 svcs=['Frühstück mit galicischen und regionalen Produkten','Öffentliches Parkhaus in 20 m','Bahnhof etwa 300 Meter entfernt','Direktbus zum Flughafen jede halbe Stunde am Platz','Ausflüge in Galicien mit lokalen Veranstaltern','Öffentlicher Computer mit Internet und Drucker'],
 loc_p='Entremurallas, 10-3º · Santiago de Compostela, Monumentalbereich. Telefon: +34 981 58 01 24 · Mobil: +34 659 57 81 22. E-Mail: mapoula@mapoula.com.',
 chips=['Was bieten die Zimmer?','Gibt es Frühstück?','Wo kann ich parken?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://direct-book.com/properties/mapouladirect/';RN=R+'?locale=en'
BOOK=dict(mode='engine',url=dict(es=R,en=RN,fr=RN,de=RN))
D=dict(name='Mapoula Pensión Boutique',ac='#232629',ac2='#4d5a3c',ac2_a11y='#414c33',book=BOOK,around=[],foot=FOOT,
 address='Entremurallas, 10-3º · Santiago de Compostela',phones=['+34 981 58 01 24','+34 659 57 81 22'],emails=['mapoula@mapoula.com'],maps='Mapoula Pensión Boutique, Entremurallas 10, Santiago de Compostela',t=T)
META=dict(repo='demo-hostal-mapoula-santiago',name='Mapoula Pensión Boutique',legal_name='HOSTAL MAPOULA S.L., NIF B42721662 (aviso legal de su web)',registry_ids=['B42721662'],
 url='https://www.mapoula.com/',domain='mapoula.com',municipality='Santiago de Compostela',province='A Coruña',sector='pensión boutique familiar en el casco histórico de Santiago de Compostela',
 read_at='2026-11-02T09:25:00+01:00',created_at='2026-11-02T09:24:00+01:00',built_at='2026-11-02T09:35:00+01:00',audit_date='2026-11-02T09:25:00+01:00',
 rating=dict(value=4.6,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Mapoula+Pensi%C3%B3n+Boutique+Santiago+de+Compostela?hl=es'),
 book=dict(mode='engine',url=R,note='motor propio enlazado desde su pagina /reservar/ («Nuestra propia web de reserva»): https://direct-book.com/properties/mapouladirect/ (es) y ?locale=en para en/fr/de, HTTP 200 los dos (02/11/2026 09:26).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué tienen las habitaciones?','K01'),('¿Hay desayuno?','K02'),('¿Dónde aparco?','K03'),('¿Dónde estáis?','K04'),('¿A qué distancia está la Catedral?','K05'),('¿Cómo llego desde el aeropuerto?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Puedo salir más tarde?','K08'),('¿Tenéis cuna?','K09'),('¿Organizáis excursiones?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Qué hacéis por la sostenibilidad?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('What do the rooms include?','K01'),('Is there breakfast?','K02'),('Where can I park?','K03'),('Where are you?','K04'),('How far is the Cathedral?','K05'),('How do I get there from the airport?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Can I check out late?','K08'),('Do you have a cot?','K09'),('Do you organise excursions?','K10'),('What is your phone number?','K11'),('What do you do for sustainability?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Que comprennent les chambres ?','K01'),('Y a-t-il un petit-déjeuner ?','K02'),('Où me garer ?','K03'),('Où êtes-vous ?','K04'),('À quelle distance est la cathédrale ?','K05'),('Comment venir depuis l’aéroport ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Puis-je partir plus tard ?','K08'),('Avez-vous un lit bébé ?','K09'),('Proposez-vous des excursions ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Que faites-vous pour l’environnement ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Was bieten die Zimmer?','K01'),('Gibt es Frühstück?','K02'),('Wo kann ich parken?','K03'),('Wo liegt die Pension?','K04'),('Wie weit ist die Kathedrale?','K05'),('Wie komme ich vom Flughafen?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Kann ich später auschecken?','K08'),('Haben Sie ein Kinderbett?','K09'),('Bieten Sie Ausflüge an?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Was tun Sie für Nachhaltigkeit?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
